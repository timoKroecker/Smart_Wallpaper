#----------------------------------------------------------------
#                          VARIABLE DATA
#----------------------------------------------------------------

positive_keywords_1 =   [
                            "münchen", "gießen", "amsterdam", "ludwigsburg", "nürnberg", "erlangen",
                            "amok", "amoklauf", "unfall", "katastrophe", "tote", "impfpflicht", "putin",
                            "wahl", "flüchtlinge", "flüchtlingslager", "schock", "terror", "angriff", "angst",
                            "klima", "biden", "harris", "niederlande", "trump", "präsident",
                            "militär", "krieg", "syrien", "feuer", "brand", "obama", "unfall", "trauer", "lockdown",
                            "kliniken", "krankenhäuser", "pfleger", "proteste", "inzidenz",
                            "flut", "überflutung"
                        ]

positive_keywords_2 =   [
                            "streik", "rekord", "pflicht", "studium", "eu", "europa", "nato", "un", "truppen",
                            "impfstoff", "impfung", "impfen", "schwer", "verletzt", "verletzte",
                            "rassismus", "rasse", "demonstration", "demonstrationen", "gesetz", "corona",
                            "empörung", "elon", "musk", "geld", "tesla", "spacex", "hyperloop", "söder",
                            "polizei", "polizist", "gesundheit", "verwirrung", "usa", "us", "krise",
                            "kohle", "antisemitismus", "extremismus", "b17", "a8", "merkel", "spahn", "virus"
                        ]

negative_keywords_1 =   [
                            "chance", "gewinnen", "angebot", "preis", "preise", "billig", "shopping", "shoppen"
                            "günstig", "günstige", "günstiger", "dreamdate", "bachelor", "bachelorette", "gutschein",
                            "gutscheine", "schnäppchen", "schnäppchenjagd", "sparen", "bvb", "fc", "fußball",
                            "club", "gewinnt", "tore", "spiel", "liga", "championsleague", "zutaten", "reiseziele",
                            "sat1", "pro7", "rtl", "tv", "flirt", "beziehung", "porno", "sex", "dhl", "wm", "em",
                            "flat", "trainer", "bundesliga", "tipps", "deals", "tricks", "treffer", "geschenk", "geschenke",
                            "bayern", "rabatt"
                        ]

negative_keywords_2 =   [
                            "verliert", "empfehlung", "empfehlungen", "test", "finden", "live", "lanz",
                            "aktie", "aktien", "wetter", "euro", "fit", "führt"
                        ]

#----------------------------------------------------------------
#                            FIXED DATA
#----------------------------------------------------------------

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
                    ["01_januar", "JAN"],
                    ["02_februar", "FEB"],
                    ["03_märz", "MRZ"],
                    ["04_april", "APR"],
                    ["05_mai", "MAI"],
                    ["06_juni", "JUN"],
                    ["07_juli", "JUL"],
                    ["08_august", "AUG"],
                    ["09_september", "SEP"],
                    ["10_oktober", "OKT"],
                    ["11_november", "NOV"],
                    ["12_dezember", "DEZ"]
                ]

colors =        [
                    (38, 38, 38),               #background
                    (10, 10, 10),               #icon_frames
                    (0, 45, 90),                #darkblue
                    (0, 68, 136)                #mediumblue
                ]

font_colors =   [
                    (200, 200, 200),            #white/ish
                    (0, 45, 90),                #blue
                    (255,215,0)                 #gold
                ]

birthdays_categories =  [
                            ["1_geburtstage", "\ntt<TAB>mm<TAB>jj<TAB>Name<ENTER> (0 wenn jj unbekannt)"]
                        ]

news_soup_ingredients = [
                            ["https://focus.de", "h4", "vr", " -Focus", 30],
                            ["https://www.spiegel.de/", "span", "hover:opacity-moderate focus:opacity-moderate", " -Spiegel", 30],
                            ["https://n-tv.de", "span", "teaser__headline", " -ntv", 30],
                            ["https://www.welt.de/", "div", "o-headline o-teaser__headline c-dreifaltigkeit__headline c-teaser-default__headline", " -Welt", 30]
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
                            ["Sonnig", "Klar"],                             #confirmed
                            ["Wolkig", "Heiter"],                           #confirmed
                            ["Bedeckt"],                                    #confirmed
                            ["Stark bewölkt", "Schauer in der Nähe"],       #confirmed
                            ["Nebel", "Feuchter Dunst"],                    #confirmed
                            ["Leichter Regen"],                             #confirmed
                            ["Regen", "Regenschauer"],                      #confirmed
                            ["Schneefall", "Schneeschauer", "Schneeregen"], #confirmed
                            ["Gewitter"]
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
                                    ["Erlangen", "ErlangenStadt"],
                                    ["Nürnberg", "NürnbergStadt"],
                                    ["Fürth", "FürthStadt"],
                                    ["Augsburg", "AugsburgStadt"],
                                    ["München", "MünchenStadt"]
                                ]