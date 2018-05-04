# Challenging the Anomaly Detection Paradigm: A Provocative Discussion

<!-- TOC -->

- [Definitions of Anomaly](#definitions-of-anomaly)
- [Problems with Anomaly Detection](#problems-with-anomaly-detection)
    - [Assumptions](#assumptions)
    - [Training Data](#training-data)
    - [Operational Usability](#operational-usability)
- [Recommendations](#recommendations)
- [References](#references)

<!-- /TOC -->

## Definitions of Anomaly

* Three types of anomalous
    * Foreign-symbol anomalous
        * Character or item appears first time
    * Foreign n-gram anomalies
        * Previously unseen sequence of characters
    * Rare n-gram anomalies
        * Sequence of characters appears more than once, but below a user specified threshold
* Anomalous not malicious
* Definition of "malicious"
    * Subjective
    * Site-specific

## Problems with Anomaly Detection

### Assumptions

* Attacks are anomalous (different from the norm)
    * Blind spots of detector
    * Hide attack actions
* Attacks are rare
    * Anomaly not the smallest cluster 
    * Scanning is on the top of flow counts
* Anomalous activity is malicious
    * Alpha flows (very large point-to-point data exchanges)
    * _DoS_
    * Flash crowds
    * _Port scans_
    * _Network scans_
    * Outage events
    * Point-to-multipoint connection (such as content distribution mechanisms)
    * _Worms_

### Training Data

* Attack-free data is available
    * Malicious behavior could last for many days
    * Attack free data hard to obtain
* Simulated data is representative
    * Suspicious simulated data
    * Labeled data expensive to obtain
* Network traffic is static
    * Hard to retrain or update IDS in a drifting environment
        * IDS should be an unsupervised learning system
    * High weight for recent data

### Operational Usability

* False alarm rates > 1% are acceptable
    * Depend on the traffic volume
* The definition of malicious is universal
    * Depend on the organization
* Administrators can interpret anomalies
    * They are tired

## Recommendations

* More clearly define
* More specific purpose
* More IDS models
* More tests

## References

* Challenging the Anomaly Detection Paradigm: A Provocative Discussion, Gates-Taylor, 2007
* CS 259D Session 13
