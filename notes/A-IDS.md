# Adaptive Intrusion Detection System via Online Machine Learning

<!-- TOC -->

- [Background Knowledge and Insights](#background-knowledge-and-insights)
- [Goals](#goals)
- [Data Source](#data-source)
- [Feature](#feature)
- [Adaptive Intrusion Detection System (A-IDS)](#adaptive-intrusion-detection-system-a-ids)
    - [Mixing Algorithm](#mixing-algorithm)
        - [Notation](#notation)
        - [Algorithm](#algorithm)
- [Experimental](#experimental)
- [Limitation](#limitation)
- [References](#references)

<!-- /TOC -->

## Background Knowledge and Insights

* Diverse network environments
* Dynamic attack types
* Adversarial environment
* IDS performance strongly depends on chosen classifier
    * Misuse IDS
        * Detect known attacks
        * SNORT: signature-based IDS
    * Anomaly IDS
        * Detect novel attacks
        * More FP
    * **Perform differently in different environments**
    * **No Free Lunch Theorem**
* Combination IDSs
    * High cost
    * Majority voting
    * Incorrect
        * Majority can be wrong
* Hedge/Boosting
    * Online learning framework
    * Chose best IDS in period T
    * Destroy the superiority of the best IDS by changing the attacks all the time
    * All IDSs perform badly
* Adaptability of the IDS
    * Adapt to dynamic adversarial environments
    * How to choose the best

## Goals

* New efficient online learning framework
* Adaptive Intrusion Detection System (**A-IDS**)

## Data Source

* ECML-PKDD HTTP 2007
    * 50,000 samples, 20% attacks
        * Attacks or Normal
    * Attacks
        * Cross-Site Scripting
        * SQL injection
        * LDAP injection
        * XPATH injection
        * Path traversal
        * Command Execution
        * SSI attacks
* CSIC HTTP 2010
    * 61,000 samples, 41% attacks
        * Anomalous or Normal
    * Traffic data
        * Realistic
        * Developed for this purpose
        * E-commerce Web APP
        * Apache server
    * Attacks
        * SQL injection
        * Buffer overflow
        * Information gathering
        * CRLF injection
        * XSS
        * Server side include
        * Parameter tampering

## Feature

* 30 features
    * Length
    * Number
    * Max
    * Min
    * Type of header
    * Four types of characters
        * Letters
        * Digits
        * Non-alphanumeric characters
            * Special meanings in programming languages
            * "special" char
        * Others
    * Entropy
    * Programming languages keywords


## Adaptive Intrusion Detection System (A-IDS)

* Base IDS
    * Base classifiers
        * Naïve Bayes
        * Bayes Network
        * Decision Stump
        * RBF Network
    * **No assumptions on selection of baseline classifiers**
    * 10-folds cross-validation
* *Loss Update*
    * Hedge/Boosting algorithm
* *Mixing Update*
    * Bousquet and Warmuth's algorithm (2002)
    * Quick recovery property of the IDSs to deal with their favorite data
        * Remembering the past average weight vector
* Supervised Framework
    * Combine results of base IDSs
    * Receive the true label of the current sample
    * Measure losses between IDS outputs and true label
    * Maintain weights for base IDSs

### Mixing Algorithm

#### Notation

* $$T$$, $$\#$$ instances
* $$t$$, $$(t=1,...,T)$$, a certain time or trial
* $$n$$, $$\#$$ base IDSs
* $$i$$, $$i \in \{ 1, 2, ..., n \}$$, the index of base IDSs
* $$x_t$$, a vector of $$n$$ IDS's output
    * A-IDS receives $$x_t$$
    * $$x_t = (x_{t,1}, ..., x_{t,n})$$
        * where $$x_{t, i} \in \{0\text{(normal)}, 1\text{(attack)}\}$$
* $$pred(t)$$, the prediction of A-IDS
* $$y_t$$, $$y_t \in \{0, 1\}$$, the true label of the $$t\text{-th}$$ instance at the time $$t$$
* $$L$$, loss function
    * For the trial $$t$$, and the $$i\text{-th}$$ IDS
    * $$L_{t, i} = (y_t - x_{t, i})^2$$
    * Measure the discrepancy between the true label and the predictions of the base IDSs
* $$v_t$$, the weight vector maintained by the A-IDS
    * $$v_t = (v_{t,1}, v_{t,2}, ..., v_{t,n})$$
    * $$v_{t,i} \geq 0$$
    * $$\sum_{i = 1}^n v_{t,i} = 1$$

#### Algorithm

* Parameters
    * $$\eta > 0$$, learning rate
    * $$0 \leq \alpha \leq 1$$
    * $$n$$
* Initialization
    * $$v_1 = v_0^m = (1/n, ...,  1/n, ..., 1/n)$$
* For $$t=1 \to T$$
    * Prediction
        * $$\hat y_t = v_t \cdot x_t$$
        * $$pred(t)$$:
            * $$0$$, $$0 \leq \hat y_t \leq 0.5$$
            * $$1$$, $$\hat y_t \geq 0.5$$
    * *Loss Update*
        * Find the best IDS from a pool of $$n$$ base ones
        * $$L_{t, i} = (y_t - x_{t, i})^2$$
        * $$e^{-\eta L_{t,i}}$$, a factor
        * $$v_{t,i}^m = {v_{t,i} e^{-\eta L_{t,i}}} / {\sum_{j=1}^n v_{t,j} e^{-\eta L_{t,j}}}$$
    * *Mixing Update*
        * $$av_t = \frac{1}{t} \sum_{q=0}^{t-1} v_q^m$$, average weight vector 
        * $$v_{t+1} = \alpha av_t + (1-\alpha)v_t^m$$

## Experimental

* Expert setting (Not Mixing Update)
    * Single intrusion detection cannot detect all types
        * Good performance on special segments
        * Need combination
    * *Loss Update*
        * $$\eta = 0.1$$
    * Not *Mixing Update*
        * $$v_{t_1,i} = v_{t,i}^m$$
        * Combination is not help
        * The performance is almost the same as the best IDS
* Expert Combining (A-IDS)
    * Simulate adversarial environment
        * Random permutation
    * 10-folds cross-validation
    * Mixing Algorithm
        * $$\eta = 0.1$$
        * $$\alpha = 0.001$$
        * Uniform Past update
* Expert Expanding (A-ExIDS)

## Limitation

* Lose Update is double-edge knife
    * The best $$v_{t,i}$$($$L_{t,i} = 0$$) controls $$v_{t,i}^m$$
    * Hard to recover if an IDS temporarily performs poorly and then performs well
    * Consequence
        * Slow adaptation about changes in IDSs' performances
        * Attackers can change attack patterns all the times

## References

* Adaptive Intrusion Detection System via Online Learning, 2012
* CS 259D Session 10
