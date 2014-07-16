#!/usr/bin/python

# Import Python MSSql library
import pymssql

# Create Database connection object
pymssqlconn = pymssql.connect(host='192.168.155.1', user='sqladmin', password='Password', database='sqldb')

