import csv
from pathlib import Path
import glob
import re
import xml.etree.ElementTree as ET

# define class keypoi to store requirements

class keypoi:
    def __init__(self, filename, friendlyname, required, detected):
        self.filename = filename
        self.friendlyname = friendlyname
        self.required = required
        self.detected = detected

    def found(self):
        self.detected += 1

    def detection(self):
        print(f"{self.friendlyname}: {self.detected} found.")

# read in required.csv file - populate keypoi objects
reqlist = []
  
with open('map-validation\\requirements.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        reqlist.append(keypoi(row[0], row[1], row[2], 0))

# add traders to requirements

reqlist.append(keypoi("tradernw", "NW Traders", 2, 0))
reqlist.append(keypoi("traderne", "NE Traders", 2, 0))
reqlist.append(keypoi("tradersw", "SW Traders", 2, 0))
reqlist.append(keypoi("traderse", "SE Traders", 2, 0))

# read in prefabs.xml files - recurse through world directories in a root path
glob_path = Path(r"J:\Games\7D2D\NitroGen_WorldGenerator\output")
file_list = [str(pp) for pp in glob_path.glob("**/prefabs.xml")]

# define blank list to keep track of which worlds work

passes = []

# start checking xml files

for file in file_list:

    # get world name from path name
    world = re.search("([A-Za-z0-9\-]*)(?=.prefabs\.xml$)", file).group()
    print(world)
    print("")

    # reset detected counters
    for req in reqlist:
        req.detected = 0

    #read in xml
    prefabs = ET.parse(file)
    root = prefabs.getroot()

    # count key pois
    for decoration in root.iter('decoration'):
        name = decoration.get('name')
        if re.match("trader.*", name):
            position = decoration.get('position')
            xpos = int(re.search("^(-?\d{1,4})", position).group())
            zpos = int(re.search("(-?\d{1,4}$)", position).group())
            if zpos >= 0:
                if xpos < 0:
                    keypoi.found(reqlist[-4]) # Found in NW quadrant
                else:
                    keypoi.found(reqlist[-3]) # Found in NE quadrant
            else:
                if xpos < 0:
                    keypoi.found(reqlist[-2]) # Found in SW quadrant
                else:
                    keypoi.found(reqlist[-1]) # Found in SE quadrant
        else:
            for req in reqlist[:-4]:
                if re.match(req.filename, name):
                    keypoi.found(req)
                    break

    # reset score
    score = 0

    # calculate score
    for req in reqlist:
        if int(req.detected) >= int(req.required):
            print(f"{req.friendlyname}: {req.detected} of {req.required} found - Pass")
            score += 1
        else:
            print(f"{req.friendlyname}: {req.detected} of {req.required} found - Fail")
    print("")
    # calculate pass and add to the list if appropriate
    if score == len(reqlist):
        print(f"{world} score out of {len(reqlist)}: {score} - Pass")
        passes.append(world)
    else:
        print(f"{world} score out of {len(reqlist)}: {score} - Fail")
    print("\n")

# print summary
if len(passes) == 0:
    print("No passes in batch.")
else:
    print("List of passes:")
    for apass in passes:
        print(apass)
