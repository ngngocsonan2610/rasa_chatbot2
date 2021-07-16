#%% lib
import sqlite3
import pandas as pd
#%% create

# #Connecting to sqlite
# conn = sqlite3.connect('testbooking.db')

# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# #Doping EMPLOYEE table if already exists.
# cursor.execute("DROP TABLE IF EXISTS TESTBOOKING")

# #Creating table as per requirement
# sql ='''CREATE TABLE TESTBOOKING(
#    PNR NVARCHAR(10) NOT NULL,
#    NAME CHAR(30),
#    FLIGHT_DATE DATETIME,
#    PID INT(9),
#    PAYMENT FLOAT  
# )'''
# cursor.execute(sql)
# print("Table created successfully........")

# # Commit your changes in the database
# conn.commit()

# #Closing the connection
# conn.close()


# # %% insert
# conn = sqlite3.connect('testbooking.db')
# print("Opened database successfully")

# conn.execute("INSERT INTO TESTBOOKING (PNR,NAME,FLIGHT_DATE,PID,PAYMENT) \
#       VALUES ('1A2B3C', 'Ng Thi A', '2021-06-06', 123456789, 200000.00 )")

# conn.execute("INSERT INTO TESTBOOKING (PNR,NAME,FLIGHT_DATE,PID,PAYMENT) \
#       VALUES ('2A2B2C', 'Tr Van A', '2021-06-07', 111222333, 300000.00 )")

# conn.execute("INSERT INTO TESTBOOKING (PNR,NAME,FLIGHT_DATE,PID,PAYMENT) \
#       VALUES ('3A3B3C', 'Tr Van B', '2021-06-08', 333666888, 350000.00 )")

# conn.execute("INSERT INTO TESTBOOKING (PNR,NAME,FLIGHT_DATE,PID,PAYMENT) \
#       VALUES ('3A3B3C', 'Ng Thi C', '2021-06-09', 111333555, 350000.00 )")

# conn.execute("INSERT INTO TESTBOOKING (PNR,NAME,FLIGHT_DATE,PID,PAYMENT) \
#       VALUES ('3A3B3C', 'Ng Thi D', '2021-06-09', 999888777, 400000.00 )")


# conn.commit()
# print( "Records created successfully")
# conn.close()
# %% query
# conn = sqlite3.connect('testbooking.db')

# # con = sqlite3.connect("data/portal_mammals.sqlite")
# df = pd.read_sql_query("SELECT * from TESTBOOKING", conn)

# # Verify that result of SQL query is stored in the dataframe
# print(df.head())

# conn.close()
#%%
DB_PATH = 'actions/testbooking.db'
#%%
def query_pid(pid='111222333'):
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT * from TESTBOOKING WHERE PID={}".format(pid)
    df = pd.read_sql_query(query, conn)
    conn.close()
    if df.shape[0] > 0:
        _result = [str(df.columns[idx])+': '+str(df.iloc[0,:][idx])
                    for idx in range(4) ]
        _result = ', '.join(_result)
    else:
        _result = 'PID không tìm thấy'
    return _result

# query_pid(pid='111222333')
# query_pid(pid='111222336')

#%%
def query_pnr(pnr='ABC123'):
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT * from TESTBOOKING WHERE PNR='{}'".format(str(pnr))
    df = pd.read_sql_query(query, conn)
    conn.close()
    if df.shape[0] > 0:
        _result = [str(df.columns[idx])+': '+str(df.iloc[0,:][idx])
                    for idx in range(4) ]
        _result = ', '.join(_result)
    else:
        _result = 'PNR không tìm thấy'
    return _result

# query_pnr(pnr='ABC123')

# query_pnr(pnr='1A2B3C')