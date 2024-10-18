import csv
import random

filnavn = "spotify_data.csv"

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=",")

    overskrifter = next(filinnhold)
    print("Headers:", overskrifter)

    total_streams_index = 1 
    artist_index = 0  

    rad = list(filinnhold)


    if len(rad) > 0:
        rad_index = random.randint(0, len(rad) - 1)
        rad_index2 = random.randint(0, len(rad) - 1)
        bestemt_rad = rad[rad_index]
        bestemt_rad2 = rad[rad_index2]
        
        print(f"Artist: {bestemt_rad[artist_index]}, Total Streams: {int(bestemt_rad[total_streams_index]):,d}")
        print(f"Artist: {bestemt_rad2[artist_index]}, Total Streams: {int(bestemt_rad2[total_streams_index]):,d}")
    else:
        print("Raden finnes ikke")

    ditt_svar = input(f"Har '{bestemt_rad[artist_index]}' flere streams enn '{bestemt_rad2[artist_index]}'(H/L)?: ").upper()
    svar = ""

    if int(bestemt_rad[total_streams_index]) > int(bestemt_rad2[total_streams_index]):
        svar = "H"
    else:
        svar = "L"

    if ditt_svar == svar:
        print("Du svarte riktig")
    else:
        print("Du svarte feil")
