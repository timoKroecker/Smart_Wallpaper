weekdays =      [
                    ["MO", "Montag"],
                    ["DI", "Dienstag"],
                    ["MI", "Mittwoch"],
                    ["DO", "Donnerstag"],
                    ["FR", "Freitag"],
                    ["SA", "Samstag"],
                    ["SO", "Sonntag"]
                ]

months =        [
                    ["Januar", "JAN"],
                    ["Februar", "FEB"],
                    ["März", "MRZ"],
                    ["April", "APR"],
                    ["Mai", "MAI"],
                    ["Juni", "JUN"],
                    ["Juli", "JUL"],
                    ["August", "AUG"],
                    ["September", "SEP"],
                    ["Oktober", "OKT"],
                    ["November", "NOV"],
                    ["Dezember", "DEZ"]
                ]

backup_colors =        [
                    (38, 38, 38),               #background
                    (10, 10, 10),               #icon_frames
                    (0, 45, 90),                #darkblue
                    (0, 68, 136)                #mediumblue
                ]

colors =        [
                    (10, 10, 30),               #background
                    (20, 20, 60),               #icon_frames
                    (30, 30, 90),               #icon_frames_2
                    (15, 15, 45)                #icon_frames_3
                ]

font_colors =   [
                    (200, 200, 200),            #white/ish
                    (0, 0, 0),                  #background
                    (255,215,0),                #gold
                    (40, 40, 120),              #icon_frames_2
                    (250, 125, 0)               #orange
                ]

birthdays_categories =  [
                            ["1_geburtstage", "\ntt<TAB>mm<TAB>jj<TAB>Name<ENTER> (0 wenn jj unbekannt)"]
                        ]

news_soup_ingredients = [
                            ["https://focus.de", "h3", "", " -Focus", 30],
                            ["https://www.spiegel.de/", "span", "hover:opacity-moderate focus:opacity-moderate", " -Spiegel", 30],
                            ["https://n-tv.de", "span", "teaser__headline", " -ntv", 30],
                            ["https://www.welt.de/", "h4", "c-teaser__headline", " -Welt", 30]
                        ]

backup = ["https://www.tagesschau.de/", "span", "teaser__headline", " -Tagesschau", 30]

unwanted_characters =   ["\n", "+"]

expence_categories =    [
                            ["1_fixkosten", "Fixkosten"],
                            ["2_lebensmittel", "Lebensmittel"],
                            ["3_haushalt", "Haushalt"],
                            ["4_freizeit", "Freizeit"],
                            ["5_transport", "Transport"]
                        ]

weather_descriptions =  [
                            ["Sonnig", "Klar"],
                            ["Wolkig", "Heiter"],
                            ["Bedeckt"],
                            ["Stark bewölkt", "Schauer in der Nähe"],
                            ["Nebel", "Feuchter Dunst"],
                            ["Leichter Regen", "Sprühregen"],
                            ["Regen", "Regenschauer"],
                            ["Schneefall", "Schneeschauer", "Schneeregen"],
                            ["Gewitter", "Schweres Gewitter", "Leichter Regen mit Gewitter"]
                        ]

calendar_categories =   [
                            ["1_termine", "\ntt<TAB>mm<TAB>jj<TAB>Name<ENTER>"],
                            ["2_muttertage", "\ntt<TAB>mm<TAB>jj<ENTER>"],
                            ["3_vatertage", "\ntt<TAB>mm<TAB>jj<ENTER>"]
                        ]

text_file_header =      [
                            "+++++++++++++++++++++\n",
                            "\n+++++++++++++++++++++\n\n|||||||||||||||||||||\nvvvvvvvvvvvvvvvvvvvvv\n"
                        ]

incidents_soup_broth =  "https://www.lgl.bayern.de/gesundheit/infektionsschutz/infektionskrankheiten_a_z/coronavirus/karte_coronavirus/#uebersicht"

incidents_soup_ingredients =    [
                                    ["Erlangen", "Stadt"],
                                    ["Nürnberg", "Stadt"],
                                    ["Fürth", "Stadt"],
                                    ["Augsburg", "Stadt"],
                                    ["München", "Stadt"]
                                ]

incidents_colors =      [
                            [(170, 60, 60), (255, 90, 90)],      #red
                            [(149, 60, 170), (224, 90, 255)],    #purple
                            [(47, 146, 170), (71, 219, 255)],    #cyan
                            [(47, 170, 52), (71, 255, 78)],      #green
                            [(170, 159, 50), (255, 239, 75)]     #yellow
                        ]

bar_colors =    [
                    (170,143,0),    #orange1
                    (225,189,106)    #orange2
                ]