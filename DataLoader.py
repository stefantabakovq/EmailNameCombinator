import pandas as pd


class DataLoader:
    """
    Load names into dataframe, parse columns & rows
    """
    def __init__(self,
                 domainsPath="./data/data_domains.csv",
                 documentPath="./data/data_names.csv"):
        self.documentPath = documentPath
        self.domainsPath = domainsPath

    def load_names_data(self):
        try:
            df = pd.read_csv(self.documentPath)
            return df
        except FileNotFoundError:
            print(f"File {self.documentPath} not found!")
            return None

    def read_domains_data(self):
        try:
            df = pd.read_csv(self.domainsPath)
            return df
        except FileNotFoundError:
            print(f"File {self.domainsPath} not found!")
            return None