import yaml

def run():
    path = "jokes2signs.yaml"
    yaml.dump(yaml.safe_load(open(path)), open(path, 'w'))
