from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 

def make_table():
    query = "CREATE TABLE Project" \
            "(" \
            "projId BIGINT UNSIGNED NOT NULL PRIMARY KEY, " \
            "stuff1 INT UNSIGNED, " \
            "stuff2 VARCHAR(30), " \
            "stuff3 INT UNSIGNED, " \
            "stuff4 MEDIUMINT UNSIGNED, " \
            "stuff5 TINYINT(1) UNSIGNED, " \
            "stuff6 TINYINT UNSIGNED, " \
            "stuff7 TINYINT UNSIGNED, " \
            "stuff8 TINYINT UNSIGNED, " \
            "stuff9 TINYINT UNSIGNED, " \
            "stuff10 TINYINT UNSIGNED, " \
            "stuff11 MEDIUMINT UNSIGNED, " \
            "stuff12 FLOAT, " \
            "stuff13 VARCHAR(15), " \
            "stuff14 VARCHAR(200), " \
            "label TINYINT(1) UNSIGNED, " \
            "stuff15 TINYINT(1) UNSIGNED, " \
            "stuff16 TINYINT UNSIGNED" \
            ")"
    
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.execute(query)
    
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
def main():
    make_table()
 
if __name__ == '__main__':
    main()
