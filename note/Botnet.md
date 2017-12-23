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
- [Rallying Mechanisms](#rallying-mechanisms)
- [IP flux](#ip-flux)
- [Domain flux](#domain-flux)
    - [Domain wildcarding](#domain-wildcarding)
    - [Domain generation algorithms](#domain-generation-algorithms)
- [Blind Proxy Redirection](#blind-proxy-redirection)
- [Botnet Detection Challenges](#botnet-detection-challenges)
- [Reference](#reference)

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
    * infected websites, email attachments, removable media, etc.
* Secondary injection
    * Host downloads & runs binaries, becomes a bot
    * FTP, HTTP, or P2P
* Connection or Rally
    * process of establishing connection with C&C
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

## Rallying Mechanisms

* C&C location resolution
* Static Lists
    * Hard-coded list of IP addresses
    * Can be detected via a feed of botnet IPs
* Fluxing
    * Add resilience
    * Types
        * IP flux
        * Domain flux

## IP flux

* Constant changing of IP address information
* Single flux
    * Multiple (100s-1000s) IP addresses associated
with a domain name
    * IP addresses registered and de-registered rapidly
        * Round-robin allocation
        * Short Time to Live (TTL) for DNS A records
* Double flux
    * Flux IP address of fully-qualified domain name
    * Flux IP address of DNS server (NS records) used to look up IP address

## Domain flux

### Domain wildcarding

* Use wildcarding in DNS records
    * Example: *.domain.com
* Useful for spamming/phishing; wildcard information used to
    * Identify victim (e.g., rjhgbrwh.domain.com)
    * Track success

### Domain generation algorithms

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

## Botnet Detection Challenges

* Botnet traffic similar to normal traffic
    * Likely encrypted as well
* Botnets evolve rapidly
    * New bots constantly getting added
    * Changing protocols
    * Changing architectures
    * Changing infection models
    * Fast flux hosting

## Reference

* [Botnet Communication Topologies](https://www.damballa.com/downloads/r_pubs/WP_Botnet_Communications_Primer.pdf)
* CS 259D Lecture 2
