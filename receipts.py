"""Lint the receipts, build the README ledger from them, and check that cited sources still resolve.

    python3 receipts.py lint            # every receipt has its fields, sections and pinned sources
    python3 receipts.py ledger          # rewrite the tables between the markers in README.md
    python3 receipts.py ledger --check  # fail if README.md is out of date
    python3 receipts.py links           # needs network and git: do the cited sources still exist?

Standard library only. A receipt opens with a restricted YAML front matter block:
one field per line, free-text values single-quoted; see receipts/TEMPLATE.md.
"""

import argparse
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RECEIPTS = ROOT / "receipts"

# What was changed, from the narrowest thing to the thing that does the improving.
CHANGED = {
    "answer": "One answer",
    "program": "A program or proof",
    "harness": "A reusable harness",
    "weights": "Model weights",
    "improver": "The improver itself",
}
# Who checked the number, from weakest to strongest.
VERIFIED = {
    "reported": "Authors report it",
    "recalculated": "Recalculated from released outcomes",
    "rerun": "Independently rerun",
    "checkable": "Anyone can check the artifact",
}
TRANSFER = {"held": "Held", "mixed": "Mixed", "failed": "Did not hold", "untested": "Not tested"}
TEXT_FIELDS = ("title", "question", "system")
FIELDS = (*TEXT_FIELDS, "year", "changed", "verified", "transfer")
SECTIONS = ("Claim", "Change", "Controls", "Result", "Verified", "Open", "Try it")

URL = re.compile(r"https?://[^\s)>\"\]]+")
ARXIV = re.compile(r"https?://arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})(v\d+)?")
GH_FILE = re.compile(r"https?://github\.com/([\w.-]+/[\w.-]+)/(?:blob|tree)/([^/\s)#]+)(?:/([^\s)#?]*))?")
GH_REPO = re.compile(r"https?://github\.com/([\w.-]+/[\w.-]+?)(?:\.git)?/?$")
SHA = re.compile(r"[0-9a-f]{40}$")


def parse(path):
    """Returns (fields, body). Raises ValueError with a readable message."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("must open with a `---` block of fields")
    head, body = text[4:].split("\n---\n", 1)
    fields = {}
    for line in head.split("\n"):
        if not line.strip(" "):
            continue
        key, sep, value = line.partition(": ")
        if not sep or not value.strip(" ") or not re.fullmatch(r"[a-z]+", key):
            raise ValueError(f"cannot read field line {line!r}; expected `key: value`")
        if key in fields:
            raise ValueError(f"duplicate field {key}")
        if re.search(r"[\x00-\x1f\x7f-\x9f\u2028\u2029\ufffe\uffff]", value):
            raise ValueError(f"{key} must be on one line without control characters")
        value = value.strip(" ")
        if key in TEXT_FIELDS:
            # Decode precisely the single-quoted YAML subset used in the template.
            if not re.fullmatch(r"'(?:[^']|'')+'", value):
                raise ValueError(f"{key} must be single-quoted; double any apostrophe inside")
            value = value[1:-1].replace("''", "'")
            if not value.strip():
                raise ValueError(f"{key} must not be empty")
        fields[key] = value
    return fields, body


def problems(path):
    try:
        fields, body = parse(path)
    except ValueError as exc:
        return [str(exc)]
    out = [f"missing field {k}" for k in FIELDS if k not in fields]
    out += [f"unknown field {k}" for k in fields if k not in FIELDS]
    for key, allowed in (("changed", CHANGED), ("verified", VERIFIED), ("transfer", TRANSFER)):
        if key in fields and fields[key] not in allowed:
            out.append(f"{key} must be one of {', '.join(allowed)} (got {fields[key]!r})")
    if "year" in fields and not re.fullmatch(r"(19|20)\d\d", fields["year"]):
        out.append("year must be four digits")
    if "question" in fields and not fields["question"].endswith("?"):
        out.append("question must be a question a reader could answer differently after reading")
    labels = re.findall(r"^\*\*([^*:]+):\*\*", body, re.M)
    if labels != list(SECTIONS):
        out.append(f"sections must be, in order: {', '.join(SECTIONS)} (found {', '.join(labels) or 'none'})")
    for m in ARXIV.finditer(body):
        if not m.group(2):
            out.append(f"arXiv link without a version: {m.group(0)}")
    for m in GH_FILE.finditer(body):
        if not SHA.match(m.group(2)):
            out.append(f"GitHub file link not pinned to a commit: {m.group(0)}")
    if not URL.search(body):
        out.append("no source link")
    return out


def load():
    rows = []
    for path in sorted(RECEIPTS.glob("*.md")):
        if path.name == "TEMPLATE.md":
            continue
        fields, _ = parse(path)
        rows.append({**fields, "path": f"receipts/{path.name}"})
    order = list(CHANGED)
    return sorted(rows, key=lambda r: (order.index(r["changed"]), r["year"], r["title"]))


def ledger(rows):
    out = ["| Receipt | Before you rely on it, ask | What changed | Who checked | Elsewhere |", "| --- | --- | --- | --- | --- |"]
    for r in rows:
        out.append(f"| [{r['title']}]({r['path']}) · {r['year']} | {r['question']} | {CHANGED[r['changed']]} | "
                   f"{VERIFIED[r['verified']]} | {TRANSFER[r['transfer']]} |")
    return "\n".join(out)


def grid(rows):
    """How many receipts sit at each level of change and each level of checking."""
    out = ["| | " + " | ".join(VERIFIED.values()) + " |", "| --- |" + " :---: |" * len(VERIFIED)]
    for c, label in CHANGED.items():
        cells = []
        for v in VERIFIED:
            n = sum(1 for r in rows if r["changed"] == c and r["verified"] == v)
            cells.append(str(n) if n else "·")
        out.append(f"| **{label}** | " + " | ".join(cells) + " |")
    return "\n".join(out)


def inject(text, name, body):
    start, stop = f"<!-- {name} -->", f"<!-- /{name} -->"
    i, j = text.find(start), text.find(stop)
    if i < 0 or j < i:
        raise SystemExit(f"README.md is missing the {start} ... {stop} markers")
    return text[: i + len(start)] + "\n" + body + "\n" + text[j:]


def build_readme(text, rows):
    return inject(inject(text, "ledger", ledger(rows)), "grid", grid(rows))


# ---------------------------------------------------------------- links

def markdown_files():
    return [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]


def cited_urls():
    urls = {}
    for path in markdown_files():
        for u in URL.findall(path.read_text(encoding="utf-8")):
            urls.setdefault(u.rstrip(".,;:"), path.relative_to(ROOT).as_posix())
    return urls


def http_status(url, tries=3):
    for n in range(tries):
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (awesome-rsi-receipts link check)"})
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.status
        except urllib.error.HTTPError as exc:
            if exc.code not in (429, 500, 502, 503) or n + 1 == tries:
                return exc.code
        except (urllib.error.URLError, TimeoutError, OSError):
            if n + 1 == tries:
                return None
        time.sleep(4 * (n + 1))
    return None


def git(args, cwd=None):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, timeout=300)


def pinned_ok(repo, sha, paths):
    """Does the commit exist, and each path at it? One shallow, blob-less fetch per commit."""
    with tempfile.TemporaryDirectory() as tmp:
        git(["init", "-q", "--bare", tmp])
        if git(["fetch", "-q", "--depth", "1", "--filter=blob:none", f"https://github.com/{repo}", sha], cwd=tmp).returncode:
            return {p: False for p in paths}
        return {p: not p or git(["cat-file", "-e", f"FETCH_HEAD:{p}"], cwd=tmp).returncode == 0 for p in paths}


def classify(status):
    if status is not None and 200 <= status < 400:
        return "ok"
    if status in (404, 410):
        return "dead"
    return "unverifiable"  # 403, 429, 5xx, timeouts: the site refused or failed, which says nothing about the page


def check_links(urls):
    """Returns [(level, url, where, detail)] with level ok | dead | unverifiable."""
    found, pinned = [], {}
    for url, where in sorted(urls.items()):
        m = GH_FILE.match(url)
        if m and SHA.match(m.group(2)):
            pinned.setdefault((m.group(1), m.group(2)), []).append((url, where, (m.group(3) or "").rstrip("/")))
            continue
        m = GH_REPO.match(url)
        if m or GH_FILE.match(url):
            repo = (m or GH_FILE.match(url)).group(1)
            ok = git(["ls-remote", f"https://github.com/{repo}", "HEAD"]).returncode == 0
            found.append(("ok" if ok else "dead", url, where, "git ls-remote"))
            continue
        if ARXIV.match(url):
            time.sleep(3)  # arXiv asks automated clients to go slowly
        status = http_status(url)
        found.append((classify(status), url, where, f"HTTP {status}"))
    for (repo, sha), items in pinned.items():
        ok = pinned_ok(repo, sha, {p for _, _, p in items})
        found += [("ok" if ok[p] else "dead", url, where, f"git {sha[:7]}:{p or '(commit)'}") for url, where, p in items]
    return found


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("what", choices=["lint", "ledger", "links"])
    ap.add_argument("--check", action="store_true", help="ledger: fail instead of writing when README.md is stale")
    a = ap.parse_args(argv)
    bad = 0
    for path in sorted(RECEIPTS.glob("*.md")):
        if path.name != "TEMPLATE.md":
            for p in problems(path):
                bad += 1
                print(f"receipts/{path.name}: {p}", file=sys.stderr)
    if bad:
        return 1
    rows = load()
    if a.what == "lint":
        print(f"ok: {len(rows)} receipts")
        return 0
    if a.what == "ledger":
        readme = ROOT / "README.md"
        new = build_readme(readme.read_text(encoding="utf-8"), rows)
        if a.check:
            if new != readme.read_text(encoding="utf-8"):
                print("README.md is out of date; run python3 receipts.py ledger", file=sys.stderr)
                return 1
            print("README.md is up to date")
            return 0
        readme.write_text(new, encoding="utf-8")
        print(f"README.md written from {len(rows)} receipts")
        return 0
    found = check_links(cited_urls())
    for level, url, where, detail in found:
        if level != "ok":
            print(f"{level.upper():12} {url}  ({where}; {detail})")
    dead = sum(1 for f in found if f[0] == "dead")
    print(f"{len(found)} links: {dead} dead, {sum(1 for f in found if f[0] == 'unverifiable')} could not be checked")
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
