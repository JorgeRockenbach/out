import pyodbc

server = 'localhost' 
database = 'out' 
username = 'root' 
password = 'root' 
cnxn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 ANSI Driver}; SERVER=localhost; PORT=3306; DATABASE=out; UID=root; PWD=root')
cursor = cnxn.cursor()