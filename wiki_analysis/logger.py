#  Copyright (c) 2019 Nikita Karamov <nick@karamoff.ru>

from colorama import init, Fore, Style


class Logger:
    LEVELS = ('debug', 'info', 'warning', 'error')

    def __init__(self, verbosity='info'):
        init()
        self.verbosity = verbosity

    def debug(self, message):
        if self.LEVELS.index(self.verbosity) <= self.LEVELS.index('debug'):
            print(Fore.WHITE + message + Style.RESET_ALL)

    def info(self, message):
        if self.LEVELS.index(self.verbosity) <= self.LEVELS.index('info'):
            print(message)

    def warning(self, message):
        if self.LEVELS.index(self.verbosity) <= self.LEVELS.index('warning'):
            print(Fore.YELLOW + message + Style.RESET_ALL)

    def error(self, message):
        if self.LEVELS.index(self.verbosity) <= self.LEVELS.index('error'):
            print(Fore.RED + message + Style.RESET_ALL)
