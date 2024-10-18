import csv
import random

filnavn = "spotify_data.csv"

with open(filnavn, encoding="utf-8-sig") as fil:
    filinhold_ufiltrert = fil.read().replace("-", ";")
    filinhold_ufiltrert2 = fil.read().replace(",", ";")
    filinnhold = csv.reader(filinhold_ufiltrert2.splitlines(), delimiter=";")

    overskrifter = next(filinnhold)
    print("Headers:", overskrifter)

    total_streams_index = 2
    artist_index = 0  

    rad = list(filinnhold)

    rad_index = random.randint(0, len(rad) - 1)
    rad_index2 = random.randint(0, len(rad) - 1)
    bestemt_rad = rad[rad_index]
    bestemt_rad2 = rad[rad_index]

    print("Artist, sang navn:", bestemt_rad[artist_index], "Totale Streams:", bestemt_rad[total_streams_index])
    print("Har denne sangen flere eller færre avspillninger enn?", bestemt_rad2[artist_index])
    
    bruker_gjett = input("Trykk h for Høyere, og l for Lavere")

    if (bruker_gjett == 'h' and int(bestemt_rad2[total_streams_index]) > int(bestemt_rad[total_streams_index])) or \
       (bruker_gjett == 'l' and int(bestemt_rad2[total_streams_index]) < int(bestemt_rad[total_streams_index])):
        print("Riktig! {} har {} avspillninger.".format(bestemt_rad2[artist_index], bestemt_rad2[total_streams_index]))
    else:
        print("Feil! {} har {} avspillninger.".format(bestemt_rad2[artist_index], bestemt_rad2[total_streams_index]))
