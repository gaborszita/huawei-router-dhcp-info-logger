# Router DHCP info logger

Description:
I had issues with my Huwaei HG8121H	router DHCP server assinging IP addresses. 
To find the source of the issue, I created this little python project that 
automatically logs in the router web GUI every 10 minutes using pyppeteer and 
logs all the assigned IP addresses to a MySQL/MariaDB database. This helped me 
figure out what was causing the problem.

Database tables:
- logs
  - id: INT UNSIGNED NOT NULL AUTO_INCREMENT
  - time: TIMESTAMP or DATETIME, TIMESTAMP recommended NOT NULL
  - success: BOOLEAN NOT NULL
- logs_data
  - hostname: VARCHAR(255)
  - ip: INT UNSIGNED
  - mac: CHAR(17)
  - lease_time: INT UNSIGNED
  - device_type: VARCHAR(255)
  - log_id: INT UNSIGNED NOT NULL

Required packages:
- pyppeteer, mysql-connector-python
