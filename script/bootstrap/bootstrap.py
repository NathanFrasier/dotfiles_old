#!/usr/bin/env python3
import platform

bootstrap_switch = {"Linux":linux_bootstrap}

def main():
    #call one of the bootstrap functions based on the current OS system
    try:
        bootstrap_switch[platform.system()]()
    except KeyError as e:
        print("I don't know how to bootstrap this system!")

def linux_bootstrap():
    pass
if __name__ == '__main__':
    main()
