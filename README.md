# map-validation

This python script will check for the presence of key POIs in the prefabs.xml of a 7D2D World.
It is aimed at validation of a batch of generated worlds to speed up the process of checking if a World is appropriate for a server.


## Example Output:

```
OutbackDecayJune1

Dishong Tower: 5
CrackaBook Tower: 5
Higashi Building: 6
Shotgun Messiah Factory: 9
Shamway Factory: 7
JB Hifi: 3
Woolworths: 3
Bunnings: 5
KFC: 5
Tiffs Car Lot: 20
Traders:
NW: 2
NE: 1
SW: 6
SE: 3
OutbackDecayJune1 score out of 11: 10 - Fail


OutbackDecayJune2

Dishong Tower: 5
CrackaBook Tower: 7
Higashi Building: 5
Shotgun Messiah Factory: 6
Shamway Factory: 7
JB Hifi: 3
Woolworths: 5
Bunnings: 7
KFC: 2
Tiffs Car Lot: 18
Traders:
NW: 3
NE: 1
SW: 4
SE: 4
OutbackDecayJune2 score out of 11: 9 - Fail


OutbackDecayJune3

Dishong Tower: 6
CrackaBook Tower: 6
Higashi Building: 7
Shotgun Messiah Factory: 10
Shamway Factory: 9
JB Hifi: 5
Woolworths: 4
Bunnings: 8
KFC: 5
Tiffs Car Lot: 18
Traders:
NW: 3
NE: 2
SW: 5
SE: 2
OutbackDecayJune3 score out of 11: 11 - Pass


OutbackDecayJune4

Dishong Tower: 6
CrackaBook Tower: 5
Higashi Building: 6
Shotgun Messiah Factory: 9
Shamway Factory: 9
JB Hifi: 5
Woolworths: 7
Bunnings: 5
KFC: 4
Tiffs Car Lot: 18
Traders:
NW: 1
NE: 4
SW: 2
SE: 5
OutbackDecayJune4 score out of 11: 10 - Fail


OutbackDecayJune5

Dishong Tower: 5
CrackaBook Tower: 5
Higashi Building: 8
Shotgun Messiah Factory: 9
Shamway Factory: 10
JB Hifi: 4
Woolworths: 3
Bunnings: 3
KFC: 3
Tiffs Car Lot: 17
Traders:
NW: 1
NE: 3
SW: 1
SE: 7
OutbackDecayJune5 score out of 11: 10 - Fail
```