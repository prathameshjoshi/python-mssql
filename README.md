Hi,

This repository contains template for the connection between python and mssql.

Before starting connection go thought to do list.

1.  Connect to MSSQL database server using MSSQL Server Management Studio.
2.  Create New user and assign default database to the user.
3.  Change Authentication mode to Windows and SQL User.
4.  Make sure SQL services are running in the windows machine.
5.  Change firewall rule, add incoming rule and grant access to the SQL server on port 1433.
6.  Try telnet connection from remote machine on port 1433
7.  Try to connect to the MSSQL server using newly created server.
8.  Use Freetds and tsql to check database connection.
9.  Run following command to test connection
     a. tsql -H <hostname or ipaddress> -p <portnumber> -U <username>
10. Once the connection is successful ready to use template.
