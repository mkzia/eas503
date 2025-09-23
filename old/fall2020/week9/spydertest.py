import pandas as pd
import sqlite3
conn = sqlite3.connect("join_example_database.db")
cur = conn.cursor()
sql_statement = "select Quantities.product, Quantities.quantity FROM Quantities Where quantity > 60;"
df = pd.read_sql_query(sql_statement, conn)
print(df)


df.to_csv('dbex_1.csv', index = False)
data = pd.read_csv("dbex_1.csv") 
print(df.equals(data))


def dbex_1():
    """
    Return all products with quantity greater than 60;
    output columns: product_name, product_quantity
    output (df, sql_statement)
    """

    import pandas as pd
    import sqlite3
    conn = sqlite3.connect("join_example_database.db")
    cur = conn.cursor()
    sql_statement = "select Quantities.product, Quantities.quantity FROM Quantities Where quantity > 60;"
    df = pd.read_sql_query(sql_statement, conn)
    return (df, sql_statement)


df, sql_statement = dbex_1()

data = pd.read_csv("dbex_1.csv") 
conn = sqlite3.connect("join_example_database.db")
cur = conn.cursor()
df = pd.read_sql_query(sql_statement, conn)

assert df.equals(data) == True