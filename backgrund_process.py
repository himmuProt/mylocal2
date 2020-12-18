
from subprocess import PIPE, run
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="him"
)

mycursor = mydb.cursor()


def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout
lis=[]
my_output = out("ps -eo lstart").strip()
my_output=my_output.split('\n')
# print(my_output)
for i in my_output:
    lis.append(i)


for i in lis:
    sql='INSERT INTO timestamp (timesdata) VALUES (%s)'
    val=[(i)]
    mycursor.execute(sql,val)

mydb.commit()

