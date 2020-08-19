import yaml
#TODO add some error handling

sourceFile = None
destFile = None


def init():
    global sourceFile, destFile
    
    file1 = open(r'dummy-anthos.yml')
    file2 = open(r'dummy-config.yml')
    
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
    result = yaml.safe_dump(destFile, open(r'anthos-gke.yml', 'w'), default_flow_style=False)
    print(result)

main()
