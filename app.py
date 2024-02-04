import pandas as pd
import numpy as np
import sqlite3

con = sqlite3.connect("test_data.db")

df = pd.read_sql_query("SELECT * from restaurant", con)

# Use pivot_table instead of pivot
pivot_df = df.pivot_table(
    index=['user_id'],
    columns=['restaurant'],
    values=['rating']
)

# Save the HTML representation to a file
pivot_df.to_html("output.html")

con.close()