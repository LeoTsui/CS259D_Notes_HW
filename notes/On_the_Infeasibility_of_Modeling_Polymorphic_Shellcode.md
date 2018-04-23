# On the Infeasibility of Modeling Polymorphic Shellcode

<!-- TOC -->

- [Background Knowledge and Insights](#background-knowledge-and-insights)
    - [Shellcode](#shellcode)
    - [Signature Matching](#signature-matching)
    - [Decoder and Decoder Detector](#decoder-and-decoder-detector)
- [Goals and Contributions](#goals-and-contributions)
- [Polymorphic Engine Analysis](#polymorphic-engine-analysis)
    - [Notation](#notation)
    - [Problem Definition](#problem-definition)
    - [Measures](#measures)
        - [Spectral Image](#spectral-image)
        - [Minimum Euclidian distance](#minimum-euclidian-distance)
        - [Variation strength](#variation-strength)
        - [Propagation strength](#propagation-strength)
        - [Overall strength](#overall-strength)
- [Hybrid Engine: Combining Polymorphism and Blending](#hybrid-engine-combining-polymorphism-and-blending)
- [References](#references)

<!-- /TOC -->

## Background Knowledge and Insights

### Shellcode

* Traditional shellcode structure
    * [nop][**payload**][retaddr]
* Encrypted shellcode structure
    * [nop][**decoder**][**encpayload**][retaddr]
* Modern obfuscation technique
    * Automatically re-write code
        * Hard(NP-complete) to decompose to graph
    * Code-obfuscation
        * Encrypt
        * Dynamically decrypt at runtime
        * Remain code obfuscated at transmission

### Signature Matching

* String-based signatures
    * Snort
* Detection heuristics
    * Frequency of various packet types
* Identification of NOP sled
* Signature from the actual actual exploit code
* Statistical measures of packet content

### Decoder and Decoder Detector

* Look for decoder rather than payload
* **How well the decoder can be hidden**
    * Rearranging and randomizing the order of the individual ciphers components
    * Randomly chosen keys
    * Insert junk instructions
* Decoder
    * Components
        * Modification operation
            * `add`, `sub`, `xor`, etc.
        * Loop component
            * `jmpz`
    * Maintenance behaviors, more than "decoding"
        * Clear register
        * Multiple cipher operation
        * Calculate the location of the executable

## Goals and Contributions

* Describe shellcode and code obfuscation techniques
* Measure the strengths of polymorphic engines
* Introduce a hybrid engine
* Proved: Given any normal statistical model, there is a significant probability that an attacker can craft successful targeted attacks against it.

## Polymorphic Engine Analysis

### Notation

* $$n$$, $$\#$$ string bytes
* $$N$$, $$\#$$ samples
* $$\mathbf{x}$$ ($$\mathbf{y}$$), set of column vectors (samples)
* $$\mathbf{x}_i$$ ($$\mathbf{x}_j$$), $$i, j  = 1 ... N$$, the $$i^{th}$$ ($$j^{th}$$) vector (sample) in the set $$\mathbf{x}$$
* $$\mathbf{x}(i)$$, the $$i^{th}$$ component of the vector $$\mathbf{x}$$

### Problem Definition

* Given $$n$$ bytes, there exist $$256^n$$ possible strings
* *x86* code of length $$n$$ is a subspace
* How difficult is it to model this subspace?

### Measures

####  Spectral Image

![visualization of shellcode variations](images/visualization_of_shellcode_variations.png)

* $$D$$ decoders of length $$N$$
* Compile into $$D \times N$$ matrix
* Display matrix as image
    * `0x00`-`0xFF`: black-white

#### Minimum Euclidian distance

* Intuition: Decoders can shift order of operations
* String $$\mathbf{x}$$ as point in $$n$$-dimensional Euclidian space
    * Example (2D): "ab" $$\rightarrow (97, 98)$$
* Minimum Euclidian Distance: 
    * Minimum normalized distance between two points under arbitrary byte-level rotations
    * $$rot(\mathbf{y}, r)$$, rotate the string $$\mathbf{y}$$ to the left by $$r$$-bytes, with wraparound

<p align="center">$$\delta(\mathbf{x}, \mathbf{y}) = \min_{1 \leq r \leq n}\{\frac{\parallel \mathbf{x} = rot(\mathbf{y}, r) \parallel}{\parallel \mathbf{x} \parallel + \parallel \mathbf{y} \parallel}\}$$</p>

#### Variation strength

* Magnitude of the space covered by span of points in $$n$$-space corresponding to detectors
* Decoders $$x_1, x_2, ..., x_N$$ in $$n$$-space
* $$\lambda_1, \lambda_2, ..., \lambda_n$$, eigenvalues of covariance matrix
* Variation strength:

<p align="center">$$\Psi(\text{engine}) = \frac{1}{d}\sum_{i = 1}^{d}{\sqrt{\lambda_i}}$$</p>

#### Propagation strength

* Worst case of variation strength measure
    * Decoder is distributed on a hollow $$n$$-dimensional sphere with a large radius
* Efficacy in making sample pairs different
* Consider fully connected graph with decoders as nodes
    * Edge weight $$=$$ minimum Euclidian distance
    * Average edge weight $$=$$ propagation strength
* $$\eta = \#$$ salient bytes in samples
* $$\delta(\mathbf{x}, \mathbf{y})$$, distance between two samples
    * Flexible selection of distance function $$\delta$$
* Default: uniform prior, $$p(\delta(\cdot)) = 1$$
* Propagation strength:

<p align="center">$$\Phi(engine) = (1 - \frac{\eta}{n})\int\int p(\delta(\mathbf{x}, \mathbf{y}))\delta(\mathbf{x}, \mathbf{y})d\mathbf{x} d\mathbf{y}$$</p>

#### Overall strength

* Measure polymorphic engine:

<p align="center">$$\Pi(\text{engine}) = \Psi(\text{engine}) \cdot \Phi(\text{engine})$$</p>

## Hybrid Engine: Combining Polymorphism and Blending

* CLET: byte distribution blending
* ADMutate: Polymorphism
    * Random looking decoder, recursive NOP sled
* Combine CLET and ADMutate
    * Blend in with normal traffic
    * Blending bytes can be randomly permuted
    * RETADDR can be added with a random offset
    * 4-byte salient artifact too small to use as a signature
    * Essentially impossible to model

## References

* On the Infeasibility of Modeling Polymorphic Shellcode, Song et al, 2007
* On the Infeasibility of Modeling Polymorphic Shellcode Re-thinking the role of learning in intrusion detection systems, Song et al, 2009
* CS 259D Session 14
