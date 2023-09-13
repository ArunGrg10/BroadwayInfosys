from est_connection import estd_connection

cursor = estd_connection()

# cursor.execute("DROP TABLE STUDENTTESTTB") # paila ko table delete garere naya create garxa


sql = """
CREATE TABLE STUDENT(
    ID CHAR(20),
    NAME CHAR(20),
    AGE INT
)
"""

cursor.execute(sql)
print("TABLE CREATED SUCCESSFULLY !!")


