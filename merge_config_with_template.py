import sys
import argparse
import yaml
#TODO add some error handling

source_file = None
dest_file = None

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
    global source_file, dest_file, config, template

    file1 = open(template, 'r')
    file2 = open(config, 'r')

    dest_file = yaml.load(file1, Loader=yaml.FullLoader)
    source_file = yaml.load(file2, Loader=yaml.FullLoader)

def replace_value(file):
    for key in file:
        #fix for multiple keys with same name
        if key == "databaseEncryption" and source_file[key]:
            file[key] = source_file[key]
        #####################################
        elif isinstance(file[key], dict):
            file[key] = replace_value(file[key])
        elif key in source_file:
            file[key] = source_file[key]
    return file

def main():
    global dest_file, output
    init()
    dest_file = replace_value(dest_file)
    result = yaml.safe_dump(dest_file, open(output, 'w'), default_flow_style=False)
    print(result)

main()
