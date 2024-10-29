import pygame as pyg
import random as rd
import csv
import pandas as pandasForSortingCSV
import colorama
from colorama import Fore, Style
import sys
 
colorama.init(autoreset=True)
 
filnavn = "spotify_data.csv"
highscore_fil = "highscore_fil.csv"
 
with open(filnavn, encoding="utf-8-sig") as fil:
    filinhold_ufiltrert = fil.read().replace("-", ",")
    filinnhold = csv.reader(filinhold_ufiltrert.splitlines(), delimiter=",")
 
    total_streams_index = 2
    sang_index = 1
    artist_index = 0  
 
    rad = list(filinnhold)
 
def velg_sanger():
    ikke_riktig_sang = True
    while ikke_riktig_sang:
        rad_index = rd.randint(2, 1000)
        rad_index2 = rd.randint(2, 1000)
        forste_sang = rad[rad_index]
        andre_sang = rad[rad_index2]
 
        try:
            forste_streams = int(forste_sang[total_streams_index])
            andre_streams = int(andre_sang[total_streams_index])
 
            if (rad_index != rad_index2 and
                len(forste_sang[sang_index]) < 10 and len(andre_sang[sang_index]) < 10 and
                len(forste_sang[artist_index]) < 10 and len(andre_sang[artist_index]) < 10):
                ikke_riktig_sang = False
 
        except ValueError:
            continue
 
    return forste_sang, andre_sang
 
def forkort_streams(streams):
    streams = str(streams)
 
    if len(streams) == 10:
        streams = int(streams) // 10**8
        resultat = str(streams)[:1] + "," + str(streams)[1:]
        return resultat + "B"
    
    elif 7 <= len(streams) <= 9:
        streams = int(streams) // 10**6
        resultat = str(streams)
        return resultat + "M"
    
    return streams
 
def legg_til_highscore(navn, poeng):
    with open(highscore_fil, mode='a', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([navn, poeng])
 
def display_leaderboard():
    # angi datasettet
            csvData = pandasForSortingCSV.read_csv("highscore_fil.csv") 

            # sorterer dataene
            csvData.sort_values(csvData.columns[1], axis=0, ascending=[False], inplace=True) 
            y_position = 100  # Start y-position for the text
            for i in range(10):
                row = csvData.iloc[i]  # Access the specific row
                text_to_display = f"{row[0]}: {row[1]}"  # Format the text (adjust column index as needed)
                skriv_tekst(text_to_display, tekst_font_mindre2, (0, 0, 0), 600, y_position)
                y_position += 50  # Move the y-position down for the next line (adjust based on font size)
 
 
pyg.init()
 
storrelse = [1200, 800]
skjerm = pyg.display.set_mode((storrelse))
skjerm_farge = 255, 255, 255
 
tekst_font = pyg.font.SysFont(None, 100, bold=True)
tekst_font_mindre = pyg.font.SysFont(None, 50, bold=True)
tekst_font_storre = pyg.font.SysFont(None, 150, bold=True)
tekst_font_mindre2 = pyg.font.SysFont(None, 75, bold=True)
horl_farge = 0, 0, 0
leaderboard_farge = 0, 0, 0
inst_farge = 0, 0, 0
 
def skriv_tekst(tekst, font, tekst_farge, x, y):
    img = font.render(tekst, True, tekst_farge)
    img_rect = img.get_rect(center=(x, y))
    skjerm.blit(img, img_rect)
 
klokke = pyg.time.Clock()
 
bruker_gjett = None
start_tekst = True
neste_niva = False
neste_niva_delay = 0
antall_riktig = 0
spill_ferdig = 0
rikitg = False
gamemeny = True
higher_or_lower = False
leaderboard = False
instillinger = False
venstre_tekst_farge = 255, 255, 255
hoyre_tekst_farge = 255, 255, 255
pa_nytt_farge = 255, 255, 255
tokk_feil = False
delay_pa = False
timer_start2 = 0
navn_input_active = False
navn_input = ""
enter_highscore = False
tbake_ledrbrd_farge = 0, 0, 0
 
forste_sang, andre_sang = velg_sanger()
 
run = True
while run:
 
    delta_tid = klokke.tick(60)
    skjerm.fill((skjerm_farge))
 
    mouse_click = pyg.mouse.get_pressed()
    mouse_pos = pyg.mouse.get_pos()
 
    if gamemeny:
        skriv_tekst("IT2 prosjekt", tekst_font_storre, (0, 0, 0), 600, 280)
    
        horl_tekst = tekst_font_mindre2.render("Higher or Lower", True, horl_farge)
        horl_rect = horl_tekst.get_rect(center=(600, 400))
        skjerm.blit(horl_tekst, horl_rect)
 
        leaderboard_tekst = tekst_font_mindre2.render("Leaderboard", True, leaderboard_farge)
        leaderboard_rect = leaderboard_tekst.get_rect(center=(600, 470))
        skjerm.blit(leaderboard_tekst, leaderboard_rect)
 
        skriv_tekst("Laget av Herman, Martin", tekst_font_mindre, (0, 0, 0), 600, 650)
        skriv_tekst("Mohammed, Preben og Julie", tekst_font_mindre, (0, 0, 0), 600, 700)
 
        if horl_rect.collidepoint(mouse_pos):
            horl_farge = 0, 0, 255
            if mouse_click[0]:
               gamemeny = False
               higher_or_lower = True
               timer_start = pyg.time.get_ticks()
        else:
            horl_farge = 0, 0, 0
 
        if leaderboard_rect.collidepoint(mouse_pos):
            leaderboard_farge = 0, 0, 255
            if mouse_click[0]:
                leaderboard = True
                gamemeny = False
                timer_start = pyg.time.get_ticks()
        else:
            leaderboard_farge = 0, 0, 0
    else:
        if leaderboard:
            display_leaderboard()
 
            tbake_ledrbrd = tekst_font_mindre.render("Trykk her for å gå tilbake", True, (tbake_ledrbrd_farge))
            tbake_ledrbrd_rect = tbake_ledrbrd.get_rect(center=(230, 50))
            skjerm.blit(tbake_ledrbrd, tbake_ledrbrd_rect)
 
            if tbake_ledrbrd_rect.collidepoint(mouse_pos):
                tbake_ledrbrd_farge = 0, 0, 255
                if mouse_click[0]:
                    leaderboard = False
                    gamemeny = True
            else:
                tbake_ledrbrd_farge = 0, 0, 0
        else:
 
            venstre_omrade = pyg.Rect(0, 0, 600, 800)
            hoyre_omrade = pyg.Rect(600, 0, 600, 800)
            pyg.draw.rect(skjerm, (255, 75, 75), venstre_omrade)
            pyg.draw.rect(skjerm, (75, 75, 255), hoyre_omrade)
 
            if not tokk_feil:
 
                skriv_tekst(f"{antall_riktig} poeng", tekst_font_mindre, (255, 255, 255), 70, 50)
 
                if int(forste_sang[total_streams_index]) > int(andre_sang[total_streams_index]):
                    mest_streams = int(forste_sang[total_streams_index])
                    storst_sang = forste_sang[sang_index]
                    minst_streams = int(andre_sang[total_streams_index])
                    minst_sang = andre_sang[sang_index]
                else:
                    mest_streams = int(andre_sang[total_streams_index])
                    storst_sang = andre_sang[sang_index]
                    minst_streams = int(forste_sang[total_streams_index])
                    minst_sang = forste_sang[sang_index]
 
                if neste_niva:
                    neste_niva_delay += delta_tid
                    if neste_niva_delay > 2500:
                        neste_niva = False
                        antall_riktig += 1
                        start_tekst = True
                        bruker_gjett = None
                        neste_niva_delay = 0
                        spill_ferdig += 1
                        rikitg = False
                        forste_sang, andre_sang = velg_sanger()
 
                if start_tekst:
                    venstre_sang_tekst = tekst_font.render(forste_sang[sang_index], True, (venstre_tekst_farge))
                    venstre_sang_rect = venstre_sang_tekst.get_rect(center=(300, 300))
                    skjerm.blit(venstre_sang_tekst, venstre_sang_rect)
 
                    venstre_artist_tekst = tekst_font.render(forste_sang[artist_index], True, (venstre_tekst_farge))
                    venstre_artist_rect = venstre_artist_tekst.get_rect(center=(300, 400))
                    skjerm.blit(venstre_artist_tekst, venstre_artist_rect)
                    
                    venstre_streams_tekst = tekst_font.render(forkort_streams(forste_sang[total_streams_index]), True, (venstre_tekst_farge))
                    venstre_streams_rect = venstre_streams_tekst.get_rect(center=(300, 500))
                    skjerm.blit(venstre_streams_tekst, venstre_streams_rect)
                    
                    hoyre_sang_tekst = tekst_font.render(andre_sang[sang_index], True, (hoyre_tekst_farge))
                    hoyre_sang_rect = hoyre_sang_tekst.get_rect(center=(900, 300))
                    skjerm.blit(hoyre_sang_tekst, hoyre_sang_rect)
                    
                    hoyre_artist_tekst = tekst_font.render(andre_sang[artist_index], True, (hoyre_tekst_farge))
                    hoyre_artist_rect = hoyre_artist_tekst.get_rect(center=(900,400))
                    skjerm.blit(hoyre_artist_tekst, hoyre_artist_rect)
                    
                    hoyre_streams_tekst = tekst_font.render("..?..", True, (hoyre_tekst_farge))
                    hoyre_streams_rect = hoyre_streams_tekst.get_rect(center=(900,500))
                    skjerm.blit(hoyre_streams_tekst, hoyre_streams_rect)
 
                    skriv_tekst("Or", tekst_font_mindre, (255, 255, 255), 600, 400)
 
                else:
                    if bruker_gjett == "h" and int(forste_sang[total_streams_index]) > int(andre_sang[total_streams_index]) or bruker_gjett == "l" and int(forste_sang[total_streams_index]) < int(andre_sang[total_streams_index]):
                        skriv_tekst(f"Det er riktig, {storst_sang} har", tekst_font, (255, 255, 255), 600, 300)
                        skriv_tekst(f"{forkort_streams(mest_streams - minst_streams)} flere streams", tekst_font, (255, 255, 255), 600, 400)
                        skriv_tekst(f"enn {minst_sang}", tekst_font, (255, 255, 255), 600, 500)
                        neste_niva = True
                        rikitg = True
                    else:
                        skriv_tekst(f"Det er feil, {storst_sang} har", tekst_font, (255, 255, 255), 600, 300)
                        skriv_tekst(f"{forkort_streams(mest_streams - minst_streams)} flere streams", tekst_font, (255, 255, 255), 600, 400)
                        skriv_tekst(f"enn {minst_sang}", tekst_font, (255, 255, 255), 600, 500)
                        tokk_feil = True
                
                tid_etter_start = pyg.time.get_ticks()
 
                if tid_etter_start - timer_start >= 1000:
 
                    if (venstre_sang_rect.collidepoint(mouse_pos) or
                        venstre_artist_rect.collidepoint(mouse_pos) or
                        venstre_streams_rect.collidepoint(mouse_pos)):
                        venstre_tekst_farge = 200, 200, 200
                        if mouse_click[0] and start_tekst:
                            bruker_gjett = "h"
                            start_tekst = False
                    else:
                        venstre_tekst_farge = 255, 255, 255
 
                    if (hoyre_sang_rect.collidepoint(mouse_pos) or
                        hoyre_artist_rect.collidepoint(mouse_pos) or
                        hoyre_streams_rect.collidepoint(mouse_pos)):
                        hoyre_tekst_farge = 200, 200, 200
                        if mouse_click[0] and start_tekst:
                            bruker_gjett = "l"  
                            start_tekst = False
                    else:
                        hoyre_tekst_farge = 255, 255, 255
 
            if higher_or_lower and tokk_feil:
                skriv_tekst(f"Det var feil, du fikk ", tekst_font, (255, 255, 255), 600, 300)
                skriv_tekst(f" {antall_riktig}, antall riktig", tekst_font, (255, 255, 255), 600, 400)
                 
                skriv_tekst("Skriv ditt navn for highscore: ", tekst_font_mindre, (255, 255, 255), 600, 450)
                navn_input_active = True
 
                skriv_tekst(navn_input, tekst_font_mindre, (255, 255, 255), 600, 500)
 
                if enter_highscore:
                    legg_til_highscore(navn_input.upper(), antall_riktig)
                    higher_or_lower = False
                    gamemeny = True
                    navn_input_active = False
                    navn_input = ""
                    antall_riktig = 0
                    bruker_gjett = None
                    tokk_feil = False
                    start_tekst = True
                    enter_highscore = False
                    forste_sang, andre_sang = velg_sanger()
 
                pa_nytt_tekst = tekst_font_mindre2.render("gå til gamemeny", True, (pa_nytt_farge))
                pa_nytt_rect = pa_nytt_tekst.get_rect(center=(600, 600))
                skjerm.blit(pa_nytt_tekst, pa_nytt_rect)
 
                if pa_nytt_rect.collidepoint(mouse_pos):
                    pa_nytt_farge = 200, 200, 200
                    if mouse_click[0] and not delay_pa:
                        delay_pa = True
                        timer_start2 = pyg.time.get_ticks()
 
                    if delay_pa:
                        tid_etter_start2 = pyg.time.get_ticks()
                        if tid_etter_start2 - timer_start2 >= 500:
                            higher_or_lower = False
                            gamemeny = True
                            delay_pa = False
                            antall_riktig = 0
                            tokk_feil = False
                            start_tekst = True
                            forste_sang, andre_sang = velg_sanger()
                else:
                    pa_nytt_farge = 255, 255, 255
    
    for event in pyg.event.get():
            if event.type == pyg.QUIT:
                run = False
 
            if navn_input_active:
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_BACKSPACE:
                        navn_input = navn_input[:-1]
                    elif event.key == pyg.K_RETURN:
                        enter_highscore = True
                    else:
                        navn_input += event.unicode
 
    pyg.display.update()
 
pyg.quit()
