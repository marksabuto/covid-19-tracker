import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df = df[df["location"].isin(["Kenya", "United States", "India"])]
    df["date"] = pd.to_datetime(df["date"])
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    clean_data("../data/owid-covid-data.csv", "../data/processed_data.csv")