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

def velg_sanger():
    ikke_riktig_sang = True
    while ikke_riktig_sang:
        rad_index = rd.randint(2, 1000)
        rad_index2 = rd.randint(2, 1000)
        forste_sang = rad[rad_index]
        andre_sang = rad[rad_index2]

        if rad_index != rad_index2 and len(forste_sang[sang_index]) < 10 and len(andre_sang[sang_index]) < 10 and len(forste_sang[artist_index]) < 10  and len(andre_sang[artist_index]) < 10:
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
hoyre_tekst_farge = 255, 255, 255
venstre_tekst_farge = 255, 255, 255

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

        inst_tekst = tekst_font_mindre2.render("Instillinger", True, inst_farge)
        inst_rect = inst_tekst.get_rect(center=(600, 540))
        skjerm.blit(inst_tekst, inst_rect)

        if horl_rect.collidepoint(mouse_pos):
            horl_farge = 0, 0, 255
            if mouse_click[0]:
                higher_or_lower = True
                gamemeny = False
                timer_start = pyg.time.get_ticks()
        else:
            horl_farge = 0, 0, 0

        if leaderboard_rect.collidepoint(mouse_pos):
            ftl_farge = 0, 0, 255
            if mouse_click[0]:
                leaderboard = True
                gamemeny = False
                timer_start = pyg.time.get_ticks()
        else:
            ftl_farge = 0, 0, 0

        if inst_rect.collidepoint(mouse_pos):
            inst_farge = 0, 0, 255
            if mouse_click[0]:
                instillinger = True
                gamemeny = False
                timer_start = pyg.time.get_ticks()
        else:
            inst_farge = 0, 0, 0
    else:
        if leaderboard:
            #skriv leadboard in her
            ma_bare_ha_noe_her = 2
        elif higher_or_lower:

            venstre_omrade = pyg.Rect(0, 0, 600, 800)
            hoyre_omrade = pyg.Rect(600, 0, 600, 800)
            pyg.draw.rect(skjerm, (255, 75, 75), venstre_omrade)
            pyg.draw.rect(skjerm, (75, 75, 255), hoyre_omrade)


            if spill_ferdig < 10:

                skriv_tekst(f"{antall_riktig}/10", tekst_font_mindre, (255, 255, 255), 70, 50)

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
                    hoyre_sang_tekst = tekst_font.render(forste_sang[sang_index], True, (hoyre_tekst_farge))
                    hoyre_sang_rect = hoyre_sang_tekst.get_rect(center=(300, 300))
                    skjerm.blit(hoyre_sang_tekst, hoyre_sang_rect)

                    hoyre_artist_tekst = tekst_font.render(forste_sang[artist_index], True, (hoyre_tekst_farge))
                    hoyre_artist_rect = hoyre_artist_tekst.get_rect(center=(300, 400))
                    skjerm.blit(hoyre_artist_tekst, hoyre_artist_rect)
                    
                    hoyre_streams_tekst = tekst_font.render(forkort_streams(forste_sang[total_streams_index]), True, (hoyre_tekst_farge))
                    hoyre_streams_rect = hoyre_streams_tekst.get_rect(center=(300, 500))
                    skjerm.blit(hoyre_streams_tekst, hoyre_streams_rect)
                    
                    venstre_sang_tekst = tekst_font.render(andre_sang[sang_index], True, (venstre_tekst_farge))
                    venstre_sang_rect = venstre_sang_tekst.get_rect(center=(900, 300))
                    skjerm.blit(venstre_sang_tekst, venstre_sang_rect)
                    
                    venstre_artist_tekst = tekst_font.render(andre_sang[artist_index], True, (venstre_tekst_farge))
                    venstre_artist_rect = venstre_artist_tekst.get_rect(center=(900,400))
                    skjerm.blit(venstre_artist_tekst, venstre_artist_rect)
                    
                    venstre_streams_tekst = tekst_font.render("..?..", True, (venstre_tekst_farge))
                    venstre_streams_rect = venstre_streams_tekst.get_rect(center=(900,500))
                    skjerm.blit(venstre_streams_tekst, venstre_streams_rect)

                    skriv_tekst("høyre eller venstre?", tekst_font_mindre, (255, 255, 255), 600, 650)

                    if inst_rect.collidepoint(mouse_pos):
                        inst_farge = 0, 0, 255
                        if mouse_click[0]:
                            instillinger = True
                            gamemeny = False
                            timer_start = pyg.time.get_ticks()

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
                        neste_niva = True
                
                tid_etter_start = pyg.time.get_ticks()

                if tid_etter_start - timer_start >= 1000:

                    if (hoyre_sang_rect.collidepoint(mouse_pos) or 
                        hoyre_artist_rect.collidepoint(mouse_pos) or 
                        hoyre_streams_rect.collidepoint(mouse_pos)):
                        hoyre_tekst_farge = 200, 200, 200  
                        if mouse_click[0] and start_tekst: 
                            bruker_gjett = "h" 
                            start_tekst = False 
                    else:
                        hoyre_tekst_farge = 255, 255, 255

                    if (venstre_sang_rect.collidepoint(mouse_pos) or 
                        venstre_artist_rect.collidepoint(mouse_pos) or 
                        venstre_streams_rect.collidepoint(mouse_pos)):
                        venstre_tekst_farge = 200, 200, 200 
                        if mouse_click[0] and start_tekst: 
                            bruker_gjett = "l"  
                            start_tekst = False 
                    else:
                        venstre_tekst_farge = 255, 255, 255

            else: 
                if antall_riktig >= 5:
                    skriv_tekst("Bra jobba!", tekst_font, (0, 0, 0), 600, 300)
                    skriv_tekst(f"Du fikk {antall_riktig}/3 riktige", tekst_font, (0, 0, 0), 600, 400)
                elif 0 < antall_riktig < 5:
                    skriv_tekst(f"Du fikk bare {antall_riktig}/3 riktig", tekst_font, (0, 0, 0), 600, 400)
                else:
                    skriv_tekst("damn", tekst_font, (0, 0, 0), 600, 300)
                    skriv_tekst(f"du fikk ingen riktig", tekst_font, (0, 0, 0), 600, 400)
        else:
            #skriv settings in her
            ma_bare_ha_noe_her = 3

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False

    
   
pyg.mixer.music.load(game.music.mp3)
pyg.mixer.music.play(-1)


while run:  
    for event in pyg.event.get():     
        if event.type==pyg.quit():
            run = False

    pyg.display.update()

pyg.mixer.music.stop()

    pyg.display.update()

pyg.quit()
