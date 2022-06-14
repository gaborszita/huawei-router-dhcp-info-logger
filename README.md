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

Setup instructions
1. Create your MySQL/MariaDB database with the tables described above. Make 
   sure you create a user for the dhcp logger application and grant him access 
   to the tables.
2. Make a copy `sample_config.py` and name it `config.py`. Then, fill out all 
   fields in `config.py`.
3. Test if the logger works by running `ip_info_printer.py`. It should print 
   out the DHCP info acquired from the router to the screen.
4. If all DHCP info was correctly logged in step 3, you are ready to continue 
   to log it to the database. Run `ip_info_scheduled_logger.py` and it will
   log all the DHCP info to the database every `x` seconds, where `x` is the 
   number of seconds you set in the config file. Check if it was correctly 
   logged in the database.
5. (optional) If you want to set up a dedicated computer to logging the DHCP, 
   you can create a service for the `ip_info_scheduled_logger.py`, or, if 
   you're on Linux, you can simply put it in the `/etc/rc.local` file.
6. View the logged DHCP info. If you know SQL, you can use plain SQL commands 
   in the console, but I recommend using a GUI program called LibreOffice 
   Base. It is a free and open-source software. You can open the 
   `view_dhcp_info.odb` file in Base and it already has two queries done 
   for you.
   
Explanation of files:
- `ip_info_database_logger.py`: Logs DHCP info to the database.
- `ip_info_getter.py`: Gets the DHCP info from the router using 
   pyppeteer.
- `ip_info_printer.py`: Prints out the DHCP info to the screen.
- `ip_info_scheduled_logger.py`: Logs DHCP info to the database every `x` 
   seconds, where `x` is the number of seconds set in `config.py`.
- `view_dhcp_info.odb`: LibreOffice Base file for viewing DHCP info.

Required packages:
- pyppeteer, mysql-connector-python
