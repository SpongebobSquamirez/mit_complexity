from python_mysql_dbconfig import read_db_config
import pymysql
from pymysql import Error


def run_query(query):
    try:
        db_config = read_db_config()
        conn = pymysql.connect(**db_config)
 
        cursor = conn.cursor()
        cursor.execute(query)
    
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()

def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def query_with_fetchmany(*args):
    # LIMIT 0,10000"
    query = "SELECT a, b, c, d, e, f, g, " \
                "h, i, j, k FROM project " \
            "WHERE category = %s" \
            "LIMIT %s"
    try:
        #dbconfig = read_db_config()
        conn = pymysql.connect("localhost","python1","pas","table")
        cursor = conn.cursor(pymysql.cursors.SSCursor)
        cursor.execute(query, args)
        #row = cursor.fetchone()
        for row in iter_row(cursor, 1):
            if row is None:
                print("none")
            else:
                yield row
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
        
def update_data(*args):
    query = "UPDATE tweets2014_3 " \
            "SET sentiment=%s " \
            "WHERE dex=%s "
            
    try:
        conn = pymysql.connect("localhost","python1","pas","blank")
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()

def insert_data(*args):
    query = "INSERT INTO Tweets2014_3(sentiment) " \
            "VALUES(%s)"
    #print(query, args)
    try:
        #db_config = read_db_config()
        conn = pymysql.connect("localhost","python1","pas","blank")
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
def main():
    query = "CREATE TABLE Tweets2014" \
            "(" \
            "dex INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, " \
            "tweetId BIGINT UNSIGNED NOT NULL, " \
            "text VARCHAR(140), " \
            "name VARCHAR(15), " \
            "latitude DECIMAL(10,8), " \
            "longitude DECIMAL(11,8), " \
            "created_at VARCHAR(30), " \
            "time_zone VARCHAR(30), " \
            "lang VARCHAR(5), " \
            "retweeted BOOLEAN, " \
            "user_mentions VARCHAR(160), " \
            "hashtags VARCHAR(160), " \
            "favorite_count INT UNSIGNED, " \
            "in_reply_to_screen_name VARCHAR(15), " \
            "retweet_count INT UNSIGNED, " \
            "followers_count INT UNSIGNED, " \
            "statuses_count INT UNSIGNED, " \
            "screen_name VARCHAR(15), " \
            "in_reply_to_user_id INT UNSIGNED, " \
            "user_id INT UNSIGNED, " \
            "in_reply_to_status_id_str BIGINT UNSIGNED" \
            ")"
    run_query(query)


if __name__ == '__main__':
    main()
