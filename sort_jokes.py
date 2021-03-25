import yaml
path = "jokes2signs.yaml"
yaml.dump(yaml.safe_load(path), open(path, 'w'))