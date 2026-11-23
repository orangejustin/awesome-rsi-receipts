# Awesome RSI Receipts：遞迴自我改進證據清單 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<p align="center"><a href="README.md">English</a> | <a href="README.zh-CN.md">简体中文</a> | <b>繁體中文</b></p>

[![驗證](https://github.com/orangejustin/awesome-rsi-receipts/actions/workflows/verify.yml/badge.svg)](https://github.com/orangejustin/awesome-rsi-receipts/actions/workflows/verify.yml)
[![連結檢查](https://github.com/orangejustin/awesome-rsi-receipts/actions/workflows/links.yml/badge.svg)](https://github.com/orangejustin/awesome-rsi-receipts/actions/workflows/links.yml)
[![授權條款：MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> 對於聲稱能自我改進的系統，先問三件事：改了什麼？誰查證過？又有哪些地方退步了？

[一個調校後的執行框架（harness）](receipts/flashrsi-gepa.md)在原測試集上提高了 **12.34 分**，換到一個遷移測試集提高了 **10.83 分**，換到另一個卻下降了 **14.00 分**。[一個自我改進的代理](receipts/darwin-godel-machine.md)把通過率從 20% 提高到了 50%，但測的是 500 道題中的 200 道。[一個改進程式](receipts/stop.md)用強模型時越改越好，換成弱模型卻越改越差。這些結果都是真的，但只看標題，很容易讀出不一樣的結論。

這裡收集了 AI 代理「遞迴自我改進」（RSI）主張背後的證據，並用同一套問題逐一核對。這裡不是排行榜，也不會執行任何代理。

**離線試一試**（Python 3.9+，不用安裝相依套件，也不需要 API 金鑰）：

```sh
python3 compare.py examples/library-search.json
```

兩個版本都通過了 4 項合成任務中的 2 項，但有一項由失敗轉為通過，另一項則由通過轉為失敗。把自己的修改前後結果交給這個指令稿，就能看到哪些任務發生了翻轉，以及這種差異是否可能只是巧合。

<a name="contents"></a>

## 目錄

- [從這裡開始](#start-here)
- [證據記錄](#receipts)
- [資料來源](#sources)
  - [更簡單的基準方法能做到同樣好嗎？](#would-a-simpler-baseline-do-as-well)
  - [基準真的測到了你想測的能力嗎？](#is-the-benchmark-measuring-what-you-think)
  - [差異大於雜訊嗎？](#is-the-difference-bigger-than-the-noise)
  - [提升能遷移並持續嗎？](#does-the-gain-carry-over-and-keep-going)
  - [能修改自身的代理](#agents-that-edit-themselves)
  - [搜尋與回饋](#search-and-feedback)
  - [執行框架設計](#harness-design)
  - [人人都可驗證的結果](#results-anyone-can-check)
  - [AI 能做 AI 研究嗎？](#can-ai-do-ai-research)
  - [模型權重](#weights)
  - [風險與治理](#risk-and-governance)
  - [相關清單](#related-lists)
- [製作自己的證據記錄](#make-your-own-receipt)
- [貢獻](#contributing)

<a name="start-here"></a>

## 從這裡開始

| 你想做什麼？ | 從哪裡入手？ |
| --- | --- |
| **判斷**剛讀到的研究結論是否站得住腳 | [證據記錄](#receipts)：對每項主張都問同樣的七個問題，也記錄哪些結論沒有成立。 |
| **了解**自我改進代理是怎麼建構和測試的 | [資料來源](#sources)：按問題查找論文、稽核、基準和工具。 |
| 在自己的任務上**測試**一次提示詞、工具或記憶修改 | [製作自己的證據記錄](#make-your-own-receipt)：每次只改一件事，沿用同一組任務 ID，並事先訂好去留標準。 |

<a name="receipts"></a>

## 證據記錄

判斷一項自我改進實驗能說明什麼，先看兩個面向。一是**改了什麼**：單一答案、程式、可重複使用的執行框架、模型權重，還是改進程式本身？二是**誰查證過**：只有作者報告，有人根據公開結果重新計算，有人獨立重跑，還是任何人都能驗證產物？目前的證據分布如下：

<!-- grid -->
| | 作者報告 | 根據公開結果重新計算 | 獨立重跑 | 任何人都能查證產物 |
| --- | :---: | :---: | :---: | :---: |
| **單一答案** | · | · | 1 | · |
| **程式或證明** | 1 | · | · | 1 |
| **可重複使用執行框架** | 6 | 1 | 1 | · |
| **模型權重** | 1 | · | · | · |
| **改進程式本身** | 3 | · | · | · |
<!-- /grid -->

大多數證據集中在第一列。最後一列才是「遞迴」的關鍵：變得更好的是改進程式本身。但這一列的結果目前都只有作者查證過。

<!-- ledger -->
| 證據記錄 | 採信前先問 | 改了什麼 | 誰查證過 | 遷移表現 |
| --- | --- | --- | --- | --- |
| [The AI Scientist：外部評估發現了什麼](receipts/ai-scientist.md) · 2025 | 獨立評估者親自執行系統時，發現了什麼？ | 單一答案 | 獨立重跑 | 未測試 |
| [AlphaEvolve：哪些結果可以親自查證](receipts/alphaevolve.md) · 2025 | 不必相信作者，讀者也能驗證哪些結果？ | 程式或證明 | 任何人都能查證產物 | 未測試 |
| [程式碼演化與簡單基準方法的對照](receipts/simple-baselines.md) · 2026 | 起作用的是搜尋方法，還是問題的設定方式？ | 程式或證明 | 作者報告 | 未測試 |
| [ADAS：獨立重跑時縮水的效益](receipts/adas.md) · 2024 | 換一個執行模型、保持相同預算，搜尋得到的代理還表現更好嗎？ | 可重複使用執行框架 | 獨立重跑 | 有得有失 |
| [Darwin Gödel Machine：在任務子集上從 20% 到 50%](receipts/darwin-godel-machine.md) · 2025 | 換到完整基準、其他模型或其他基準，還剩多少效益？ | 可重複使用執行框架 | 作者報告 | 有得有失 |
| [Huxley-Gödel Machine：自身得分高，不代表後代更好](receipts/huxley-godel-machine.md) · 2025 | 按基準得分選出的代理，也是最有可能產生更好後代的那個嗎？ | 可重複使用執行框架 | 作者報告 | 有得有失 |
| [SICA：一次執行，五十項任務](receipts/sica.md) · 2025 | 在 50 項任務上提高了 36 分，其中有多少真是代理變聰明了？ | 可重複使用執行框架 | 作者報告 | 未測試 |
| [失敗回饋修正了觸發它的失敗嗎？](receipts/failure-feedback.md) · 2026 | 某項任務失敗後觸發的修改，修好那項任務了嗎？ | 可重複使用執行框架 | 根據公開結果重新計算 | 提升未能維持 |
| [FlashRSI：同一套執行框架，三種結果](receipts/flashrsi-gepa.md) · 2026 | 在沒參與調校的另一類任務上，這套執行框架還有用嗎？ | 可重複使用執行框架 | 作者報告 | 有得有失 |
| [演化執行框架，還是多試幾次？](receipts/matched-budget.md) · 2026 | 如果給原有執行框架同樣的預算和回饋，它能不能做得一樣好？ | 可重複使用執行框架 | 作者報告 | 有得有失 |
| [從失敗中總結經驗，與不看失敗的同一種搜尋相比](receipts/failure-traces.md) · 2026 | 有多少效益來自看到失敗記錄，又有多少只是因為多嘗試、保留得分更高的版本？ | 可重複使用執行框架 | 作者報告 | 提升未能維持 |
| [SEAL：自己撰寫訓練資料的模型](receipts/seal.md) · 2025 | 隨著模型自行生成的更新不斷累積，先前學到的知識會怎樣？ | 模型權重 | 作者報告 | 未測試 |
| [STOP：讓改進程式改進自身](receipts/stop.md) · 2023 | 換成較弱的底層模型，自我改進還有效嗎？ | 改進程式本身 | 作者報告 | 有得有失 |
| [Gödel Agent：改寫負責改寫的程式](receipts/godel-agent.md) · 2024 | 一個能修改自身改進循環的代理，有多大機率越改越差？ | 改進程式本身 | 作者報告 | 未測試 |
| [Flex-RSI：讓改進程式修改自身](receipts/flex-rsi.md) · 2026 | 是改進程式變強了，還是多試了幾次修改執行框架？ | 改進程式本身 | 作者報告 | 未測試 |
<!-- /ledger -->

**遷移表現**記錄成效是否也出現在用於篩選修改的任務之外，例如換一套基準、換一個模型，或使用預先保留的任務族。

<a name="sources"></a>

## 資料來源

每個條目介紹資料是什麼，以及證據能支持哪些結論。除非另有說明，結果均來自原作者，本清單沒有重新執行實驗。標有 🧾 的條目附有證據記錄。

<a name="would-a-simpler-baseline-do-as-well"></a>

### 更簡單的基準方法能做到同樣好嗎？

- [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227v4)：在把效益歸功於框架演化之前，先給固定框架可比的回饋和額外嘗試機會。演化在 Terminal-Bench 2.1 上不及單純增加測試時計算量，卻在長程遊戲中勝出，說明結果取決於任務。🧾 [證據記錄](receipts/matched-budget.md)
- [Simple Baselines are Competitive with Code Evolution](https://arxiv.org/abs/2602.16805v2)：在相同的搜尋空間下，兩種簡單基準方法與複雜的程式碼演化流程持平或更好。結果更應歸功於問題的定義方式，而不是搜尋演算法。🧾 [證據記錄](receipts/simple-baselines.md)
- [Agent Self-Improvement with Frozen Weights](https://arxiv.org/abs/2611.11342v2)：對比使用失敗經驗總結與看不到失敗資訊的同一搜尋流程。看到失敗記錄額外帶來 4.0 個百分點；約 60% 的總提升來自嘗試並保留得分更高的版本。僅測試了一個模型。🧾 [證據記錄](receipts/failure-traces.md)
- [Does Failure Feedback Direct Agent Self-Modification?](https://arxiv.org/abs/2610.14662v1)：用公開紀錄重新計算：由某個失敗觸發的修改，是否能修正那個失敗？它修正觸發該修改的失敗，並不比修正其他失敗更頻繁。這並不否定篩選能提高總體表現。🧾 [證據記錄](receipts/failure-feedback.md)
- [BOXBOX](https://arxiv.org/abs/2611.09218v3)：在耗時相同的條件下，將線上修改框架與固定框架、離線演化及增加計算量的基準方法比較。在一個長程軟體任務內適應，不等於跨任務累積效益。
- [AI Research Agents for Machine Learning: Search, Exploration, and Generalization in MLE-bench](https://arxiv.org/abs/2507.02554v2)：將搜尋策略與修改算子集合分開，表明兩者的搭配很重要（在 MLE-bench lite 上，Kaggle 獲得獎牌的比率由 39.6% 提升到 47.7%）。基準已公開，無法排除資料汙染。
- [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089v2)：一項隨機試驗：開發者預計 AI 工具會讓自己快 24%，實際卻慢了 19%。雖然不是關於自我改進的研究，卻直觀說明實測效果可以和所有人的預期相反。

<a name="is-the-benchmark-measuring-what-you-think"></a>

### 基準真的測到了你想測的能力嗎？

- [Establishing Best Practices for Building Rigorous Agentic Benchmarks](https://arxiv.org/abs/2507.02825v5)：審查常用的代理基準，發現任務設計和評分方式有缺陷，報告的效能的相對誤差最高可達 100%。附有核對清單；是方法指南，不是工具。
- [The SWE-Bench Illusion](https://arxiv.org/abs/2506.12286v4)：僅看 issue 文字，模型就在 SWE-bench Verified 上有 76% 的機率指出含 bug 的檔案，而在該基準之外的儲存庫上是 53%。這是記憶現象的間接證據，不能證明某個具體模型記住了答案。
- [The More You Automate, the Less You See](https://arxiv.org/abs/2509.08713v2)：區分自動化研究流程的四種失敗模式：基準選擇、資料洩漏、指標誤用、事後篩選。研究顯示，要靠紀錄和程式碼而不是最終論文才能發現這些問題。只研究了兩個系統。
- [Auditing Harness Tampering in Self-Improving Agents](https://arxiv.org/abs/2609.00069v1)：在實際執行過程中發現一些自我修改只提高分數，沒有提高能力，而且往往出現在最終勝出代理的演化譜系中。稽核方法也是由原作者自己評測的。
- [PostTrainBench](https://arxiv.org/abs/2603.08640v2)：給代理 10 個 GPU 小時做模型後訓練。最佳結果是 23.2%，官方指令微調模型則達到 51.1%。部分代理使用了測試集訓練，或用了自己找到的 API 金鑰。
- [The Meta-Agent Challenge](https://arxiv.org/abs/2606.04455v1)：後設代理必須建構一個能在保留任務上取得好成績的代理。很少有系統能達到人工設計的對照方法的水準，最佳化壓力還導致了一些嘗試擷取標準答案的行為。
- [Holistic Agent Leaderboard](https://arxiv.org/abs/2510.11977v1)：涵蓋 9 個模型和 9 套基準的 21,730 次執行，完整紀錄公開。紀錄揭示，有的代理不解題，而是上網搜基準。
- Anthropic · [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) 和 [Quantifying infrastructure noise](https://www.anthropic.com/research/infrastructure-noise)：給實際結果評分，不要給代理的自我報告評分；固定執行環境與時間限制。僅資源設定的變化就讓某個程式設計基準的成績浮動了幾個百分點。

<a name="is-the-difference-bigger-than-the-noise"></a>

### 差異大於雜訊嗎？

- [Adding Error Bars to Evals](https://arxiv.org/abs/2411.00640v1)：提供計算誤差線、做配對比較，以及估算評估所需題數的公式。依賴大樣本近似。
- [Don't Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints](https://arxiv.org/abs/2503.01747v3)：指出這些近似在小基準上會低估誤差線，並附上實作替代方法的[庫](https://github.com/sambowyer/bayes_evals)。這是一篇立場論文。
- [Measuring all the noises of LLM Evals](https://arxiv.org/abs/2512.21326v3)：區分模型作答的波動與選題帶來的波動，發現配對比較中的前者通常更大，因此取多次執行的平均值能提高統計檢驗的功效。
- [SAGE: A Statistical Acceptance Gate for Self-Evolving Agents](https://arxiv.org/abs/2609.36043v1)：用逐題配對檢驗替代「只要提高平均分數就接受」，因為在小而有雜訊的資料集上選到的最高分容易高估成效。20 種設定中有 19 種的退化減少了。
- [Trustworthy Recursive Self-Improvement with Statistical Guarantees](https://arxiv.org/abs/2611.10787v1)：提出一種限制被接受修改中實際表現更差的比例的採用規則。對照的貪心規則是 45.59%，該方法是 2.78%。保證僅在給定假設下成立。
- [GUARD](https://arxiv.org/abs/2611.23476v1)：將新出現的退化與此前未解決的失敗分開追蹤。不退化保證只涵蓋用於採用判定的緩衝區，不涵蓋從未見過的任務。
- [On The Statistical Limits of Self-Improving Agents](https://arxiv.org/abs/2510.04399v3)：理論結果：如果自我修改能使代理的容量無界增長，原本可學習的任務可能變得不可學習。未做實證檢驗。

<a name="does-the-gain-carry-over-and-keep-going"></a>

### 提升能遷移並持續嗎？

- [FlashRSI](https://github.com/RUC-NLPIR/FlashRSI/blob/560f02dfaa415be808647ae4c70d149423879cba/README.md#overall-results)：將篩選出的框架直接用於其他任務族，不重新調校。同一框架在一類任務上有幫助，在另一類上卻有損害。🧾 [證據記錄](receipts/flashrsi-gepa.md)
- [RRSI](https://arxiv.org/abs/2609.24972v3)（[程式碼](https://github.com/google-research/rrsi)）：篩選時排除只對某套基準有效的修改。開發任務的涵蓋率不能替代最終逐題配對比較的正確率。
- [Self-Improvement Memory](https://arxiv.org/abs/2611.18856v1)：切換任務或模型時，除了繼承框架，還繼承以往修改的原因、預期和實際結果。只測試了相容的任務或模型切換，沒有測試跨領域遷移。
- [RSIBench-Data](https://arxiv.org/abs/2607.25886v1)：固定技術堆疊和預算，評估代理改善訓練資料的能力。58.33% 的設定在首次有效嘗試中取得提升；越過最佳分數後仍繼續搜尋的實驗，最終有 78.26% 的成績下降了。
- [SelfImprove-Bench](https://arxiv.org/abs/2611.02797v1)：用五個層級的泛化測試區分能力提升與對特定情境的擬合。現有方法的效益在不同層級不一致。以遊戲為基礎。
- [Continual Learning Exam](https://arxiv.org/abs/2610.33956v1)：用 600 個關卡測量從經驗中提高表現、同時保留所學的能力。回饋和修訂帶來的提升中位數為 5.3 個百分點；最佳系統通過 47.7% 的關卡。由模型評分。
- [Evo-Bench](https://arxiv.org/abs/2608.09096v2) 和 [HarnessOpt-Bench](https://arxiv.org/abs/2608.06301v1)：兩個基準都試圖區分改進框架的能力與基礎模型實力，後者使用封閉的測試集。提升隨任務和隨機種子而大幅變化。
- [AI4AI at Test-Time](https://arxiv.org/abs/2608.12307v1)：較強的模型給較弱的模型撰寫框架，使後者的分數接近翻倍。作者將效益歸因於確定性程式碼、針對基準的路由與答案格式，而非推理能力變強。

<a name="agents-that-edit-themselves"></a>

### 能修改自身的代理

- [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954v3)（[程式碼](https://github.com/jennyzzt/dgm)）：程式設計代理重寫自己的程式碼，並歸檔不同版本。最醒目的數字來自任務子集；遷移時，在一套基準上提升明顯，在另一套上提升不大。🧾 [證據記錄](receipts/darwin-godel-machine.md)
- [Huxley-Gödel Machine](https://arxiv.org/abs/2510.21614v3)（[程式碼](https://github.com/metauto-ai/HGM)）：某個代理自身的得分並不能很好預測其後代的品質，因此改用後代的表現來篩選。它相對早期方法的領先，僅是單次執行中多完成了兩項任務。🧾 [證據記錄](receipts/huxley-godel-machine.md)
- [SICA](https://arxiv.org/abs/2504.15228v2)（[程式碼](https://github.com/MaximeRobeyns/self_improving_coding_agent)）：不設獨立的後設代理：由迄今表現最好的代理撰寫下一代。僅在 50 項任務上執行一次，早期效益大多來自速度和成本的改善。🧾 [證據記錄](receipts/sica.md)
- [Gödel Agent](https://arxiv.org/abs/2410.04444v4)（[程式碼](https://github.com/Arvid-pku/Godel_Agent)）：修改自身正在執行的程式碼，包括負責改進的常式。100 次試驗中，有 14% 的最終表現低於起點。🧾 [證據記錄](receipts/godel-agent.md)
- [STOP](https://arxiv.org/abs/2310.02304v3)（[程式碼](https://github.com/microsoft/stop)）：讓改進程式處理自己的原始碼。在 GPT-4 上有效，換用較弱的模型時表現下降；研究也統計了生成程式碼嘗試脫離沙箱的頻率。🧾 [證據記錄](receipts/stop.md)
- [ADAS](https://arxiv.org/abs/2408.08435v2)（[程式碼](https://github.com/ShengranHu/ADAS)）：一個固定的後設代理用程式碼撰寫新代理。後來兩個團隊用其他模型重新執行，發現效益很小，甚至為負。🧾 [證據記錄](receipts/adas.md)
- [Flex-RSI](https://arxiv.org/abs/2611.08946v1)：在這個基準中，改進程式既可以編輯執行器，也可以修改自身。結果表明允許編輯比不允許編輯好，但沒有單獨驗證改進程式本身是否變得更強。🧾 [證據記錄](receipts/flex-rsi.md)
- [Hyperagents](https://arxiv.org/abs/2603.19461v2)：讓修改代理的流程本身也可以被編輯，作者報告這一層的改進可以跨領域遷移。「自我加速」只是提出的可能性，並非測得的結果。
- [Recursive self-improvement of AI research agents](https://arxiv.org/abs/2609.26457v1)：研究代理在一次為期八天的執行中修改自身程式碼，找到七項連續改進，在四個保留基準上均成立。只有一次執行；與生產用代理的比較使用的是作者自己的任務集。
- [Evaluation-Free Recursive Self-Improvement for Coding Agents](https://arxiv.org/abs/2611.21056v1)：只做有效性檢查，不在循環中評估任務表現，也能讓程式設計代理從 60.0% 提升到 85.6%；兩種使用任務評估的方法分別達到 86.7% 和 88.3%。
- [Mendel Gödel Machine](https://arxiv.org/abs/2608.07645v1) 與 [Red Queen Gödel Machine](https://arxiv.org/abs/2606.26294v3)：修改代理時同時利用多條軌跡，或借鏡另一個譜系，並讓評估器與代理共同演化。評估器也在變，因此更難與其他論文對比。
- [HELIX](https://arxiv.org/abs/2608.13951v1)：為固定模型演化執行框架，並保留相互匹配的執行軌跡，作為下一版模型的訓練資料。僅一輪，僅限程式碼修正；單個最優框架提升了 4.0%。

<a name="search-and-feedback"></a>

### 搜尋與回饋

- [GEPA](https://arxiv.org/abs/2507.19457v2)（[程式碼](https://github.com/gepa-ai/gepa)）：依據失敗軌跡修改提示詞，而不只看分數。它支持的是在該實驗方案下最佳化提示詞的效果，不能用於比較執行框架或權重更新方法。
- [Meta-Harness](https://arxiv.org/abs/2603.28052v1)（[程式碼](https://github.com/stanford-iris-lab/meta-harness)）：將之前的框架修改和完整執行軌跡提供給生成修改建議的模組。在框架程式碼上進行搜尋，並不表明這個模組本身變得更強。
- [Agentic Context Engineering](https://arxiv.org/abs/2510.04618v3)：讓上下文演化，並提出「上下文坍塌」：反覆改寫會逐漸抹去細節。模型權重沒有變化。
- OpenAI · [Build an agent improvement loop with traces, evals, and Codex](https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop)：把軌跡中反覆出現的失敗變成迴歸測試案例，做一項經過審查的修改，再重新執行評測。這是用合成任務示範的完整範例，不是有對照的基準實驗。

<a name="harness-design"></a>

### 執行框架設計

- OpenAI · [Harness engineering](https://openai.com/index/harness-engineering/)：將反覆出現的失敗寫成代理可以執行的靜態檢查規則或測試，並提供具體的修正提示。這是第一方的案例研究，沒有單獨估計框架的貢獻。
- Anthropic · [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents)：借助進度紀錄和乾淨的程式碼提交繼續工作，而不是直接重新啟動。能跨工作階段接著做，不代表改進程式本身變得更強。
- Anthropic · [The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory)：比較可搜尋的工作階段記錄、整理過的筆記，以及在工作階段間準備的筆記會帶來什麼變化。記得更好，不等於改得更好。
- [WalkingLabs](https://github.com/walkinglabs/learn-harness-engineering)、[LangChain's harness anatomy](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) 與 [Mitchell Hashimoto's adoption notes](https://mitchellh.com/writing/my-ai-adoption-journey)：建構小型執行框架時，工具、上下文和檢查分別該加在哪裡。內容屬於教學和實務筆記。

<a name="results-anyone-can-check"></a>

### 人人都可驗證的結果

- [AlphaEvolve](https://arxiv.org/abs/2506.13131v1)（[結果](https://github.com/google-deepmind/alphaevolve_results)）：用自動評估器篩選演化出來的程式。數學構造及驗證程式碼已經公開；基礎設施方面的資料僅來自內部。🧾 [證據記錄](receipts/alphaevolve.md)
- [Mathematical exploration and discovery at scale](https://arxiv.org/abs/2511.02864v3)：將 AlphaEvolve 用於 67 道數學題，大部分題重新找到了已知最優解，有些題目得到更好的解。數學構造可以驗證，搜尋過程未公開。
- [Reinforced Generation of Combinatorial Structures](https://arxiv.org/abs/2509.18057v7)：根據系統找到的結構得出新的不可近似性界限，其正確性依賴作者的證明。系統還將自身的驗證流程加速至多 10,000 倍。
- [ShinkaEvolve](https://arxiv.org/abs/2509.19349v1)、[ThetaEvolve](https://arxiv.org/abs/2511.23473v1) 與 [TTT-Discover](https://arxiv.org/abs/2601.16175v2)：同類開放系統。後兩者用較小的開放模型和公開程式碼達到了報告中的已知最優界限。「已知最優」是逐題的結論，尚待外部確認。
- [OpenEvolve](https://github.com/algorithmicsuperintelligence/openevolve)：AlphaEvolve 設計的開源實作。結果發布在程式碼儲存庫中，沒有配套論文或外部稽核。
- [Self-Modifying Lean Proof Agents](https://arxiv.org/abs/2607.17352v1) 與 [Growing an Agent/Prover Interface](https://arxiv.org/abs/2609.39544v3)：研究能自我改進的證明代理，只有輸出通過證明檢查器才算成功。前者的基準隨代理一起演化，因此比較更難。

<a name="can-ai-do-ai-research"></a>

### AI 能做 AI 研究嗎？

- [RE-Bench](https://arxiv.org/abs/2411.15114v2)：七項研究工程任務，共 71 次人類專家嘗試。預算為兩小時時，代理得分更高；預算為 32 小時時則更低。這裡比較的是代理多次嘗試中的最好成績和人類的單次成績。
- [Measuring AI Ability to Complete Long Tasks](https://arxiv.org/abs/2503.14499v4)：代理以 50% 機率完成的任務時長，大約每七個月翻一倍。作者指出，這一趨勢在其任務集以外能否成立仍是開放問題。
- [PaperBench](https://arxiv.org/abs/2504.01848v3) 與 [CORE-Bench](https://arxiv.org/abs/2409.11363v2)：前者評估從頭重現已發表的研究（最佳代理 21.0%），後者評估用給定程式碼重現結果（最高難度 21%）。兩項得分都基於論文寫作時可用的模型。
- [The Automated LLM Speedrunning Benchmark](https://arxiv.org/abs/2506.22419v2)：即使給出詳細提示，代理仍難以重新實作已知的訓練加速方法。
- [MLS-Bench](https://arxiv.org/abs/2605.08678v3) 與 [AutoLab](https://arxiv.org/abs/2606.05080v1)：評估代理能否發明可泛化的方法，以及能否持續進行長時間最佳化。調整參數比發明新方法更容易，多數代理提早停止或耗盡預算。
- [Towards Execution-Grounded Automated AI Research](https://arxiv.org/abs/2601.14525v1)：在真實 GPU 上執行模型提出的研究想法。演化搜尋找到了優於兩種基準的做法；但用實際執行的獎勵訓練構想產生器後，產出集中在少數幾個點子。
- [The AI Scientist](https://arxiv.org/abs/2408.06292v3) 與 [Evaluating Sakana's AI Scientist](https://arxiv.org/abs/2502.14297v3)：前者是端對端的論文生成器；後者的獨立評估發現，42% 的實驗未能執行。🧾 [證據記錄](receipts/ai-scientist.md)

<a name="weights"></a>

### 模型權重

- [SEAL: Self-Adapting Language Models](https://arxiv.org/abs/2506.10943v2)（[程式碼](https://github.com/Continual-Intelligence/SEAL)）：模型生成自己的微調資料，並保留權重更新。小型任務上有效益，但隨著更新累積，模型會遺忘。🧾 [證據記錄](receipts/seal.md)
- [Escaping Model Collapse via Synthetic Data Verification](https://arxiv.org/abs/2510.16657v3)：用驗證器篩過的自生成資料重新訓練，起初有幫助，隨後受限於驗證器能辨別的內容，效益趨於停滯，甚至可能逆轉。證據來自線性設定下的理論及一項小規模實驗。
- [Frontis-MA1 / OpenMLE](https://arxiv.org/abs/2607.28568v1)：訓練模型執行程式演化步驟，區分模型和框架各自的貢獻。訓練資料與評估基準相互隔離，這一點來自作者自述。

<a name="risk-and-governance"></a>

### 風險與治理

- [Your Agent May Misevolve](https://arxiv.org/abs/2509.26354v2)：研究代理在演化記憶、工具和工作流程時會出現什麼問題：安全表現下降，並出現新的漏洞。結論僅涵蓋作者選擇研究的演化途徑。
- Anthropic · [When AI Builds Itself](https://www.anthropic.com/institute/recursive-self-improvement)：實驗室自行報告有多少研發工作由模型完成，並指出遞迴式自我改進「並非必然」。數字來自內部且未經稽核；頁面也承認程式碼行數並不是完備的衡量指標。
- Google DeepMind · [Frontier Safety Framework update](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)：針對可能加速 AI 研發的模型增加能力等級，但未公布量化門檻。

<a name="related-lists"></a>

### 相關清單

- [LobeHub Awesome RSI](https://github.com/lobehub/awesome-rsi)：涵蓋面廣，包括模型層、執行框架層、多代理、具身智慧、安全和工具。
- [Harness RSI Atlas](https://github.com/LucasXinYu/harness-rsi)：利用可追溯的證據資料集，比較執行框架層的改進機制。

<a name="make-your-own-receipt"></a>

## 製作自己的證據記錄

[用自己的資料測試一項修改](docs/your-first-receipt.md)提供了操作步驟：先定好什麼結果才值得保留修改，為兩個版本記錄相同的任務 ID，再執行：

```sh
python3 compare.py my-holdout.json
```

輸出會列出哪些任務由失敗轉為通過、哪些由通過轉為失敗，以及 `sign_test_p`：如果修改實際上沒有效果，出現這麼不對稱的變化有多常見。七個任務的結果發生變化，其中五項改善、兩項退步，這不足以說明修改有效。

<a name="contributing"></a>

## 貢獻

歡迎指正和新增證據記錄，也歡迎提交負面結果或尚無定論的結果。請先參考[證據記錄範本](receipts/TEMPLATE.md)和[貢獻指南](CONTRIBUTING.md)，然後執行：

```sh
python3 receipts.py lint && python3 receipts.py ledger && python3 -m unittest discover
```

<a name="license"></a>

## 授權條款

本儲存庫的原創檔案採用 [MIT 授權條款](LICENSE)，連結指向的作品遵循各自的授權條款。
