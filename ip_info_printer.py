from ip_info_getter import IpInfoGetter

# This file prints out IP info to the console

if __name__ == "__main__":
    ipinfo = IpInfoGetter.get_ip_info()
    for row in ipinfo:
        print(row)