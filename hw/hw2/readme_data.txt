This file explains the content of the file with raw touch data recorded for the touchalytics project.

The corresponding paper is
"Touchalytics: On the Applicability of Touchscreen Input as a Behavioral Biometric for Continuous Authentication" 
by
Mario Frank, Ralf Biedert, Eugene Ma, Ivan Martinovic, and Dawn Song

Please contact Mario Frank if questions come up.
Contact details and additional information can be found at http://www.mariofrank.net/touchalytics/index.html





The columns of the dataset are 
'phone ID',
'user ID', 
'document ID', 
'time[ms]', 
'action', 
'phone orientation', 
'x-coordinate', 
'y-coordinate', 
'pressure', 
'area covered', 
'finger orientation'.

Detailed descriptions below.




Phone ID:
indicates the phone and the experimenter that recorded the data
reaches from 1-5
1 : Nexus 1, Experimenter E
2 : Nexus S, Experimenter M
3 : Nexus 1, Experimenter R
4 : Samsung Galaxy S, Experimenter I
5 : Droid Incredible, Experimenter E

user ID:
anonymous users

doc id:
This number indicates the document that the user saw on screen while we collected the data. Every document represents a different session, i.e. the user has put down the device between working on different documents.
The breaks between doc ids 1-5 and 6-7 are several minutes, respectively. Data with doc ids 6 and 7 has been collected 7 to 14 days after doc ids 1-5
1: Wikipedia article 
2: Wikipedia article 
3: Wikipedia article 
4: Image comparison game
5: Image comparison game
6: Wikipedia article 
7: Image comparison game


time[ms]:
absolute time of recorded action (ms since 1970).

action:
can take three values 0: touch down, 1: touch up, 2: move finger on screen. In our paper, a stroke is defined as all actions between a 0 and a 1 if there is a xy-displacement between these actions. Clicks are actions between 0 and 1 without displacement.


'phone orientation', 'x-coordinate', 'y-coordinate', 'pressure', 'area covered', 'finger orientation'
are the values returned from the Android API at the current action.



