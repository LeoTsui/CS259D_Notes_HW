This file explains the content of the file touch features recorded for the touchalytics project.

The corresponding paper is
"Touchalytics: On the Applicability of Touchscreen Input as a Behavioral Biometric for Continuous Authentication" 
by
Mario Frank, Ralf Biedert, Eugene Ma, Ivan Martinovic, and Dawn Song

Please contact Mario Frank if questions come up.
Contact details and additional information can be found at http://www.mariofrank.net/touchalytics/index.html





The columns
'phone ID',
'user ID', 
'document ID', 
contain label information and should not be used for testing.





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




The remaingin columns contain extracted features. The feature names are given by the cell array.
Our paper describes how individual features have been computed from the raw data.




