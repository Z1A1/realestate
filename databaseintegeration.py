import mysql.connector
def DataUpdate(country,cost,bedrooms,bathrooms,months,property_type,email):

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="schoolqa",
    auth_plugin='mysql_native_password'
   )
  mycursor = mydb.cursor()
  mycursor.execute("CREATE TABLE buyhome (country VARCHAR(255),cost VARCHAR(255),bedrooms VARCHAR(255)  ,bathrooms  VARCHAR(255)  ,months VARCHAR(255) ,property_type VARCHAR(255) ,email  VARCHAR(255)) ")
  