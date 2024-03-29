""" Contains all game parameters in one place """

from colorama import init, Fore, Style, Back

init(autoreset=True)


MATRIX_WIDTH = 85
MATRIX_LENGTH = 30

SPEED = 1
LIVES = 3

# color escape sequences
colors = {
    'Blue': '\x1b[0;34m',
    'Green': '\x1b[0;32m',
    'Cyan': '\x1b[0;36m',
    'Red': '\x1b[0;31m',
    'Purple': '\x1b[0;35m',
    'Brown': '\x1b[0;33m',
    'Gray': '\x1b[0;37m',
    'Light Green': '\x1b[1;32m',
    'Light Cyan': '\x1b[1;36m',
    'Yellow': '\x1b[1;33m',
    'White': '\x1b[1;37m',
    'Black': '\x1b[1;30m'
}
bcolors = {
    'Blue': '\x1b[0;44m',
    'Green': '\x1b[0;42m',
    'Cyan': '\x1b[0;46m',
    'Red': '\x1b[0;41m',
    'Purple': '\x1b[0;45m',
    'Brown': '\x1b[0;43m',
    'Gray': '\x1b[0;47m',
    'Light Green': '\x1b[1;42m',
    'Light Cyan': '\x1b[1;46m',
    'Yellow': '\x1b[1;43m',
    'White': '\x1b[1;47m',
    'Black': '\x1b[1;40m'
}

RESET = '\x1b[0m'

