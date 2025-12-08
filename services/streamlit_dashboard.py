import pandas as pd
import matplotlib.pyplot as plt
import random
import plotly.express as px


df = pd.read_excel("pogoda_rozszerzona.xlsx")
#
#konwertowanie str wyglądającego na datę, na prawdziwą datę; trzeba podać format
df["timestamp_dt"] = pd.to_datetime(
    df["timestamp"],
    format="%H:%M:%S %d-%m-%Y"
)


# sortowanie po timestamp
df = df.sort_values("timestamp_dt", ascending=True) #ascending - rosnąco
#
#
# # wykres punktowy: temp. vs wilgotność
#
# plt.figure() #dodajemy wykres
# plt.scatter(df["temp"], df["humidity"]) #musimy podać wartości x i y
#
# #definiujemy opisy wykresu
# plt.title("Temp. vs wilgotność")
# plt.xlabel("Temp. w C")
# plt.ylabel("Wilgotność")
#
# #plt.show() #pokazujemy wykres
#
# # Histogram rozkładu temperatur
# plt.figure()
# # wyciąganie wartości y, x i informacji o słupkach
# y_values, x_values, patches = plt.hist(df['temp'])
# plt.xlabel("Temperatura")
# plt.ylabel("Liczba obserwacji")
# plt.title("Rozkład temperatur")
# plt.ylim(0,20)
#
# print(y_values, x_values, patches)
# for p in patches:
#     p.set_facecolor((random.random(), random.random(), random.random()))
#
# plt.show()
#
# # Wykres pudełkowy - temperatury wg. miasta
# top_cities = df["place"].value_counts().head(5).index
#
# # wybór wierszy, które mają jedno z 5 miast w wartościach place
# subset = df[ df["place"].isin(top_cities) ]
# # wypis wszystkich wierszy (:) i tylko kolumny "place
# # print(subset.loc[:, ["place"]])
#
# data_for_box = [
#     subset[subset["place"] == city]["temp"]
#     for city in top_cities
# ]
#
# plt.figure()
# plt.boxplot(data_for_box, labels=top_cities)
# plt.show()
#
# # Temperatura i temp. odczuwalna, w czasie dla jednego miasta
# city = "Lisbon"
# city_df = df[df["place"] == city]
#
# plt.figure()
# plt.plot(city_df["timestamp_dt"], city_df["temp"], label="Temperatura")
# plt.plot(city_df["timestamp_dt"], city_df["temp_feels_like"], label="Odczuwalna")
#
# plt.legend()
#
# plt.title(f"Temperatura w czasie - {city}")
#
# plt.show()

#---- PLOTLY ----

#fig = px.pie(
#     data_frame=df,
#     names="description",
#     title="Udział typów pogody"
# )

#fig.show()