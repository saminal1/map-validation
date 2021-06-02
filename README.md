# map-validation

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/R6R54MYBL)

This python script will check for the presence of key POIs in the prefabs.xml of a 7D2D World.
It is aimed at validation of a batch of generated worlds to speed up the process of checking if a World is appropriate for a server.

## Example Output:

### Console
```
OutbackJune1

Dishong Tower: 2 of 3 found - Fail
Cracka Books Tower: 4 of 3 found - Pass
Higashi Building: 1 of 2 found - Fail
Building Site: 6 of 2 found - Pass
Shotgun Messiah Factory: 5 of 4 found - Pass
Shamway Factory: 9 of 4 found - Pass
Waterworks: 12 of 2 found - Pass
JB Hifi: 5 of 3 found - Pass
Woolworths: 6 of 3 found - Pass
Bunnings: 7 of 3 found - Pass
KFC: 12 of 3 found - Pass
Tiff's Cars: 11 of 3 found - Pass
NW Traders: 4 of 2 found - Pass
NE Traders: 2 of 2 found - Pass
SW Traders: 1 of 2 found - Fail
SE Traders: 4 of 2 found - Pass

OutbackJune1 score out of 16: 13 - Fail


OutbackJune2

Dishong Tower: 0 of 3 found - Fail
Cracka Books Tower: 4 of 3 found - Pass
Higashi Building: 1 of 2 found - Fail
Building Site: 3 of 2 found - Pass
Shotgun Messiah Factory: 4 of 4 found - Pass
Shamway Factory: 6 of 4 found - Pass
Waterworks: 19 of 2 found - Pass
JB Hifi: 6 of 3 found - Pass
Woolworths: 2 of 3 found - Fail
Bunnings: 4 of 3 found - Pass
KFC: 13 of 3 found - Pass
Tiff's Cars: 7 of 3 found - Pass
NW Traders: 5 of 2 found - Pass
NE Traders: 2 of 2 found - Pass
SW Traders: 0 of 2 found - Fail
SE Traders: 4 of 2 found - Pass

OutbackJune2 score out of 16: 12 - Fail


OutbackJune3

Dishong Tower: 4 of 3 found - Pass
Cracka Books Tower: 4 of 3 found - Pass
Higashi Building: 2 of 2 found - Pass
Building Site: 5 of 2 found - Pass
Shotgun Messiah Factory: 4 of 4 found - Pass
Shamway Factory: 4 of 4 found - Pass
Waterworks: 22 of 2 found - Pass
JB Hifi: 5 of 3 found - Pass
Woolworths: 2 of 3 found - Fail
Bunnings: 7 of 3 found - Pass
KFC: 14 of 3 found - Pass
Tiff's Cars: 7 of 3 found - Pass
NW Traders: 1 of 2 found - Fail
NE Traders: 5 of 2 found - Pass
SW Traders: 3 of 2 found - Pass
SE Traders: 1 of 2 found - Fail

OutbackJune3 score out of 16: 13 - Fail


OutbackJune4

Dishong Tower: 4 of 3 found - Pass
Cracka Books Tower: 5 of 3 found - Pass
Higashi Building: 4 of 2 found - Pass
Building Site: 8 of 2 found - Pass
Shotgun Messiah Factory: 4 of 4 found - Pass
Shamway Factory: 5 of 4 found - Pass
Waterworks: 11 of 2 found - Pass
JB Hifi: 8 of 3 found - Pass
Woolworths: 3 of 3 found - Pass
Bunnings: 5 of 3 found - Pass
KFC: 11 of 3 found - Pass
Tiff's Cars: 9 of 3 found - Pass
NW Traders: 3 of 2 found - Pass
NE Traders: 2 of 2 found - Pass
SW Traders: 3 of 2 found - Pass
SE Traders: 5 of 2 found - Pass

OutbackJune4 score out of 16: 16 - Pass


List of passes:
OutbackJune4
```
### Excel
[Imgur](https://i.imgur.com/3I24NFl.png)