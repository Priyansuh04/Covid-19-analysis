import requests
import pandas as pd

url = "https://raw.githubusercontent.com/MainakRepositor/Datasets/master/covid_19_india.csv"

res = requests.get(url)

with open("suicide_data.csv", "wb") as file:
    file.write(res.content)

df = pd.read_csv("suicide_data.csv")
print(df.head())