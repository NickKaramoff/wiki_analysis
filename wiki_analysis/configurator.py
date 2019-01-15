#  Copyright (c) 2019 Nikita Karamov <nick@karamoff.ru>

import os
from pathlib import Path
import shutil

from logger import Logger
from ruamel.yaml import YAML
from argument_parser import parse

lg = Logger()

_default = {
    'database': {
        'host': 'localhost',
        'port': '5432',
        'dbname': 'wiki_analysis',
        'username': 'wiki',
        'password': 'wiki',
        'drop': True,
    },
    'fetch': {
        'lang': None,
        'all_pages_path': '/wiki/Special:AllPages',
        'timeout': 30,
        'skip': True,
    },
    'analyze': {
        'iterations': 20,
        'top_pages_amount': 25,
    },
}


def _get_yaml_config(yml_path):
    if os.path.isfile(yml_path):
        yaml = YAML(typ='safe')
        yaml_config = yaml.load(open(yml_path))
    else:
        lg.warning(
            'Config file is not found. Default values will be used and written'
            'to {}'.format(yml_path)
        )
        yaml = YAML()
        yaml.dump(_default, open(yml_path, 'x'))
        yaml_config = {}

    return yaml_config


def merge_replace_dict(source: dict, destination: dict):
    for k, v in source.items():
        if isinstance(v, dict):
            merge_replace_dict(v, destination[k])
        else:
            destination[k] = v


def get_config(args):
    parsed_args = parse(args)
    yml_path = parsed_args['config'] or str(Path.home()) + '/wiki_config.yml'
    from_args = {
        'database': {
            'drop': parsed_args['drop'],
        },
        'fetch': {
            'lang': parsed_args['lang'],
            'skip': parsed_args['skip'],
        }
    }
    from_args = {k: v for k, v in from_args.items() if v}

    yaml_config = _get_yaml_config(yml_path)

    _default['script'] = {
        'headers': {'User-Agent': 'wiki_analysis/0.4'},
        'term_width': shutil.get_terminal_size().columns,
    }

    config = {**_default}

    merge_replace_dict(yaml_config, config)
    merge_replace_dict(from_args, config)

    if config['fetch']['lang']:
        return config
    else:
        lg.error('Language not provided! Please launch the app with lang '
                 'argument or add it to the config file!')
        exit(1)
