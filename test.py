import json
from jinja2 import Template
import yaml
from json import dumps

sourceFile = None
destFile = None
#TODO add some error handling

#initialize the files and and take them in as dictionaries
def init():
    global sourceFile, destFile
    
    file1 = open(r'test.yml')
    file2 = open(r'test2.yml')
    
    destFile = yaml.load(file1, Loader=yaml.FullLoader)
    sourceFile = yaml.load(file2, Loader=yaml.FullLoader)

# reading a level of the destination file for keys and sub dictionaries
def replace_level(level):
    #Iterate through the dictionaries and compare the keys
    for key in level:
        if isinstance(level[key], dict):
            level[key] = replace_level(level[key])
        elif key in sourceFile:
            level[key] = sourceFile[key]
    return level


def main():
    global destFile
    init()
    #substitute the values
    destFile = replace_level(destFile)
    #dump the yaml file
    result = yaml.safe_dump(destFile, open(r'out.yml', 'w'), default_flow_style=False)
    #print the result to the terminal
    print(result)

main()
