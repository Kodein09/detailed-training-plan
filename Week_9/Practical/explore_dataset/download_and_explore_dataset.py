import pandas as pd

dataset = pd.read_csv("train.csv")

# def dataset_analysis(df: pd.DataFrame) -> str:
#     result = {
#         "---Shape---": df.shape,
#         "---Info---": df.info(),
#         "---Describe---": df.describe(),
#         "---Head---": df.head()
#     }
#     return f"{result}\n\n---Is null---\n{df.isnull().sum()}"

def data_analysis(df: pd.DataFrame) -> str:
    return (f"---Info---\n{df.info()}"
            f"\n---Shape--- {df.shape}"
            f"\n---Describe\n{df.describe()}"
            f"\n---Head---\n{df.head()}"
            f"\n---Is null---\n{df.isnull().sum()}")

print(data_analysis(dataset))