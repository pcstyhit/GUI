import os
import json

DIR_LOOP = 3


def update_configurations():
    project_path = os.path.abspath(__file__)

    for _ in range(DIR_LOOP):
        project_path = os.path.dirname(project_path)

    config_file = f'{project_path}/config.json'
    with open(file=config_file, mode='r') as f:
        configurations = json.load(f)
        configurations['project_path'] = project_path

    return configurations


CONFIGS = update_configurations()
