#!/usr/bin/env python3.7

"""scratch_02.py.

Second Program of SCRATCH.

"""
from my_modules import scratch_01 as sc


print("This is scratch_02.py")


def main():
    """Docstring."""
    print("This is scratch_02.py main()")
    print("scratch_01.log('LOG_02.Log', 'scratch_02.py') has been called.")
    sc.log('LOG_02.Log', 'scratch_02.py')
    print('sc.hello("User") has been called.')
    sc.hello("User")


if __name__ == '__main__':
    print("This is scratch_02.py if __name__ == '__main__':")
    main()
