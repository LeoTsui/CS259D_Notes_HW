# A Multi-Model Approach to the Detection of Web-Based Attacks

<!-- TOC -->

- [Background Knowledge and Insights](#background-knowledge-and-insights)
    - [Assumptions of Anomaly Detection](#assumptions-of-anomaly-detection)
    - [Web Security](#web-security)
    - [Web-related Attack Detection](#web-related-attack-detection)
- [Goals and Contributions](#goals-and-contributions)
- [Sample Date](#sample-date)
- [Data model](#data-model)
- [Detection models](#detection-models)
    - [Attribute length](#attribute-length)
        - [User](#user)
        - [Attacker](#attacker)
        - [Learning](#learning)
        - [Detection](#detection)
    - [Attribute character distribution](#attribute-character-distribution)
        - [User](#user-1)
        - [Attacker](#attacker-1)
        - [Learning](#learning-1)
        - [Detection](#detection-1)
    - [Structural Inference](#structural-inference)
        - [User](#user-2)
        - [Attacker](#attacker-2)
        - [Learning](#learning-2)
        - [Detection](#detection-2)
    - [Token finder](#token-finder)
        - [User](#user-3)
        - [Attacker](#attacker-3)
        - [Learning](#learning-3)
        - [Detection](#detection-3)
    - [Attribute presence or absence](#attribute-presence-or-absence)
        - [User](#user-4)
        - [Attacker](#attacker-4)
        - [Learning](#learning-4)
        - [Detection](#detection-4)
    - [Attribute order](#attribute-order)
        - [User](#user-5)
        - [Attacker](#attacker-5)
        - [Learning](#learning-5)
        - [Detection](#detection-5)
    - [Access frequency](#access-frequency)
        - [User](#user-6)
        - [Attacker](#attacker-6)
        - [Learning](#learning-6)
        - [Detection](#detection-6)
    - [Inter-request time delay](#inter-request-time-delay)
        - [User](#user-7)
        - [Attacker](#attacker-7)
        - [Learning](#learning-7)
        - [Detection](#detection-7)
    - [Invocation order](#invocation-order)
        - [User](#user-8)
        - [Attacker](#attacker-8)
        - [Learning](#learning-8)
        - [Detection](#detection-8)
- [Limitation](#limitation)
- [References](#references)

<!-- /TOC -->

## Background Knowledge and Insights

### Assumptions of Anomaly Detection

* Relay on models of the intended behavior of user and application
* Assume attack patterns is **different** from normal behavior
* The **difference** can be expressed either **quantitatively** or **qualitatively**
* Interprets deviations from this "normal" behavior as **evidence**

### Web Security

* Web servers accessible by outside world
* Web apps developed with security as an afterthought

### Web-related Attack Detection

* Misuse-based detection
    * Example: Snort
        * 1037 out of 2464 signatures
    * Hard to keep up-to-date
        * Time-intensive, error-prone, requires significant security expertise
    * Challenge with apps developed in-house
    * Unable to detect un-modeled attacks
* Anomaly-based
    * Applicable to custom-developed web apps
    * Support detection of new attacks

## Goals and Contributions

* Unsupervised, learning-based anomaly detection
* Deployed on host
* A number of different models
    * Reduce vulnerability of mimicry attacks
* Target specific types of applications
    * More focused analysis

## Sample Date

| Data set  | Time interval | Size (MByte) | HTTP queries | Programs | Program requests | Attributes |
|-----------|---------------|--------------|--------------|----------|------------------|------------|
| Google    | 1 h           | 236          | 640,506      | 3        | 490,704          | 1,611,254  |
| UCSB      | 297 days      | 1001         | 9,951,174    | 2        | 4617             | 7993       |
| TU Vienna | 80 days       | 251          | 2,061,396    | 8        | 713,500          | 765,399    |

## Data model

![Sample web server access log entry](images/Sample_web_server_access_log_entry.png)

* An ordered set $$U=\{u_1,u_2,...,u_m\}$$ of URIs
    * Extract from successful GET requests
    * $$200 \leq \text{return-code} < 300$$
* Components of $$u_i$$
    * Path to desired resource: $$path_i$$
    * Optional path information: $$pinfo_i$$
    * Optional query string: $$q$$
        * Following a `?` Character
        * Passing parameters to referenced resource
        * Attributes and values: $$q = (a_1, v_1), (a_2, v_2), ..., (a_n, v_n)$$
        * $$A$$, the set of all attributes, $$a_i$$ belongs to $$A$$
        * $$v_i$$, string
        * $$S_q = \{a_1=v_1, a_2=v_2, ..., a_n=v_n\}$$
* URIs without query strings not included in $$U$$
* $$U_r$$: subset of $$U$$ with resource path $$r$$
    * Partition $$U$$
    * Anomaly detection run independently on each $$U_r$$

## Detection models

* One query, one model
* Alerting on a single anomalous attribute is **necessarily cautious**
* Training mode
    * Create profiles for each server-side program and each of its attributes
    * Establish suitable thresholds
        * Store the highest anomaly score
        * Default thresholds: $$10\%$$ larger than the max anomaly score in training mode
* Detection mode
    * Task: returns probability $$p$$ of normalcy
    * Anomaly Score, $$\sum_{m \in \text{Models}} w_m (1 - p_m)$$
        * Has an associated weight $$w$$
            * Default $$\text{value} = 1$$, in this paper

### Attribute length

* Length distribution not follow a smooth curve
* Distribution has a large variance

#### User

* Fixed size tokens
    * Session identifiers
* Short input strings
    * Fields in an HTML form

#### Attacker

* Buffer overflow: shell code and padding
    * Several hundred bytes
* XSS

#### Learning

* Estimate mean $$\mu$$ and variance $$\sigma^2$$ of lengths in training data

#### Detection

* Strings with length larger than mean
    * If $$\text{length} < \text{mean}$$, $$p = 1$$
    * Padding not effective
* Chebyshev inequality is weak bound
* Useful to flag only significant outliers

### Attribute character distribution

* Character distribution: sorted relative frequencies
    * Lost connection between individual characters and relative frequencies
        * `passwd`: 0.33, 0.17, 0.17, 0.17, 0.17, 0, ..., 0
        * As same as `aabcde`
    * Fall smoothly for human-readable tokens
    * Fall quickly for malicious input

#### User

* Observations about attributes
    * Regular structure
    * Mostly human readable
    * Almost always contain only printable characters
* Frequencies of query parameters distribution
    * Similar identical to a standard English text

#### Attacker

* Repeated padding characters cause frequencies drop extremely fast
* Example
    * Buffer overflow: needs to send binary data and padding
    * Directory traversal exploit: many `.` in attribute value

#### Learning

* Character distribution of each observed attribute is stored
* Average of all character distributions computed

#### Detection

* Variant of the $$\text{Pearson}\ \chi^2\text{-test}$$
    * Goodness-of-fit
* Bins: $$\{[0], [1, 3], [4, 6], [7, 11], [12, 15], [16, 255]\}$$
* For each query attribute:
    * Compute character distribution
    * Observed frequencies $$O_i$$ : Aggregate over bins
    * Expected frequencies $$E_i$$ : Learned character distribution attribute length
* Compute: $$\chi^2 = \sum_{i=0}^{i<6} \frac{(O_i - E_i)^2}{E_i}$$
* Read corresponding probability

### Structural Inference

#### User

* Parameter structure
    * Regular grammar describing all of its legitimate values

#### Attacker

* Exploits requiring different parameter structure
    * Examples: Buffer overflow, directory traversal, XSS
* Simple manifestations of an exploit
    * Unusually long parameters
    * Parameters containing repetitions of non-printable characters
* **Evasion**
    * Replace non-printable characters by groups of printable characters

#### Learning

* Seems to be "reasonable"
* Stop before lost much structural information
* Goal: Find a model(NFA) with highest likelihood given training examples
* Markov model/Non-deterministic finite automaton (NFA)
    * "Reasonable generalization"
    * $$P_s(o)$$: probability of emitting symbol $$o$$ at state $$S$$
    * $$P(t)$$: probability of transition $$t$$
    * Output: paths from Start state to Terminalstate
* Bayesian model induction
    * $$P(\text{model}\mid\text{training}\_\text{data}) = \frac{p(\text{training}\_\text{data}\mid\text{model})*p(\text{model})}{p(\text{training}\_\text{data})}$$
    * $$P(\text{training}\_\text{data})$$ a scaling factor; ignored
    * $$P(\text{model})$$: preference towards smaller models
        * Total number of states: $$N$$
        * Total number of transitions at each state $$S$$: $$T(S)$$
        * Total number of emissions at each state $$S$$: $$E(S)$$
    * Start with a model exactly reflecting input data
    * Gradually merge states
    * Until posterior probability does not increase
    * Cost: $$O((n*L)^3)$$ with n training input strings, and L maximum length of each string
    * Up to $$n*L$$ states
    * $$\frac{(n*L)(n*L-1)}{2}$$ comparisons for each merging
    * Up to $$n*(L-1)$$ merges
* Optimizations
    * Viterbi path approximations
    * Path prefix compression
    * Cost: $$O(n*L^2)$$

#### Detection

* First option: Compute probability of query attribute
    * Issue: probabilities of all input words sum up to $$1$$
    * all words have small probabilities
* Output:
    * $$p = 1$$ if word is a valid output of Markov model
    * $$p = 0$$ otherwise

### Token finder

* Goal: determine whether values of an attribute are drawn from an enumerated set of tokens

#### User

* Web applications often require one out of a few possible values for certain query attributes
    * Example: flags, indices

#### Attacker

* Use these attributes to pass illegal values

#### Learning

* Argument are enumerated or random value
    * r.v.: when the number of different argument instances grows proportional to the total number of argument instances
    * Enumeration: not exit that increase
* Compute correlation $$\rho$$ between $$f$$ and $$g$$
    * $$f(x) = x$$
    * $$g(x)$$, $$g$$ is like a "enumeration counter"
        * $$g(x) = g(x-1)+1$$ if $$x^{th}$$ value is new
        * $$g(x) = g(x-1)-1$$ if $$x^{th}$$ value was seen before
        * $$g(x) = 0$$ if $$x = 0$$
    * $$Corr = \frac{Covar(f, g)}{\sqrt{Var(f)Var(g)}}$$
        * If $$Corr < 0$$, then enumeration
        * If enumeration, then store all values for use in detection phase

#### Detection

* If enumeration: value expected to be among stored values
    * Output $$p = 1$$ or $$p = 0$$ correspondingly
    * Hash table lookup, efficiency
* If random: $$p = 1$$

### Attribute presence or absence

#### User

* URIs typically produced not directly by user, but by scripts, forms, client-side programs
    * Regularity in number, name, order of parameters

#### Attacker

* Hand-crafted attacks typically break this regularity
    * Incomplete or malformed requests to probe/exploit web app
        * Missing argument
        * Mutually exclusive arguments appearing together

#### Learning

* Create a model of acceptable subsets of attributes
* Record each distinct set $$S_q$$
    * Each query $$q$$ during training
    * Hash table

#### Detection

* Lookup the attribute set in hash table
    * Return $$p = 1$$ or $$p = 0$$ correspondingly

### Attribute order

#### User

* Same parameters in the same order
* Sequential program logic preserves order even when some attributes left out

#### Attacker

* Arbitrary
* No influence on the execution of the program

#### Learning

* Attribute $$a_s$$ precedes $$a_t$$
    * $$a_s$$, $$a_t$$ appear together in at least one query
    * $$a_s$$ comes before $$a_t$$ when they appear together
* Directed graph, $$G$$
* Vertex $$v_i$$ corresponds to attribute $$a_i$$
    * $$\#$$ vertices = $$\#$$ attributes
* For each training query, add edges between nodes of ordered attribute pairs
    * Directed edges correspond to orders of attribute pairs
* Find all strongly connected components (SCC) of the graph
* Remove edges between nodes in same SCC
    * Remove "order"s from disordered attributes groups
* For each node, find all reachable nodes
* Add corresponding pairs $$(a_s, a_t)$$ to set of precedence orders $$O$$
* Tarjan's algorithm, $$O(v + e)$$

#### Detection

* Find all order violations
    * Return $$p = 0$$ or $$p = 1$$ correspondingly

### Access frequency

* Frequency patterns of different server-side web applications
* Two types of frequencies
    * Frequency of application being accessed from a certain client
        * Base on IP address
    * Total frequency of all accesses

#### User

* Eg 1. Authentication script
    * Very infrequently for each individual client
* Eg 2. Search script
    * High for particular client
    * Low for total

#### Attacker

* Suddenly increase access frequency
* Probing
* Guess parameter values
* Evasion: slow down

#### Learning

* Divide training time to intervals of fixed time (e.g., 10 sec)
* Count accesses in each interval
* Find total and client-specific distributions

#### Detection

* Chebyshev probability for total, and for client
* Return average of the two probabilities

### Inter-request time delay

#### User

* Wide variance

#### Attacker

* Regular delay between each successive request
    * Surveillance
    * Scripted probe

#### Learning

* Find distribution of normal delays
    * Similar to character distribution model

#### Detection

* $$\text{Pearson}\ \chi^2\text{-test}$$

### Invocation order

* Order of invocation of web-based applications for each client
    * Infer session structure regularity
    * Similar to structural inference model
        * Sequence of queries, not
        * Parameters syntax of a query

#### User

* Invocation order can be generated by a certain Markov model

#### Attacker

* Can be detected when attacking application logic
* Cannot be outputed by that model

#### Learning

* Group queries based on source IP
    * Session: Queries within an interval of time
    * Build NFA for sessions
* Independent of server-side applications

#### Detection

* $$p = 1$$ or $$p = 0$$ depending on session being an output of NFA

## Limitation

* Google, nearly half of the number of false positives
    * Anomalous search strings that contain instances of non-printable characters
        * Probably requests issued by users with incompatible character sets
    * Extremely long strings
        * Such as URLs directly pasted into the search field

## References

* A multi-model approach to the detection of web-based attacks, 2005
* CS 259D Lecture 8
