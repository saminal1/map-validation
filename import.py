from pathlib import Path
import glob
import re

glob_path = Path(r"J:\Games\7D2D\KingGen")
file_list = [str(pp) for pp in glob_path.glob("**/prefabs.xml")]
for file in file_list:
    print(file)
    world = re.search("([A-Za-z0-9\-]*)(?=.prefabs\.xml$)", file).group()
    print(str(world))