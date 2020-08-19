import sys
import argparse
import yaml
#TODO add some error handling

sourceFile = None
destFile = None

parser = argparse.ArgumentParser()
parser.add_argument('--configFile', required=True)
parser.add_argument('--templateFile', required=True)
parser.add_argument('--outputFile', required=True)

args = parser.parse_args()
config = args.configFile
template = args.templateFile
output = args.outputFile

print(config)
print(template)
print(output)

def init():
    global sourceFile, destFile, config, template

    file1 = open(template, 'r')
    file2 = open(config, 'r')

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
    global destFile, output
    init()
    destFile = replace_value(destFile)
    result = yaml.safe_dump(destFile, open(output, 'w'), default_flow_style=False)
    print(result)

main()
