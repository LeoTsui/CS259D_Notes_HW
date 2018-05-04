# The Security of Machine Learning

<!-- TOC -->

- [Background Knowledge and Goal](#background-knowledge-and-goal)
- [Framework](#framework)
    - [Security analysis](#security-analysis)
    - [Taxonomy](#taxonomy)
    - [Notation](#notation)
    - [Adversarial learning game](#adversarial-learning-game)
- [Learn, Attack and Defend](#learn-attack-and-defend)
    - [Attack: Causative and Integrity](#attack-causative-and-integrity)
    - [Attack: Causative and Availability](#attack-causative-and-availability)
    - [Attack: Exploratory and Integrity](#attack-exploratory-and-integrity)
    - [Attack: Exploratory and Availability](#attack-exploratory-and-availability)
    - [Defend: Against Exploratory Attacks](#defend-against-exploratory-attacks)
        - [Defenses against attacks without probing](#defenses-against-attacks-without-probing)
        - [Defenses against probing attacks](#defenses-against-probing-attacks)
    - [Defend: Against Causative Attacks](#defend-against-causative-attacks)
- [Case Study: SpamBayes](#case-study-spambayes)
- [References](#references)

<!-- /TOC -->

## Background Knowledge and Goal

* Evaluate the quality of a learning system
* Determine whether it satisfies requirements for secure learning
* Computer security evaluation
    * Determining classes of attacks on the system
    * Evaluating the resilience of the system against those attacks
    * Strengthening the system against those classes of attacks
* **Use same model to evaluate secure learning**

## Framework

### Security analysis

* Security goals
    * Integrity goal
    * Availability goal
* Threat model
    * Attacker goal/incentives
        * Cost function
            * **Cost of defender** corresponds to **benefit of attacker**
    * Attacker capabilities
        * Attackers have knowledge of machine learning
            * Training algorithm
            * Training dataset
        * Attackers can generate arbitrary instances, or not
        * Attackers can control training data, to what extent
        * Attackers annnot control
            * Label by hand labeled
            * Arrival order of packets

### Taxonomy

* **Influence** (**capability**, influence training data or not)
    * **Causative**, attacks influence learning with control over training data
    * **Exploratory**, attacks exploit misclassifications but do not affect training
* **Security violation** (**type**)
    * **Integrity**, attacks compromise assets via false negatives
    * **Availability**, attacks cause denial of service, usually via false positives
* **Specificity** (**specific intention**)
    * **Targeted**, attacks focus on a particular instance
    * **Indiscriminate**, attacks encompass a wide class of instances
* **Influence** determines structure of the game and move sequence
* **Security violation** and **specificity** determine cost function

### Notation

![notation](images/SecML-MLJ2010.notation.png)

### Adversarial learning game

* Exploratory game
    * Defender Choose procedure $$H$$ for selecting hypothesis
    * Attacker Choose procedure $$A_E$$ for selecting distribution $$\mathbb{P}_E$$
        * Construct an unfavorable evaluation distribution concentrating probability mass on high-cost instances
* Causative game
    * Defender Choose procedure $$H$$ for selecting hypothesis
    * Attacker Choose procedures $$A_T$$ and $$A_E$$ for selecting distributions
* Defenders' trade-off
    * Better performance on worst-case vs Less effective on average

## Learn, Attack and Defend

*"Defender" is the "Learner"*

### Attack: Causative and Integrity

* Contamination in PAC learning (Kearns and Li 1993)
    * PAC, probably approximately correct
    * **Learner**
        * Success with $$P \geq 1 - \delta$$
        * $$P_\text{incorrect} \leq \epsilon$$
    * **Attacker**
        * Control over training data with fraction $$\beta$$
        * Prevent the learner form succeeding if $$\beta \geq \epsilon / (1 + \epsilon)$$
* Spam foretold
    * **Attacker**
        * Send non-spam resembling the desired spam
        * eg: polysemous words. "watch"
    * **Learner**
        * Mis-train: Misses eventual spam(s)
* Red herring (Newsome et al. 2006)
    * **Attacker**
        * Introduce spurious features into all malicious instances used by defender for training
        * At attack time, malicious instances lack the spurious features and bypass the filter
    * **Learner**
        * Learn spurious features as necessary elements of malicious behavior

### Attack: Causative and Availability

* Rogue filter (Nelson et al. 2008)
    * **Attacker**
        * Send spam resembling benign messages
            * Include both spam words and benign words
    * **Learner**
        * Associates benign words with spam
* Correlated outlier (Newsome et al. 2006)
    * **Attacker**
        * Add spurious features to malicious instances
    * **Learner**
        * Filter blocks benign traffic with those features
* Allergy attack (Chung and Mok 2006, 2007)
    * Against Autograph, a worm signature generation system
    * **Learner**
        * Phase I, Identify infected nodes, based on behavioral patterns
        * Phase II, Learn new blocking rules by observing traffic from infected nodes
    * **Attacker**
        * Phase I, Convince Autograph that an attack node is infected by scanning
        * Phase II, Send crafted packets from attack node, causing Autograph to lean rules blocking begin traffic (DoS)

### Attack: Exploratory and Integrity

* Shifty spammer, good word attacks (Lowd and Meek 2005b and Wittel and Wu 2004)
    * **Attacker**
        * Craft spam so as to evade classifier without direct influence over the classifier itself
            * Exchange common spam words with less common synonyms
            * Add benign words to sanitize spam
* Polymorphic blending (Fogla and Lee 2006)
    * **Attacker**
        * Encrypt attack traffic so it appears statistically identical to normal traffic
* Mimicry attack (Tan et al. 2002)
    * Example: attacking sequence-based IDS
        * Shortest malicious subsequence longer than IDS window size
* Feature drop (FDROP, Amir Globerson and Sam Roweis 2006)
* Reverse engineering (Lowd and Meek 2005a)
    * **Attacker**
        * Seeks the worst case for classifier, best case for attacker

### Attack: Exploratory and Availability

* Mistaken identity (Moore et al. 2006)
    * **Attacker**
        * Interfere with legitimate operation without influence over training
            * Create a spam campaign with target's email address as the From: address of spams
            * Flood of message bounces, vacation replies, angry responses, etc. fill target's inbox
* Spoofing
    * **Learner**
        * IPS trained on intrusion traffic blocks hosts that originate intrusions
    * **Attacker**
        * Attack node spoofs legitimate host's IP address
* Algorithmic complexity (Dredze et al. 2007; Wang et al. 2007)
    * **Attacker**
        * Sending spams embedded in images

### Defend: Against Exploratory Attacks

#### Defenses against attacks without probing

* Training data
    * **Defender**
        * Limit information accessible to attacker
* Feature selection
    * **Defender**
        * Example: use inexact string matching in feature selection to defeat obfuscation of words in spams
        * Avoid spurious features
        * Regularization: smooth weights, defend against feature deletion
* Hypothesis space/learning procedures
    * **Defender**
        * Complex space harder to decode, but also harder to learn
        * Regularization: balance complexity and over-fitting

#### Defenses against probing attacks

* Analysis of reverse engineering
    * **Attacker**
        * Do not need to model the classifier explicitly
        * Find lowest-attacker-cost instance
    * **Defender**
        * Adversarial classifier reverse engineering (ACRE)
        * ACRE find the lowest-attacker-cost
* Randomization
    * **Defender**
        * Random decision instead of binary decision
* Limiting/misleading feedback
    * **Defender**
        * Eliminating bounce emails
        * Sending fraudulent feedback

### Defend: Against Causative Attacks

* Data sanitization
    * Reject On Negative Impact (RONI)
    * **Learner**
        * Train two classifier, by whether including a certain instance
        * Measure the accuracy of them
        * Determine the instance is malicious, or not
        * Reject the instance as detrimental in its effect
* Robustness
    * Robust Statistics, Boiling frog defense
        * Mean, Mean Squared Error(MSE), Standard Deviation
        * Median, Median Absolute Deviation(MAD)
    * Proper regularization
* Online prediction with experts
    * Multi-classifier systems

## Case Study: SpamBayes

| (**Targeted** or **Indiscriminate**) | **Integrity**                                                 | **Availability**                                                                        |
| ------------------------------------ | ------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Causative**                        | **Spam foretold**: mis-train **a** or **any** particular spam | **Rogue filter**: mis-train filter to block **a certain** or **arbitrary** normal email |
| **Exploratory**                      | **Shifty spammer**: obfuscate **a** or **any** chosen spam    | **Unwanted reply**: flood **a particular** or **any of several** target inbox           |

* Method
    * Send attack emails with legitimate words
    * Legitimate words receive higher spam scores
    * Future legitimate emails more likely filtered
* Types
    * Indiscriminate: Dictionary attack
    * Targeted: Focused attack
* Goals
    * Get target to disable spam filter
    * DoS against a bidding competitor

## References

* The security of machine learning, 2010
* CS 259D Session 10
