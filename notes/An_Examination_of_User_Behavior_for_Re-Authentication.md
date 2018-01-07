# An Examination of User Behavior for Re-Authentication

<!-- TOC -->

- [Background Knowledge and Insight](#background-knowledge-and-insight)
    - [Re-authentication](#re-authentication)
    - [Behavioral Biometrics (Re-)authentication](#behavioral-biometrics-re-authentication)
- [Objective of User Re–authentication System](#objective-of-user-reauthentication-system)
- [Multimodal Data Analysis](#multimodal-data-analysis)
- [Sample Collection](#sample-collection)
    - [Data Set I](#data-set-i)
    - [Data Set II](#data-set-ii)
    - [Data Set III](#data-set-iii)
- [Data Processing and Features Extract](#data-processing-and-features-extract)
    - [Mouse](#mouse)
        - [Mouse Data](#mouse-data)
        - [Mouse Feature Hierarchy](#mouse-feature-hierarchy)
        - [Mouse Features](#mouse-features)
    - [Keystroke](#keystroke)
        - [Keystroke Data](#keystroke-data)
        - [Keystroke Feature Hierarchy](#keystroke-feature-hierarchy)
        - [Keystroke Features](#keystroke-features)
    - [GUI](#gui)
        - [GUI Data](#gui-data)
        - [GUI Feature Hierarchy](#gui-feature-hierarchy)
        - [GUI Features](#gui-features)
    - [Summary of Feature Space](#summary-of-feature-space)
- [Implementation schemes](#implementation-schemes)
- [Experimental](#experimental)
- [Reference](#reference)

<!-- /TOC -->

> Most of the incidents (83%) were executed physically from within the insider's organization and took place during normal business hours.
> 
> The impact of nearly all insider incidents in the banking and finance sector was a financial loss for the victim organization: in 30% of the cases the financial loss exceeded $500,000. Many victim organizations incurred harm to multiple aspects of the organization.
> 
> <div align="right">US Secret Service National Threat Assessment Center (NTAC), Insider threat study (2004)</div>

## Background Knowledge and Insight

### Re-authentication

* Continuous authentication of a user for the duration of the user's login session
* Current user same as user who authenticated
* Stolen credentials
* Approaches
    * Indirect: profiling OS and applications
        * System call invocations, call-stack data operation, program trace analysis
    * Direct: profiling valid user
        * Command line input data, keystroke dynamics, mouse activity, GUI events
* Process
    * Collect clean data from each user
    * Build profile of normal behavior for each user
    * Use profile to compare behavior of current user with that of a valid user
    * Any significant behavioral difference flagged

### Behavioral Biometrics (Re-)authentication

* Attackers evade classical IDS
* Deployment scenarios
    * Open setting
        * Public library, internet cafe
        * Unsupervised learning
        * Only data from valid user available for profiling
    * Closed setting
        * Corporate office, government building
        * Possible to collect data from all users
        * Supervised learning

## Objective of User Re–authentication System

* Computer Security Objective
    * To design and implement an on–line, scalable user re–authentication system founded on the data collected from user's inputs (mouse and keyboard) and Graphical User Interface (GUI) events for the purpose of detecting an attacker.
* Machine Learning Objective
    * To design an accurate, classification system for detecting outliers (e.g., intruders) in high dimensional temporal sequence data when the amount of data per user is limited
* Goal
    1. Detect insiders pretending to be other insiders;
    1. Detect outsiders pretending to be insiders;
    1. Discriminate users in a pair–wise sense;
    1. Determine the sensitivity of user profiles on different hardware configurations;
    1. Discriminate users when they are behaving in an identical manner;
    1. Determine the degree of system's scalability and computational efficiency;
    1. Determine the strength of each data source (e.g., the mouse, keystrokes and GUI) individually and in combination;
    1. Exploit granularity of the data to obtain a comprehensive feature space;
    1. Reduce the candidate feature space to a subset of most predictive features;
    1. Improve the accuracy measure when the amount of data per user dataset is limited.

## Multimodal Data Analysis

* More than one data source
* Combine sources at
    * Data level
        * Can miss on characteristics
    * Feature level
        * Classifier using all features put together
    * Classifier level
        * Separate classifier per data source
        * Voting scheme for final decision

## Sample Collection

### Data Set I

* 61 volunteers
    * Task 1:
        * Reading assignment
        * 20 questions about assignment
    * Task 2:
        * Set of web pages
        * Another set of questions
    * Average 4 hours of data collection
        * Average 92K data points, 4.5MB per user

### Data Set II

* One user, five different computer and I/O configurations
* Same tasks as Data set I

### Data Set III

* 73 volunteers executing the same task
* Compared with Data set I
    * No pause time
    * Smaller in size and more dense with the I/O events

## Data Processing and Features Extract

* Directly profile valid users
* Keystrokes
* Mouse movements
* GUI events
* Data point (format)
    * Event ID (assigned by OS)
    * X screen coordinates
    * Y screen coordinates
    * System time
    * Application
        * Not be used as Feature

### Mouse

#### Mouse Data

* All Windows mouse events

#### Mouse Feature Hierarchy

* Mouse
    * NC Moves
    * Mouse Events
        * Clicks
            * Single
            * Double
        * Wheel
    * Mouse Moves
*  Client area: area of application window below the menu and toolbars
*  Rate of client area mouse movements
    * Several hundred movements per second
    * Too large, did not collect all movements
    * Recorded every 100ms if & only if cursor position changed
*  Single & double clicks
    * Most infrequent events
    * Higher granularity not helpful
    * Not record press duration

#### Mouse Features

* Mouse event features
    * Over a window of W data points
        * \# of events in each mouse category & subcategory
            * Other features extracted from two subsequent events or two events separated by K data points (events of same category or subcategory)
                * K a parameter for each user and type of event
    * Features: Mean, SD, skewness (3 rd moment) of
        * Distance
        * Speed = distance(P,Q)/time(P,Q)
        * Angle of orientation
        * X coordinate
        * Y coordinate
        * N-graph duration (N between 1-8)
            * Elapsed time between first & Nth data point
    * Total of 200 features
* Mouse movements features
    * NC moves features
        * Similar to event features
        * Distance, speed, angle, etc. computed
            * Between two subsequent NC moves
            * Two NC moves separated by K data points
        * Total of 40 features
    * Client area moves
        * Similar to NC mouse movement features
        * Total of 40 features

### Keystroke

#### Keystroke Data

* Two types in Windows OS
    * WM_KEYDOWN
    * WM_KEYUP
    * Event ID uniquely identifying the key

#### Keystroke Feature Hierarchy

* Keystroke
    * Function
        * Example: F1-F12
    * Control
        * Example: Control, Alt, Delete
    * Regular
        * Letters
        * Numbers
    * Mouse-key
        * Example: Page Up/Down, Tab, arrow keys
    * Other
        * Example: punctuation keys, Pause/Break, PrtSc/SysRq

#### Keystroke Features

*  Over a window of W data points
    * \# of events in each category & subcategory
    * \# of occurrences of each letter & each numeral
        * 26 alphabet features, 10 numeric features
    * Mean, stdv, skewness
        * N-graph duration between consecutive keystrokes (N between 1-8)
    * Total of 236 features

### GUI

#### GUI Data

* Data induced by 138 GUI events
* Grouped into a hierarchy based on function

#### GUI Feature Hierarchy

* GUI
    * Spatial
        * Window
            * Scroll bar, minimize, maximize, restore, move, etc.
        * Control
            * Application & process control, open/close, etc.
        * Menu
            * Open, select, navigate, close, etc.
        * Item
            * List, button, etc.
    * Temporal
        * Icon
        * Dialog
        * Query
        * Combo box
            * Open/close, select, move, resize, etc.
        * Miscellaneous
            * Power up/down, language change, background color change, etc.

#### GUI Features

* Spatial features
    * Over a window of W data points
        * \# of events in each spatial category
        * Subsequent spatial events or spatial events separated by K data points
            * Mean, stdv, skewness
            * Distance
            * Speed
            * Angle of orientation
            * X coordinate
            * Y coordinate
            * N-graph duration (N between 1-8)
        * Total of 200 features
* Temporal features
    * Over a window of W data points
        * \# of events in each temporal category
        * Subsequent temporal events or temporal events separated by K data points
            * Mean, stdv, skewness
            * N-graph duration (N between 1-8)
        * Total of 240 features

### Summary of Feature Space

* Window size W: for each user
    * Tested: 100, 300, 500, 1000
    * Chosen: 500
* Frequency K: for each user & subcategory
    * Tested: 1, 5, 10, 15, 20
    * Chosen: 8 for frequent events, 1 otherwise
        * Frequent: induced > 10 times per second
        * Frequent events
            * All mouse events
            * Mouse movements
            * Mouse wheel movements
            * NC mouse movements
            * All GUI events
            * Spatial+Temporal
            * Temporal
            * Window
            * Dialog
* Candidate feature space: 956 dimensions
* Hierarchical groupings improve performance
    * Removing features from lower levels of mouse hierarchy lowered classifier performance

## Implementation schemes

* Two schemes
    * Classify one feature vector instance at a time
        * C4.5
        * If the instance matched normal profile, serve request
        * Else, alert system admin, ask re-auth, or close session
        * May cause high false alarm rates
    * Smoothing
        * Look at a window of n (n between 1-11) feature vector instances
        * If m (m between 1,n) of those matched profile, serve request
        * Overlapping windows
        * W-s old points, s new points
        * s = 50, equivalent to 5 second intervals
        * Reduces time-to-alarm
* False bell rate
    * Bell, a sequence of contiguous alarms without the interrupting "normal" window
    * False bell rate = FB / (\# positive instances)
* Evaluation
    * 10-fold cross validation

## Experimental

* Pairwise Discrimination
    * Discriminate normalcy
* Anomaly Detection
    * Detect an insider pretending to be another insider
* Unseen User Detection
    * Detect an outsider pretending to be an insider
* Tracking a Valid User
    * Identify the same valid user on different hardware

## Reference

* An examination of user behavior for re- authentication (M. Pusara's PhD thesis, 2007)
* Toward Reliable User Authentication through Biometrics
* CS 259D Lecture 4
