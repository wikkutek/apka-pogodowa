from services.openweather_api import fetch_weather
from services.excel_files import save_to_excel, read_excel_file
#from services.dashboard import create_plots
from config import Config
import time
from services.mysql_db import create_record


while True:
    weather = fetch_weather()
    save_to_excel(weather)
    # weather_data = read_excel_file(Config.XLSX_PATH)
    # weather_data = read_excel_file("./services/pogoda_rozszerzona.xlsx")
    # create_plots(weather_data)
    print("Pobrałem dane")
    create_record(weather)
    time.sleep(20)





# -------
# #importujemy z naszego folderu SERVICES z pliku openweather stworzoną funkcję
# from services.excel_files import save_to_excel, read_excel_file
# from services.openweather_api import fetch_weather
# from config import Config
# import time
#
#
# # wywołujemy tu przywołaną funkcję
# #weather = fetch_weather()
#
# #zapisujemy plik w excelu
# #save_to_excel(weather)
# #print(weather)
#
# #odczytujemy zapisanego excela w pythonie
# #weather_data = read_excel_file(Config.XLSX_PATH)
# #print(weather_data)
#
# #pobieranie danych co pewien okres
#
# while True:
#     weather = fetch_weather()
#     save_to_excel(weather)
#     #weather_data = read_excel_file(Config.XLSX_PATH)
#     wheather_data = read_excel_file("./services/pogoda_rozszerzona.xlsx")
#     create_plots(weather_data)
#     print("Pobrałem dane") #wyrzuca komunikat, że pobrał dane, które zapisał w excelu
#
#     time.sleep(10000) #po każdym wykonaniu pętla usypia się na 10s

