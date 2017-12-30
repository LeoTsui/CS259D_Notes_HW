# CS 259D Data Mining for Cyber Security Notes Introduction

**The notes are the supplement to papers and handouts of [CS 259D](https://web.stanford.edu/class/cs259d)**

Github: [CS259D_Notes_HW](https://github.com/LeoTsui/CS259D_Notes_HW)

GitBook: [CS259D Notes](https://leotsui.gitbooks.io/cs259d-notes/)

---

<!-- TOC -->

- [Lectures](#lectures)
    - [Introduction](#introduction)
    - [Botnets](#botnets)
    - [Insider Threats](#insider-threats)
    - [Behavioral Biometrics](#behavioral-biometrics)
    - [Web Security](#web-security)
    - [Phishing Detection](#phishing-detection)
    - [Automatic Alert Correlation](#automatic-alert-correlation)
    - [Multi-Classifier Systems, Intrusion Detection Systems (IDSs)](#multi-classifier-systems-intrusion-detection-systems-idss)
    - [Deep Packet Inspection](#deep-packet-inspection)
    - [Polymorphism](#polymorphism)
    - [Machine Learning for Security](#machine-learning-for-security)
    - [Adversarial Machine-Learning](#adversarial-machine-learning)
    - [Security at Industry](#security-at-industry)
- [Homework](#homework)
    - [Homework1](#homework1)
    - [Homework2](#homework2)
    - [Homework3](#homework3)
    - [Homework4](#homework4)

<!-- /TOC -->

## Lectures

### Introduction

* Overview of information security, current security landscape, the case for security data mining

### Botnets

* Botnet topologies, botnet detection using NetFlow analysis
    * Lecture 2
    * BotMiner: Clustering Analysis of Network Traffic for Protocol- and Structure- Independent Botnet Detection
    * BotFinder: Finding Bots in Network Traffic Without Deep Packet Inspection
* Botnet detection using DNS analysis
    * Lecture 3
    * EXPOSURE: Finding Malicious Domains Using Passive DNS Analysis (2011)

### Insider Threats

* Introduction to insider threats, masquerader detection strategies
    * Lecture 3
    * One-class Training for Masquerade Detection (2003)

### Behavioral Biometrics

* Active authentication using behavioral and cognitive biometrics
    * Lecture 4
    * An examination of user behavior for re-authentication (M. Pusara’s PhD thesis,2007)
* Mouse dynamics analysis for active authentication
    * Lecture 5
    * Continuous authentication for mouse dynamics: A pattern-growth approach (Shen C, Cai Z, Guan X. 2012)
    * Lecture 7
    * An Efficient User Verification System via Mouse Movements, 2011
* Touch and swipe pattern analysis for mobile active authentication
    * Lecture 7
    * Touchalytics: On the Applicability of Touchscreen Input as a Behavioral Biometric for Continuous Authentication, 2013

### Web Security

* Web threat detection via web server log analysis
    * Lecture 8
    * A multi-model approach to the detection of web-based attacks, 2005
* Alert aggregation for web security
    * Lecture 12
    * Using Generalization and Characterization Techniques in the Anomaly-based Detection of Web Attacks, Robertson et al., 2006

### Phishing Detection

* Phishing email detection, phishing website detection
    * Lecture 16
    * Learning to Detect Phishing Emails, Fette et al, 2007
    * Cantina: A content-based approach to detecting phishing websites, Zhang et al, 2007

### Automatic Alert Correlation

* Building attack scenarios from individual alerts correlation
    * Lecture 20
    * A Comprehensive Approach to Intrusion Detection Alert Correlation, Valeur et al, 2004

### Multi-Classifier Systems, Intrusion Detection Systems (IDSs)

* Overview of multi-classifier systems (MCS), advantages of MCS in security analytics
    * Lecture 10
    * Adaptive Intrusion Detection System via Online Learning, 2012

### Deep Packet Inspection

* Packet payload modeling for network intrusion detection
    * Lecture 12
    * PAYL: Anomalous payload-based network intrusion detection, Wang-Stolfo 2004
* One-class multi-classifier systems, one-class MCS for packet payload modeling and network intrusion detection
    * Lecture 15
    * McPAD : A Multiple Classifier System for Accurate Payload-based Anomaly Detection, Perdisci et al, 2009

### Polymorphism

* Polymorphic blending attacks, infeasibility of modeling polymorphic attacks
    * Lecture 14
    * Polymorphic Blending Attacks, Fogla et al, 2006
    * On the Infeasibility of Modeling Polymorphic Shellcode, Song et al, 2007

### Machine Learning for Security

* Challenges in applying machine learning (ML) to security, guidelines for applying ML to security
    * Lecture 13
    * Outside the closed world: On using machine learning for network intrusion detection, Sommer-Paxson, 2010
    * Challenging the Anomaly Detection Paradigm: A Provocative Discussion, Gates-Taylor, 2007
    * The Base-Rate Fallacy and Its Implications for the Difficulty of Intrusion Detection, Axelsson, 1999

### Adversarial Machine-Learning

* Security of machine learning
    * Lecture 10
    * The security of machine learning, 2010

### Security at Industry

* Security at Wells Fargo
    * Lecture 6
    * Guest speaker Avi Avivi, VP Enterprise Information Security Architecture at Wells Fargo
* Security at Union Bank
    * Lecture 9
    * Guest speaker Gary Lorenz, Chief Information Security Officer (CISO) and Managing Director at MUFG Union Bank
* Security Data Mining at Google
    * Lecture 11
    * Guest speaker Massimiliano Poletto, head of Google Security Monitoring Tools group
* Industry Perspectives
    * Q&A with guest speaker Michael Fey, EVP and CTO of Intel Security Group (aka McAfee)

## Homework

### Homework1

* Question 1. Botnets
* Question 2. Anomaly Detection via "Eigenface" of Command History
* Question 3. Continuous Authentication via Biometric Behavior

### Homework2

* Question 1. Quizzes
* Question 2. Touch Biometrics
* Question 3. Merits of Entropy in Attack Detection/Diagnostics

### Homework3

* Analyse e-mail packets

### Homework4

* Quizzes
