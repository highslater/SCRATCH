#!/usr/bin/env python3.7

"""scratch_01.py.

First Program of SCRATCH.

"""
import logging
from platform import python_version
from sys import hexversion
from datetime import datetime as dt

print("This is scratch_01.py")


def hello(name):
    """Docstring."""
    print("\n\t***   Hello", name, "   ***\n")


def log(log, filename):
    """Docstring."""
    now = dt.today()
    print_version_info = True
    print_time = True
    log_format = "%(levelname)s %(asctime)s - %(message)s"
    version_info = "The Python Version is: {}  #{}".format(
        python_version(), str(hexversion))
    logging.basicConfig(filename="LOG_files/" + log,
                        level=logging.DEBUG, format=log_format,
                        filemode='w')
    logger = logging.getLogger()
    logger.info(version_info) if print_version_info else None
    logger.info(now.strftime("%A, %B, %d, %Y")) if print_time else None
    logger.info(filename + " RUN / START")

    print("Today is:", now.strftime("%A, %B, %d, %Y")) if print_time else None
    print(version_info) if print_version_info else None


def main():
    """Docstring."""
    print("This is scratch_01.py main(), log() has been called")
    log('LOG_01.Log', 'scratch_01.py')


if __name__ == '__main__':
    print("This is scratch_01.py if __name__ == '__main__':")
    main()
