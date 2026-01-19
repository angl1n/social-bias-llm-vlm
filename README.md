<div align="center">
  <h1>Social Bias in LLMs and VLMs</h1>
  <img alt="papers" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fangl1n%2Fsocial-bias-llm-vlm%2Fmain%2Fbadges%2Fpapers.json" />
</div>
This curated list brings together key methods, datasets, and benchmarks related to social bias in LLMs and VLMs.

As multimodal models continue to advance, understanding, evaluating, and mitigating social bias has become an increasingly important research direction. This repository is intended as a practical index for researchers and engineers to quickly track relevant work and recent progress.

Contributions are welcome—feel free to open a Pull Request to add high-quality resources.




## Table of Contents
- [Social Bias in LLMs and VLMs](#social-bias-in-llms-and-vlms)
    - [Foundations](#foundations)
    - [Survey](#survey)
    - [Data & Benchmarks](#data--benchmarks)
    - [Mitigation](#mitigation)
    - [Findings](#findings)


## Foundations
### Sociology
| Title | Introduction | Date | Code |
| :--- | :---: | :---: | :---: |
| [![Publish](https://img.shields.io/badge/Journal-American%20Journal%20of%20Sociology'07-blue)]()<br/>[Getting a Job: Is There a Motherhood Penalty?](https://www.journals.uchicago.edu/doi/10.1086/511799) | Motherhood Penalty | 2007-03 | - |
| [![Publish](https://img.shields.io/badge/Journal-J%20Pers%20Soc%20Psychol'06-blue)]()<br/>[A Meta-Analytic Test of Intergroup Contact Theory](https://ideas.wharton.upenn.edu/wp-content/uploads/2018/07/Pettigrew-Tropp.pdf) | Contact Works | 2006-05 | - |
| [![Publish](https://img.shields.io/badge/Journal-American%20Economic%20Review'04-blue)]()<br/>[Are Emily and Greg More Employable Than Lakisha and Jamal? A Field Experiment](https://www.aeaweb.org/articles?id=10.1257/0002828042002561) | The Quality Paradox| 2004-09 | [Code](https://doi.org/10.3886/E116023V1) |
| [![Publish](https://img.shields.io/badge/Journal-J%20Pers%20Soc%20Psychol'98-blue)]()<br/>[Measuring Individual Differences in Implicit Cognition: The Implicit Association Test](https://faculty.washington.edu/agg/pdf/Gwald_McGh_Schw_JPSP_1998.OCR.pdf) | Latency is the Key | 1998-06 | - |
| [![Publish](https://img.shields.io/badge/Journal-American%20Sociological%20Review'97-blue)]()<br/>[Rethinking Racism: Toward a Structural Interpretation](https://newuniversityinexileconsortium.org/wp-content/uploads/2022/02/Eduardo-Bonilla-Silva-Rethinking-Racism-Toward-a-Structural-Interpretation.pdf) | Racialized Social System | 1997-06 | - |
| [![Publish](https://img.shields.io/badge/Journal-American%20Sociological%20Review'93-blue)]()<br/>[Opposition to Race-Targeting: Self-Interest, Stratification Ideology, or Racial Attitudes?](https://www.jstor.org/stable/pdf/2096070.pdf) | Self-Interest is weak |  1993-08 | - |
| [![Publish](https://img.shields.io/badge/Book-SAGE'91-blue)]()<br/>[Understanding Everyday Racism: An Interdisciplinary Theory](https://sk.sagepub.com/books/understanding-everyday-racism-an-interdisciplinary-theory) | Racism is Routine | 1991-07 | - |
| [![Publish](https://img.shields.io/badge/Journal-Pacific%20Sociological%20Review'58-blue)]()<br/>[Race Prejudice as a Sense of Group Position](https://journals.sagepub.com/doi/10.2307/1388607) | Group-level “sense of Position” | 1958-03 | - |
| [![Publish](https://img.shields.io/badge/Journal-Journal%20of%20Applied%20Sociology'25-blue)]()<br/>[Measuring Social Distances](https://brocku.ca/MeadProject/Bogardus/Bogardus_1925c.html) | Degree of Intimacy | 1925-03 | - |
### NLP (Pre-LLM)
| Title | Introduction | Date | Code |
| :--- | :---: | :---: | :---: |
| [![Publish](https://img.shields.io/badge/Conference-ACL'20-blue)]()<br/>[Language (Technology) is Power: A Critical Survey of “Bias” in NLP](https://aclanthology.org/2020.acl-main.485.pdf) | - | 2020-07 | - |
| [![Publish](https://img.shields.io/badge/Conference-ICCV'19-blue)]()<br/>[Balanced Datasets Are Not Enough: Estimating and Mitigating Gender Bias in Deep Image Representations](https://arxiv.org/pdf/1811.08489) | <img width="700" alt="image" src="figures/BalancedDatasetsAreNotEnough.png">| 2019-10 | [Github](https://github.com/uvavision/Balanced-Datasets-Are-Not-Enough) |


## Survey
### LLM Surveys
| Title | Introduction | Date | Code |
| :--- | :---: | :---: | :---: |
| [![Publish](https://img.shields.io/badge/Conference-CL'24-blue)]()<br/>[Bias and Fairness in Large Language Models: A Survey](https://arxiv.org/pdf/2309.00770) | <img width="700" alt="image" src="figures/BiasAndFairnessInLargeLanguageModels_ASurvey.png">| 2024-09 | [Github](https://github.com/i-gallegos/Fair-LLM-Benchmark) |
| [![Publish](https://img.shields.io/badge/Journal-ACM%20SIGKDD%20Explorations'24-blue)]()<br/>[Fairness in Large Language Models: A Taxonomic Survey](https://arxiv.org/pdf/2404.01349) | <img width="700" alt="image" src="figures/FairnessInLargeLanguageModels_ATaxonomicSurvey.png">| 2024-07 | - |
| [![Publish](https://img.shields.io/badge/Conference-ACL'22-blue)]()<br/>[An Empirical Survey of the Effectiveness of Debiasing Techniques for Pre-trained Language Models](https://arxiv.org/pdf/2110.08527) | -| 2022-05 | [Github](https://github.com/McGill-NLP/bias-bench) |
### VLMs Surveys
| Title | Introduction | Date | Code |
| :--- | :---: | :---: | :---: |
| [![Publish](https://img.shields.io/badge/Journal-ACM%20Computing%20Surveys'25-blue)]()<br/>[Fairness in Deep Learning: A Survey on Vision and Language Research](https://doi.org/10.1145/3637549) | <img width="700" alt="image" src="figures/FairnessInDeepLearning_Survey.png">| 2025-02 | - |
| [Survey of Social Bias in Vision-Language Models](https://arxiv.org/pdf/2309.14381) | <img width="700" alt="image" src="figures/SurveyOfSocialBiasInVisionLanguageModels.png">| 2023-09 | - |






## Data & Benchmarks
### LLMs
| Title | Introduction | Date | Code |
| :--- | :---: | :---: | :---: |
| [How Quantization Shapes Bias in Large Language Models](https://arxiv.org/pdf/2508.18088v2.pdf) | <img width="700" alt="image" src="figures/HowQuantizationShapesBiasInLLMs.png">| 2026-01 | [Github](https://github.com/insait-institute/quantization-affects-social-bias) |
| [![Publish](https://img.shields.io/badge/Conference-Findings%20of%20EMNLP'25-blue)]()<br/>[What’s Not Said Still Hurts: A Description-Based Evaluation Framework for Measuring Social Bias in LLMs](https://arxiv.org/pdf/2502.19749) | <img width="700" alt="image" src="figures/HiddenBiasBenchmark.png">| 2025-09 | [Github](https://github.com/JP-25/Hidden-Bias-Benchmark) |
| [![Publish](https://img.shields.io/badge/Conference-COLM'25-blue)]()<br/>[Investigating Intersectional Bias in Large Language Models using Confidence Disparities in Coreference Resolution](https://arxiv.org/pdf/2508.07111) | <img width="700" alt="image" src="figures/WinoIdentity.png">| 2025-08 | [Github](https://github.com/apple/ml-winoidentity) |
| [![Publish](https://img.shields.io/badge/Workshop-ICLR'25-blue)]()<br/>[MALIBU Benchmark: Multi-Agent LLM Implicit Bias Uncovered](https://arxiv.org/pdf/2507.01019) | <img width="700" alt="image" src="figures/MALIBU_Benchmark.png">| 2025-04 | - |
| [![Publish](https://img.shields.io/badge/Conference-Findings%20of%20NAACL'25-blue)]()<br/>[FLEX: A Benchmark for Evaluating Robustness of Fairness in Large Language Models](https://aclanthology.org/2025.findings-naacl.199.pdf) | <img width="700" alt="image" src="figures/FLEX_RobustnessOfFairness.png">| 2025-04 | [Github](https://github.com/ekgus9/FLEX) |
| [![Publish](https://img.shields.io/badge/Workshop-NeurIPS'24-blue)]()<br/>[Evaluating and Mitigating Discrimination in Language Model Decisions](https://arxiv.org/pdf/2312.03689) | <img width="700" alt="image" src="figures/EvaluatingAndMitigatingDiscriminationInLanguageModelDecisions.png">| 2024-12 | - |
| [![Publish](https://img.shields.io/badge/Conference-EMNLP'24-blue)]()<br/>[Towards Implicit Bias Detection and Mitigation in Multi-Agent LLM Interactions](https://arxiv.org/pdf/2410.02584) | <img width="700" alt="image" src="figures/MultiAgent_ImplicitBias.png">| 2024-10 | [Github](https://github.com/MichiganNLP/MultiAgent_ImplicitBias) |
| [![Publish](https://img.shields.io/badge/Conference-Findings%20of%20ACL'24-blue)]()<br/>[Ask LLMs Directly, “What shapes your bias? ”: Measuring Social Bias in Large Language Models](https://arxiv.org/pdf/2406.04064) | <img width="700" alt="image" src="figures/AskLLMsDirectly_WhatShapesYourBias.png">| 2024-08 | [Github(BBQ)](https://github.com/nyu-mll/BBQ/tree/main) |
| [![Publish](https://img.shields.io/badge/Conference-ACL'23-blue)]()<br/>[CHBias: Bias Evaluation and Mitigation of Chinese Conversational Language Models](https://arxiv.org/pdf/2305.11262) | <img width="700" alt="image" src="figures/CHBias.png">| 2023-05 | [Github](https://github.com/hyintell/CHBias) |
| [![Publish](https://img.shields.io/badge/Conference-Findings%20of%20ACL'22-blue)]()<br/>[BBQ: A Hand-Built Bias Benchmark for Question Answering](https://arxiv.org/pdf/2110.08193) | <img width="700" alt="image" src="figures/BBQ.png">| 2022-05 | [Github](https://github.com/nyu-mll/BBQ) |




### VLMs
| Title | Introduction | Date | Code |
| :--- | :---: | :---: | :---: |
| [![Publish](https://img.shields.io/badge/Conference-EMNLP'25-blue)]()<br/>[VISBIAS: Measuring Explicit and Implicit Social Biases in Vision Language Models](https://arxiv.org/pdf/2503.07575) | <img width="700" alt="image" src="figures/VisBias.png">| 2025-11 | [Github](https://github.com/uscnlp-lime/VisBias) |
| <br/>[VIGNETTE: Socially Grounded Bias Evaluation for Vision-Language Models](https://arxiv.org/pdf/2505.22897) | <img width="700" alt="image" src="figures/VIGNETTE.png">| 2025-05 | [Github](https://github.com/chahatraj/Vignette) |
| [![Publish](https://img.shields.io/badge/Conference-EMNLP'24-blue)]()<br/>[ModSCAN: Measuring Stereotypical Bias in Large Vision-Language Models  from Vision and Language Modalities](https://arxiv.org/pdf/2410.06967) | <img width="700" alt="image" src="figures/ModSCAN.png">| 2024-11 | [Github](https://github.com/TrustAIRLab/ModSCAN) |
| [![Publish](https://img.shields.io/badge/Conference-EMNLP'21-blue)]()<br/>[Are Gender-Neutral Queries Really Gender-Neutral? Mitigating Gender Bias in Image Search](https://arxiv.org/pdf/2109.05433) | <img width="700" alt="image" src="figures/AreGenderNeutralQueriesReallyGenderNeutral.png">| 2021-11 | [Github](https://github.com/eric-ai-lab/Mitigate-Gender-Bias-in-Image-Search) |



## Mitigation
| Title | Introduction | Date | Code |
| :--- | :---: | :---: | :---: |
| [![Publish](https://img.shields.io/badge/Conference-Findings%20of%20EMNLP'25-blue)]()<br/>[Open-DeBias: Toward Mitigating Open-Set Bias in Language Models](https://aclanthology.org/2025.findings-emnlp.1364.pdf) | <img width="700" alt="image" src="figures/OpenDeBias_OpenSetBias.png">| 2025-11 | [Resource](https://sites.google.com/view/open-debias25s)|
| [Debiasing Reward Models by Representation Learning with Guarantees](https://arxiv.org/pdf/2510.23751) | <img width="700" alt="image" src="figures/DebiasingRewardModels_RepresentationLearning_Guarantees.png">| 2025-10 | - |
| [![Publish](https://img.shields.io/badge/Workshop-NeurIPS'25-blue)]()<br/>[Robustly Improving LLM Fairness in Realistic Settings via Interpretability](https://openreview.net/pdf?id=fHBb8BisyW) | <img width="700" alt="image" src="figures/RobustlyImprovingLLMFairness_Interpretability.png">| 2025-09 | [Github](https://github.com/adamkarvonen/llm_bias) |
| [![Publish](https://img.shields.io/badge/Conference-NeurIPS'25-blue)]()<br/>[Guiding LLM Decision-Making with Fairness Reward Models](https://openreview.net/pdf/9c67b8ffdbef13dfa1266b41fef89b0ccc4f7f74.pdf) | <img width="700" alt="image" src="figures/GuidingLLMDecisionMaking_FairnessRewardModels.png">| 2025-09 | [Github](https://github.com/zarahall/fairness-prms) |
| [![Publish](https://img.shields.io/badge/Conference-IJCAI'25-blue)]()<br/>[Wisdom from Diversity: Bias Mitigation Through Hybrid Human-LLM Crowds](https://arxiv.org/pdf/2505.12349) | <img width="700" alt="image" src="figures/HybridCrowds.png">| 2025-08 | - |
| [![Publish](https://img.shields.io/badge/Conference-ACL'23-blue)]()<br/>[Prompt Tuning Pushes Farther, Contrastive Learning Pulls Closer: A Two-Stage Approach to Mitigate Social Biases](https://aclanthology.org/2023.acl-long.797.pdf) | <img width="700" alt="image" src="figures/PromptTuning_ContrastiveLearning_TwoStage.png">| 2023-07 | - |
| [![Publish](https://img.shields.io/badge/Conference-ACL'23-blue)]()<br/>[BLIND: Bias Removal With No Demographics](https://aclanthology.org/2023.acl-long.490.pdf) | <img width="700" alt="image" src="figures/BLIND.png">| 2023-07 | [Github](https://github.com/technion-cs-nlp/BLIND) |
| [![Publish](https://img.shields.io/badge/Conference-Findings%20of%20EMNLP'22-blue)]()<br/>[Don’t Just Clean It, Proxy Clean It: Mitigating Bias by Proxy in Pre-Trained Models](https://aclanthology.org/2022.findings-emnlp.372.pdf) | <img width="700" alt="image" src="figures/DontJustCleanIt_ProxyCleanIt.png">| 2022-12 | Data: <br/>[WIKI](https://github.com/conversationalai/unintended-ml-bias-analysis)<br/>[Madlibs](https://github.com/conversationalai/unintended-ml-bias-analysis/blob/main/archive/unintended_ml_bias/eval_datasets/bias_madlibs_89k.csv)<br/>[BIOS](https://github.com/microsoft/biosbias) |
| [![Publish](https://img.shields.io/badge/Conference-NeurIPS'20-blue)]()<br/>[Fairness without Demographics through Adversarially Reweighted Learning](https://arxiv.org/pdf/2006.13114) | <img width="700" alt="image" src="figures/FairnessWithoutDemographics_ARL.png">| 2020-11 | - |




## Findings
| Title | Introduction | Date | Code |
| :--- | :---: | :---: | :---: |
| [![Publish](https://img.shields.io/badge/Conference-EMNLP'24-blue)]()<br/>[Systematic Biases in LLM Simulations of Debates](https://arxiv.org/pdf/2402.04049) | <img width="700" alt="image" src="figures/Systematic_Biases_in_LLM_Simulations_of_Debates.png">| 2024-12 | - |
| [![Publish](https://img.shields.io/badge/Conference-ACL'22-blue)]()<br/>[Upstream Mitigation Is Not All You Need: Testing the Bias Transfer Hypothesis in Pre-Trained Language Models](https://aclanthology.org/2022.acl-long.247.pdf) | <img width="700" alt="image" src="figures/UpstreamMitigation_BiasTransferHypothesis.png">| 2022-05 | Adapted code:<br/>[HurtfulWords](https://github.com/MLforHealth/HurtfulWords) <br/> [sent_debias](https://github.com/pliang279/sent_debias) <br/>[biosbias](https://github.com/microsoft/biosbias) <br/> [unintended-ml-bias-analysis](https://github.com/conversationai/unintended-ml-bias-analysis) <br/> [roberta-base](https://huggingface.co/roberta-base) |
| [![Publish](https://img.shields.io/badge/Conference-EACL'21-blue)]()<br/>[Challenges in Automated Debiasing for Toxic Language Detection](https://aclanthology.org/2021.eacl-main.274.pdf) | <img width="700" alt="image" src="figures/ChallengesInAutomatedDebiasingForToxicLanguageDetection.png">| 2021-04 | [Github](https://github.com/XuhuiZhou/Toxic_Debias) |









---
---

<details>
<summary><b>Disclaimer</b></summary>

This repository is intended for educational and research purposes only. The images and figures displayed in this repository are the property of their respective authors and publishers and are used here for illustrative purposes to facilitate quick browsing and understanding of the papers.

If you are a copyright holder and would like any content removed, please open an issue, and I will remove it promptly.

</details>