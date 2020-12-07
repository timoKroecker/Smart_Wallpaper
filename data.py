#----------------------------------------------------------------
#                          VARIABLE DATA
#----------------------------------------------------------------

birthdays =     [
                    [20, 8, 1966, "Mom"],
                    [28, 11, 1965, "Dad"],
                    [3, 4, 0, "Yvonne Meier"],
                    [7, 11, 1962, "Jan Meier"],
                    [4, 1, 1987, "Daisy"],
                    [13, 3, 2019, "Nelly Meier"],
                    [30, 12, 0, "Mireya Ortega Bajaña"],
                    [29, 8, 0, "Greet Meier"],
                    [13, 2, 0, "Oma Kröcker"],
                    [20, 10, 1970, "Peter Kröcker"],
                    [9, 10, 1989, "Manu Mierau"],
                    [5, 9, 1992, "Tobi Mierau"],
                    [16, 5, 1994, "Jenny Martini"],
                    [16, 5, 1986, "Larissa Schulze"],

                    [3, 1, 1996, "Raphy Beldzik"],
                    [21, 12, 1995, "Micha Kolb"],
                    [9, 2, 1997, "Sarah Plenio"],
                    [16, 5, 1992, "Johannes Stabenow"],
                    [20, 9, 1996, "Anni Schütz"],
                    [14, 9, 1988, "Flo Banhardt"],
                    [9, 6, 1992, "Judy Banhardt"],
                    [31, 7, 1992, "Solomon Gavrilla"],

                    [25, 8, 1996, "Fabian Thomas-Barein"],
                    [12, 12, 1996, "Moritz Riehn"],
                    [31, 12, 1996, "Nikola Cvisic"],
                    [25, 7, 1996, "Adrian Lück"],

                    [21, 6, 1997, "Mahmoud AbuIsaac"],
                    [10, 2, 0, "Mohammed Al Ahmad"],
                    [4, 12, 0, "Anas Asad"],
                    [13, 11, 0, "Hadhemi Sekri"],
                    [9, 3, 1996, "Pavel Boodo"],
                    [2, 5, 0, "Boris Kamdem Taffo"],
                    [9, 4, 0, "Orelle"],
                    [12, 12, 1997, "Marcel Achner"],
                    [10, 9, 0, "Lascha Lobjanidze"],
                    [3, 11, 1998, "Meruna Yugarajah"],
                    [15, 8, 1995, "Minh Quan Nguyen"],
                    [2, 12, 0, "Hercules"],

                    [31, 8, 1996, "Eva Martens"],
                    [24, 5, 0, "Dave Lüttmann"],
                    [13, 7, 0, "Philipp Breuer"],
                    [14, 7, 1998, "Nijat Dilshat"]
                ]

mothersday =    [
                    [10, 5, 2020],
                    [9, 5, 2021],
                    [8, 5, 2022],
                    [14, 5, 2023],
                    [12, 5, 2024],
                    [11, 5, 2025],
                    [10, 5, 2026],
                    [9, 5, 2027],
                    [14, 5, 2028],
                    [13, 5, 2029]
                ]

fathersday =    [
                    [21, 5, 2020],
                    [13, 5, 2021],
                    [26, 5, 2022],
                    [18, 5, 2023],
                    [9, 5, 2024],
                    [29, 5, 2025],
                    [14, 5, 2026],
                    [6, 5, 2027],
                    [25, 5, 2028],
                    [10, 5, 2029]
                ]

positive_keywords_1 =   [
                            "münchen", "gießen", "amsterdam", "ludwigsburg", "nürnberg", "erlangen",
                            "amok", "amoklauf", "unfall", "katastrophe", "todesfälle", "tote", "impfpflicht", "putin",
                            "wahl", "flüchtlinge", "flüchtlingslager", "schock", "terror", "angriff", "angst",
                            "klima", "biden", "harris", "niederlande", "trump", "präsident",
                            "militär", "krieg", "syrien", "feuer", "obama", "unfall", "trauer", "lockdown",
                            "kliniken", "krankenhäuser", "pfleger", "proteste"
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
                            "flat", "trainer", "bundesliga", "tipps", "deals", "tricks", "treffer"
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
                            ["1_geburtstage", "\ntt<TAB>mm<TAB>jj<TAB>Name<ENTER> (0 wenn jj unbekannt)"],
                            ["2_muttertage", "\ntt<TAB>mm<TAB>jj<ENTER>"],
                            ["3_vatertage", "\ntt<TAB>mm<TAB>jj<ENTER>"]
                        ]

news_soup_ingredients = [
                            ["https://www.rt1.de/nachrichten/augsburg/", "h3", "headline", " -rt1/aux", 5],
                            ["https://focus.de", "h4", "vr", " -Focus", 30],
                            ["https://www.spiegel.de/", "span", "hover:opacity-moderate focus:opacity-moderate", " -Spiegel", 30],
                            ["https://n-tv.de", "span", "teaser__headline", " -ntv", 30],
                            ["https://www.welt.de/", "div", "o-headline o-teaser__headline c-dreifaltigkeit__headline c-teaser-default__headline", " -Welt", 30]
                        ]

unwanted_characters =   ["\n"]

expence_categories =    [
                            ["1_fixkosten", "Fixkosten"],
                            ["2_lebensmittel", "Lebensmittel"],
                            ["3_haushalt", "Haushalt"],
                            ["4_freizeit", "Freizeit"],
                            ["5_transport", "Transport"]
                        ]

weather_descriptions =  [
                            ["Sonnig"],                                     #confirmed
                            ["Wolkig"],                                     #confirmed
                            ["Bedeckt"],                                    #confirmed
                            ["Stark bewölkt", "Schauer in der Nähe"],       #confirmed
                            ["Nebel"],                                      #confirmed
                            ["Leichter Regen"],                             #confirmed
                            ["Regen", "Regenschauer"],                                      #confirmed
                            ["Schneefall"],
                            ["Gewitter"]
                        ]