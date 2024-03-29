from PIL import Image, ImageDraw, ImageFont
import math

import birthday_scraper as bs
from data import colors
from data import font_colors
from data import incidents_colors

WIDTH = 1600
HEIGHT = 900
FONT = "fonts/SANFW___.ttf"
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
PIXEL_PER_ICON_Y = (HEIGHT - BOTTOM_BORDER) / 10 + 4
MARGIN_X = PIXEL_PER_ICON_X / 16
MARGIN_Y = PIXEL_PER_ICON_Y / 6
RADIUS = 9
DIAMETER = 2 * RADIUS
EXTRA_Y = -10
PLOT_BOX_ROW_HEIGHT = 500

def create_raw_image(added_days):
    img = Image.new('RGB', (WIDTH, HEIGHT), color = colors[0])
    draw_primer_widgets(img, added_days)
    return img

def draw_primer_widgets(img, added_days):
    draw = ImageDraw.Draw(img)
    #name_label
    draw_box(draw, (0, 9.5), (5, 1), colors[1]) 
    #date
    draw_box(draw, (11, 9.5), (5, 1), colors[1]) 
    time_string = bs.get_time_string(added_days)
    draw.text((1240 - (len(time_string) + 1) * 2, 870), "Letzter reload: " + time_string, font=SECOND_FONT, fill=font_colors[0])
    #main folders
    draw_box(draw, (5, 8), (6, 1), colors[1]) 

def draw_calendar_widgets(img, todays_list, num_events_today, months_list):
    draw = ImageDraw.Draw(img)
    draw_content_box(draw, (0, 0), (4, 9.5), "Kalendar")

    draw_todays_calendar_list(draw, todays_list, 35, 86)
    draw_extended_list(draw, months_list, num_events_today, 35, 100, 170, 86)

    return img

def draw_todays_calendar_list(draw, todays_list, pos_x1, pos_y):
    for entry in todays_list:
        draw.text((pos_x1, pos_y), entry, font=MAIN_FONT, fill=font_colors[2])
        pos_y = pos_y + 30

def draw_birthday_widgets(img, todays_list, num_events_today, months_list):
    draw = ImageDraw.Draw(img)
    draw_content_box(draw, (4, 0), (4, 4.5), "Geburtstage")
    draw_todays_birthday_list(draw, todays_list, 435, 740, 86)
    draw_extended_list(draw, months_list, num_events_today, 435, 500, 600, 86)
    return img

def draw_todays_birthday_list(draw, todays_list, pos_x1, pos_x2, pos_y):
    for entry in todays_list:
        draw.text((pos_x1, pos_y), entry[0], font=MAIN_FONT, fill=font_colors[2])
        draw.text((pos_x2, pos_y), entry[1], font=MAIN_FONT, fill=font_colors[2])
        pos_y = pos_y + 30

def draw_extended_list(draw, months_list, num_events_today, pos_x1, pos_x2, pos_x3, pos_y, extra_x = -5):
    if(num_events_today != 0):
        pos_y = pos_y + (num_events_today + 1) * 30 - 8
        draw.rectangle((pos_x1 - 25 - extra_x, pos_y - 20, pos_x1 + 355 + extra_x, pos_y - 15), fill=colors[2])
    for entry in months_list:
        draw.text((pos_x1, pos_y), entry[0], font=THIRD_FONT, fill=font_colors[0])
        draw.text((pos_x2, pos_y), entry[1], font=THIRD_FONT, fill=font_colors[0])
        if(len(entry[2]) > 25):
            string_array = compress(entry[2], line_length=25)
            for line in string_array:
                draw.text((pos_x3, pos_y), line, font=THIRD_FONT, fill=font_colors[0])
                pos_y = pos_y + 25
            pos_y = pos_y - 25
        else:
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
    draw_content_box(draw, (8, 0), (4, 4.5), "Finanzen")

    draw.text((1140, 80), month_str, font=BOLD_GEORGIA_13, fill=font_colors[3])
    draw_finance_month_list(draw, month_expences, month_total)

    draw.rectangle((815, 232, 1185, 237), fill=colors[2])

    draw.text((1129, 370), year_str, font=BOLD_GEORGIA_15, fill=font_colors[3])
    draw_finance_year_list(draw, year_expences, year_total)
    return img

def draw_finance_month_list(draw, expences, total):
    pos_x1 = 835
    pos_x2 = 990
    pos_x3 = 1080
    pos_y = 85
    for entry in expences:
        draw.text((pos_x1, pos_y), entry[0], font= FOURTH_FONT, fill=font_colors[0])
        draw_expence_value(draw, entry[2], pos_x2, pos_y - 5, 8, GEORGIA_14, "%")
        draw_expence_value(draw, entry[1], pos_x3 + 20, pos_y - 5, 8, GEORGIA_14, "€")
        pos_y = pos_y + 22

    draw.rectangle((pos_x1, pos_y, pos_x3 + 30, pos_y + 1), fill=font_colors[0])
    draw.text((pos_x1, pos_y + 13), total[0], font= THIRD_FONT, fill=font_colors[0])
    draw_expence_value(draw, total[1], pos_x3 + 20, pos_y + 9, 10, GEORGIA_15, "€")

def draw_finance_year_list(draw, expences, total):
    pos_x1 = 835
    pos_x2 = 990
    pos_x3 = 1080
    pos_y = 250
    for entry in expences:
        draw.text((pos_x1, pos_y), entry[0], font= FOURTH_FONT, fill=font_colors[0])
        draw_expence_value(draw, entry[2], pos_x2, pos_y - 5, 8, GEORGIA_14, "%")
        draw_expence_value(draw, entry[1], pos_x3 + 20, pos_y - 5, 8, GEORGIA_14, "€")
        pos_y = pos_y + 22

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
    draw_content_box(draw, (12, 0), (4, 5), "Nachrichten")
    draw_headline_list(draw, headline_list)
    return img

def draw_headline_list(draw, headline_list):
    pos_x = 1235
    pos_y_array = [86]
    for i in range(3):
        pos_y_array.append(pos_y_array[-1] + 90)
    for i in range(4):
        pos_y = pos_y_array[i]
        comp_headline = compress(headline_list[i], line_length=40)
        for line in comp_headline:
            draw.text((pos_x, pos_y), line, font=THIRD_FONT, fill=font_colors[0])
            pos_y = pos_y + 25

def compress(string, line_length=30):
    splitted_words = string.split(" ")
    string_array = []
    comp_line = ""
    row_len = -1
    for word in splitted_words:
        if(row_len + len(word) + 1 <= line_length):
            comp_line = comp_line + word + " "
            row_len = row_len + len(word) + 1
        else:
            string_array.append(comp_line)
            comp_line = word + " "
            row_len = len(word)
    string_array.append(comp_line)
    return string_array

def draw_weather_widgets(img, weather_list):
    draw = ImageDraw.Draw(img)

    draw.text((113 - len(weather_list[0]) * 2, 868), weather_list[0], font=GEORGIA_15, fill=font_colors[0])
    if(weather_list[1] != None):
        weather_icon = Image.open("weather/icons/" + weather_list[1], "r")
        weather_icon = weather_icon.resize((33, 33), Image.ANTIALIAS)
        img.paste(weather_icon, (43, 860), weather_icon)
    #sunrise/sunset
    if(weather_list[2] != None and weather_list[3] != None):
        #sunrise
        sunrise_icon = Image.open("weather/icons/sunrise.png", "r")
        sunrise_icon = sunrise_icon.resize((39, 26), Image.ANTIALIAS)
        img.paste(sunrise_icon, (193, 863), sunrise_icon)
        draw.text((263 - len(weather_list[2]) * 2, 868), weather_list[2], font=GEORGIA_15, fill=font_colors[0])
        #sunset
        sunset_icon = Image.open("weather/icons/sunset.png", "r")
        sunset_icon = sunset_icon.resize((39, 26), Image.ANTIALIAS)
        img.paste(sunset_icon, (353, 866), sunset_icon)
        draw.text((423 - len(weather_list[3]) * 2, 868), weather_list[3], font=GEORGIA_15, fill=font_colors[0])

    return img

def draw_incidents_widgets(img, incidents_list, incidents_plot_cube):
    draw = ImageDraw.Draw(img)
    max_y = get_max_y_from_incidents(incidents_plot_cube)
    rows = int(math.ceil(max_y / PLOT_BOX_ROW_HEIGHT))
    draw_content_box(draw, (4, 4.5), (8, 3.5), "Inzidenzen")
    draw_plot_box(draw, (4.2, 5.125), (5.5, 2.650), rows, colors[3], colors[2])
    plot_incidences(draw, (4.2, 5.125), (5.5, 2.650), incidents_plot_cube, max_y, rows)

    pos_x1 = 995
    pos_x2 = 1155
    pos_y = 502
    iterator = 0
    for entry in incidents_list:
        draw.text((pos_x1, pos_y), entry[0], font= FOURTH_FONT, fill=incidents_colors[iterator][1])
        draw_expence_value(draw, entry[1], pos_x2, pos_y - 5, 8, GEORGIA_14, "")
        pos_y = pos_y + 40
        iterator = iterator + 1
    
    return img

def get_max_y_from_incidents(incidents_plot_cube):
    max_value = 0.0
    for matrix in incidents_plot_cube:
        for row in matrix:
            if(max_value < row[4]):
                max_value = row[4]
    return max_value

def draw_content_box(draw, pos, size, caption = None):
    draw_box(draw, pos, size, colors[1], caption=caption)
    draw_box(draw, (pos[0] + 0.05, pos[1] + 0.45), (size[0] - 0.1, size[1] - 0.5), colors[2])
    draw_box(draw, (pos[0] + 0.1, pos[1] + 0.5), (size[0] - 0.2, size[1] - 0.6), colors[1])

def plot_incidences(draw, pos, size, incidents_plot_cube, max_y, rows):
    top = pos[1] * PIXEL_PER_ICON_Y + MARGIN_Y - EXTRA_Y
    left = pos[0] * PIXEL_PER_ICON_X + MARGIN_X + RADIUS
    right = left + size[0] * PIXEL_PER_ICON_X - MARGIN_X *2 - RADIUS * 2
    bottom = top + size[1] * PIXEL_PER_ICON_Y - 6
    height = bottom - top
    width = right - left
    height_partition = height / (PLOT_BOX_ROW_HEIGHT * rows)
    width_partition = width / (len(incidents_plot_cube) - 1)
    radius = 1
    for city_iterator in range(5):
        is_successor = True
        prev_bounds = None
        day_iterator = 0
        for matrix in incidents_plot_cube:
            if(len(matrix) == 0):
                is_successor = False
            else:
                incidents_height = int(matrix[len(matrix) - city_iterator - 1][4]) * height_partition - 2
                left_bound = left + day_iterator * width_partition - radius
                bottom_bound = bottom - incidents_height + radius
                top_bound = bottom_bound - radius * 2
                right_bound = left_bound + radius * 2
                plot_partial_line(draw, [left_bound, top_bound, right_bound, bottom_bound], prev_bounds, incidents_colors[len(matrix) - city_iterator - 1][0], is_successor)
                prev_bounds = [left_bound, top_bound, right_bound, bottom_bound]
                is_successor = True
            day_iterator = day_iterator + 1

def plot_partial_line(draw, current_bounds, prev_bounds, color, is_successor):
    if(prev_bounds == None):
        return
    if(not is_successor):
        color = (150, 150, 150)
    steps = 100
    left_step = (current_bounds[0] - prev_bounds[0]) / steps
    top_step = (current_bounds[1] - prev_bounds[1]) / steps
    right_step = (current_bounds[2] - prev_bounds[2]) / steps
    bottom_step = (current_bounds[3] - prev_bounds[3]) / steps
    draw.ellipse((prev_bounds[0], prev_bounds[1], prev_bounds[2], prev_bounds[3]), fill=color)
    for i in range(steps):
        current_left = prev_bounds[0] + left_step * i
        current_top = prev_bounds[1] + top_step * i
        current_right = prev_bounds[2] + right_step * i
        current_bottom = prev_bounds[3] + bottom_step * i
        draw.ellipse((current_left, current_top, current_right, current_bottom), fill=color)

def draw_plot_box(draw, pos, size, rows, box_color, line_color):
    top = pos[1] * PIXEL_PER_ICON_Y + MARGIN_Y - EXTRA_Y
    left = pos[0] * PIXEL_PER_ICON_X + MARGIN_X
    right = left + size[0] * PIXEL_PER_ICON_X - MARGIN_X * 2
    bottom = top + size[1] * PIXEL_PER_ICON_Y
    height_partition = (bottom - top) / rows

    draw_box(draw, pos, size, box_color)
    for i in range(rows - 1):
        current_height_partition = height_partition * (i + 1)
        draw.rectangle((left, top + current_height_partition, right, top + current_height_partition + 1), fill=line_color)

def draw_university_widgets(img, todays_list, num_events_today, tomorrows_list):
    draw = ImageDraw.Draw(img)
    draw_content_box(draw, (12, 5), (4, 4.5), "Uni")
    #draw_box(draw, (12.05, 5.45), (3.9, 4), colors[1])
    #draw_box(draw, (12.1, 5.5), (3.8, 3.9), colors[2])
    #for i in range(5):
    #    draw_box(draw, (12.1, 5.5 + i * 0.78), (1.9, 0.78), colors[2])
    #    draw_box(draw, (14, 5.5 + i * 0.78), (1.9, 0.78), colors[2])

    draw_university_today(draw, todays_list)
    draw_university_tomorrow(draw, tomorrows_list)
    #draw_todays_calendar_list(draw, todays_list, 1235, 523.5)
    #draw_extended_list(draw, extended_list, num_events_today, 1235, 1300, 1370, 523.5)

    return img

def draw_university_today(draw, todays_list):
    for elem in todays_list:
        position = (elem[1] - 8) / 2
        draw_box(draw, (12.15, 5.55 + position * 0.76), (1.85, 0.76), colors[2])
        draw.text((1228, 523.5 + position * 67), elem[0], font=THIRD_FONT, fill=font_colors[0])
        time_string = str(elem[1]) + ":" + extra_zero(elem[2]) + " - " + str(elem[3]) + ":" + extra_zero(elem[4])
        draw.text((1253, 545.5 + position * 67), time_string, font=THIRD_FONT, fill=font_colors[0])

def draw_university_tomorrow(draw, tomorrows_list):
    for elem in tomorrows_list:
        position = (elem[1] - 8) / 2
        draw_box(draw, (14, 5.55 + position * 0.76), (1.85, 0.76), colors[2])
        draw.text((1413, 523.5 + position * 67), elem[0], font=THIRD_FONT, fill=font_colors[0])
        time_string = str(elem[1]) + ":" + extra_zero(elem[2]) + " - " + str(elem[3]) + ":" + extra_zero(elem[4])
        draw.text((1438, 545.5 + position * 67), time_string, font=THIRD_FONT, fill=font_colors[0])

def extra_zero(value):
    if(value < 10):
        return "0" + str(value)
    return str(value)
    
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
        draw.text((left + (right - left) / 2 - half_caption_width, top + PIXEL_PER_ICON_Y / 2.25), caption, font=MAIN_FONT, fill=font_colors[0])