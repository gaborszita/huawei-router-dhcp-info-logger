# IP info getter - router communicator

Description:
I had issues with my Huwaei HG8121H	router DHCP server assinging IP addresses. 
To find the source of the issue, I created this little python project that 
automatically logs in the router web GUI every 10 minutes using pyppeteer and 
logs all the assigned IP addresses to a MySQL/MariaDB database. This helped me 
figure out what was causing the problem. 

Required packages:
- pyppeteer, mysql-connector-python
