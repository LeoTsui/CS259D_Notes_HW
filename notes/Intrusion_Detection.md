# Intrusion Detection

<!-- TOC -->

- [Intrusion Detection System](#intrusion-detection-system)
    - [Intrusion Detection](#intrusion-detection)
    - [Intrusion Detection System](#intrusion-detection-system-1)
    - [Classifications and Pros and Cons](#classifications-and-pros-and-cons)
- [References and Recommended Readings](#references-and-recommended-readings)

<!-- /TOC -->

## Intrusion Detection System

### Intrusion Detection

* Intrusion detection is the process of monitoring a network or systems for malicious activity or policy violations

### Intrusion Detection System

![IDS](images/IDS.png)

* Intrusion Detection System (IDS), a system that combines hardware and software to detect intrusion
* Raise the alarm when possible intrusion happens

### Classifications and Pros and Cons

* Misuse based (signature based)
    * Designed to detect known attacks by signatures
    * Less false alarms
    * Frequently manual update signatures dataset
    * Cannot detect novel (Zero-day) attacks
* Anomaly based
    * Identifies the anomalies from normal behavior
    * Able to detect Zero-Day Attack
    * Profiles of normal activity are customized for every system
    * More false alarms
* Hybrid
    * Combination of misuse and anomaly detection
    * Increases the detection rate and decreases the false alarm generation

## References and Recommended Readings

* Network Anomaly Detection: Methods, Systems and Tools
* A Survey of Data Mining and Machine Learning Methods for Cyber Security Intrusion Detection
* [\[Lecture\] A Survey of Data Mining and Machine Learning Methods for Cyber Security Intrusion Detection](http://www.parkjonghyuk.net/lecture/2017-2nd-lecture/forensic/s2.pdf) by Pradip Kumar Sharma
* The Use of Computational Intelligence in Intrusion Detection Systems: A Review
* [To use the concept of Data Mining and machine learning concept for Cyber security and Intrusion detection](https://www.slideshare.net/nishantmehta9849/to-use-the-concept-of-data-mining-and-machine-learning-concept-for-cyber-security-and-intrusion-detection)
