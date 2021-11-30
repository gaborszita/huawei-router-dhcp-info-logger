#!/usr/bin/env python3

from time import sleep
from ip_info_database_logger import IpInfoDatabaseLogger
import config

# Logs ip info to database in specified time intervals

def main():
    while True:
        IpInfoDatabaseLogger.logIpInfoToDatabase()
        sleep(config.IP_LOG_INTERVAL)

if __name__ == "__main__":
    main()