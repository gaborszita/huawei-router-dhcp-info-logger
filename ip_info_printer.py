#!/usr/bin/env python3

from ip_info_getter import IpInfoGetter

# This file prints out IP info to the console

def main():
    ipinfo = IpInfoGetter.get_ip_info()
    for row in ipinfo:
        print(row)

if __name__ == "__main__":
    main()