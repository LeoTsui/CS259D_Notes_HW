# Botnet

<!-- TOC -->

- [Introduction](#introduction)
- [Starting Point](#starting-point)
- [Botnet Components](#botnet-components)
- [Botnet Lifecycle](#botnet-lifecycle)
- [Botnet C&C Topologies](#botnet-cc-topologies)
    - [Star](#star)
    - [Multi-server](#multi-server)
    - [Hierarchical](#hierarchical)
    - [Random](#random)
- [Rally Mechanisms](#rally-mechanisms)
    - [Hard-coded IP](#hard-coded-ip)
    - [Dynamic DNS](#dynamic-dns)
    - [Distributed DNS](#distributed-dns)
    - [Fluxing](#fluxing)
        - [IP Flux (Fast-Flux)](#ip-flux-fast-flux)
        - [Domain Flux](#domain-flux)
- [Blind Proxy Redirection](#blind-proxy-redirection)
- [Communication Protocols](#communication-protocols)
    - [IRC Protocol](#irc-protocol)
    - [HTTP Protocol](#http-protocol)
- [Observable Behaviors](#observable-behaviors)
    - [Network-based](#network-based)
    - [Host-based](#host-based)
    - [Global Correlated](#global-correlated)
- [Evasion and Botnet Detection Challenges](#evasion-and-botnet-detection-challenges)
- [References](#references)

<!-- /TOC -->

## Introduction

* Networks of machines compromised by malware
* Estimated 16-25% of computers on Internet part of a botnet
    * Botnet Rustock has over 1 million bots
    * Botnet Storm one of "world's top super computers"
* Applications
    * Information and identity theft
    * Distributed denial of service (DDoS)
    * Software piracy
    * Spamming/Phishing
        * Almost 80% of all email traffic
        * Example: Grum, Cutwail, Rustock
    * Underground economy
        * 10,000 bots for $15
* Scale of damage (cf. International Telecommunication Union)
    * $13.2B direct damages to global economy in 2006
    * $67.2B in direct and indirect damages to US businesses in 2005
    * Global cost of spam in 2007: $100B global, $35B in US

## Starting Point

* Internet Relay Chat (IRC)
    * Text-based chat system
    * Organize communications in channels
    * Botnets to control interactions in IRC chat rooms
        * Interpret simple commands
        * Provide administration support
        * Offer simple games/services
        * Retrieve information: OS, logins, emails, etc.
    * First IRC bot: Eggdrop, 1993

## Botnet Components

* Zombies
    * High transmission rates
    * Low levels of security
    * Distant locations
    * Mostly MS Windows

## Botnet Lifecycle

* Initial infection
    * Infected websites, email attachments, removable media, etc.
* Secondary injection
    * Host downloads & runs binaries, becomes a bot
    * FTP, HTTP, or P2P
* Connection or Rally
    * Process of establishing connection with Command and Control (C&C)
    * Happens every time the host is restarted
* Malicious activities
    * More intense message exchange between bot and C&C
* Maintenance and upgrading

## Botnet C&C Topologies

### Star

* Centralized C&C communicate with all bots
* Protocols used:
    * IRC
        * C&C functionality of SDBot, GTBot, Agobot still in use
        * Source code published by author
    * HTTP
        * Blend in with normal user traffic
        * Do-it-yourself kits
    * Instant-Messaging (IM) protocols
        * ICQ, AIM, MSN Messenger
        * Needs creating one account per bot
* Pro:
    * Speed of Control
* Con:
    * Single point of failure

### Multi-server

* Extension of Star topology
* C&C servers communicate among themselves
* Pros:
    * No single point of failure
    * Geographical optimization
* Cons:
    * Requires more planning/ effort from the operator

### Hierarchical

* One group of bots acting as servants
    * Static routable IP addresses
    * Proxy C&C instructions to client bots
* Variant: Hierarchical Kademlia
    * Set of clusters or islands of bots
    * P2P for intra-cluster communication
    * Inter-cluster communication: super bot peers
* Pros:
    * Botnet awareness: Interception of botnet won't enumerate all members, unlikely to reveal C&C
    * Ease of resale
        * Lease/resale sections of botnet to other operators
* Cons:
    * Command latency: Not suitable for real-time activities

### Random

* No centralized C&C
    * Commands injected by botmaster via any bot by sharing/publishing command files
    * Commands signed as authoritative to avoid takeover
* Future: Skype-based botnets
    * Better blend in with other P2P traffic
* Pros:
    * Highly resilient
* Cons:
    * Command latency
    * Botnet enumeration

## Rally Mechanisms

* C&C location resolution

### Hard-coded IP

* Hard-coded list of IP addresses in binary files
* Can be detected via a feed of botnet IPs

### Dynamic DNS

* Hard-coded C&C domains assigned by dynamical DNS providers
* Easy to create new C&C server, When the old server fails or be shutdown
* Detection harder when botmaster randomly changes the location

### Distributed DNS

* Botnets run own DNS service out of the reach of law enforcement or other authorities
* Bots use the DNS addresses to resolve the C&C servers
* Use high port numbers to avoid detection by security devices and gateways

### Fluxing

* Add resilience

#### IP Flux (Fast-Flux)

* Constant changing of IP address information

* Single Flux
    * Multiple (100s-1000s) IP addresses associated with a domain name
    * IP addresses registered and de-registered rapidly
        * Round-robin allocation
        * Short Time to Live (TTL) for DNS A records
* Double Flux
    * Flux IP address of Fully-Qualified Domain Name (FQDN)
    * Flux IP address of DNS server (NS records) used to look up IP address for FQDN

#### Domain Flux

* Domain Wildcarding
    * Use wildcarding in DNS records
        * Example: `*.domain.com`
    * Useful for spamming/phishing
    * Wildcard information used to
        * Identify victim
            * A unique random domain
            * Example: `rjhgbrwh.domain.com`
        * Track success
        * Bypass anti-spam technologies
* Domain Generation Algorithms
    * Create a dynamic list of FQDN's every day
        * Cryptographic domain names
    * Generated FQDN's polled by bot to find C&C
    * Example: the worm Conficker.C
        * Generates 50,000 domain names every day
        * Attempts to contact 500
        * 1% chance of update every day if operator registers only 1 domain per day
        * Preventing update requires registering 50,000 new domains every day
    * Benefit
        * Domain names generated in volume, with short (typically 1-day) life span
        * Very difficult to investigate/block all possible domain names

## Blind Proxy Redirection

* Add an extra layer of resiliency
* Proxy IP/domain lookup and C&C traffic

## Communication Protocols

### IRC Protocol

* IRC mainly designed for one to many conversations but can also handle one to one
* Most corporate networks do not allow IRC traffic so any IRC requests can determine existing external or internal bot
    * Outbound IRC requests means an already infected computer on the network
    * Inbound IRC requests mean that a network computer is being recruited

### HTTP Protocol

* Due to prevalence of HTTP usage it is harder to track a botnet that uses HTTP Protocols
* Using HTTP can allow a botnet to skirt the firewall restrictions that hamper IRC botnets
* Detecting HTTP botnets is harder but not impossible since the header fields and the payload do not match normal HTTP traffic

## Observable Behaviors

### Network-based

* Network patterns can be used to detect Botnets
    * IRC & HTTP are the most common forms of Botnet communications
    * Detectable by identifying abnormal traffic patterns
* DNS domain names
    * DNS queries to locate C&C server
    * Hosts query improper domain names
    * IP address associated with a domain name keeps changing periodically
* Traffic
    * Bursty at times, and idle the rest of the time
    * Abnormally fast responses compared to a human
    * Attacks behaviors 

### Host-based

* Botnet behavior can be observed on the host machine
    * Exhibit virus like activities
    * When executed, Botnets run a sequence of routines
        * Modifying registries
        * Modifying system files
        * Creating unknown network connections 
        * Disabling Antivirus programs

### Global Correlated

* Global characteristics are tied to the fundamentals Botnets
    * Not likely to change unless Botnets are completely redesigned and re-implemented
    * Most valuable way to detect Botnets
* Behavior the same regardless if the Botnets are communicating via IRC or HTTP
    * Global DNS queries increase due to assignment of new C&C servers
    * Network Flow disruptions

## Evasion and Botnet Detection Challenges

* Botnet traffic similar to normal traffic
    * Likely encrypted as well
* Botnets evolve rapidly
    * New bots constantly getting added
    * Changing protocols
        * Moving away from IRC
        * Taking control of
            * HTTP
            * VoIP
            * IPV6
            * ICMP
            * Skype protocols
    * Changing architectures
    * Changing infection models
    * Fast flux hosting

## References

* [Botnet Communication Topologies](https://www.damballa.com/downloads/r_pubs/WP_Botnet_Communications_Primer.pdf)
* CS 259D Lecture 2
* [Taxonomy of Botnet Threats](http://www.cs.ucsb.edu/~kemm/courses/cs595G/TM06.pdf)
* [IS 511](https://syssec.kaist.ac.kr/~yongdaek/courses/is511/index.html): [20170412_botnet-lecture](https://syssec.kaist.ac.kr/~yongdaek/courses/is511/Slides_2017/20170412_botnet-lecture.pdf)
* [MSIT 458](http://www.cs.northwestern.edu/~ychen/classes/msit458-f12/): [botnet](www.cs.northwestern.edu/~ychen/classes/msit458-f12/botnet.ppt)
