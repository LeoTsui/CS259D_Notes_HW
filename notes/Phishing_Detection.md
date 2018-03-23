# Phishing Detection

<!-- TOC -->

- [Phishing](#phishing)
- [Anti-Phishing Overview](#anti-phishing-overview)
    - [Life Cycle of Phishing Campaigns](#life-cycle-of-phishing-campaigns)
    - [Challenge](#challenge)
- [Detection](#detection)
    - [Detection Features](#detection-features)
        - [DNS](#dns)
        - [URL](#url)
        - [HTML](#html)
        - [Text semantics](#text-semantics)
        - [Visual appearance](#visual-appearance)
        - [Simulate User Interaction](#simulate-user-interaction)
    - [Detection Approaches](#detection-approaches)
        - [User Education](#user-education)
        - [Blacklist](#blacklist)
        - [Heuristic](#heuristic)
        - [Visual Similarity](#visual-similarity)
        - [Machine Learning](#machine-learning)
- [Mitigation](#mitigation)
    - [Offensive Defense Approaches](#offensive-defense-approaches)
    - [Correction Approaches](#correction-approaches)
    - [Prevention Approaches](#prevention-approaches)
- [Evaluation Metrics](#evaluation-metrics)
- [References](#references)

<!-- /TOC -->

## Phishing

Phishing is a type of computer attack that communicates socially engineered messages to humans via electronic communication channels in order to persuade them to perform certain actions for the attacker's benefit.

* First Phishing: 1995, AOL
* Phishing Motives
    * Financial gain
    * Identity hiding
    * Fame and notoriety

## Anti-Phishing Overview

### Life Cycle of Phishing Campaigns

![The life-cycle of phishing campaigns](images/life-cycle_of_phishing_campaigns.png)

### Challenge

* Resist anti-phishing education
* Ignore passive warning
* Sematic attack
    * Impossible to accurately understand natural languages
    * PhishNet-NLP(R Verma, 2012), TP: 97%, TN: 99.2%

## Detection

### Detection Features

#### DNS

* DNS-poisoning
    * Round-Trip Time (RTT)
    * Hop
* Aggregate intrusion detection information
    * Fast-flux
    * DNS TTL

#### URL

* IP-based URL
* Number of sub-domains (> 5)
* Domain/URL semantics
    * Similar altered domain name
    * [Unicode Domains](https://www.xudongz.com/blog/2017/idn-phishing/)
        * Example: `apple.com`, `аррӏе.com`

#### HTML

* Non-matching link, URL text different from `href`
* Use `iframe` tags to present phoshing login forms on legitimate websites
* The extent of linking objects (eg. images) from victim sites

#### Text semantics

* Key words
    * High TF-IDF terms
    * Check key words by Google
* Common words appeared in phishing email/website
    * Single word
        * Example: account, update, confirm, verify, secure, log, click, etc.
    * Appear in pairs/clusters
        * Example: click-account, market-plan-prices
* Common topic
    * Account compromised
    * Account modified
    * Verify account
    * (Financial) Opportunity
    * Chick the link to gain benefit
    * Ambiguous tittle
        * "Dear Valued Customer:"
* Similar company/logo name
    * Slightly alter
        * Add
        * Omit
        * Transposing letters

#### Visual appearance

* Visually similar web page, but from the un-trusted URL
* Phishing websites aim at simulating the target websites
* Attackers use `img` tag instead of HTML
    * Looks like the same website
    * Evade detector

#### Simulate User Interaction

* Response from simulating a random user login
* Response from parent/children url

### Detection Approaches

* Different Sides/levels
    * Human and Software
    * Client(eg. browser plugin) and (E-mail) Server
    * Network(eg. IP, DNS) and Application

#### User Education

* Educate users about phishing attacking, not only potential damage
* Utilize knowledge to
    * Detect Phishing
    * Regulate behavior
* Gamification
    * [Anti-Phishing Phil](http://www.ucl.ac.uk/cert/antiphishing/)(S Sheng, 2007)
    * People prefer gaming to reading
* Cannot differentiate between phishing and legitimate sites, even be educated
* Warning should be
    * Active warnings not passive
    * Immediately
    * Independent of external sources
    * Explain "Why" and "What should do"
    * Easy to read

#### Blacklist

* Low FP
* Require low system resources
* Fall on zero-hour phishing

#### Heuristic

* High FP than Blacklist
* Hard to manually maintain heuristic detector

#### Visual Similarity

* High FP than Blacklist
* Render Web page
    * Parse HTML, CSS, etc.
    * Run JavaScript, Flash, etc.
* Require more computing and memory recourses

#### Machine Learning

* Build new model from big data
* Performance better on Zero-hour phishing

## Mitigation

* **Mitigation bases on accurate detection**

### Offensive Defense Approaches

* Flood phishing website
* Difficult to measure performance

### Correction Approaches

* Take phishing resources down
    * Remove phishing content
    * Shutdown services/bot hosts
    * Close accounts

### Prevention Approaches

* Prevent attackers from starting phishing
    * Law suit
    * Penalty

## Evaluation Metrics

* Common statistical errors

## References

* Phishing Detection: A Literature Survey
* [PHISHING DETECTION](https://www.slideshare.net/ummeayesha/phishing-detection)
* A Survey of Phishing Email Filtering Techniques
* [CSCD 303 Essential Computer Security](http://penguin.ewu.edu/cscd303/), [Phishing.pdf](http://penguin.ewu.edu/cscd303/CourseNotes/CSCD303-Lecture11a-Phishing-2017.pdf)
* [cylab-anti-phishing-Aug2007.ppt](https://www.cs.cmu.edu/~jasonh/presentations/cylab-anti-phishing-Aug2007.ppt)
* Detecting Phishing Emails the Natural Language Way
* [Phishing with Unicode Domains](https://www.xudongz.com/blog/2017/idn-phishing/)
