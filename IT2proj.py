import csv
import random

filnavn = "spotify_data.csv"

with open(filnavn, encoding="utf-8-sig") as fil:
    filinhold_ufiltrert = fil.read().replace("-", ",")
    filinnhold = csv.reader(filinhold_ufiltrert.splitlines(), delimiter=",")

    total_streams_index = 2
    sang_index = 1
    artist_index = 0  

    rad = list(filinnhold)

    rad_index = random.randint(0, 200)
    rad_index2 = random.randint(0, 200)
    if rad_index == rad_index2:
        rad_index2 = int(rad_index2 + 1)

    forste_sang = rad[rad_index]
    andre_sang= rad[rad_index2]

    print("Artist, sang navn:", forste_sang[artist_index], forste_sang[sang_index], "Totale Streams:", forste_sang[total_streams_index])
    print("Har denne sangen flere eller færre avspillninger enn?", andre_sang[artist_index], andre_sang[sang_index])
    
    bruker_gjett = input("Trykk h for Høyere, og l for Lavere")

    if (bruker_gjett == 'h' and int(forste_sang[total_streams_index]) > int(andre_sang[total_streams_index])) or \
       (bruker_gjett == 'l' and int(forste_sang[total_streams_index]) < int(andre_sang[total_streams_index])):
        print("Riktig! {} har {} avspillninger.".format(andre_sang[artist_index], andre_sang[total_streams_index]))
    else:
        print("Feil! {} har {} avspillninger.".format(andre_sang[artist_index], andre_sang[total_streams_index]))
