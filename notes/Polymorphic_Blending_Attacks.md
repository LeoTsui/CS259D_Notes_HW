# Polymorphic Blending Attacks

<!-- TOC -->

- [Goals](#goals)
- [Related Work](#related-work)
- [Blending Attacks](#blending-attacks)
    - [Scheme of a polymorphic blending attack](#scheme-of-a-polymorphic-blending-attack)
    - [Polymorphism Attacks](#polymorphism-attacks)
        - [Polymorphism](#polymorphism)
        - [Three Components of Polymorphic Attack](#three-components-of-polymorphic-attack)
        - [Detection of Polymorphic Attacks](#detection-of-polymorphic-attacks)
    - [Polymorphic Blending Attacks (PBA)](#polymorphic-blending-attacks-pba)
    - [Steps of Polymorphic Blending Attacks](#steps-of-polymorphic-blending-attacks)
        - [Step 1 Learning The IDS Normal Profile](#step-1-learning-the-ids-normal-profile)
        - [Step 2 Attack Body Encryption](#step-2-attack-body-encryption)
        - [Step 3 Generate Polymorphic Decryptor](#step-3-generate-polymorphic-decryptor)
    - [Attack Packet Design](#attack-packet-design)
- [Evading PAYL](#evading-payl)
    - [Evading 1-gram](#evading-1-gram)
        - [Padding](#padding)
        - [Substitution](#substitution)
    - [Evading 2-gram](#evading-2-gram)
- [Experiment Setup](#experiment-setup)
    - [Attack Vector](#attack-vector)
    - [Dataset](#dataset)
- [Evaluation](#evaluation)
    - [PAYL Training](#payl-training)
    - [Traditional Polymorphic Attacks (CLET)](#traditional-polymorphic-attacks-clet)
    - [Polymorphic Blending Attack](#polymorphic-blending-attack)
        - [Artificial Profile](#artificial-profile)
        - [1-gram and 2-gram Attacks](#1-gram-and-2-gram-attacks)
- [Countermeasures of IDS](#countermeasures-of-ids)
- [Limitations and Improvements](#limitations-and-improvements)
- [References](#references)

<!-- /TOC -->

## Goals

* Study polymorphic blending attack
* Why network anomaly IDS based on payload statistics not work
* Case study: 1-gram and 2-gram PAYL

## Related Work

* Polymorphic attacks
    * IP/TCP transformations
    * Mutation exploits (Vigna et al.)
    * Fragroute, Whisker, AGENT, Mistfall, tPE, EXPO, DINA, ADMutate, PHATBOT, JempiScodes
    * CLET
* Defenses against polymorphism
    * Looking for executable code (Toth et al.)
    * Looking for similar structure in multiple code instances (Kruegel et al.)
    * Looking for common substrings present in multiple code instances (Polygraph)
        * Defeated by noise
    * Looking for any exploit of a known vulnerability (Shield)
    * Looking for instruction semantics, detect known code transformations (Cristodorescu et al.)
    * Detect sequence of anomalous system calls (Forest et al.)
        * Can be defeated through mimicry attacks.
        * New approaches use stack information but they can also be defeated
    * Payload-based anomaly detection
        * Use length, character distribution, probabilistic grammar and tokens to model HTTP traffic (Kruegel et al.)
        * Record byte frequency for each port's traffic (PAYL)

## Blending Attacks

### Scheme of a polymorphic blending attack

![Scheme-of-a-Polymorphic-Blending-Attack-PBA](images\Scheme-of-a-Polymorphic-Blending-Attack-PBA.png "Scheme of a polymorphic blending attack (PBA)")

### Polymorphism Attacks

#### Polymorphism
    
* Disguise the packets as normal traffic
* Change the contents of packets to make them look different from each other
* Exploit code, not used in normal
* **Making attacks look different from each other rather than normal**

#### Three Components of Polymorphic Attack
    
* Attack Vector
    * Modified part, invariant part
    * If the attack invariant is very small and exists in the normal traffic
        * Could cause high FP of IDS
* Attack Body (shellcode)
    * Register shuffling
    * Equivalent instruction substitution
    * Instruction reordering
    * Garbage insertions
    * Encryption
* Polymorphic Decryptor
    * Apply to decrypt shellcode and transfers control to shellcode
    * Obfuscate decryptor code

#### Detection of Polymorphic Attacks
    
* Exploit code and/or input data contain some characters that have very low probability of appearing in a normal packet
* **This deviation can be detected**

### Polymorphic Blending Attacks (PBA)

* Making attacks looks different from each other
* **Adjust their byte frequency to match that of legitimate traffic (look like normal)**

![Attack Scenario of Polymorphic Blending Attack](images/Attack_Scenario_of_PBA.png)

* Assumption of Realistic Attack Scenario
    * The adversary has already compromised a host X inside a network A which communicates with the target host Y inside network B
    * The adversary has knowledge of the IDS<sub>B</sub> that monitors the victim host network
    * IDS of Network B is a payload statistics based system (e.g., PAYL)
    * The IDS<sub>B</sub> has a threshold setting that can be adjusted to obtain a desired false positive rate
        * The adversary does not know the exact value of the threshold used by IDS<sub>B</sub>
        * The adversary has estimated the generally acceptable false positive and false negative rates
* Adversary's actions
    * Control host X
    * Observe the normal traffic going from X to Y
    * Estimate a normal profile (*artificial profile*) for this traffic by the same modeling technique as IDS<sub>B</sub> using
    * Creative mutated instances to match the artificial profile
    * If IDS<sub>B</sub> fails on analysing the mutated packets, the adversary succeeds in attacking
* Adversary's trade-off
    * Attack size
        * Monitor network flow size
    * Process speed
        * Attack should be economical in time and space
        * High system resource usage could cause local IDS (e.g., IDS<sub>A</sub> or host-based IDS) to initiate alerts

### Steps of Polymorphic Blending Attacks

#### Step 1 Learning The IDS Normal Profile

* Sniffing the network traffic
* Generates artificial profile
* More normal packets captured more closer to the normal profile
* Profile
    * Maximum, average size of packets
    * Rate of packets
    * Byte frequency distribution
    * Range of tokens at different offsets

#### Step 2 Attack Body Encryption

* To match the normal profile
    * Substituting every character
    * Padded with some garbage data
* Reversible operation
* Generated suitable substitution table

#### Step 3 Generate Polymorphic Decryptor

* Remove padding
* re-substitute characters
* The decryptor routine is not encrypted but be mutated

### Attack Packet Design

* Find a normal profile that similar to the attack packet
    * Character frequency (substitution table)
        * If no significantly different between new and old substitution tables, replace old by new 
    * Packet length
        * Longer than the attack packet
        * Plan B: divide attack body into multiple small packets

## Evading PAYL

### Evading 1-gram

* **Minimize the maximum frequency difference**

#### Padding

* $$\hat{\omega}$$, substituted attack body before padding
* $$\acute{\omega}$$, substituted attack body after padding
* $$\|\omega\|$$, length of $$\omega$$
* $$i$$, index of characters
* $$x$$, characters
    * $$x_i$$, the $$i^{th}$$ of the characters
* $$\lambda$$, $$\#$$ occurrences
    * $$\lambda_i$$, $$\#$$ occurrences of $$x_i$$
* $$\|\acute{\omega}\| = \|\hat{\omega}\| + \sum_{i=1}^n{\lambda_i}$$
* $$f(x_i)$$, relative frequency of character $$x_i$$ in normal traffic
* $$\hat{f}(x_i)$$, relative frequency of character $$x_i$$ in substituted attack traffic
* $$\lambda_i = \|\acute{\omega}\|f(x_i) - \|\hat{\omega}\|\hat{f}(x_i)$$
* For some characters, $$f(x_i) < \hat{f}(x_i)$$
    * **The most frequent such character need not be padded** 
* Let $$\delta = \max{(\hat{f}(x_i) / f(x_i))}$$ be the maximum overuse
    * $$\lambda_i = \|\hat{\omega}\|(\delta f(x_i) - \hat{f}(x_i))$$

#### Substitution

* To minimize padding we need to minimize $$\delta$$
* Case 1: attack chars are less numerous than legitimate chars
    * A greedy algorithm that generates one-to-many mapping
    * Sort characters by frequency in attack and legitimate traffic
    * Match frequencies in decreasing order
    * Remaining legitimate characters are assigned to attack characters that have highest to bring it down
* Case 2: attack chars are more numerous than legitimate chars
    * A greedy algorithm that generates many-to-one mapping
    * Construct a Huffman tree where leaves are characters in the attack traffic, and smallest two nodes are iteratively connected (thus most frequent characters have shortest length)
    * We must choose (not random) the labels for the edges so to preserve the original legitimate character frequency
        * Sort vertices in the tree by weight
        * Sort legitimate characters by their frequency
        * Choose the highest frequency character for the highest weight vertex
        * Remove the vertex from the list and remove the given portion of the character's frequency from further consideration
        * Resort the characters

### Evading 2-gram

* Must match all 2-byte pairs
* Represent valid 2-grams as states in FSM
* A simple approach will enumerate valid paths in FSM and map attack characters to paths randomly but this generates large code size
    * Better mapping can be obtained by using entropy information, i.e., mapping frequent characters to short paths
* Another approach will attempt to find single byte mappings so that 2-grams are also matched
    * Greedy algorithm sorts 2-grams by frequencies in legitimate and attack traffic and matches them greedily taking care not to violate any existing mappings
* Generate padding so to match the target distribution greedily

## Experiment Setup

### Attack Vector

* Windows Media Services (MS03-022)
    * Exploits a vulnerability with logging of user requests
* Attacker vector 99 bytes
    * Presented at the start of the HTTP request
* For buffer overflow attack must send 10KB of data
* Attack body opens a TCP connection and sends registry files
* Size of attack body is 558B and contains 109 unique characters
* Attack was divided into multiple packets
    * Divide decryptor into several packets
* If final blending attack packet after padding not up to 10KB, send normal packets

### Dataset

* Captured 15 days of HTTP traffic
    * From one department
    * 14 days' traffic to train the IDS (4,356,565 packets, 1.9GB)
    * Last day's traffic is used by the attacker to learn character distributions
    * Only TCP data packets are used that do not contain known attacks
* IDS builds profiles per packet length
* Selected three frequent packet sizes for the attack

## Evaluation

### PAYL Training

* PAYL training time increases with the size of the training data because new packets carry more unique n-grams

### Traditional Polymorphic Attacks (CLET)

* Tested CLET-generated polymorphic attacks against PAYL
    * CLET only adds padding to match byte frequency
    * Other polymorphic engines perform worse than CLET against PAYL
    * CLET attack sequence will avoid PAYL detection only if all packets have an anomaly score above the threshold
    * Both 1-gram and 2-gram PAYL detected all attacks with chosen threshold setting

### Polymorphic Blending Attack
    
#### Artificial Profile

* Training of the artificial profile is stopped when there is no significant improvement over existing profile (measured using Manhattan distance) within two packets

#### 1-gram and 2-gram Attacks

* For 1-gram attacks used one-to-one substitution cipher
* For 2-gram attacks used single byte encoding scheme
    * Two types of transformations were tested
    * Global substitution
        * Substitution table is constructed for entire attack body
        * Single decoding table used to decode the whole attack flow
    * Local substitution
        * Substitution table is constructed for each packet separately
        * Each packet corresponds to a decoding table
        * Padding space reduced
    * If attack characters are more numerous than those in legitimate traffic, non-existing characters were used
* 2-gram IDS had consistently higher anomaly scores for attacks but it also had higher thresholds to avoid false positives
    * Overall similar performance as 1-gram IDS
    * More costly for IDS
* Local substitution always outperformed global substitution

## Countermeasures of IDS

* IDS Models
    * More complex models
    * Blend more models
* Features
    * Syntactic and semantic information
* High speed hardware
* Measure randomness

## Limitations and Improvements

* PAYL is the only case study
* Are the assumption of PBA are realistic
* Explore techniques for continuous data streams

## References

* Polymorphic Blending Attacks, Fogla et al, 2006
* [CDA6938 Special Topic:Research in Computer and Network Security (Spring 2007)](http://www.cs.ucf.edu/~czou/CDA6938/Polymorphic_blending_attacks_Himanshu_Pagey.ppt)
* [CIS 864 - Advanced Topics in Network Security - Spring 2007](https://www.eecis.udel.edu/~sunshine/courses/S07/CIS864/blend.ppt)
* Sergio Pastrana, Agustin Orfila, Juan E. Tapiador, Pedro Peris-Lopez, Randomized Anagram revisited, In Journal of Network and Computer Applications, Volume 41, 2014, Pages 182-196, ISSN 1084-8045, 
* CS 259D Lecture 14
