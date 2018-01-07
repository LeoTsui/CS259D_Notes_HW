# Behavioral Biometrics

<!-- TOC -->

- [Three cornerstones of authentication](#three-cornerstones-of-authentication)
- [Biometrics (Something you are)](#biometrics-something-you-are)
    - [Physiological Biometrics](#physiological-biometrics)
    - [Behavioral Biometrics](#behavioral-biometrics)
    - [Social Biometric (Social Behavioural Biometric)](#social-biometric-social-behavioural-biometric)
- [Behavioral Biometrics Categories](#behavioral-biometrics-categories)
- [Implementation factors](#implementation-factors)
- [Reference](#reference)

<!-- /TOC -->

> Something you are does not generally constitute a secret.
> 
> <div align="right">NIST SP 800-63-2: Electronic Authentication Guideline</div>

## Three cornerstones of authentication

* Something you know (for example, a password)
* Something you have (for example, an ID badge or a cryptographic key)
* Something you are (for example, a fingerprint or other biometric data)

## Biometrics (Something you are)

* No biometric is "optimal" although a number of them are "admissible"
* Hard to (Not unable)
    * Steal/Transfer
    * Imitate/Duplicate

### Physiological Biometrics

* Facial features
* Fingerprints
* Voiceprints
* Hand geometry
* Iris patterns
* DNA
* Most data sampling processes require need invasive equipment
* Potential resistance from cultural, societal, and religious

### Behavioral Biometrics

* Something you do
* Model user behavior(Input, GUI changes)
* Applications
    * User authentication
    * Intrusion detection
* Advantages
    * Very low impact on usability
* Most useful in multi-modal systems
    * Complement to more robust methods
    * Highly sensitive to means of implementation
        * Example: Keyboard hardware

### Social Biometric (Social Behavioural Biometric)

* A deeply interconnected society
* Identify a person or avatar by social behavior in a certain social environment
* Social networks properties dictate communication patters in the networks of users
* Social behavioural feature
    * Virtual world avatar preferences
    * Nature of interaction (tweets, blogs, chats)
    * Content of interaction (topics, likes, opinions, emoticons, wording/writing style)
    * Online game playing strategies
    * Communication patters
* Three open questions
    * Are there some features extracted from social behavioural information that are permanent and unique enough can be used for individual authentication? 
    * What benefits the combination of social behavioural biometrics with traditional biometrics (physiological/behavioural/soft) can provide? 
    * Is it possible to use social behavioural activities for risk assessment and security threat prevention?

## Behavioral Biometrics Categories

* Authorship
    * Text or drawing made by user
        * Vocabulary, punctuation, brush strokes
* HCI-based biometrics
    * Input interaction: keystrokes, mouse, haptics
    * Software interaction: strategy, knowledge, skill
* Indirect HCI-based biometrics
    * Low-level system activities
        * System call traces, audit logs, program execution traces, registry access, storage activity, call-stack data analysis
* Kinetics: Motor-skills based biometrics
    * Rely on proper functioning of brain, skeleton, joints, nervous system
* Purely behavioral biometrics
    * Walking style, typing style, gripping style

## Implementation factors

* Required equipment
    * None
    * Multiple cameras
    * EEG sensors
* Enrollment time
    * Training time for system to recognize the user
* Persistence
    * Time it takes for features to change
* Obtrusiveness
* Error rates
    * False rejection rate (FRR)
    * False acceptance rate (FAR)
    * Equal error rate (ERR): error rate when FRR=FAR

## Reference

* NIST SP 800-63-2: Electronic Authentication Guideline
* Biometrics: A Tool for Information Security
* Behavioural biometrics: a survey and classification
* Emerging Trends in Security System Design Using the Concept of Social Behavioural Biometrics
* CS 259D Lecture 4
