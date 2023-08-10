import pandas as pd
# datainfo


def silver_energy():
    df = pd.read_csv("../data/bronze/b_stromproduktion.csv")

    #df1 = df
    # pd.set_option("display.max_rows", None)
    # pd.set_option('display.max_columns', None)

    print(df)
    # print("sample")
    # print(df.sample(10))

    df.to_csv("../data/silver/s_stromprduktion.csv", index=False)


    df1 = pd.read_csv("../data/bronze/b_landesverbrauch-endverbrauch.csv")
    print(df1)
    df1.to_csv("../data/silver/s_landesverbrauch-endverbrauch.csv")


    df2 = pd.read_csv("../data/bronze/b_landesverbrauch-estimated.csv")
    print(df2)
    df2.to_csv("../data/silver/s_landesverbrauch-estimated.csv")