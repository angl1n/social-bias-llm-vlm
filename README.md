<div align="center">
    <h1>Social Bias in LLMs and VLMs</h1>
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




## Survey
| Title | Introduction | Date | Code |
| :--- | :---: | :---: | :---: |
|






## Data & Benchmarks
### VLMs
| Title | Introduction | Date | Code |
| :--- | :---: | :---: | :---: |
| [![Publish](https://img.shields.io/badge/Conference-EMNLP'25-blue)]()<br/>[VISBIAS: Measuring Explicit and Implicit Social Biases in Vision Language Models](https://arxiv.org/pdf/2503.07575) | <img width="700" alt="image" src="figures/VisBias.png">| 2025-11 | [Github](https://github.com/uscnlp-lime/VisBias) |
| <br/>[VIGNETTE: Socially Grounded Bias Evaluation for Vision-Language Models](https://arxiv.org/pdf/2505.22897) | <img width="700" alt="image" src="figures/VIGNETTE.png">| 2025-05 | [Github](https://github.com/chahatraj/Vignette) |
| [![Publish](https://img.shields.io/badge/Conference-EMNLP'24-blue)]()<br/>[ModSCAN: Measuring Stereotypical Bias in Large Vision-Language Models  from Vision and Language Modalities](https://arxiv.org/pdf/2410.06967) | <img width="700" alt="image" src="figures/ModSCAN.png">| 2024-11 | [Github](https://github.com/TrustAIRLab/ModSCAN) |
### LLMs
| Title | Introduction | Date | Code |
| :--- | :---: | :---: | :---: |
| [![Publish](https://img.shields.io/badge/Workshop-ICLR'25-blue)]()<br/>[MALIBU Benchmark: Multi-Agent LLM Implicit Bias Uncovered](https://arxiv.org/pdf/2507.01019) | <img width="700" alt="image" src="figures/MALIBU_Benchmark.png">| 2025-04 | - |
| [![Publish](https://img.shields.io/badge/Workshop-NeurIPS'24-blue)]()<br/>[Evaluating and Mitigating Discrimination in Language Model Decisions](https://arxiv.org/pdf/2312.03689) | <img width="700" alt="image" src="figures/EvaluatingAndMitigatingDiscriminationInLanguageModelDecisions.png">| 2024-12 | - |
| [![Publish](https://img.shields.io/badge/Conference-EMNLP'24-blue)]()<br/>[Towards Implicit Bias Detection and Mitigation in Multi-Agent LLM Interactions](https://arxiv.org/pdf/2410.02584) | <img width="700" alt="image" src="figures/MultiAgent_ImplicitBias.png">| 2024-10 | [Github](https://github.com/MichiganNLP/MultiAgent_ImplicitBias) |
| [![Publish](https://img.shields.io/badge/Conference-Findings%20of%20ACL'24-blue)]()<br/>[Ask LLMs Directly, “What shapes your bias? ”: Measuring Social Bias in Large Language Models](https://arxiv.org/pdf/2406.04064) | <img width="700" alt="image" src="figures/AskLLMsDirectly_WhatShapesYourBias.png">| 2024-08 | [Github(BBQ)](https://github.com/nyu-mll/BBQ/tree/main) |
| [![Publish](https://img.shields.io/badge/Conference-Findings%20of%20ACL'22-blue)]()<br/>[BBQ: A Hand-Built Bias Benchmark for Question Answering](https://arxiv.org/pdf/2110.08193) | <img width="700" alt="image" src="figures/BBQ.png">| 2022-05 | [Github](https://github.com/nyu-mll/BBQ) |

## Mitigation
| Title | Introduction | Date | Code |
| :--- | :---: | :---: | :---: |
| [![Publish](https://img.shields.io/badge/Conference-IJCAI'25-blue)]()<br/>[Wisdom from Diversity: Bias Mitigation Through Hybrid Human-LLM Crowds](https://arxiv.org/pdf/2505.12349) | <img width="700" alt="image" src="figures/HybridCrowds.png">| 2025-08 | - |
| [![Publish](https://img.shields.io/badge/Conference-EMNLP'21-blue)]()<br/>[Are Gender-Neutral Queries Really Gender-Neutral? Mitigating Gender Bias in Image Search](https://arxiv.org/pdf/2109.05433) | <img width="700" alt="image" src="figures/AreGenderNeutralQueriesReallyGenderNeutral.png">| 2021-11 | [Github](https://github.com/eric-ai-lab/Mitigate-Gender-Bias-in-Image-Search) |



## Findings
| Title | Introduction | Date | Code |
| :--- | :---: | :---: | :---: |
| [![Publish](https://img.shields.io/badge/Conference-EMNLP'24-blue)]()<br/>[Systematic Biases in LLM Simulations of Debates](https://arxiv.org/pdf/2402.04049) | <img width="700" alt="image" src="figures/Systematic_Biases_in_LLM_Simulations_of_Debates.png">| 2024-12 | - |