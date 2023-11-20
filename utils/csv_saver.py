import pandas as pd
import os
def make_df(df_name: str, dump: dict, columns: list):
    if not os.path.exists("data"):
        os.mkdir("data")
    file_path = f"data/{df_name}.csv"
    df = pd.DataFrame(list(dump.items()), columns=columns)

    df.to_csv(file_path)

def make_df_list(df_name: str, dump: list, columns: list):
    if not os.path.exists("data"):
        os.mkdir("data")
    file_path = f"data/{df_name}.csv"
    df = pd.DataFrame(dump, columns=columns)

    df.to_csv(file_path)