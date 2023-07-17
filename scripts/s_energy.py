import pandas as pd
# datainfo


def silver_energy():
    df = pd.read_csv("../data/bronze/b_stromproduktion.csv")

    df1 = df
    # pd.set_option("display.max_rows", None)
    # pd.set_option('display.max_columns', None)

    print(df1)
    print("sample")
    print(df.sample(10))

    # df2 = df.filter(regex="(year|month|stations_)")
    # pd.set_option("display.max_rows", None)
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.width', 100)
    # #print(df2)


    df1.to_csv("../data/silver/s_stromproduktion.csv", index=False)

silver_energy()