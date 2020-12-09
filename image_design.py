from PIL import Image, ImageDraw, ImageFont
import time
import os

import birthday_scraper as bs
from data import colors
from data import font_colors

WIDTH = 1600
HEIGHT = 900
FONT = "fonts/SANFW___.TTF"
BOLD_GEORGIA = "fonts/georgiab.ttf"
GEORGIA = "fonts/georgia.ttf"
MAIN_FONT = ImageFont.truetype(FONT, 20)
SECOND_FONT = ImageFont.truetype(FONT, 17)
THIRD_FONT = ImageFont.truetype(FONT, 15)
FOURTH_FONT = ImageFont.truetype(FONT, 14)
GEORGIA_14 = ImageFont.truetype(GEORGIA, 14)
GEORGIA_15 = ImageFont.truetype(GEORGIA, 15)
BOLD_GEORGIA_13 = ImageFont.truetype(BOLD_GEORGIA, 13)
BOLD_GEORGIA_15 = ImageFont.truetype(BOLD_GEORGIA, 15)
BOTTOM_BORDER = 65
PIXEL_PER_ICON_X = WIDTH / 16
PIXEL_PER_ICON_Y = (HEIGHT - BOTTOM_BORDER) / 10
MARGIN_X = PIXEL_PER_ICON_X / 16
MARGIN_Y = PIXEL_PER_ICON_Y / 6
RADIUS = 9
DIAMETER = 2 * RADIUS
EXTRA_Y = 12

def create_raw_image(added_days):
    img = Image.new('RGB', (WIDTH, HEIGHT), color = colors[0])
    draw_primer_widgets(img, added_days)
    return img

def draw_primer_widgets(img, added_days):
    draw = ImageDraw.Draw(img)
    #name_label
    draw_box(draw, (0, -1), (3, 2), colors[1])
    draw.text((70 + 15, 28), "Smart wallpaper", font=SECOND_FONT, fill=font_colors[0])
    #date
    time_string = bs.get_time_string(added_days)
    draw_box(draw, (13, -1), (3, 2), colors[1])
    draw.text((1400, 15), "Letzter reload:", font=SECOND_FONT, fill=font_colors[0])
    draw.text((1400 - (len(time_string) + 1) * 2, 40), time_string, font=SECOND_FONT, fill=font_colors[0])
    #apps - left
    draw_box(draw, (0, 1), (3, 9), colors[1])
    #apps - top
    draw_box(draw, (5, -1), (6, 3), colors[1])
    #this semester
    draw_box(draw, (3, 9), (4, 1), colors[1])
    #freespace
    draw_box(draw, (7, 9), (8, 1), colors[1])
    #trashbin
    draw_box(draw, (15, 9), (1, 1), colors[1])
    #behind the news
    draw_box(draw, (13, 1), (3, 8), colors[1])

def draw_birthday_widgets(img, todays_list, num_events_today, months_list):
    draw = ImageDraw.Draw(img)
    #birhthdays
    draw_box(draw, (4, 3), (4, 5), colors[2], caption="Geburtstage")
    draw_box(draw, (4.1, 3.5), (3.8, 4.4), colors[3])
    draw_birthday_todays_list(draw, todays_list)
    draw_birthday_months_list(draw, months_list, num_events_today)
    return img

def draw_birthday_todays_list(draw, todays_list):
    pos_x1 = 435
    pos_x2 = 740
    pos_y = 310
    for entry in todays_list:
        draw.text((pos_x1, pos_y), entry[0], font=MAIN_FONT, fill=font_colors[2])
        draw.text((pos_x2, pos_y), entry[1], font=MAIN_FONT, fill=font_colors[2])
        pos_y = pos_y + 30

def draw_birthday_months_list(draw, months_list, num_events_today):
    pos_x1 = 435
    pos_x2 = 500
    pos_x3 = 600
    pos_y = 310
    if(num_events_today != 0):
        pos_y = pos_y + (num_events_today + 1) * 30
        line_offset = (num_events_today - 1) * 30
        draw.rectangle((410, 345 + line_offset, 790, 350 + line_offset), fill=colors[2])
    for entry in months_list:
        draw.text((pos_x1, pos_y), entry[0], font=THIRD_FONT, fill=font_colors[0])
        draw.text((pos_x2, pos_y), entry[1], font=THIRD_FONT, fill=font_colors[0])
        draw.text((pos_x3, pos_y), entry[2], font=THIRD_FONT, fill=font_colors[0])
        pos_y = pos_y + 25

def draw_finance_widgets(   img,
                            month_expences,
                            month_total,
                            month_str,
                            year_expences,
                            year_total,
                            year_str):
    draw = ImageDraw.Draw(img)
    #finance
    draw_box(draw, (8, 3), (4, 5), colors[2], caption="Finanzen")
    draw_box(draw, (8.1, 3.5), (3.8, 2.2), colors[3])
    draw_box(draw, (8.1, 5.7), (3.8, 2.2), colors[3])

    draw.text((1140, 218 + 83), month_str, font=BOLD_GEORGIA_13, fill=font_colors[1])
    draw_finance_month_list(draw, month_expences, month_total)

    draw.text((1129, 400 + 83), year_str, font=BOLD_GEORGIA_15, fill=font_colors[1])
    draw_finance_year_list(draw, year_expences, year_total)
    return img

def draw_finance_month_list(draw, expences, total):
    pos_x1 = 835
    pos_x2 = 990
    pos_x3 = 1080
    pos_y = 225 + 83
    for entry in expences:
        draw.text((pos_x1, pos_y), entry[0], font= FOURTH_FONT, fill=font_colors[0])
        draw_expence_value(draw, entry[2], pos_x2, pos_y - 5, 8, GEORGIA_14, "%")
        draw_expence_value(draw, entry[1], pos_x3 + 20, pos_y - 5, 8, GEORGIA_14, "€")
        pos_y = pos_y + 24

    draw.rectangle((pos_x1, pos_y, pos_x3 + 30, pos_y + 1), fill=font_colors[0])
    draw.text((pos_x1, pos_y + 13), total[0], font= THIRD_FONT, fill=font_colors[0])
    draw_expence_value(draw, total[1], pos_x3 + 20, pos_y + 9, 10, GEORGIA_15, "€")

def draw_finance_year_list(draw, expences, total):
    pos_x1 = 835
    pos_x2 = 990
    pos_x3 = 1080
    pos_y = 409 + 83
    for entry in expences:
        draw.text((pos_x1, pos_y), entry[0], font= FOURTH_FONT, fill=font_colors[0])
        draw_expence_value(draw, entry[2], pos_x2, pos_y - 5, 8, GEORGIA_14, "%")
        draw_expence_value(draw, entry[1], pos_x3 + 20, pos_y - 5, 8, GEORGIA_14, "€")
        pos_y = pos_y + 24

    draw.rectangle((pos_x1, pos_y, pos_x3 + 30, pos_y + 1), fill=font_colors[0])
    draw.text((pos_x1, pos_y + 13), total[0], font= THIRD_FONT, fill=font_colors[0])
    draw_expence_value(draw, total[1], pos_x3 + 20, pos_y + 9, 10, GEORGIA_15, "€")

def draw_expence_value(draw, value_str, pos_x, pos_y, offset, custom_font, trailer):
    index = len(value_str)
    while(index >= 0):
        if(index == len(value_str)):
            draw.text((pos_x, pos_y), trailer, font=custom_font, fill=font_colors[0])
        else:
            draw.text((pos_x, pos_y), value_str[index], font=custom_font, fill=font_colors[0])
        pos_x = pos_x - offset
        index = index - 1

def draw_news_widgets(img, headline_list):
    draw = ImageDraw.Draw(img)
    #news
    draw_box(draw, (13, 1), (3, 8), colors[2], caption="Nachrichten")
    draw_box(draw, (13.1, 1.5), (2.8, 1.85), colors[3])
    draw_box(draw, (13.1, 3.35), (2.8, 1.85), colors[3])
    draw_box(draw, (13.1, 5.2), (2.8, 1.85), colors[3])
    draw_box(draw, (13.1, 7.05), (2.8, 1.85), colors[3])
    draw_headline_list(draw, headline_list)
    return img

def draw_headline_list(draw, headline_list):
    pos_x = 1330
    pos_y = 140
    for i in range(4):
        comp_headline = compress_headline(headline_list[i])
        draw.text((pos_x, pos_y), comp_headline, font=THIRD_FONT, fill=font_colors[0])
        pos_y = pos_y + 155

def compress_headline(headline):
    splitted_words = headline.split(" ")
    comp_headline = ""
    row_len = -1
    for word in splitted_words:
        if(row_len + len(word) + 1 <= 30):
            comp_headline = comp_headline + word + " "
            row_len = row_len + len(word) + 1
        else:
            comp_headline = comp_headline + "\n\n" + word + " "
            row_len = len(word)
    return comp_headline

def draw_weather_widgets(img, weather_list):
    draw = ImageDraw.Draw(img)
    #today
    draw_box(draw, (3, -1), (2, 2), colors[2])
    draw_box(draw, (3.1, -0.5), (1.8, 1.4), colors[3])
    draw.text((425 - len(weather_list[0]) * 2, 22), weather_list[0], font=GEORGIA_15, fill=font_colors[0])
    if(weather_list[1] != None):
        weather_icon = Image.open("weather/icons/" + weather_list[1], "r")
        weather_icon = weather_icon.resize((45, 45), Image.ANTIALIAS)
        img.paste(weather_icon, (340, 8), weather_icon)
    #sunrise/sunset
    if(weather_list[2] != None and weather_list[3] != None):
        draw_box(draw, (11, -1), (2, 2), colors[2])
        draw_box(draw, (11.1, -0.5), (1.8, 1.4), colors[3])
        #sunrise
        sunrise_icon = Image.open("weather/icons/sunrise.png", "r")
        sunrise_icon = sunrise_icon.resize((39, 26), Image.ANTIALIAS)
        img.paste(sunrise_icon, (1140, 5), sunrise_icon)
        draw.text((1225 - len(weather_list[2]) * 2, 8), weather_list[2], font=GEORGIA_15, fill=font_colors[0])
        #sunset
        sunset_icon = Image.open("weather/icons/sunset.png", "r")
        sunset_icon = sunset_icon.resize((39, 26), Image.ANTIALIAS)
        img.paste(sunset_icon, (1140, 35), sunset_icon)
        draw.text((1225 - len(weather_list[3]) * 2, 38), weather_list[3], font=GEORGIA_15, fill=font_colors[0])
    return img
    
def draw_box(draw, pos, size, fill_color, caption=None):
    top = pos[1] * PIXEL_PER_ICON_Y
    left = pos[0] * PIXEL_PER_ICON_X
    right = left + size[0] * PIXEL_PER_ICON_X
    bottom = top + (size[1] + 1) * PIXEL_PER_ICON_Y
    draw.ellipse((left + MARGIN_X, top + MARGIN_Y - EXTRA_Y, left + MARGIN_X + DIAMETER, top + MARGIN_Y + DIAMETER - EXTRA_Y), fill=fill_color)
    draw.ellipse((right - MARGIN_X - DIAMETER, top + MARGIN_Y - EXTRA_Y, right - MARGIN_X, top + MARGIN_Y + DIAMETER - EXTRA_Y), fill=fill_color)
    draw.ellipse((left + MARGIN_X, bottom - MARGIN_Y - DIAMETER - BOTTOM_BORDER - EXTRA_Y, left + MARGIN_X + DIAMETER, bottom - MARGIN_Y - BOTTOM_BORDER - EXTRA_Y), fill=fill_color)
    draw.ellipse((right - MARGIN_X - DIAMETER, bottom - MARGIN_Y - DIAMETER - BOTTOM_BORDER - EXTRA_Y, right - MARGIN_X, bottom - MARGIN_Y - BOTTOM_BORDER - EXTRA_Y), fill=fill_color)
    draw.rectangle((left + MARGIN_X + RADIUS, top + MARGIN_Y - EXTRA_Y, right - MARGIN_X - RADIUS, bottom - MARGIN_Y - BOTTOM_BORDER - EXTRA_Y), fill=fill_color)
    draw.rectangle((left + MARGIN_X, top + MARGIN_Y + RADIUS - EXTRA_Y, right - MARGIN_X, bottom - MARGIN_Y - RADIUS - BOTTOM_BORDER - EXTRA_Y), fill=fill_color)
    if(caption!=None):
        half_caption_width = (len(caption) + 1) * 4
        draw.text((left + (right - left) / 2 - half_caption_width, top + PIXEL_PER_ICON_Y / 5.5), caption, font=MAIN_FONT, fill=font_colors[0])