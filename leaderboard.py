import csv
import random
import colorama
import pandas as pandasForSortingCSV 
from colorama import Fore, Back, Style

colorama.init(autoreset=True)



filnavn = "spotify_data.csv"
highscore_fil = "highscore_fil.csv"
spiller_navn = input("Velg et kallenavn: ").upper()



with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=",")

    # overskrifter = next(filinnhold)
    # print("Headers:", overskrifter)

    total_streams_index = 1
    artist_index = 0

    rad = list(filinnhold)

    svar = ""
    ditt_svar = ""
    score = 0

    while svar == ditt_svar:

        if len(rad) > 0:
            rad_index = random.randint(0, len(rad) - 1)
            rad_index2 = random.randint(0, len(rad) - 1)
            bestemt_rad = rad[rad_index]
            bestemt_rad2 = rad[rad_index2]
            antall_streams = int(bestemt_rad[total_streams_index])
            antall_streams2 = int(bestemt_rad2[total_streams_index])

            print(
                f"Artist: {bestemt_rad[artist_index]}, Total Streams: {antall_streams:,d}"
            )
            print(
                f"Artist: {bestemt_rad2[artist_index]}, Total Streams: {antall_streams2:,d}"
            )
        else:
            print("Raden finnes ikke")

        ditt_svar = input(
            f"Har '{bestemt_rad[artist_index]}' flere streams enn '{bestemt_rad2[artist_index]}'({Fore.GREEN}H{Fore.RESET}/{Fore.RED}L{Fore.RESET})?: "
        ).upper()

        if int(bestemt_rad[total_streams_index]) > int(
            bestemt_rad2[total_streams_index]
        ):
            svar = "H"
        else:
            svar = "L"

        if ditt_svar == svar:
            print("Du svarte riktig")
            score += 1
        else:
            print("Du svarte feil")
            with open(highscore_fil, "a") as fil:
                fil.write(f"{spiller_navn},{score} \n")
            
            with open(highscore_fil, encoding="utf-8") as fil:
                innhold = fil.read()
            print(innhold)
            
    print(f"Du fikk {Fore.GREEN}{score} {Fore.RESET}riktige")
    # angi datasettet
    csvData = pandasForSortingCSV.read_csv("highscore_fil.csv") 

    # sorterer dataene
    csvData.sort_values(csvData.columns[1], axis=0, ascending=[False], inplace=True) 

print(csvData[:10])
