from bs4 import BeautifulSoup
import requests
import re

from data import positive_keywords_1 as pk1
from data import positive_keywords_2 as pk2
from data import negative_keywords_1 as nk1
from data import negative_keywords_2 as nk2
from data import news_soup_ingredients as ingr
from data import unwanted_characters as unwntd

def scrape_news_headlines(print_on=False):
    scored_selections = []
    for i in range(len(ingr)):
        scored_selections.append(cook_soup(i))
    if(scored_selections[0] == None):
        return None

    total_scored_selection = scored_selections[0]
    for i in range(len(scored_selections) - 1):
        if(scored_selections[i + 1] != None):
            total_scored_selection = total_scored_selection + scored_selections[i + 1]

    total_ranked_selection = get_ranked_selection(total_scored_selection, print_on)
    return total_ranked_selection

def cook_soup(index):
    req = None
    try:
        req = requests.get(ingr[index][0])
    except:
        return None
    soup = BeautifulSoup(req.text, 'lxml')
    matches = soup.find_all(ingr[index][1], class_=ingr[index][2])
    if(len(matches) == 0):
        matches = soup.find_all(ingr[index][1], itemprop=ingr[index][2])
    if(len(matches) == 0):
        matches = soup.find_all(ingr[index][1], itemprop_=ingr[index][2])
    return get_scored_selection(matches, ingr[index][3], ingr[index][4])

def get_scored_selection(matches, source, num_headlines):
    selection = []
    while(len(selection) < num_headlines):
        headline = matches.pop(0).text
        headline = remove_spiegel_timestamp(headline)
        headline = remove_unwanted_characters(headline)
        if(len(headline) > 30 and len(headline) < 90 and not contains_headline(headline, selection, source)):
            score = calculate_headline_score(headline.lower())
            entry = []
            entry.append(headline + source)
            entry.append(score)
            selection.append(entry)
    return selection

def calculate_headline_score(headline):
    score = 0
    splitted_headline = re.findall(r"[\w']+", headline)
    for word in splitted_headline:
        if(contains_word(word, pk1)):
            score = score + 3
        elif(contains_word(word, pk2)):
            score = score + 1
        elif(contains_word(word, nk1)):
            score = score - 3
        elif(contains_word(word, nk2)):
            score = score - 1
    return score

def contains_word(elem, array):
    for entry in array:
        if(elem == entry):
            return True
    return False

def contains_headline(elem, array, source):
    for entry in array:
        if(elem + source == entry[0]):
            return True
    return False

def get_ranked_selection(selection, print_on):
    ranked_selection = []
    while(len(selection) != 0):
        index = get_index_w_best_score(selection)
        if(print_on):
            print(str(selection[index][1]) + "   " + selection[index][0])
        ranked_selection.append(selection.pop(index)[0])
    return ranked_selection

def get_index_w_best_score(selection):
    maximum = -100
    index = -1
    for i in range(len(selection)):
        if(selection[i][1] > maximum):
            maximum = selection[i][1]
            index = i
    return index

def remove_unwanted_characters(headline):
    for char in unwntd:
        headline = headline.replace(char, "")
    return headline

def remove_spiegel_timestamp(headline):
    index = 0
    for i in range(len(headline)):
        timestamp_caught = False
        if( len(headline) - i <= 14 and
            i + 4 <= len(headline) and
            headline[i] == "V" and
            headline[i + 1] == "o" and
            headline[i + 2] == "r" and
            headline[i + 3] == " "):

            try:
                int(headline[i + 4])
                timestamp_caught = True
                index = i
            except:
                pass
        if(timestamp_caught):
            return headline[0:index]
    return headline

#------------------------TESTS------------------------------------

def test_soup(index):
    req = None
    try:
        req = requests.get(ingr[index][0])
    except:
        return None
    soup = BeautifulSoup(req.text, 'lxml')
    matches = soup.find_all(ingr[index][1], itemprop=ingr[index][2])
    sel = get_scored_selection(matches, ingr[index][3], ingr[index][4])
    sel = get_ranked_selection(sel, True)

#test_soup(0)

#scrape_news_headlines(print_on=True)