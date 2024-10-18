import csv
import random

filnavn = "spotify_data.csv"

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=",")

    overskrifter = next(filinnhold)
    print("Headers:", overskrifter)

    total_streams_index = 2 
    artist_index = 0  

    rad = list(filinnhold)


    if len(rad) > 0:
        rad_index = random.randint(0, len(rad) - 1)
        bestemt_rad = rad[rad_index]

        print("Artist:", bestemt_rad[artist_index], "Total Streams:", bestemt_rad[total_streams_index])
    else:
        print("Raden finnes ikke")
