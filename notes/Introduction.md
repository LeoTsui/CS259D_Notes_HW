# Introduction

<!-- TOC -->

- [Information Security Goals](#information-security-goals)
- [Attack](#attack)
    - [Attackers and Motivations](#attackers-and-motivations)
    - [Vulnerabilities](#vulnerabilities)
    - [Attack Categories](#attack-categories)
    - [Basic Attack Steps](#basic-attack-steps)
    - [Attack Tools](#attack-tools)
    - [Advance Persistent Threats: APT](#advance-persistent-threats-apt)
- [Defense](#defense)
    - [Detective Security](#detective-security)
    - [Risk Management: Controls](#risk-management-controls)
    - [Preventive Measures](#preventive-measures)
    - [Defense in Depth](#defense-in-depth)
    - [Reactive Defense](#reactive-defense)
- [Data Mining in Security](#data-mining-in-security)
    - [Why Big Data](#why-big-data)
    - [Explosion of Malware](#explosion-of-malware)
    - [Detection Taxonomy](#detection-taxonomy)
        - [Information source](#information-source)
        - [Analysis strategy](#analysis-strategy)
        - [Time aspects](#time-aspects)
        - [Activeness](#activeness)
        - [Continuality](#continuality)
- [References](#references)

<!-- /TOC -->

> There are only two types of companies: those that have been hacked, and those that will be. Even that is merging into one category: those that have been hacked and will be again.
> 
> <div align="right">Robert Mueller FBI Director</div>

## Information Security Goals

* C-I-A triad
    * Confidentiality
        * Unauthorized disclosure of information
    * Integrity
        * Unauthorized modification of information
    * Availability
        * Unauthorized withholding of information or resources
* Others
    * Privacy
    * Authenticity
    * Non-repudiation
    * Accountability
    * Auditability

## Attack

### Attackers and Motivations

* Script-kiddies
    * Motivated by curiosity
* Cybercriminals
    * Motivated by profit
    * Typical demographics: east European, Brazilian
* Nation-state hackers
    * Motivated by power
    * Typical demographics: east Asian, middle eastern
* Hacktivists
    * Motivated by ideology
    * Typical demographics: north American, western European
* Cyber-mercenaries
    * Hired by to attack
* Insiders
    * Motivated by disgruntlement

### Vulnerabilities

* Backdoors
    * Kleptographic attack
    * Rootkit
* Denial of Service
    * Resource exhaustion
    * Attack amplifiers (e.g., poorly designed FTP, DNS)
    * Application or OS exploit
* Eavesdropping
    * Listening to private communication on network
    * Monitoring hardware electro-magnetic transmissions
* Exploits
    * Gain control of a computer system, allow privilege escalation, or denial of service attack
    * Used in Trojan horses, viruses
* Social Engineering
    * Humans: the weakest link in security

### Attack Categories

* Probe
    * Information gathering (1:1, 1:m, m:1, m:n modes)
    * IPSweep, portsweep, nmap, etc.
* Denial of Service (DoS)
    * TCP SYN flood, Ping of Death, smurf, neptune, etc.
* Remote to Local attacks (R2L)
    * Brute force/Dictionary attack, buffer overflow, unverified input attacks
    * Social engineering, Trojans
* User to Root attacks (U2R)
    * Buffer overflow, rootkit, etc.
* Infections
    * Trojans/worms/viruses
    * Spreading attacks

### Basic Attack Steps

* Prepare
    * Gather info: Valid IP addresses & ports, OS, software type & version
* Exploit
* Leave behind
    * Backdoors
* Clean up
    * Restart crashed daemons, clean registry/log files
* Variable order and duration
    * Attacker's skill level
    * Type of vulnerability to exploit
    * Prior knowledge
    * Starting location of attacker

### Attack Tools

* Information gathering
    * Sniffing: capture packets traversing network
        * Tcpdump, Ethereal, Gulp, Net2pcap, Dsniff, etc.
    * Network mapping/scanning/fingerprinting: hosts/IPs/ports, protocol details
        * Nmap, Amap, Vmap, Ttlscan, P0f, Xprobe, Queso, etc.
* Attack launching
    * Trojans
        * Danger, NukeNabbler, AIMSpy, NetSpy, etc.
    * DoS attacks
        * Targa, Burbonic, HOIC, LOIC, etc.
    * Packet forging tools
        * Packeth, Packit, Packet Excalibur, Nemesis, Tcpinject, Libnet, SendIP, etc.
    * Application layer tools
        * Code Red Worm, Nimda Worm, AppDDoS, RefRef, etc.
    * User attack tools
        * Ntfsdos, Yaga, etc.

### Advance Persistent Threats: APT

* Targeted attack against a high-value asset
* Low and slow
* Avoid alerts
    * Use stolen user credentials
    * Zero-day exploits
    * Low profile in network
    * Slow progress: Operating over months or years
    * Beyond limited correlation time windows of today's IDSs
* Multi-stage
    * Exploitation
    * Command and control
    * Lateral movement
    * Breach
* Typical Goals
    * Steal intellectual property (IP)
    * Gain access to sensitive customer data
    * Access strategic business information
        * Financial gain, embarrassment, blackmail, data poisoning, illegal insider trading, disrupting organization's business
* Attackers
    * Well-funded
    * Highly skilled
    * Motivated
    * Targeted on specific data from specific organization

## Defense

### Detective Security

* 1st Generation: Intrusion detection systems (IDS)
    * 100% protection/prevention impossible
    * Layered security
* 2nd Generation: Security information and event management (SIEM)
    * Correlate alerts from different intrusion detection sensors
    * Present actionable information to security analyst
* 3rd Generation: Big Data analytics for security
    * Contextual security intelligence
    * Long-term correlations

### Risk Management: Controls

* Administrative
    * Policies, guidelines
        * Password policies
        * Payment Card Industry Data Security Standard (PCIDSS)
        * Principle of least privilege
* Physical
    * Doors, locks, etc.
    * Principle of separation of duties
* Logical
    * Use software and data

### Preventive Measures

* Protocols
    * Secure Socket Layer (SSL): source authentication
* Host-based protections
    * Secure operating systems, Patching
* Access control
    * Identification: username
    * Authentication: Something you know/have/are
    * Authorization: File permissions, Kerberos, Need-to-know principle
* Firewalls
    * Control inter-network traffic (e.g., from/to internet)
* Security by design
    * Principle of least privilege, Code reviews, Unit testing, Defense in depth
* Secure coding
    * Buffer overflows, Format string vulnerabilities, Code/Command injection

### Defense in Depth

* Layered approach
    * Separate systems into network sections
    * Place firewalls at section boundaries
    * Border router between ISP and firewall to filter traffic
    * Switches on each section to make sniffing less effective
    * Encryption
* Last layer of defense
    * Detection

### Reactive Defense

* Examples
    * Antivirus signatures for known malicious executables
    * Email filters for unwanted messages
    * Web filters for compromised websites
    * Sandboxes for malicious behaviors
* Median detection time between intrusion/breach to awareness of it: 300-400+ days
* Duration of zero-day attacks
    * 19 days to 30 months
    * Median of 8 months, Average of 10 months
* 61% of attacks discovered by a third party
* Businesses reluctant to disclose their breaches
    * Only 2%-30% do
* Porous perimeter
    * Cloud applications
    * Mobile/BYOD
    * Partner businesses

## Data Mining in Security

### Why Big Data

* Attack landscape
    * Attacks increasingly more sophisticated
    * Attacking constantly getting easier
        * Required attacker knowledge going down
        * Quality of attack tools increasing
    * Highly motivated attackers
        * Attacker needs to succeed only once, defense needs to be right every single time
* Attack mechanisms constantly evolving/mutating, current detection techniques failing
    * Polymorphic malwares
    * Zero-day attacks
    * APTs
* Network perimeter dissolving
    * Mobile/BYOD
    * Cloud
* Big Data technology enable storage and analysis of higher volumes & more types of data
* 2010 Verizon data breach investigation
    * In 86% of cases of breach, evidence was in the logs
    * Detection mechanisms failed to raise alerts
* How do we make sense of the data?

### Explosion of Malware

* 403 million new variants of malware created in 2011
* 100,000 unique malware samples collected daily by McAfee in 2012, Q1
* More than 100 million samples in McAfee's malware signature database by 2012 Q3
* Practically impossible to keep up with signatures

### Detection Taxonomy

#### Information source

* Host-based
    * system calls, system logs
* Network-based
* Wireless Network
* Application logs
    * DB logs, web logs
* IDS sensor alerts
    * Lower level sensor alarms

#### Analysis strategy

* Misuse detection
    * Premise
        * Knowledge of attack patterns provided by human experts
        * Signature matching
        * Data mining using labeled data sets
    * Benefit
        * High accuracy in detecting known attacks
    * Drawbacks
        * Ineffective against novel attacks
        * Signatures need updates with each new discovered attack
* Anomaly detection
    * Premise
        * Build profiles of normal behavior (users, hosts, networks)
        * Detect deviations from normal profiles
    * Benefit
        * Detect novel attacks
    * Drawback
        * Possible high false alarm rate

#### Time aspects

* Real-time
    * Analyze live data (e.g., session data)
    * Raise alert immediately if attack detected
* Offline
    * Analyze data offline
    * Useful for forensics

#### Activeness

* Passive reaction
    * Only generate alarms
    * Benefit: Human in the loop
    * Drawback: Alert may go unnoticed
        * Example: Target breach
* Active response
    * Corrective response (e.g., reconfigure firewalls)
    * Proactive (e.g., log out attacker)
    * Benefit: Speed
    * Drawback: May turn into DoS attack against

#### Continuality

* Continuous monitoring
    * Continuous real-time analysis
    * Collect information about actions immediately
    * Higher deployment effort
* Periodic analysis
    * Take periodic snapshots of the environment
    * Lower security: exploiting the window of opportunity between two snapshots

## References

* CS 259D Lecture 1
