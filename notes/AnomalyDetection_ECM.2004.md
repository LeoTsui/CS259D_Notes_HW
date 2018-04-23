# Anomaly Detection Using Layered Networks Based on Eigen Co-occurrence Matrix Note

<!-- TOC -->

- [Background Knowledge](#background-knowledge)
- [Insights and Goals](#insights-and-goals)
- [Eigen co-occurrence matrix (ECM)](#eigen-co-occurrence-matrix-ecm)
- [References](#references)

<!-- /TOC -->

## Background Knowledge

* Hard to accurately model user behavior
    * Dynamic user's behavior
    * Difficult to capture completely
* Model user behavior
    * Feature vector
        * Histogram
            * No sequence
        * N-grams
            * N-connected sequence
        * Correlation between un-adjacent events
    * Network model
        * Automaton
            * Require well-defined rules
            * Various contexts not have well-defined rules
        * Bayesian network
            * Bayesian network indicates the direction of causality between the corresponding variables
            * Topology must be predefined
        * Hidden Markov Model (HMM)
            * Hard to build an adequate topology

## Insights and Goals

* Assumption
    * The dynamic behavior of a user appearing in a sequence can be captured by correlating not only connected events but also events that are not adjacent to each other while appearing within a certain distance (non-connected events)
* ECM, Eigen co-occurrence matrices
    * Inspired by the Eigenface technique
    * Three main components
        * Modeling of the dynamic features of a sequence
        * Extraction of the principal features of the resulting model
        * Automatic construction of a layered network from the extracted principal features

## Eigen co-occurrence matrix (ECM)

* Handwritten Notes :)

## References

* Anomaly Detection Using Layered Networks Based on Eigen Co-occurrence Matrix
* Anomaly Detection Using Integration Model of Vector Space and Network Representation
