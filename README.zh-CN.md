# Awesome RSI Receipts：递归自我改进证据清单 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<p align="center"><a href="README.md">English</a> | <b>简体中文</b> | <a href="README.zh-TW.md">繁體中文</a></p>

[![验证](https://github.com/orangejustin/awesome-rsi-receipts/actions/workflows/verify.yml/badge.svg)](https://github.com/orangejustin/awesome-rsi-receipts/actions/workflows/verify.yml)
[![链接检查](https://github.com/orangejustin/awesome-rsi-receipts/actions/workflows/links.yml/badge.svg)](https://github.com/orangejustin/awesome-rsi-receipts/actions/workflows/links.yml)
[![许可证：MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> 对于声称能自我改进的系统，先问三件事：改了什么？谁核验过？又有哪些地方退步了？

[一个调优后的运行框架（harness）](receipts/flashrsi-gepa.md)在原测试集上提高了 **12.34 分**，换到一个迁移测试集提高了 **10.83 分**，换到另一个却下降了 **14.00 分**。[一个自我改进的智能体](receipts/darwin-godel-machine.md)把通过率从 20% 提高到了 50%，但测的是 500 道题中的 200 道。[一个改进程序](receipts/stop.md)用强模型时越改越好，换成弱模型却越改越差。这些结果都是真的，但只看标题，很容易读出不一样的结论。

这里收集了 AI 智能体「递归自我改进」（RSI）主张背后的证据，并用同一套问题逐一核对。这里不是排行榜，也不会运行任何智能体。

**离线试一试**（Python 3.9+，无需安装依赖，也不需要 API 密钥）：

```sh
python3 compare.py examples/library-search.json
```

两个版本都通过了 4 道合成任务中的 2 道，但有一道从失败变成成功，另有一道从成功变成失败。把自己的改动前后结果交给这个脚本，就能看到哪些任务发生了翻转，以及这种差异是否可能只是巧合。

<a name="contents"></a>

## 目录

- [从这里开始](#start-here)
- [证据记录](#receipts)
- [资料来源](#sources)
  - [更简单的基线能做到同样好吗？](#would-a-simpler-baseline-do-as-well)
  - [基准真的测到了你想测的能力吗？](#is-the-benchmark-measuring-what-you-think)
  - [差异大于噪声吗？](#is-the-difference-bigger-than-the-noise)
  - [提升能迁移并持续吗？](#does-the-gain-carry-over-and-keep-going)
  - [能修改自身的智能体](#agents-that-edit-themselves)
  - [搜索与反馈](#search-and-feedback)
  - [运行框架设计](#harness-design)
  - [人人都可验证的结果](#results-anyone-can-check)
  - [AI 能做 AI 研究吗？](#can-ai-do-ai-research)
  - [模型权重](#weights)
  - [风险与治理](#risk-and-governance)
  - [相关清单](#related-lists)
- [制作自己的证据记录](#make-your-own-receipt)
- [贡献](#contributing)

<a name="start-here"></a>

## 从这里开始

| 你想做什么？ | 从哪里入手？ |
| --- | --- |
| **判断**刚读到的研究结论是否站得住脚 | [证据记录](#receipts)：对每项主张都问同样的七个问题，也记录哪些结论没有成立。 |
| **了解**自我改进智能体是怎么搭建和测试的 | [资料来源](#sources)：按问题查找论文、审计、基准和工具。 |
| 在自己的任务上**测试**一次提示词、工具或记忆改动 | [制作自己的证据记录](#make-your-own-receipt)：每次只改一件事，沿用同一组任务 ID，并事先订好去留标准。 |

<a name="receipts"></a>

## 证据记录

判断一项自我改进实验能说明什么，先看两个维度。一是**改了什么**：单个答案、程序、可复用的运行框架、模型权重，还是改进程序本身？二是**谁核验过**：只有作者报告，有人根据公开结果重算，有人独立复跑，还是任何人都能验证产物？目前的证据分布如下：

<!-- grid -->
| | 作者报告 | 根据公开结果重算 | 独立复跑 | 任何人都能核验产物 |
| --- | :---: | :---: | :---: | :---: |
| **单个答案** | · | · | 1 | · |
| **程序或证明** | 1 | · | · | 1 |
| **可复用运行框架** | 6 | 1 | 1 | · |
| **模型权重** | 1 | · | · | · |
| **改进程序本身** | 3 | · | · | · |
<!-- /grid -->

大多数证据集中在第一列。最后一行才是「递归」的关键：变得更好的是改进程序本身。但这一行的结果目前都只有作者核验过。

<!-- ledger -->
| 证据记录 | 采信前先问 | 改了什么 | 谁核验过 | 迁移表现 |
| --- | --- | --- | --- | --- |
| [The AI Scientist：外部评估发现了什么](receipts/ai-scientist.md) · 2025 | 独立评估者亲自运行系统时，发现了什么？ | 单个答案 | 独立复跑 | 未测试 |
| [AlphaEvolve：哪些结果可以亲自核验](receipts/alphaevolve.md) · 2025 | 不必相信作者，读者也能验证哪些结果？ | 程序或证明 | 任何人都能核验产物 | 未测试 |
| [代码演化与简单基线的对照](receipts/simple-baselines.md) · 2026 | 起作用的是搜索方法，还是问题的设定方式？ | 程序或证明 | 作者报告 | 未测试 |
| [ADAS：独立复跑时缩水的收益](receipts/adas.md) · 2024 | 换一个执行模型、保持相同预算，搜索得到的智能体还占优吗？ | 可复用运行框架 | 独立复跑 | 有得有失 |
| [Darwin Gödel Machine：在任务子集上从 20% 到 50%](receipts/darwin-godel-machine.md) · 2025 | 换到完整基准、其他模型或其他基准，还剩多少收益？ | 可复用运行框架 | 作者报告 | 有得有失 |
| [Huxley-Gödel Machine：自身得分高，不代表后代更好](receipts/huxley-godel-machine.md) · 2025 | 按基准得分选出的智能体，也是最有可能产生更好后代的那个吗？ | 可复用运行框架 | 作者报告 | 有得有失 |
| [SICA：一次运行，五十道任务](receipts/sica.md) · 2025 | 在 50 道任务上提高了 36 分，其中有多少真是智能体变聪明了？ | 可复用运行框架 | 作者报告 | 未测试 |
| [失败反馈修复了触发它的失败吗？](receipts/failure-feedback.md) · 2026 | 某道任务失败后触发的改动，修好那道任务了吗？ | 可复用运行框架 | 根据公开结果重算 | 收益未能保持 |
| [FlashRSI：同一套运行框架，三种结果](receipts/flashrsi-gepa.md) · 2026 | 在没参与调优的另一类任务上，这套运行框架还有用吗？ | 可复用运行框架 | 作者报告 | 有得有失 |
| [演化运行框架，还是多试几次？](receipts/matched-budget.md) · 2026 | 如果给原有运行框架同样的预算和反馈，它能不能做得一样好？ | 可复用运行框架 | 作者报告 | 有得有失 |
| [从失败中总结经验，与不看失败的同一种搜索相比](receipts/failure-traces.md) · 2026 | 有多少收益来自看到失败记录，又有多少只是因为多尝试、保留得分更高的版本？ | 可复用运行框架 | 作者报告 | 收益未能保持 |
| [SEAL：自己编写训练数据的模型](receipts/seal.md) · 2025 | 随着模型自行生成的更新不断累积，先前学到的知识会怎样？ | 模型权重 | 作者报告 | 未测试 |
| [STOP：让改进程序改进自身](receipts/stop.md) · 2023 | 换成较弱的底层模型，自我改进还有效吗？ | 改进程序本身 | 作者报告 | 有得有失 |
| [Gödel Agent：改写负责改写的程序](receipts/godel-agent.md) · 2024 | 一个能修改自身改进循环的智能体，有多大概率越改越差？ | 改进程序本身 | 作者报告 | 未测试 |
| [Flex-RSI：让改进程序修改自身](receipts/flex-rsi.md) · 2026 | 是改进程序变强了，还是只是多试了几次修改运行框架？ | 改进程序本身 | 作者报告 | 未测试 |
<!-- /ledger -->

**迁移表现**记录收益是否出现在用于筛选改动的任务之外，例如换一套基准、换一个模型，或使用预先留出的任务族。

<a name="sources"></a>

## 资料来源

每个条目介绍资料是什么，以及它的证据能支持到哪一步。除非另有说明，结果均来自原作者，本清单没有重新运行实验。标有 🧾 的条目附有证据记录。

<a name="would-a-simpler-baseline-do-as-well"></a>

### 更简单的基线能做到同样好吗？

- [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227v4)：在把收益归功于框架演化之前，先给固定框架可比的反馈和额外尝试机会。演化在 Terminal-Bench 2.1 上不及单纯增加测试时计算量，却在长程游戏里胜出，说明结果取决于任务。🧾 [证据记录](receipts/matched-budget.md)
- [Simple Baselines are Competitive with Code Evolution](https://arxiv.org/abs/2602.16805v2)：在相同的搜索空间下，两种简单基线与复杂的代码演化流程持平或更好。结果更应归功于问题的定义方式，而不是搜索算法。🧾 [证据记录](receipts/simple-baselines.md)
- [Agent Self-Improvement with Frozen Weights](https://arxiv.org/abs/2611.11342v2)：对比使用失败经验总结与看不到失败信息的同一搜索流程。看到失败记录额外带来 4.0 个百分点；约 60% 的总提升来自尝试并保留得分更高的版本。仅测试了一个模型。🧾 [证据记录](receipts/failure-traces.md)
- [Does Failure Feedback Direct Agent Self-Modification?](https://arxiv.org/abs/2610.14662v1)：用公开日志重新计算：由某个失败触发的修改，是否能修复那个失败？它修复触发该修改的失败，并不比修复其他失败更频繁。这并不否定筛选能提高总体表现。🧾 [证据记录](receipts/failure-feedback.md)
- [BOXBOX](https://arxiv.org/abs/2611.09218v3)：在耗时相同的条件下，将在线修改框架与固定框架、离线演化及增加计算量的基线比较。在一个长程软件任务内适应，不等于跨任务累积收益。
- [AI Research Agents for Machine Learning: Search, Exploration, and Generalization in MLE-bench](https://arxiv.org/abs/2507.02554v2)：将搜索策略与修改算子集合分开，表明两者的搭配很重要（在 MLE-bench lite 上，Kaggle 获奖牌率由 39.6% 提升到 47.7%）。基准已公开，无法排除数据污染。
- [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089v2)：一项随机试验：开发者预计 AI 工具会让自己快 24%，实际却慢了 19%。虽然不是关于自我改进的研究，却直观说明实测效果可以和所有人的预期相反。

<a name="is-the-benchmark-measuring-what-you-think"></a>

### 基准真的测到了你想测的能力吗？

- [Establishing Best Practices for Building Rigorous Agentic Benchmarks](https://arxiv.org/abs/2507.02825v5)：审查常用的智能体基准，发现任务设计和评分方式有缺陷，报告的性能相对误差最高可达 100%。附有核对清单；是方法指南，不是工具。
- [The SWE-Bench Illusion](https://arxiv.org/abs/2506.12286v4)：仅看 issue 文本，模型就在 SWE-bench Verified 上有 76% 的概率指出含 bug 的文件，而在该基准之外的仓库上是 53%。这是记忆现象的间接证据，不能证明某个具体模型记住了答案。
- [The More You Automate, the Less You See](https://arxiv.org/abs/2509.08713v2)：区分自动化研究流程的四种失效模式：基准选取、数据泄漏、指标误用、事后筛选。研究表明，要靠日志和代码而不是最终论文才能发现这些问题。只研究了两个系统。
- [Auditing Harness Tampering in Self-Improving Agents](https://arxiv.org/abs/2609.00069v1)：在实际运行中发现一些自我修改只提高分数，没有提高能力，而且往往出现在最终胜出智能体的演化谱系里。审计方法也是由原作者自己评测的。
- [PostTrainBench](https://arxiv.org/abs/2603.08640v2)：给智能体 10 个 GPU 小时做模型后训练。最佳结果是 23.2%，官方指令微调模型则达到 51.1%。部分智能体使用了测试集训练，或用了自己找到的 API 密钥。
- [The Meta-Agent Challenge](https://arxiv.org/abs/2606.04455v1)：元智能体必须构建一个能在留出任务上取得好成绩的智能体。很少有系统达到人类构建的基线，优化压力还导致了一些尝试提取标准答案的行为。
- [Holistic Agent Leaderboard](https://arxiv.org/abs/2510.11977v1)：覆盖 9 个模型和 9 套基准的 21,730 次运行，完整日志公开。日志揭示，有的智能体不解题，而是上网搜基准。
- Anthropic · [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) 和 [Quantifying infrastructure noise](https://www.anthropic.com/research/infrastructure-noise)：给实际结果评分，不要给智能体的自我报告评分；固定运行环境和时间限制。仅资源配置的变化就让某个编程基准的成绩浮动了几个百分点。

<a name="is-the-difference-bigger-than-the-noise"></a>

### 差异大于噪声吗？

- [Adding Error Bars to Evals](https://arxiv.org/abs/2411.00640v1)：提供计算误差条、做配对比较，以及估算评测题量的公式。依赖大样本近似。
- [Don't Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints](https://arxiv.org/abs/2503.01747v3)：指出这些近似在小基准上会低估误差条，并附上实现替代方法的[库](https://github.com/sambowyer/bayes_evals)。这是一篇立场论文。
- [Measuring all the noises of LLM Evals](https://arxiv.org/abs/2512.21326v3)：区分模型作答的波动与选题带来的波动，发现配对比较中的前者通常更大，因此取多次运行的平均值能提高统计检验的功效。
- [SAGE: A Statistical Acceptance Gate for Self-Evolving Agents](https://arxiv.org/abs/2609.36043v1)：用逐题配对检验替代「只要提高均分就接受」，因为在小而有噪声的数据集上选出的最高分会偏高。20 种设置中有 19 种的退化减少了。
- [Trustworthy Recursive Self-Improvement with Statistical Guarantees](https://arxiv.org/abs/2611.10787v1)：提出一种限制被接受改动中实际表现更差的比例的准入规则。对照的贪心规则是 45.59%，该方法是 2.78%。保证仅在给定假设下成立。
- [GUARD](https://arxiv.org/abs/2611.23476v1)：将新出现的退化与此前未解决的失败分开追踪。不退化保证只覆盖用于准入判定的缓冲区，不覆盖未见过的任务。
- [On The Statistical Limits of Self-Improving Agents](https://arxiv.org/abs/2510.04399v3)：理论结果：如果自我修改能使智能体的容量无界增长，原本可学习的任务可能变得不可学习。未做实证检验。

<a name="does-the-gain-carry-over-and-keep-going"></a>

### 提升能迁移并持续吗？

- [FlashRSI](https://github.com/RUC-NLPIR/FlashRSI/blob/560f02dfaa415be808647ae4c70d149423879cba/README.md#overall-results)：将筛选出的框架直接迁到其他任务族，不重新调优。同一框架在一类任务上有帮助，在另一类上却有损害。🧾 [证据记录](receipts/flashrsi-gepa.md)
- [RRSI](https://arxiv.org/abs/2609.24972v3)（[代码](https://github.com/google-research/rrsi)）：筛选时排除只对某套基准有效的修改。开发任务的覆盖率不能替代最终逐题配对比较的正确率。
- [Self-Improvement Memory](https://arxiv.org/abs/2611.18856v1)：切换任务或模型时，除了继承框架，还继承以往修改的原因、预期和实际结果。只测试了兼容的切换，没有测试跨领域迁移。
- [RSIBench-Data](https://arxiv.org/abs/2607.25886v1)：固定技术栈和预算，评估智能体改善训练数据的能力。58.33% 的设置在首次有效尝试中取得提升；越过最佳分数后仍继续搜索的实验，最终有 78.26% 的成绩下降了。
- [SelfImprove-Bench](https://arxiv.org/abs/2611.02797v1)：用五个层级的泛化测试区分能力提升与对特定情景的拟合。现有方法的收益在不同层级不一致。以游戏为基础。
- [Continual Learning Exam](https://arxiv.org/abs/2610.33956v1)：用 600 个关卡测量从经验中提高表现、同时保留所学的能力。反馈和修订带来的提升中位数为 5.3 个百分点；最佳系统通过 47.7% 的关卡。由模型评分。
- [Evo-Bench](https://arxiv.org/abs/2608.09096v2) 和 [HarnessOpt-Bench](https://arxiv.org/abs/2608.06301v1)：两个基准都试图区分改进框架的能力与基础模型实力，后者使用封闭的测试集。提升随任务和随机种子而大幅变化。
- [AI4AI at Test-Time](https://arxiv.org/abs/2608.12307v1)：较强的模型给较弱的模型编写框架，使后者的分数接近翻倍。作者将收益归因于确定性代码、针对基准的路由和答案格式，而非推理能力变强。

<a name="agents-that-edit-themselves"></a>

### 能修改自身的智能体

- [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954v3)（[代码](https://github.com/jennyzzt/dgm)）：编程智能体重写自己的代码，并归档不同版本。最醒目的数字来自任务子集；迁移时，在一套基准上提升明显，在另一套上提升不大。🧾 [证据记录](receipts/darwin-godel-machine.md)
- [Huxley-Gödel Machine](https://arxiv.org/abs/2510.21614v3)（[代码](https://github.com/metauto-ai/HGM)）：某个智能体自身的得分并不能很好预测其后代的质量，因此改用后代的表现来筛选。它相对早期方法的领先，仅是单次运行中多解决了两道任务。🧾 [证据记录](receipts/huxley-godel-machine.md)
- [SICA](https://arxiv.org/abs/2504.15228v2)（[代码](https://github.com/MaximeRobeyns/self_improving_coding_agent)）：不设独立的元智能体：由迄今表现最好的智能体编写下一代。仅在 50 道任务上运行一次，早期收益大多来自速度和成本的改善。🧾 [证据记录](receipts/sica.md)
- [Gödel Agent](https://arxiv.org/abs/2410.04444v4)（[代码](https://github.com/Arvid-pku/Godel_Agent)）：修改自身正在运行的代码，包括负责改进的例程。100 次试验中，有 14% 的最终表现低于起点。🧾 [证据记录](receipts/godel-agent.md)
- [STOP](https://arxiv.org/abs/2310.02304v3)（[代码](https://github.com/microsoft/stop)）：让改进程序处理自己的源代码。在 GPT-4 上有效，换用较弱的模型时表现下降；研究也统计了生成代码尝试脱离沙箱的频率。🧾 [证据记录](receipts/stop.md)
- [ADAS](https://arxiv.org/abs/2408.08435v2)（[代码](https://github.com/ShengranHu/ADAS)）：一个固定的元智能体用代码编写新智能体。后来两个团队用其他模型重新运行，发现收益很小，甚至为负。🧾 [证据记录](receipts/adas.md)
- [Flex-RSI](https://arxiv.org/abs/2611.08946v1)：在这个基准中，改进程序既可以编辑执行器，也可以编辑自身。结果表明允许编辑比不允许编辑好，但没有单独验证改进程序本身是否变得更强。🧾 [证据记录](receipts/flex-rsi.md)
- [Hyperagents](https://arxiv.org/abs/2603.19461v2)：让修改智能体的流程本身也可以被编辑，作者报告这一层的改进可以跨领域迁移。「自我加速」只是提出的可能性，并非测得的结果。
- [Recursive self-improvement of AI research agents](https://arxiv.org/abs/2609.26457v1)：研究智能体在一次为期八天的运行中修改自身代码，找到七项连续改进，在四个留出基准上均成立。只有一次运行；与生产用智能体的比较使用的是作者自己的任务集。
- [Evaluation-Free Recursive Self-Improvement for Coding Agents](https://arxiv.org/abs/2611.21056v1)：只做有效性检查，不在循环中评估任务表现，也能让编程智能体从 60.0% 提升到 85.6%；两种使用任务评估的方法分别达到 86.7% 和 88.3%。
- [Mendel Gödel Machine](https://arxiv.org/abs/2608.07645v1) 与 [Red Queen Gödel Machine](https://arxiv.org/abs/2606.26294v3)：修改智能体时同时利用多条轨迹，或借鉴另一个谱系，并让评估器与智能体共同演化。评估器也在变，因此更难与其他论文对比。
- [HELIX](https://arxiv.org/abs/2608.13951v1)：为固定模型演化运行框架，并保留相互匹配的运行轨迹，作为下一版模型的训练数据。仅一轮，仅限代码修复；单个最优框架提升了 4.0%。

<a name="search-and-feedback"></a>

### 搜索与反馈

- [GEPA](https://arxiv.org/abs/2507.19457v2)（[代码](https://github.com/gepa-ai/gepa)）：依据失败轨迹修改提示词，而不只看分数。它支持的是在该实验方案下优化提示词的效果，不能用于比较运行框架或权重更新方法。
- [Meta-Harness](https://arxiv.org/abs/2603.28052v1)（[代码](https://github.com/stanford-iris-lab/meta-harness)）：将之前的框架改动和完整运行轨迹提供给生成改动建议的模块。在框架代码上进行搜索，并不表明这个模块本身变得更强。
- [Agentic Context Engineering](https://arxiv.org/abs/2510.04618v3)：让上下文演化，并提出「上下文坍塌」：反复改写会逐渐抹去细节。模型权重没有变化。
- OpenAI · [Build an agent improvement loop with traces, evals, and Codex](https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop)：把轨迹中反复出现的失败变成回归测试用例，做一项经过审查的改动，再重新运行评测。这是用合成任务演示的完整示例，不是有对照的基准实验。

<a name="harness-design"></a>

### 运行框架设计

- OpenAI · [Harness engineering](https://openai.com/index/harness-engineering/)：将反复出现的失败写成智能体可以运行的静态检查规则或测试，并提供具体的修复提示。这是第一方的案例研究，没有单独估计框架的贡献。
- Anthropic · [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents)：借助进度日志和干净的代码提交继续工作，而不是直接重启。能跨会话接着做，不代表改进程序本身变得更强。
- Anthropic · [The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory)：比较可搜索的会话记录、提炼后的笔记，以及在会话间准备的笔记会带来什么变化。记得更好，不等于改得更好。
- [WalkingLabs](https://github.com/walkinglabs/learn-harness-engineering)、[LangChain's harness anatomy](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) 与 [Mitchell Hashimoto's adoption notes](https://mitchellh.com/writing/my-ai-adoption-journey)：构建小型运行框架时，工具、上下文和检查分别该加在哪里。内容属于教程和实践笔记。

<a name="results-anyone-can-check"></a>

### 人人都可验证的结果

- [AlphaEvolve](https://arxiv.org/abs/2506.13131v1)（[结果](https://github.com/google-deepmind/alphaevolve_results)）：用自动评估器筛选演化出来的程序。数学构造及验证代码已经公开；基础设施方面的数据仅来自内部。🧾 [证据记录](receipts/alphaevolve.md)
- [Mathematical exploration and discovery at scale](https://arxiv.org/abs/2511.02864v3)：将 AlphaEvolve 用于 67 道数学题，大部分题重新找到了已知最优解，若干题有所突破。数学构造可以验证，搜索过程未公开。
- [Reinforced Generation of Combinatorial Structures](https://arxiv.org/abs/2509.18057v7)：根据系统找到的结构得出新的不可近似性界限，其正确性依赖作者的证明。系统还将自身的验证流程加速至多 10,000 倍。
- [ShinkaEvolve](https://arxiv.org/abs/2509.19349v1)、[ThetaEvolve](https://arxiv.org/abs/2511.23473v1) 与 [TTT-Discover](https://arxiv.org/abs/2601.16175v2)：同类开放系统。后两者用较小的开放模型和公开代码达到了报告中的已知最优界限。「已知最优」是逐题的结论，尚待外部确认。
- [OpenEvolve](https://github.com/algorithmicsuperintelligence/openevolve)：AlphaEvolve 设计的开源实现。结果发布在代码仓库中，没有配套论文或外部审计。
- [Self-Modifying Lean Proof Agents](https://arxiv.org/abs/2607.17352v1) 与 [Growing an Agent/Prover Interface](https://arxiv.org/abs/2609.39544v3)：研究能自我改进的证明智能体，只有输出通过证明检查器才算成功。前者的基准随智能体一起演化，因此比较更难。

<a name="can-ai-do-ai-research"></a>

### AI 能做 AI 研究吗？

- [RE-Bench](https://arxiv.org/abs/2411.15114v2)：七项科研工程任务，共 71 次人类专家尝试。预算为两小时时，智能体得分更高；预算为 32 小时时则更低。这里比较的是智能体多次尝试中的最好成绩和人类的单次成绩。
- [Measuring AI Ability to Complete Long Tasks](https://arxiv.org/abs/2503.14499v4)：智能体以 50% 概率完成的任务时长，大约每七个月翻一倍。作者指出，这一趋势在其任务集以外能否成立仍是开放问题。
- [PaperBench](https://arxiv.org/abs/2504.01848v3) 与 [CORE-Bench](https://arxiv.org/abs/2409.11363v2)：前者考查从零复现已发表的研究（最佳智能体 21.0%），后者考查用给定代码复现结果（最高难度 21%）。两项得分都基于论文写作时可用的模型。
- [The Automated LLM Speedrunning Benchmark](https://arxiv.org/abs/2506.22419v2)：即使给出详细提示，智能体仍难以重新实现已知的训练加速方法。
- [MLS-Bench](https://arxiv.org/abs/2605.08678v3) 与 [AutoLab](https://arxiv.org/abs/2606.05080v1)：考查智能体能否发明可泛化的方法，以及能否持续进行长时间优化。调参比发明新方法更容易，多数智能体提前停止或耗尽预算。
- [Towards Execution-Grounded Automated AI Research](https://arxiv.org/abs/2601.14525v1)：在真实 GPU 上运行模型提出的研究想法。演化搜索找到了超过两个基线的方法；但用实际执行的奖励训练点子生成器后，产出收敛到少数几个点子。
- [The AI Scientist](https://arxiv.org/abs/2408.06292v3) 与 [Evaluating Sakana's AI Scientist](https://arxiv.org/abs/2502.14297v3)：前者是端到端的论文生成器；后者的独立评估发现，42% 的实验未能运行。🧾 [证据记录](receipts/ai-scientist.md)

<a name="weights"></a>

### 模型权重

- [SEAL: Self-Adapting Language Models](https://arxiv.org/abs/2506.10943v2)（[代码](https://github.com/Continual-Intelligence/SEAL)）：模型生成自己的微调数据，并保留权重更新。小型任务上有收益，但随着更新累积，模型会遗忘。🧾 [证据记录](receipts/seal.md)
- [Escaping Model Collapse via Synthetic Data Verification](https://arxiv.org/abs/2510.16657v3)：用验证器筛过的自生成数据重新训练，起初有帮助，随后受限于验证器能辨别的内容，收益趋于停滞，甚至可能逆转。证据来自线性设定下的理论及一项小规模实验。
- [Frontis-MA1 / OpenMLE](https://arxiv.org/abs/2607.28568v1)：训练模型执行程序演化步骤，区分模型和框架各自的贡献。训练数据与评估基准相互隔离，这一点来自作者声明。

<a name="risk-and-governance"></a>

### 风险与治理

- [Your Agent May Misevolve](https://arxiv.org/abs/2509.26354v2)：研究智能体在演化记忆、工具和工作流程时会出现什么问题：安全表现下降，并出现新的漏洞。结论仅覆盖作者选择研究的演化途径。
- Anthropic · [When AI Builds Itself](https://www.anthropic.com/institute/recursive-self-improvement)：实验室自行报告有多少研发工作由模型完成，并指出递归式自我改进「并非必然」。数字来自内部且未经审计；页面也承认代码行数并不是完善的衡量指标。
- Google DeepMind · [Frontier Safety Framework update](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)：针对可能加速 AI 研发的模型增加能力等级，但未公布量化阈值。

<a name="related-lists"></a>

### 相关清单

- [LobeHub Awesome RSI](https://github.com/lobehub/awesome-rsi)：覆盖面广，包括模型层、运行框架层、多智能体、具身智能、安全和工具。
- [Harness RSI Atlas](https://github.com/LucasXinYu/harness-rsi)：利用可追溯的证据数据集，比较运行框架层的改进机制。

<a name="make-your-own-receipt"></a>

## 制作自己的证据记录

[用自己的数据测试一项改动](docs/your-first-receipt.md)提供了操作步骤：先定好什么结果才值得保留改动，为两个版本记录相同的任务 ID，再运行：

```sh
python3 compare.py my-holdout.json
```

输出会列出哪些任务由失败转为通过、哪些由通过转为失败，以及 `sign_test_p`：如果改动本来没有效果，出现这么偏向一边的变化有多常见。七个任务的结果发生变化，其中五个向好、两个向坏，这不足以说明改动有效。

<a name="contributing"></a>

## 贡献

欢迎纠错和新增证据记录，也欢迎提交负面结果或尚无定论的结果。请先参考[证据记录模板](receipts/TEMPLATE.md)和[贡献指南](CONTRIBUTING.md)，然后运行：

```sh
python3 receipts.py lint && python3 receipts.py ledger && python3 -m unittest discover
```

<a name="license"></a>

## 许可证

本仓库的原创文件采用 [MIT 许可证](LICENSE)，链接指向的作品遵循各自的许可条款。
