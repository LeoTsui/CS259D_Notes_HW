# Deep Packet Inspection and Polymorphism

<!-- TOC -->

- [Packet Inspection](#packet-inspection)
    - [Depth of Packet Inspection](#depth-of-packet-inspection)
    - [Deep Packet Inspection(DPI)](#deep-packet-inspectiondpi)
- [Evade Deep Packet Inspection](#evade-deep-packet-inspection)
- [References](#references)

<!-- /TOC -->

## Packet Inspection

### Depth of Packet Inspection

![Packet Inspection Depth](images/DPI_2.png)

### Deep Packet Inspection(DPI)

* Most network flows are not correctly classified using port-based classification(traditional packet inspection)

![Domain of Deep Packet Inspection](images/DPI_1.png)

* Deep packet inspection: check the payload of the packets, and handle the packets based on specific patterns present in the payload
* Applications
    * Network Security
        * Malicious URLs/websites
        * Malicious payload
        * Inside data loss prevention(DLP)
        * Signature detection
    * Bandwidth Management
    * User Profiling/Ad Injection
    * Billing and Metering of Traffic
    * Information Regulations and Filtering
    * Copyright Enforcement
    * Government Surveillance and censorship
* Challenges
    * Performance bottlenecks at OS and hardware levels
    * Hard to scale with high speed links
    * Massive and variable feature signatures
    * Encrypted traffic
    * Polymorphism of payloads
    * Privacy and legal concerns

## Evade Deep Packet Inspection

* Traffic Obfuscation
* Encryption and Tunneling
* Polymorphism
    * Interleaving meaningful instructions with DO-NOTHING instructions
    * Using different instructions to achieve the same result
    * Shuffling the register set used in each version of the polymorphic decryptor
    * Decrypting and reencrypting parts of the polymorphic decryptor as it is being executed
    * Using several layers of decryptors

## References

* [What is Deep Packet Inspection ?](https://computersecuritypgp.blogspot.com/2016/04/deep-packet-inspection.html)
* [Deep Packet Inspection : The impact of a new technology on Internet regulation](http://globalgovernanceprogramme.eui.eu/wp-content/uploads/2013/01/Milton-Mueller.pdf)
* Deep packet inspection tools and techniques in commodity platforms: Challenges and trends
* [White paper on Deep Packet Inspection](http://tec.gov.in/pdf/Studypaper/White%20paper%20on%20DPI.pdf)
