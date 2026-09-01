
# Capstone Proposal
## Multi-Agent RAG Under Misinformation: Do Verification Architectures Improve Abstention or Amplify Poisoned Evidence?
### Proposed by: Dr. Amir Jafari
#### Email: ajafari@gwu.edu
#### Advisor: Amir Jafari
#### The George Washington University, Washington DC  
#### Data Science Program


## 1 Objective:  

            The objective of this project is to systematically evaluate whether different forms of multi-agent reasoning improve robustness to poisoned retrieved evidence compared with a single-agent RAG baseline. The central 
            research question is:
            
            When retrieved evidence is missing, do multi-agent verification architectures improve appropriate abstention compared with single-agent RAG, or do they amplify and create misinformation into confident 
            consensus? Does this hold when testing against different multi-agent forms? Does multi-hop reasoning worsen the odds of hallucinating missing evidence?
            
            The study will construct controlled RAG evaluation conditions using paired clean and poisoned versions of MuSiQue questions. The underlying question and ground-truth answer will remain fixed while critical
            retrieved evidence is manipulated to support a plausible but incorrect conclusion. This paired design will allow the effect of evidence poisoning to be measured independently of question difficulty.
            A single-agent RAG system will serve as the experimental baseline. Three families of multi-agent architectures will then be evaluated, representing different mechanisms through which multiple agents might 
            improve or degrade robustness:
            - Critique-based architectures, in which a solver's answer and supporting evidence are evaluated by a critic before revision or abstention.
            - Independent-agent architectures, in which multiple agents reason separately before their answers are combined through voting or another aggregation mechanism.
            - Interactive architectures, in which agents exchange information through discussion, debate, or consensus formation before producing a final answer.
            These architectures test three distinct mechanisms for multi-agent verification: explicit critique, independent reasoning and redundancy, and inter-agent communication. Comparing them under the same clean and 
            missing evidence conditions will allow the study to investigate not only whether multi-agent systems are more robust than single-agent RAG, but which forms of multi-agent interaction are responsible for robustness 
            or misinformation amplification.
            Another design feature, will be the systematic manipulation of what evidence is removed. That meaning, sometimes the entire evidence bit will be removed, while other times we may break the multi-hop chain so the model can't
            actually find the piece of evidence within the evidence documents.
            The primary outcomes will be answer correctness, missing-evidence adoption, and appropriate abstention. Secondary outcomes will include unsupported-answer rate, agent agreement and disagreement, evidence attribution, 
            and the frequency with which multiple agents converge on the same incorrect answer. For interactive architectures, changes in agent answers before and after communication will also be measured to determine whether 
            interaction corrects or propagates misinformation. We also will track if certain methods for removing evidence are more likely to lead to hallucinations or incorrect consensus.
            Key Objectives:
            1. Build a reproducible paired benchmark in which MuSiQue retrieval evidence can be systematically removed while preserving the original question and known ground-truth answer.
            2. Establish a single-agent RAG baseline for measuring the effect of missing retrieval evidence.
            3. Evaluate critique-based multi-agent architectures to determine whether explicit verification and revision improve robustness to missing evidence.
            4. Evaluate independent-agent architectures to determine whether independent reasoning and aggregation reduce correlated errors and missing-answer adoption.
            5. Evaluate interactive multi-agent architectures to determine whether communication and consensus help agents correct misinformation or cause incorrect beliefs to propagate between agents when evidence is missing.
            6. Compare the three multi-agent architecture families against the single-agent baseline under identical clean and missing evidence conditions.
            7. Measure missing evidence amplification by determining whether multi-agent interaction increases the frequency, consistency, or convergence of incorrect answers supported by missing evidence.
            8. Analyze which architectural mechanisms -- critique, independent reasoning, voting or aggregation, and inter-agent communication -- are associated with greater robustness or greater susceptibility to missing 
            evidence.
            9. Determine which evidence removal strategies are most likely to induce hallucinations or incorrect consensus.
            10. Produce practical design recommendations for multi-agent RAG systems operating in environments where retrieved evidence may be unreliable or adversarially manipulated.
            

![Figure 1: Example figure](2026_Fall_8.png)
*Figure 1: Caption*

## 2 Dataset:  

            The project will use MuSiQue (Multi-hop Questions via Single-hop Question Composition) as the primary evaluation dataset. MuSiQue is a multi-hop question-answering benchmark containing 
            questions that require reasoning across multiple supporting facts. Its question-answer structure and associated supporting evidence make it well suited for controlled experiments in which 
            evidence can be modified while the underlying question and ground-truth answer remain fixed.

            TIER 1 -- CLEAN MUSIQUE DATASET:
              1. The original MuSiQue examples will provide the clean evaluation condition. Each selected example contains a question with a known ground-truth answer and evidence needed to answer the question.
              2. The clean condition will preserve the original factual evidence associated with each question. This establishes the baseline for measuring whether single-agent and multi-agent RAG architectures can correctly answer questions when reliable evidence is available.
              3. A fixed subset of eligible MuSiQue questions will be selected using documented filtering criteria and random seeds. The same questions will subsequently be used to construct the poisoned condition, creating paired clean and poisoned examples.

            TIER 2 -- MISSING MUSIQUE DATASET:
              4. A corresponding missing-evidence version of the selected MuSiQue examples will be constructed by removing critical evidence while preserving the original question. If we determine this is unneeded and we can just exclude evidence from the dataset we will determine that as we get more into the project.
              5. Missing-evidence examples will omit one or more evidence passages necessary for deriving the correct answer. Controlled transformations may include removing entities, dates, quantities, locations, relationships, or other facts necessary for deriving the correct answer.
              6. Each missing-evidence example will preserve the original ground-truth answer while additionally recording the incorrect answer or conclusion supported by the missing evidence. This allows the experiment to determine whether a system follows the missing evidence, retains the correct answer, produces an unrelated hallucination, or appropriately abstains.
              7. Missing-evidence procedures will be standardized and reproducible so that evidence removal is applied consistently across the evaluation set rather than manually introducing arbitrary gaps.

            TIER 3 -- PAIRED EVALUATION SET:
              8. Every selected question will have both a clean and poisoned condition. The question itself and underlying ground truth remain fixed while the reliability of the available evidence changes.
              9. This paired design controls for question difficulty and allows the effect of poisoned evidence to be measured directly within the same questions.
              10. Single-agent RAG and each multi-agent verification architecture will be evaluated on the same paired examples, ensuring that differences in performance can be attributed to the architecture and evidence condition rather than differences in the underlying questions.

            DATASET / PIPELINE PREPARATION:
              - Download and preprocess MuSiQue into a standardized representation containing the question, ground-truth answer, supporting evidence, and relevant metadata.
              - Select a fixed evaluation subset using documented filtering criteria and random seeds.
              - Generate a poisoned counterpart for each selected clean example using a reproducible evidence-transformation pipeline.
              - Store explicit metadata identifying the evidence condition (clean or poisoned), original ground-truth answer, and, for poisoned examples, the false answer supported by the manipulated evidence.
              - Validate the poisoned examples to ensure that the modified evidence genuinely supports the intended false conclusion while remaining relevant and plausible within the context of the question.
              - Use identical paired clean/poisoned examples across the single-agent and multi-agent experimental conditions.
              - Cache the finalized evaluation dataset locally so that all experiments operate on a fixed benchmark and do not depend on changing external information during evaluation.
            

## 3 Rationale:  

            This problem becomes especially important for multi-agent systems. Verification architectures commonly use multiple agents to independently solve a task, critique another agent’s reasoning,
            debate alternatives, or reach a consensus. These mechanisms can potentially improve reliability by introducing redundancy and disagreement detection. At the same time, they introduce a second 
            possibility: if multiple agents rely on the same misleading retrieval context, their interactions may reinforce the false evidence. A critic may validate an incorrect answer because it is 
            supported by the poisoned documents, and a consensus mechanism may transform several correlated errors into a highly confident final response.

            The important distinction is therefore not simply whether multi-agent systems achieve higher average accuracy. The more consequential question is whether they behave correctly when the evidence itself is not 
            trustworthy. A robust system should recognize when its available evidence is insufficient or inconsistent and abstain rather than manufacture certainty. This makes appropriate abstention and confidence 
            calibration central evaluation targets rather than treating every question as requiring an answer.

            The proposed project is designed around this failure mode. By controlling the evidence presented to the system, the experiment can directly compare behavior under clean, missing, conflicting, and poisoned 
            retrieval while keeping the task and ground truth fixed. This allows the effect of the verification architecture to be separated from the underlying difficulty of the question.

            The project is also practically relevant. Agentic RAG systems are increasingly used in research, enterprise search, automated analysis, and decision-support workflows where multiple LLM calls are combined 
            specifically to increase trustworthiness. If additional agents merely increase confidence in retrieval errors, then architectural redundancy alone is not a meaningful safety mechanism. Conversely, if particular 
            verification structures reliably increase abstention or identify corrupted evidence, that provides an actionable design principle for agentic RAG systems.

            The contribution of this project is therefore an empirical characterization of when multi-agent verification helps and when it hurts under adversarial or unreliable retrieval. Rather than asking whether 
            multi-agent systems are generally better than single agents, the study focuses on a narrower and more defensible question: whether verification architectures improve epistemic behavior when the system’s own 
            evidence is misleading. The result can be useful regardless of direction. Evidence that multi-agent systems improve abstention would identify architectures that are more robust to retrieval failures, while 
            evidence of misinformation amplification would expose an important reliability limitation in current agentic RAG designs.
            

## 4 Approach:  

            Phase 1: Foundations & Experimental Design — Weeks 1–2

            Week 1: Project Setup & Background Research

              - Set up the GitHub repository and basic project structure.
              - Finalize the proposal, central research question, and scope.
              - Conduct targeted literature review on multi-agent verification/debate/critique, RAG robustness and retrieval poisoning, hallucination and abstention, and misinformation amplification/correlated agent errors.
              - Identify the strongest existing work and clarify how this experiment differs.
              - Download and inspect MuSiQue.
              - Define the initial experimental variables: single-agent vs. multi-agent, clean vs. poisoned evidence, shared vs. independent retrieval, and verification/aggregation strategy.
              - Define what appropriate abstention and misinformation amplification mean operationally, even if the exact metrics are not finalized yet.
              

            Week 2: MuSiQue Analysis, Dataset Construction, and Experimental Design/Conceptualization

              - Perform exploratory data analysis of dataset size and splits, question/answer structure, number of reasoning hops, supporting vs. distractor passages, answer types, and evidence structure.
              - Trace several examples manually from question → supporting evidence → answer.
              - Determine which MuSiQue examples are suitable for controlled poisoning.
              - Design the poisoning methodology, including what part of the evidence gets changed, how a false answer is selected, how much evidence is poisoned, and how to ensure poisoned evidence plausibly supports the false answer.
              - Manually create a small pilot set of paired clean/poisoned examples and inspect them for validity.
              - Define the standardized example schema that the later RAG pipeline will consume.


            Phase 2: Dataset Construction & Single-Agent RAG Baseline (Weeks 3-5)

            Week 3: Clean/Poisoned Dataset Construction

            - Finalize the MuSiQue subset used for the main experiments.
            - Implement the clean/poisoned dataset generation pipeline.
            - Ensure that we successfully implement different strategies for evidence removal, including complete removal and breaking multi-hop chains.
            - Define reproducible poisoning rules for modifying critical supporting evidence.
            - Generate paired clean and poisoned examples for the selected MuSiQue questions.
            - Store metadata for each example, including but not limited to:
                - question,
                - ground-truth answer,
                - clean evidence,
                - poisoned evidence,
                - poisoned/false answer,
                - reasoning-hop structure,
                - poisoning location/type,
                - evidence removal strategy (complete removal vs. breaking multi-hop chains).
            - Manually validate a sample of generated missing-evidence examples.
            - Revise evidence removal rules if examples are ambiguous, implausible, or do not actually support the intended missing-evidence scenario.

            Weeks 4 and 5: Single-Agent RAG Baseline

            - Implement the baseline single-agent RAG pipeline.
            - Standardize prompting and model configuration.
            - Evaluate the baseline on clean MuSiQue examples.
            - Verify that the baseline achieves reasonable performance before introducing poisoned evidence.
            - Run the same baseline on poisoned examples.
            - Log the model answer, supporting evidence used, abstention behavior, and relevant model outputs needed for later analysis.
            - Identify obvious pipeline or dataset failures before proceeding to multi-agent experiments.

            - Finalize the primary evaluation metrics.
            - Implement automated evaluation for:
                - answer correctness,
                - missing-evidence adoption,
                - appropriate abstention,
                - unsupported hallucination,
                - confidence/certainty where measurable.
            - Define the operational criteria for missing-evidence amplification.
            - Compare single-agent performance between paired clean and poisoned conditions.
            - Analyze how frequently poisoned evidence changes a previously correct answer into an incorrect answer.
            - Establish the single-agent baseline that all later multi-agent architectures will be compared against.
            - Freeze the main dataset generation procedure and baseline evaluation protocol before beginning the multi-agent phase.
            
            - Should also begin working on multi-agent architectures as well -> this is important to get ahead of the pipeline runs.


            Phase 3: Multi-Agent Architecture Implementation (Weeks 5-9)

            Weeks 5 and 6: Core Multi-Agent Pipeline

            - Implement a common agent interface so all architectures use the same underlying model, prompts, dataset inputs, and output format where applicable.
            - Implement the first multi-agent verification architecture using a solver-critic design:
                - solver produces an answer from retrieved evidence,
                - critic evaluates the answer and supporting evidence,
                - solver revises or abstains based on the critique.
            - Repeat the above step for all other agent architectures we plan to test (will test at least 3 different architectures including the single-agent baseline).
            - Implement structured logging of each agent's initial answer, critique, revised answer, final answer, and abstention decision. This will be a working progress, the more information we log the better.
            - Run the architecture on a small clean/poisoned development subset.
            - Verify that agent communication and decision logic behave as intended.
            - Compare preliminary behavior against the single-agent baseline and identify implementation issues.

            Weeks 7 and 8: Additional Architectures & Controlled Variants

            - Implement additional multi-agent verification strategies needed for the main comparison.
            - Implement an independent-agent architecture in which multiple agents reason separately before their outputs are aggregated.
            - Implement voting and/or consensus-based aggregation between independent agents.
            - Implement shared-evidence and independent-evidence variants where appropriate.
            - Ensure all architectures use matched model configurations, questions, evidence conditions, and evaluation procedures.
            - Run clean and poisoned development experiments across all architectures.
            - Validate that each architecture produces the outputs required by the evaluation pipeline.
            - Finalize and freeze the multi-agent architectures that will be used in the main experiments.
            
            - Important that in these 2 weeks we closely validate that the experiment is working as expected. The earlier we validate this works, the smoother the actual experimental pipeline will go.


            Phase 4: Main Experimental Evaluation (Weeks 9-11)

            Weeks 9 and 10: Full Clean vs. Poisoned Evaluation

            - Run the single-agent baseline and all finalized multi-agent architectures on the full paired MuSiQue evaluation set.
            - Evaluate each architecture under both clean and poisoned evidence conditions.
            - Use identical model settings, prompts, dataset examples, and evaluation procedures across architectures.
            - Record all agent-level and system-level outputs needed for later analysis.
            - Measure:
                - answer correctness,
                - poisoned-answer adoption,
                - appropriate abstention,
                - unsupported hallucination,
                - agreement/disagreement between agents,
                - final consensus behavior.
                - any other metrics that we think of along the way that could improve our experimental question
            - Check for failed runs, malformed outputs, or logging inconsistencies before beginning analysis.

            Week 11: Architecture Comparison and Robustness Analysis

            - Compare each multi-agent architecture against the single-agent baseline.
            - Measure how much performance changes when moving from clean to poisoned evidence. Note we expect it to be worse, but abstention rate is the important factor here.
            - Analyze whether multi-agent verification reduces or increases poisoned-answer adoption.
            - Compare appropriate abstention rates across architectures.
            - Evaluate whether agent disagreement is associated with better detection of poisoned evidence.
            - Compare shared-retrieval and independent-retrieval conditions where applicable.
            - Compare critique, voting, and consensus mechanisms where applicable.
            - Identify architectures that appear more robust to poisoned evidence and architectures that amplify it.

            Week 12: Missing evidence Amplification and Error Analysis

            - Define and compute the final missing-evidence amplification metrics.
            - Identify cases where multi-agent interaction causes agents to converge on an incorrect missing-evidence answer.
            - Compare initial agent responses with final system decisions to determine whether communication corrected or reinforced errors.
            - Categorize common failure modes, such as:
                - all agents independently trusting the missing-evidence,
                - one incorrect agent influencing initially correct agents,
                - critique reinforcing rather than correcting an incorrect answer,
                - voting producing a confident incorrect majority,
                - consensus suppressing legitimate disagreement.
            - Perform qualitative analysis on representative examples.
            - Run appropriate statistical comparisons on the main metrics.
            - Determine which architectural properties are most strongly associated with robustness versus misinformation amplification.


            Phase 5: Robustness, Ablations, and Generalization (Weeks 12-13)

            Week 12: Ablation and Sensitivity Experiments

            - Run targeted ablation experiments based on the main Phase 4 findings.
            - Vary the proportion or severity of missing-evidence to determine how architectures respond as evidence quality degrades.
            - Compare shared-retrieval and independent-retrieval configurations while holding the agent architecture constant.
            - Remove or modify individual verification components, such as critique or voting, to determine whether they are responsible for observed robustness or amplification.
            - Test whether increasing the number of agents improves robustness or simply increases agreement on missing-evidence answers.
            - Measure the effect of each experimental change using the same primary metrics established in Phase 4.
            - Prioritize ablations that directly explain the main experimental results rather than exhaustively testing every possible configuration.

            Week 13: Robustness and Generalization Checks

            - Can we test this pipeline on other underlying models? Original experiment performed on one model, but if done on mutiple models this could be a more robust claim.
            - Repeat key experiments across multiple random seeds or repeated runs to quantify variability from stochastic model outputs.
            - Test whether the main findings remain consistent across different MuSiQue question characteristics, such as reasoning-hop count or poisoning type.
            - Evaluate whether results are driven by specific subsets of questions or represent a broader pattern across the evaluation set.
            - Test a second model where computationally feasible to determine whether the observed behavior is specific to the primary LLM.
            - Perform statistical comparisons and uncertainty estimation for the primary results.
            - Revisit representative failure cases and verify that measured misinformation amplification reflects genuine system behavior rather than dataset or evaluation artifacts.
            - Finalize the set of results that directly support or contradict the project's hypotheses.


            Phase 6: Final Analysis, Writing, and Presentation (Weeks 14-16)

            Weeks 14 and 15: Final Results and Analysis

            - Complete any remaining experimental runs or targeted follow-up experiments.
            - Consolidate results from the baseline, multi-agent, and robustness experiments.
            - Generate final tables and figures for the primary evaluation metrics.
            - Perform final statistical analyses and uncertainty estimates.
            - Determine which hypotheses are supported, contradicted, or remain inconclusive.
            - Summarize the primary findings regarding whether multi-agent verification reduces or amplifies the effects of poisoned evidence.
            - Identify the architectural properties most strongly associated with robustness or misinformation amplification.

            Week 16: Paper Drafting

            - Write the methodology and experimental design sections.
            - Document the MuSiQue poisoning procedure and evaluation protocol.
            - Write the results section using finalized experiments.
            - Write the discussion section interpreting the results and their implications for multi-agent RAG systems.
            - Document limitations, potential confounders, and threats to validity.
            - Update the related-work section based on the final scope of the project.

            Weeks 15 and 16: Paper Revision and Final Validation

            - Complete the full paper draft.
            - Review all reported results against experiment outputs for accuracy.
            - Verify that figures, tables, metrics, and statistical results are reproducible from saved experiment outputs.
            - Perform any small follow-up analyses required to address gaps discovered during writing.
            - Revise the paper based on advisor and team feedback.
            - Finalize the GitHub repository, documentation, configuration files, and reproducibility instructions.

            Week 17: Final Deliverables and Presentation

            - Finalize and submit the capstone paper.
            - Create the final presentation and supporting visualizations.
            - Present the research question, experimental design, main findings, and practical implications.
            - Clearly distinguish observed results from interpretations and limitations.
            - Prepare examples illustrating representative cases of successful verification and misinformation amplification.
            - Complete final repository cleanup and archive experiment configurations and results.

            

## 5 Timeline:  

            Week 1:    Prepare proposal, lit review, github repository setup, initial project plan drafted, background research, and dataset loaded
            Week 2:    Have datasets cleaned, repository ready to go, environments set up, versions all standardized, and eda completed
            Week 3:    Finalize and clean the dataset. Dataloaders in order, setup for data pipeline initialization complete
            Week 4:    Single-agent baseline with RAG implementation should start this week. Ideally have a working pipeline by end of week
            Week 5:    Finish up single agent RAG baseline run. Output results and initial analysis. Start implementing multi-agent if haven't done so yet
            Week 6:    Core multi-agent pipeline should be worked on extensively.
            Week 7-8:    Continue improving multi-agent pipeline, robust benchmarking is necessary so no major issues arise one experiment is ready
            Weeks 9-11:    Run the experiments for multi-agent pipeline
            Week 12:   Error analysis and debugging of the multi-agent pipeline
            Week 13:   Robustness check
            Week 14-16: Work on paper and presentation

            TOTAL: 16 weeks (one semester)

            KEY MILESTONES:
            - Week 4:  Single agent RAG baseline complete
            - Week 8:  Multi-agent pipeline should mostly have taken shape
            - Week 11: Run multi-agent experiments
            - Week 16: Paper and presentation submission

            DELIVERABLES BY WEEK 16:
            - Benchmark for multi-agent pipeline performance with poisoned information
            - Research paper draft (8-10 pages)
            - Open-source repository with reproducible notebooks
            


## 6 Expected Number Students:  

            RECOMMENDED: 3 students
            ROLE DISTRIBUTION

              STUDENT 1: CRITIQUE-BASED MULTI-AGENT MODELING
              - Help construct and validate the paired clean/poisoned MuSiQue dataset.
              - Implement the single-agent RAG baseline used across the project.
              - Implement the critique-based multi-agent architecture (solver-critic).
              - Design and test different critique and revision strategies.
              - Run clean and poisoned evidence experiments for the critique-based architecture.
              - Perform ablations such as removing the critic, modifying revision behavior, or varying critique rounds.
              - Analyze when critique successfully corrects poisoned answers versus reinforces misinformation.
              - Contribute to shared statistical analysis, error analysis, and paper writing.

              Primary Research Question:
              Does explicit critique and revision improve robustness to poisoned retrieval evidence?

              STUDENT 2: INDEPENDENT-AGENT / ENSEMBLE MODELING
              - Help construct and validate the paired clean/poisoned MuSiQue dataset.
              - Implement the independent-agent architecture in which multiple agents reason separately.
              - Implement voting or other aggregation mechanisms for combining independent agent responses.
              - Run clean and poisoned evidence experiments for the independent-agent architecture.
              - Compare shared versus independently retrieved evidence where appropriate.
              - Perform ablations such as varying the number of agents or aggregation strategy.
              - Analyze whether independent reasoning reduces correlated errors and poisoned-answer adoption.
              - Contribute to shared statistical analysis, error analysis, and paper writing.

              Primary Research Question:
              Does independent multi-agent reasoning provide useful redundancy against poisoned retrieval evidence?

              STUDENT 3: INTERACTIVE / CONSENSUS MULTI-AGENT MODELING
              - Help construct and validate the paired clean/poisoned MuSiQue dataset.
              - Implement an interactive multi-agent architecture using discussion, debate, or consensus formation.
              - Track individual agent answers before and after communication.
              - Run clean and poisoned evidence experiments for the interactive architecture.
              - Perform ablations such as varying communication rounds or consensus requirements.
              - Measure whether initially correct agents change to poisoned answers after interacting with other agents.
              - Analyze when communication corrects misinformation versus propagates misinformation through the group.
              - Contribute to shared statistical analysis, error analysis, and paper writing.

              Primary Research Question:
              Does inter-agent communication correct misinformation, or does it cause misinformation to propagate and produce incorrect consensus?

              SHARED RESPONSIBILITIES
              - Finalize the research question and hypotheses.
              - Design the MuSiQue poisoning methodology.
              - Implement the missing-evidence poisoning methodology, and come up with evidence removal plans and scenarios and ensure that we can track this effectively.
              - Build and validate the clean/poisoned evaluation dataset.
              - Develop common RAG and agent infrastructure.
              - Standardize model configurations, prompts, retrieval conditions, and logging.
              - Define evaluation metrics and misinformation amplification criteria.
              - Run and verify final experiments.
              - Perform statistical comparisons across architectures.
              - Conduct qualitative error analysis.
              - Interpret results across all three modeling approaches.
              - Write the final paper and prepare the presentation.
            

## 7 Possible Issues:  

            TECHNICAL CHALLENGES AND SOLUTIONS:

            1. Parametric Knowledge May Allow the Model to Answer Without Retrieved Evidence:
            - ISSUE: Because MuSiQue questions are based on factual information, the underlying LLM may already know some answers from pretraining. If a required evidence passage is removed, the model could still answer correctly from memory rather than from the retrieved evidence.
            - SOLUTION: Run a separate closed-book diagnostic in which the same question is presented without retrieved context and the model is allowed to answer from internal knowledge. Questions answered correctly closed-book will be flagged and analyzed separately rather than automatically treated as evidence-grounded successes. During the actual RAG experiments, agents will be instructed to answer only from the provided evidence and log the evidence IDs supporting their answers so unsupported responses can be identified even when the final answer happens to be factually correct.

            2. Missing-Evidence Examples May Still Be Answerable:
            - ISSUE: Removing one supporting passage or reasoning hop may not actually make a question unsupported. Remaining passages, distractors, or indirect clues may still provide enough information to derive the answer.
            - SOLUTION: Validate the evidence-removal procedure on a development subset before the main experiment. Confirm that the removed information is necessary for completing the reasoning chain and record the evidence-removal strategy for each example.

            3. Appropriate Abstention May Be Difficult to Measure Reliably:
            - ISSUE: Models may express uncertainty in many different ways rather than returning a standardized abstention response, making automated evaluation inconsistent.
            - SOLUTION: Use a structured output format requiring every agent to return both its answer and an explicit answer-or-abstain decision. Validate automated abstention scoring against a manually reviewed subset before applying it to the full evaluation.

            4. Multiple Agents May Produce Correlated Unsupported Answers:
            - ISSUE: Adding more agents does not guarantee independent verification. Agents using the same model, prompts, and incomplete evidence may produce the same unsupported answer, creating false consensus.
            - SOLUTION: Record every agent's response before aggregation or communication and measure agreement and disagreement at the agent level. Compare the frequency of false consensus across critique-based, independent-agent, and interactive architectures.

            5. Agent Communication May Reinforce Rather Than Correct Errors:
            - ISSUE: In interactive architectures, an unsupported answer from one agent may influence other agents during discussion or debate, causing the group to converge on an answer that is not supported by the available evidence.
            - SOLUTION: Store agent responses before and after communication. Measure whether initially abstaining or disagreeing agents move toward an unsupported answer after interaction and compare these transitions across communication strategies.

            6. Architecture Comparisons May Be Confounded by Unequal Compute:
            - ISSUE: Multi-agent architectures naturally require more model calls, tokens, and inference time than the single-agent baseline. Any performance improvement could therefore result from additional inference effort rather than the architecture itself.
            - SOLUTION: Keep the underlying model, retrieval inputs, temperature, dataset examples, and other applicable settings consistent across architectures. Report model-call count, token usage, and latency alongside accuracy, abstention, and false-consensus metrics.

            7. Experimental Run Count May Exceed the Available Semester Budget:
            - ISSUE: Testing several architectures, evidence-removal strategies, agent counts, random seeds, and models could produce more experimental runs than can reasonably be completed during the semester.
            - SOLUTION: Define and freeze the primary experiment matrix before the main evaluation. Prioritize one primary model, a fixed MuSiQue subset, clean and missing-evidence conditions, and the core architecture comparisons. Additional models and ablations will be extensions if time and compute permit.

            8. Library, Dataset, and Model Version Drift May Affect Reproducibility:
            - ISSUE: Changes to dataset, transformer, retrieval, or agent-framework libraries during the semester could alter experimental behavior or break the pipeline.
            - SOLUTION: Pin tested dependency versions, record model and dataset revisions, use fixed random seeds, save prompts and experiment configurations, and cache the finalized evaluation dataset used for the main experiments.

            9. The Backbone Model May Not Reliably Perform Specialized Agent Roles:
            - ISSUE: The selected model may not faithfully perform critic, debater, verifier, or aggregation roles. For example, a critic may always agree with the solver or debate agents may never meaningfully revise their answers, causing architectures to appear equivalent for the wrong reason.
            - SOLUTION: Measure critic-agreement rate, answer-change rate, role-compliance rate, and non-convergence on the development subset before the main experiment. Cap interaction rounds with an explicit stopping rule and report these diagnostics alongside the primary metrics. If specialized verification behavior is weak at the selected model scale, that will be reported as a limitation or finding rather than silently treated as evidence that architectures are equivalent.

            RISK MITIGATION TIMELINE:
            - Early setup: Validate MuSiQue structure, the missing-evidence construction process, the closed-book diagnostic, and the standardized evaluation schema.
            - Baseline development: Validate the single-agent pipeline and confirm that missing-evidence examples genuinely test insufficient support and abstention.
            - Multi-agent development: Validate each architecture on a development subset and inspect agent-level logs for correlated errors, false consensus, role compliance, and malformed outputs.
            - Main experiments: Monitor run completion, model-call counts, token usage, latency, and failed runs while preserving intermediate outputs.
            - Final analysis: Perform statistical comparisons and manual error analysis to verify that measured abstention and false consensus reflect genuine system behavior rather than evaluation artifacts.
            - Final repository freeze: Pin tested dependencies, dataset revisions, model configurations, prompts, and experiment outputs needed for reproducibility.
            


## Contact
- Author: Amir Jafari
- Email: [ajafari@gwu.edu](mailto:ajafari@gwu.edu)
- GitHub: [](https://github.com/)
