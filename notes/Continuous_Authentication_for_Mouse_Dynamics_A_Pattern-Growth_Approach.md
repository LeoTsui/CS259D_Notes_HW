# Continuous Authentication for Mouse Dynamics: A Pattern-Growth Approach

<!-- TOC -->

- [Background Knowledge](#background-knowledge)
- [Goal and Contribution](#goal-and-contribution)
- [Data(Mouse Behavior Data)](#datamouse-behavior-data)
    - [Data Source](#data-source)
    - [Mouse Behavior Analysis](#mouse-behavior-analysis)
    - [Mouse Behavior Pattern Mining](#mouse-behavior-pattern-mining)
        - [Notation](#notation)
        - [Mining Method](#mining-method)
        - [References-Behavior Pattern Generation and Matching](#references-behavior-pattern-generation-and-matching)
        - [Behavior Pattern Analysis](#behavior-pattern-analysis)
- [Feature](#feature)
    - [Feature Construction from Mined Pattern](#feature-construction-from-mined-pattern)
    - [Empirical Feature Study](#empirical-feature-study)
- [Detection Implementation](#detection-implementation)
- [Limitation](#limitation)
- [References](#references)

<!-- /TOC -->

## Background Knowledge

* User Authentication Mechanism
    * Only at the initial login session
    * Continuous (re)authentication
        * Passive
        * Transparent to users
            * No hit on usability
* Mouse dynamics
    * Intrinsic behavioral variables
        * Intrinsic human factors
            * Biological or emotional status of the user
        * External environmental variables
            * Software environment, task, interaction mode
    * No enough data for malicious users
    * No public data set in mouse dynamics research
* Mouse Behavior Pattern
    * Frequently **recurring** behavior segments
    * **Fixed** series of consecutive operations
* Hypothesis
    * Observation
        * Measurements extracted from behavior patterns are more stable than from holistic behavior
    * Assumption
        * Recurring and fixed behavior patterns
            * Provide more stable and discriminative features or measurements
            * Allow to more accurately characterize the discriminable components of mouse behavior
* One-Class Classification
    * Only legitimate user patterns are available
    * Useing both the legitimate user's and impostors' samples is not practical
        * Too much impostors' samples in realistic applications

## Goal and Contribution

* Using a pattern-growth­ based mining method to extract frequent-behavior segments
* One-class classification
* Established a new mouse behavioral data set
* Develop a simple and efficient continuous user authentication method

## Data(Mouse Behavior Data)

### Data Source

* Set an experimental environment
* Same computer hardware configuration
* All users are college students(Some people majoring in computer science)
* 28 participants
    * ~90,000 mouse actions/user
    * 30 sessions
        * Each 30 minute
        * Internet surfing, word processing, online chatting, programming, online gaming
        * Between 30-60 days per participant
* Data record
    * Event type (e.g., mouse move/click), position, timestamp, application information

### Mouse Behavior Analysis

* Mouse events
    * System messages sent to receiving applications
        * Inform current cursor position & mouse button status
    * Types
        * Mouse Down
        * Mouse Up
        * Mouse Wheel
        * Mouse Move
* Mouse actions
    * Single click
        * Mouse down followed by mouse up
    * Double click
        * Mouse down, up, down, up
    * Common movement
        * General mouse movement with no clicks
    * Point and click movement
        * Mouse movement followed by single/double click
    * Drag and drop movement
        * Mouse down, movement, mouse up
    * Silence
        * No mouse operation
* Encoded **Mouse action** into **Mouse operation**
* Mouse operation
    * Truple:
        * `<action-type, application-type, screen-area, window-position, timestamp>`
* Mouse-Behavior pattern: recurring & fixed segments
    * Micro-habitual patterns
        * Subconscious/habitual factors urging GUI interactions
    * Task-intended patterns
        * Operating habits under certain applications (e.g., using certain function of an application)
            * Example: creating a new document in a word processing app

### Mouse Behavior Pattern Mining

#### Notation

* $$I = \{i_1 , i_2, ..., i_n\}$$, a set of all mouse operations
* $$\mathrm{operation}\text{-}\mathrm{set}$$, a set of mouse operations
    * Example: $$\{(1,3,4,0), (2,1,4,0), (3,1,4,0)\}$$
* $$s$$, sequence: ordered list of operation sets by user ID and timestamp
    * $$s = \{s_1, s_2, ..., s_k\}$$, each $$s_j$$
        * An $$\text{operation-set}$$ (subset of $$I$$), $$s_j \subset I$$, for $$1 \leq j \leq l$$
        * Called an element of sequence $$s$$
        * $$s_j = \langle x_1, x_2, ..., x_m \rangle$$, each $$x_k$$ is a mouse operation
    * Example:
        * $$s = \{\langle(1,3,4,0)\rangle, \langle(1,3,4,0), (2,1,4,0), (3,1,4,0)\rangle, \langle(2,1,2,1)\rangle\}$$
        * $$\mathrm{length}(s) = 5$$
* $$\alpha$$, a subsequence of $$s$$
    * Example
        * $$\{\langle(1,3,4,0)\rangle\}$$ is a subsequence of $$\{\langle(1,3,4,0), (2,1,4,0), (3,1,4,0)\rangle\}$$
* $$L$$, length of sequence: the number of mouse operation instances
    * $$\text{L-sequence}$$: A sequence of length $$L$$
* $$S$$, a mouse operation sequence database
    * A set of triples $$\langle ID, sid, s \rangle$$
        * $$ID$$, the user ID
        * $$sid$$, a sequence $$ID$$
        * $$s$$, a sequence
* $$\mathrm{Support_S} (\alpha)$$ = $$\#$$ tuples in databases $$S$$ that contain $$\alpha$$
* Sequential pattern, if $$\mathrm{Support_S} \geq \xi$$
    * $$\xi$$ a given threshold
* **Problem Statement**
    * Sequential mouse behavior pattern mining is
        * Input
            * Mouse operation sequence $$S$$
            * minimun support threshold $$\xi$$
        * Output
            * Complete set of all frequent mouse behavior patterns in $$S$$

#### Mining Method

* PrefixSpan
    * Mining Sequential Patterns by Pattern­ Growth: The PrefixSpan Approach (2004)
    * Project the database into a set of smaller databases
        * Based on set of patterns mined so far
    * Mine locally frequent patterns in each projected database

#### References-Behavior Pattern Generation and Matching

* Create "baseline", normal behavior pattern generation
    * For each user
        * Mine behavior patterns from each session
        * Collect all patterns as reference behavior pattern
* Pattern matching
    * Given a new operation sequence match against mined patterns
        * Search patterns
        * Output all matching patterns

#### Behavior Pattern Analysis

* Set minimum support $$8\%$$
    * Trade-off value, between minimum support and true effectiveness of behavior patterns

## Feature

* Frequent-behavior patterns cannot be used directly

### Feature Construction from Mined Pattern

* Click elapsed time
    * Time spent by user to perform a click action
    * Single click: $$\mathrm{Avg}$$, $$\mathrm{SD}$$ of overall time
    * Double click: $$\mathrm{Avg}$$, $$\mathrm{SD}$$ of overall & 3 interval times
* Movement speed
    * Average movement speed for different types of mouse movement
    * 24 types: 8 directions, 3 distance ranges
* Movement acceleration
    * Average acceleration for different types of mouse movement
    * Similar to movement speed
* Relative position of extreme speed of the movement curve
    * Example: 0.5 for middle position of movement speed curve
* **Total: 92 features**
    * 20 click-related features
    * 24 movement-related features
        * Only from common & point-and-click movements
    * 24 acceleration-related features
    * 24 extreme-speed-related features

### Empirical Feature Study

* Stability of Features in Behavior Pattern
    * Feature can be skewed by
        * Environmental variables
        * Human factors
    * Example
        * Finding documents (Not sure where is it)
    * Kernel density estimation
        * a non-parametric way of estimating the probability density function (PDF) of a random variable
    * Compute PDF for each feature from
        * Behavior patterns
        * Holistic behavior
* Discriminability of Features in Behavior Patterns
    * The features extracted from behavior pattern evidently superior to those extracted from holistic behavior
        * More stable
        * More discriminable
* Statistical Dispersion of Features Across Subjects

## Detection Implementation

* Nearest-Neighbor
    * $$k = 3$$
    * Anomaly score
        * Mahalanobis distance between test & training feature vectors
* Neural Network
    * Single hidden layer
        * Input nodes, $$p$$
        * Hidden nodes, $$\lfloor2p/3\rfloor$$
        * Output node, $$1$$
    * Train the detector with every input feature vector to output $$=1.0$$
    * Test-vector fed into network, output $$\sim$$ $$1.0$$ or $$-1.0$$
* One-class SVM
    * RBF kernel

## Limitation

* Samples are only come from the certain organization (college)
* No impostors' samples
* Need to collect data and train models for every deploy

## References

* Continuous Authentication for Mouse Dynamics: A Pattern-Growth Approach (C. Shen et al., 2012)
* CS 259D Lecture 5
