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
<<<<<<< HEAD

    file1 = open(r'dummy-gke.yml')
    file2 = open(r'dummy-config.yml')
=======
    
    file1 = open(r'dummy-anthos.yml')
    file2 = open(r'dummy-config.yml')
    
>>>>>>> 48861596d6849557004cc3ded41f2230aec76fcb
    destFile = yaml.load(file1, Loader=yaml.FullLoader)
    sourceFile = yaml.load(file2, Loader=yaml.FullLoader)

# reading a level of the destination file for keys and sub dictionaries
<<<<<<< HEAD
def replace_level(file):
    #print(level)
    for key in file:
        if isinstance(file[key], dict):
            file[key] = replace_level(file[key])
        elif key in sourceFile:
            file[key] = sourceFile[key]
    return file
=======
def replace_level(level):
    #Iterate through the dictionaries and compare the keys
    for key in level:
        if isinstance(level[key], dict):
            level[key] = replace_level(level[key])
        elif key in sourceFile:
            level[key] = sourceFile[key]
    return level
>>>>>>> 48861596d6849557004cc3ded41f2230aec76fcb


def main():
    global destFile
    init()
    #substitute the values
    destFile = replace_level(destFile)
<<<<<<< HEAD
    result = yaml.safe_dump(destFile, open(r'anthos-gke.yml', 'w'), default_flow_style=False)
=======
    #dump the yaml file
    result = yaml.safe_dump(destFile, open(r'anthos-gke.yml', 'w'), default_flow_style=False)
    #print the result to the terminal
>>>>>>> 48861596d6849557004cc3ded41f2230aec76fcb
    print(result)

main()
