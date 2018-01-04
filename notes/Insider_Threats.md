# Insider Threats

<!-- TOC -->

- [Examples](#examples)
- [Two Types of Insider Attackers](#two-types-of-insider-attackers)
- [Insight](#insight)
- [Insider Attacks](#insider-attacks)
    - [Forms of Attack](#forms-of-attack)
    - [Characteristics of Insider Attacks](#characteristics-of-insider-attacks)
- [Detection Approach](#detection-approach)
- [Reference](#reference)

<!-- /TOC -->

> Despite some variation from year to year, inside jobs occur about as often as outside jobs. The lesson here, though, surely is as simple as this: organizations have to anticipate attacks from all quarters.
> 
> <div align="right">CSI/FBI COMPUTER CRIME AND SECURITY SURVEY 2005</div>

## Examples

* Vodafone Greece
    * Targeted 100+ high-ranking officials
        * Prime minister of Greece & his wife
        * Ministers: national defense, foreign affairs, justice
        * Greek European Union commissioner
        * Mayor of Athens
    * Started before Aug'04, continued till March'05
    * Detected accidentally due to rootkit update misconfig
    * Traced to an insider in Vodafone
    * Vodafone fined $76M
* Edward Snowden

## Two Types of Insider Attackers

* Traitors
    * A legitimate user with proper access credentials do evil
    * Full knowledge of systems & security policies
* Masqueraders
    * An attacker who has stolen/obtained and uses credentials of a legitimate user

## Insight

* Behavior performances can be different from normal users and attackers
* Behavior is not something that can be easily stolen
* When traitors do evil, performances deviate from normal behavior
    * Even attackers simulate normal users, they will be exposed when they start attacks

## Insider Attacks

### Forms of Attack

* Unauthorized extraction, duplication, or exfiltration of data
* Tampering with data (unauthorized changes of data or records)
* Destruction and deletion of critical assets
* Downloading from unauthorized sources or use of pirated software which might contain backdoors or malicious code
* Eavesdropping and packet sniffing
* Spoofing and impersonating other users
* Social engineering attacks
* Misuse of resources for non-business related or unauthorized activities
* Purposefully installing malicious software

### Characteristics of Insider Attacks

* Most incidents required little technical sophistication
* Actions were planned
* Motivation was financial gain
* Acts were committed while on the job
* Incidents were usually detected by non-security personnel
* Incidents were usually detected through manual procedures

## Detection Approach

* Shell command sequences (CLI)
* System calls
* Database/file accesses
* OS logs
* Web request
* Keystroke/Mouse dynamics
* Honeypots

|                                                 | Masquerader                                                                   | Internal Traitor                                                          |
| ----------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Two-Class Classifiers: Unix  Command  Sequences | High - Unfamiliar with local environment and user behavior                    | Medium - Can possibly mimic another normal user or train the classifier   |
| One-Class: Unix  Command  sequences             | High - Unfamiliar with local environment and user behavior                    | Medium - Can possibly mimic another normal user or train the classifier   |
| Unix Audit Events                               | Medium - Given proper credentials and might not trigger alerts                | Low - Application level malicious acts may not manifest as unusual events |
| Unix System Calls                               | Medium - Might not violate system call profile                                | Low - Application level malicious acts may not manifest as unusual events |
| Window Usage Events                             | Medium - Given proper credentials and might not trigger alerts                | Low - Application level malicious acts may not manifest as unusual events |
| Windows Registry access                         | Medium - unless malicious programs access Registry                            | Medium - unless malicious programs access Registry                        |
| Network Activity Audit                          | Medium - If attack uses network and attribution is possible                   | High - If attack uses network  and attribution is possible                |
| Honeypots and Decoy Technologies                | High - Unfamiliar with local information and likely to interact with honeypot | Medium - Unlikely to interact if aware of the location of honeypots       |

## Reference

* [The Athens Affair](http://spectrum.ieee.org/telecom/security/the-athens-affair)
* Insider Attack and Cyber Security: Beyond the Hacker, chapter "A Survey of Insider Attack Detection Research"
* CS 259D Lecture 3
