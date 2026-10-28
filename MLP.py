import pandas as pd

def mlp(src_path):
    df = pd.read_csv(src_path)
    #inspecting my data
    print("Dataframe head")
    print(df.head(10))

    # Droping the useless column 'Unnamed: 0'
    df = df.drop('Unnamed: 0', axis=1)

    print("\nDataframe Info")
    df.info()

    print("\nDataframe Description")
    print(df.describe())