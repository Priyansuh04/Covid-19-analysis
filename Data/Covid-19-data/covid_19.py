import requests
import pandas as pd

url = "https://raw.githubusercontent.com/MainakRepositor/Datasets/master/covid_19_india.csv"

res = requests.get(url)

with open("covid_19_data.csv", "wb") as file:
    file.write(res.content)

df = pd.read_csv("covid_19_data.csv")
print(df.head())