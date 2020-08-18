import json
from jinja2 import Template
import yaml
from json import dumps

sourceFile = None
destFile = None

def init():
    print("Initializing files and dictionaries")
    global sourceFile, destFile
    file1 = open(r'test.yml')
    file2 = open(r'test2.yml')
    destFile = yaml.load(file1, Loader=yaml.FullLoader)
    sourceFile = yaml.load(file2, Loader=yaml.FullLoader)

# reading a level of the destination file for keys and sub dictionaries
def replace_level(level):
    #print(level)
    for key in level:
        if isinstance(level[key], dict):
            level[key] = replace_level(level[key])
        elif key in sourceFile:
            level[key] = sourceFile[key]
        #elif level[key] == None:
        #    level[key] = ""
    #print(level)
    return level


def main():
    global destFile
    init()
    destFile = replace_level(destFile)
    result = yaml.safe_dump(destFile, open(r'out.yml', 'w'), default_flow_style=False)
    print(result)

main()