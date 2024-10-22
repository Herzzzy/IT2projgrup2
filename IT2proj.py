import pygame as pyg
import random as rd
import csv

filnavn = "spotify_data.csv"

with open(filnavn, encoding="utf-8-sig") as fil:
    filinhold_ufiltrert = fil.read().replace("-", ",")
    filinnhold = csv.reader(filinhold_ufiltrert.splitlines(), delimiter=",")

    total_streams_index = 2
    sang_index = 1
    artist_index = 0  

    rad = list(filinnhold)

    if len(rad)>=100:
        rad=rad[:100]

def velg_sanger():
    ikke_riktig_sang = True
    while ikke_riktig_sang:
        rad_index = rd.randint(2, 1000)
        rad_index2 = rd.randint(2, 1000)
        forste_sang = rad[rad_index]
        andre_sang = rad[rad_index2]

        if rad_index != rad_index2 and len(forste_sang[sang_index]) < 10 and len(andre_sang[sang_index]) < 10:
            ikke_riktig_sang = False

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

pyg.init()

storrelse = [1200, 800]
skjerm = pyg.display.set_mode((storrelse))
skjerm_farge = 150, 255, 150

tekst_font = pyg.font.SysFont(None, 100, bold=True)
tekst_font_mindre = pyg.font.SysFont(None, 50, bold=True)

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

forste_sang, andre_sang = velg_sanger()

run = True
while run:

    delta_tid = klokke.tick(60) 

    left_area = pyg.Rect(0, 0, 600, 800)
    right_area = pyg.Rect(600, 0, 600, 800)

    mouse_click = pyg.mouse.get_pressed()
    mouse_pos = pyg.mouse.get_pos() 

    skjerm.fill((skjerm_farge))

    if spill_ferdig < 3:

        skriv_tekst(f"{antall_riktig}/3", tekst_font_mindre, (0, 0, 0), 70, 50)

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
            if neste_niva_delay > 5000:
                neste_niva = False
                if rikitg:
                    antall_riktig += 1
                start_tekst = True
                bruker_gjett = None
                neste_niva_delay = 0
                spill_ferdig += 1
                rikitg = False
                forste_sang, andre_sang = velg_sanger()

        if start_tekst:
            skriv_tekst(forste_sang[sang_index], tekst_font, (0, 0, 0), 300, 300)
            skriv_tekst(f"-{forste_sang[artist_index]}", tekst_font, (0, 0, 0), 300, 400)
            skriv_tekst(forkort_streams(forste_sang[total_streams_index]), tekst_font, (0, 0, 0), 300, 500)
            skriv_tekst(andre_sang[sang_index], tekst_font, (0, 0, 0), 900, 300)
            skriv_tekst(f"-{andre_sang[artist_index]}", tekst_font, (0, 0, 0), 900, 400)
            skriv_tekst("..?..", tekst_font, (0, 0, 0), 900, 500)
        else:
            if bruker_gjett == "h" and int(forste_sang[total_streams_index]) > int(andre_sang[total_streams_index]) or bruker_gjett == "l" and int(forste_sang[total_streams_index]) < int(andre_sang[total_streams_index]):
                skriv_tekst(f"Det er riktig, {storst_sang} har", tekst_font, (0, 0, 0), 600, 300)
                skriv_tekst(f"{forkort_streams(mest_streams - minst_streams)} flere streams", tekst_font, (0, 0, 0), 600, 400)
                skriv_tekst(f"enn {minst_sang}", tekst_font, (0, 0, 0), 600, 500)
                neste_niva = True
                rikitg = True
            else:
                skriv_tekst(f"Det er feil, {storst_sang} har", tekst_font, (0, 0, 0), 600, 300)
                skriv_tekst(f"{forkort_streams(mest_streams - minst_streams)} flere streams", tekst_font, (0, 0, 0), 600, 400)
                skriv_tekst(f"enn {minst_sang}", tekst_font, (0, 0, 0), 600, 500)
                neste_niva = True

        if mouse_click[0] and start_tekst: 
            if left_area.collidepoint(mouse_pos): 
                bruker_gjett = "h"
                start_tekst = False
            elif right_area.collidepoint(mouse_pos):  
                bruker_gjett = "l"
                start_tekst = False

    else: 
        if antall_riktig >= 2:
            skriv_tekst("Bra jobba!", tekst_font, (0, 0, 0), 600, 300)
            skriv_tekst(f"Du fikk {antall_riktig}/3 riktige", tekst_font, (0, 0, 0), 600, 400)
        elif antall_riktig == 1:
            skriv_tekst(f"Du fikk bare {antall_riktig}/3 riktig", tekst_font, (0, 0, 0), 600, 400)
        else:
            skriv_tekst("damn", tekst_font, (0, 0, 0), 600, 300)
            skriv_tekst(f"du fikk ingen riktig", tekst_font, (0, 0, 0), 600, 400)

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False

    pyg.display.update()

pyg.quit()
