import re
import xml.etree.ElementTree as ET

# reset counters just in case

dishong = 0
crackatower = 0
higashi = 0
shotgunmessfact = 0
shamwayfact = 0
jbhifi = 0
woolworths = 0
bunnings = 0
kfc = 0
tiffs = 0
tradernw = 0
traderne = 0
tradersw = 0
traderse = 0

# read in file - this will go through directories later

prefabs = ET.parse('map-validation\prefabs.xml')
root = prefabs.getroot()

# count key pois

for decoration in root.iter('decoration'):
    name = decoration.get('name')
    position = decoration.get('position')
    xpos = int(re.search("^(-?\d{1,4})", position).group())
    zpos = int(re.search("(-?\d{1,4}$)", position).group())
    # print(str(name) + " at " + str(xpos.group()) + ", " + str(zpos.group()))
    if name[:10] == "skyscraper":
        if name[-2:] == "01":
            dishong += 1
        elif name[-2:] == "02":
            crackatower += 1
        elif name[-2:] == "03":
            higashi += 1
    if name[:7] == "factory":
        if name[-2:] == "01":
            shotgunmessfact += 1
        elif name[-2:] == "02":
            shamwayfact += 1
    if name[:5] == "store":
        if name == "store_electronics_02":
            jbhifi += 1
        elif name == "store_grocery_02":
            woolworths += 1
        elif name == "store_hardware_02":
            bunnings += 1
    if name == "diner_03":
        kfc += 1
    if name == "carlot_01":
        tiffs += 1
    if name[:6] == "trader":
        if xpos >= 0 and zpos < 0:
            tradernw += 1
        if xpos >= 0 and zpos >= 0:
            traderne += 1
        if xpos < 0 and zpos < 0:
            tradersw += 1
        if xpos < 0 and zpos >= 0:
            traderse += 1 

    
# output final count of each key poi

print("Dishong Tower: " + str(dishong))
print("CrackaBook Tower: " + str(crackatower))
print("Higashi Building: " + str(higashi))
print("Shotgun Messiah Factory: " + str(shotgunmessfact))
print("Shamway Factory: " + str(shamwayfact))
print("JB Hifi: " + str(jbhifi))
print("Woolworths: " + str(woolworths))
print("Bunnings: " + str(bunnings))
print("KFC: " + str(kfc))
print("Tiffs Car Lot: " + str(tiffs))
print("Traders:")
print("NW: " + str(tradernw))
print("NE: " + str(traderne))
print("SW: " + str(tradersw))
print("SE: " + str(traderse))

# start scoring
""" Require:
3 Dishong Towe
3 CrackaBooks Tower
2 Higashi
4 Shotgun Messiah Factory
4 Shamway Factory
3 JB Hifi
3 Woolworths
3 Bunnings
3 KFC
3 Tiffs Cars
2 Traders in each quadrant
"""

score = 0

if dishong > 2:
    score += 1
if crackatower > 2:
    score += 1
if higashi > 1:
    score += 1
if shotgunmessfact > 3:
    score += 1
if shamwayfact > 3:
    score += 1
if jbhifi > 2: 
    score += 1
if woolworths > 2:
    score += 1
if bunnings > 2:
    score += 1
if kfc > 2:
    score += 1
if tiffs > 2:
    score += 1
if tradernw >= 2 and traderne >= 2 and tradersw >= 2 and traderse >= 2:
    score += 1
if score == 11:
    print("Score out of 11: " + str(score) + " - Pass")
else:
    print("Score out of 11: " + str(score) + " - Fail")