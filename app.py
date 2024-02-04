import pandas as pd
import numpy as np
import sqlite3
import re

def table_setup(user_id_1, user_id_2 = None, user_id_3 = None, user_id_4 = None):
    # change according to database
    con = sqlite3.connect("test_data.db")

    # selecting the rows by user
    df = pd.read_sql_query(
        'SELECT * '
        'FROM restaurant r '
        f' WHERE user_id = "{user_id_1}" '

        'UNION '

        'SELECT * '
        'FROM restaurant r2 '
        f' WHERE user_id = "{user_id_2}"',
        con,
        )
    
    # creating a pivot table
    pivot_df = df.pivot_table(
        index=['user_id'],
        columns=['restaurant'],
        values=['rating']
    ).fillna(0)

    # saving the pivot table to a html file -- TESTING
    pivot_df.to_html("output.html")

    con.close()

table_setup('A', 'B')
