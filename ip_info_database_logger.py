import mysql.connector
from datetime import datetime

import pyppeteer
import config
from ip_info_getter import IpInfoGetter

class IpInfoDatabaseLogger:
    def logIpInfoToDatabase():
        db = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USERNAME,
            password=config.DB_PASSWORD,
            database=config.DB_DATABASE
        )

        cursor = db.cursor()

        time_now = datetime.now()
        time_now = time_now.strftime("%Y-%m-%d %H:%M:%S")

        success = False
        try:
            ip_info = IpInfoGetter.get_ip_info()
            success = True
        except pyppeteer.errors.PyppeteerError:
            success = False
        except pyppeteer.errors.BrowserError:
            success = False
        except pyppeteer.errors.ElementHandleError:
            success = False
        except pyppeteer.errors.NetworkError:
            success = False
        except pyppeteer.errors.PageError:
            success = False
        except pyppeteer.errors.TimeoutError:
            success = False


        cursor.execute("LOCK TABLES logs WRITE, logs_data WRITE")
        sql = ("SELECT AUTO_INCREMENT "
            "FROM information_schema.TABLES "
            "WHERE TABLE_SCHEMA='" + config.DB_DATABASE + "' AND "
            "TABLE_NAME='logs'")
        cursor.execute(sql)
        result = cursor.fetchone()
        log_id = result[0]
        sql = "INSERT INTO logs (time, success) VALUES (%s, %s)"
        val = (time_now, success)
        cursor.execute(sql, val)

        if success:    
            for row in ip_info:
                sql = ("INSERT INTO logs_data "
                    "(hostname, ip, mac, lease_time, device_type, log_id) "
                    "VALUES (%s, INET_ATON(%s), %s, %s, %s, %s)")
                hostname = row[0]
                ip = row[1]
                mac = row[2].replace(":", "")
                lease_time = row[3][:-3]
                device_type = row[4]
                val = (hostname, ip, mac, lease_time, device_type, log_id)
                cursor.execute(sql, val)
        else:
            pass

        db.commit()
        cursor.execute("UNLOCK TABLES")

        cursor.close()
        db.close()