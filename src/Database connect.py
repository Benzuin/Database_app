import pyodbc

count = 0
Secret = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"
database = "DATABASELEARNING"
serverName = "BENZUIN-LAPTOP"

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + serverName + ';DATABASE=' + database +
                      ';Trusted_Connection=yes;')
print(conn)
cursor = conn.cursor()

for i in alphabet:
    count += 1
    cursor.execute("Insert into Alphabet values (" + str(count) + ", '" + i + "');commit;")

code = input("Type in the word you want to have converted to a number\n")
for i in code:
    cursor.execute("select * from Alphabet where letter = '" + i + "'")
    for row in cursor:
        Secret += str(row[0])

print(Secret)
cursor.execute("DELETE FROM Alphabet WHERE cijfer is not null;commit;")
