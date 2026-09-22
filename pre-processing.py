import pandas as pd

# reading all csv data
def readAllCSV():
    for i in range(1, 19):
        print(f"{"-"*50}")
        print(f"DATASET {i}")
        print(f"{"-"*50}")
        
        csv = pd.read_csv(f"./dataset/dataset{i}.csv")
        print(csv)
        print("\n") 

# reading individual csv data
def readCSV(num: int):
    print(f"\nDATASET {num}:")
    csv = pd.read_csv(f"./dataset/dataset{num}.csv")
    print(csv)
    print("\n") 
        

#check all csv info
def checkAllCSVInfo():
    for i in range(1, 19):

        df = pd.read_csv(f"./dataset/dataset{i}.csv")

        print(f"{"-"*50}")
        print(f"DATASET {i}")
        print(f"{"-"*50}")
        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\nCOLUMNS DATA:")

        for column in df.columns:
            print(f"\n{column}")
            print(f"Type: {df[column].dtype}")
            print(f"Unique values: {df[column].nunique()}")
            print(f"Examples: {df[column].dropna().unique()[:10]}")


# dividing last column into 3 individual column
def divideCombinedColumn(num: int):
    df = pd.read_csv(f"./dataset/dataset{num}.csv")
    
    last_column = df.columns[-1]
    split_data = df[last_column].str.split(r'\s{2,}|\t', expand=True)
    
    split_data.columns = [
        "tunnel_parents",
        "label",
        "detailed-label"
    ]
    
    df = df.drop(columns=[last_column])
    df = pd.concat([df, split_data], axis=1)
    df.to_csv(f"./dataset/dataset{num}.csv", index=False)
    
    print(f"Combined column fixed for dataset {num}")


# check dash values of dataset
def checkDashValue():
    for i in range(1, 2):
        csv = pd.read_csv(f"./dataset/dataset{i}.csv")
        dash_count = (csv == "-").sum()

        print(f"{"-"*50}")
        print(f"DATASET {i}")
        print(f"{"-"*50}")
        print(dash_count[dash_count > 0])
        print(f"\nTotal rows: {csv.shape[0]}")

checkDashValue()