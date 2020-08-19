import sys

import yaml
#TODO add some error handling

sourceFile = None
destFile = None


def init():
    global sourceFile, destFile
    
    file1 = open(sys.argv[2], 'r')
    file2 = open(sys.argv[1], 'r')
    
    destFile = yaml.load(file1, Loader=yaml.FullLoader)
    sourceFile = yaml.load(file2, Loader=yaml.FullLoader)

def replace_value(file):
    for key in file:
        if isinstance(file[key], dict):
            file[key] = replace_value(file[key])
        elif key in sourceFile:
            file[key] = sourceFile[key]
    return file


def main():
    global destFile
    init()
    destFile = replace_value(destFile)
    result = yaml.safe_dump(destFile, open(sys.argv[3], 'w'), default_flow_style=False)
    print(result)

main()
