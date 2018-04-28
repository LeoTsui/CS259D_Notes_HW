# McPAD : A Multiple Classifier System for Accurate Payload-based Anomaly Detection

<!-- TOC -->

- [Goals and Contributions](#goals-and-contributions)
- [Architecture](#architecture)
    - [One-class SVM](#one-class-svm)
    - [Fusion rules](#fusion-rules)
    - [McPAD](#mcpad)
    - [Attacks](#attacks)
- [Data](#data)
- [Limitation](#limitation)
- [References and Recommended Readings](#references-and-recommended-readings)

<!-- /TOC -->

## Goals and Contributions

* Improve $$2$$-grams

## Architecture

### One-class SVM

* [Introduction to One-class Support Vector Machines](http://rvlasveld.github.io/blog/2013/07/12/introduction-to-one-class-support-vector-machines/)

### Fusion rules

* Combine all different One-Class SVM
* Min, Max, Mean, Product, Majority voting
* Applied to a-posteriori class probabilities under different models, $$p_i(\mathrm{x}|\omega)$$
* Assuming uniform distribution for outliers can turn these rules into class-conditional probabilities

### McPAD

![Overview of McPAD](images/McPAD.png)

* Feature Extraction
    * $$2_v$$-grams, $$65536$$ dimensions
        * $$n$$-grams, $$256^n$$ dimensions
        * For $$v = 0$$, $$2$$-gram model (of PAYL)
        * Size of sliding window, $$v + 2$$
    * No auto way to derive $$2_(v-1)$$-grams, $$2_(v-2)$$-grams from $$2_v$$-grams
        * Not like $$n$$-grams
        * Different $$v$$ cause different structural information about the payload
* Feature Reduction
    * Feature clustering algorithm

### Attacks

* Generic attacks
* Shell-code attacks
* CLET attacks
* PBA(Polymorphic Blending Attack) attacks

## Data

* Normal
    * DARPA
    * GATECH
* Attacks
    * Public non-polymorphic HTTP attack
    * Create polymorphic HTTP attack
    * Hard to collect a sufficient amount of attack traffic

## Limitation

* [High FP rate](http://www.cse.chalmers.se/edu/course/DAT285B/SLIDESNOTES/NGramPresentation.pptx)

## References and Recommended Readings

* McPAD : A Multiple Classifier System for Accurate Payload-based Anomaly Detection, Perdisci et al, 2009
* HMMPayl: An intrusion detection system based on Hidden Markov Models, Ariu, 2011
* [McPAD and HMMPayl Two Multiple-Classifier Payload-based Anomaly Detectors](http://pralab.diee.unica.it/en/HMMPayl_and_McPAD)
* CS 259D Lecture 15
