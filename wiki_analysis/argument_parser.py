#  Copyright (c) 2019 Nikita Karamov <nick@karamoff.ru>

import argparse


def parse(args):
    parser = argparse.ArgumentParser(
        description='This app analyzes the pages of Wikipedia, finding the '
                    'most valuable ones using Google\'s PageRank algorithm.',
        epilog='You can set these and other arguments using the '
               'wiki_config.yml file located in your home folder. You can also '
               'use a different config file.'
    )

    parser.add_argument('lang',
                        action='store',
                        nargs='?',
                        default=None,
                        help='language of the desired Wikipedia')

    parser.add_argument('-v', '--version',
                        action='version',
                        version='0.5.0')
    parser.add_argument('-c', '--config',
                        metavar='FILE',
                        help='specify a different config file')
    parser.add_argument('-d', '--drop',
                        action='store_true',
                        help='drop the tables if they exist')
    parser.add_argument('-s', '--skip',
                        action='store_true',
                        help='only analyze existing data')

    return parser.parse_args(args)
