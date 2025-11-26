import pandas as pd
import os
from config import Config

# data1 = {
#     "Kraj" : ["Polska", "Niemcy", "Japonia"],
#     "Stolica" : ["Warszawa", "Berlin", "Tokyo"],
#     "Populacja" : ["36", "80", "120"]
# }
#
# df1 = pd.DataFrame(data1)
#
# # df1.to_csv("test.csv", encoding="utf8") #zrzucanie do csv
# df1.to_excel("test2.xlsx")
#
#
#
# data2 = [
#     {
#         "Kraj" : "Polska",
#         "Stolica" : "Warszawa",
#         "Populacja" : "36"
#     },
#     {
#         "Kraj" : "Niemcy",
#         "Stolica" : "Berlin",
#         "Populacja" : "80"}
# ]
#
# df2 = pd.DataFrame(data2)
# #print(df2)



def save_to_excel(data):
    try:
        new_df = pd.DataFrame([data]) #nowy df
        if os.path.exists(Config.XLSX_PATH): #jeśli plik istenieje
            current = pd.read_excel(Config.XLSX_PATH) #odczytujemy obecny
            concat_data = pd.concat([current, new_df], ignore_index=True) #łączymy to co było z tym nowym
            concat_data.to_excel(Config.XLSX_PATH, index=False) #zrzucamy ten nowy/połączony plik do excela
        else:

            new_df.to_excel(Config.XLSX_PATH, index=False) #jeśli ścieżka nie istnieje, to nowego df zapisujemy w excel

    except Exception as e:
        print(e)

def read_excel_file(path):
    try:
        file = pd.read_excel(path)
        return file
    except Exception as e:
        print(e)

