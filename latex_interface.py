import matplotlib.pyplot as plt
import subprocess
import pathlib
import shutil
import os

import database_interface as dbi
import data as dat

from util import get_date, sign, format_dm, string_to_tex

PLOT_WIDTH_1 = 0.627
PLOT_WIDTH_2 = 0.65

TEMP_PATH = str(pathlib.Path(__file__).parent.resolve()) + "/latex/templates"
BASE_TEMP_PATH = TEMP_PATH + "/base_temp.tex"
SECTION_PATH = TEMP_PATH + "/section.tex"
MON_BAL_TEMP_PATH = TEMP_PATH + "/balance_temp.tex"
MON_EXP_TEMP_PATH = TEMP_PATH + "/monthly_expenditure_temp.tex"
YEAR_EXP_TEMP_PATH = TEMP_PATH + "/yearly_expenditure_temp.tex"
LONG_TABLE_TEMP_PATH = TEMP_PATH + "/long_table_temp.tex"
MINIPAGE_TEMP_PATH = TEMP_PATH + "/minipage_temp.tex"
INCLUDE_PNG_PATH = TEMP_PATH + "/include_png.tex"
TEX_PLAYGROUND_PATH = str(pathlib.Path(__file__).parent.resolve()) + "/latex/playground"
PDF_PATH = str(pathlib.Path(__file__).parent.resolve()) + "/pdf"
PNG_PATH = str(pathlib.Path(__file__).parent.resolve()) + "/latex/playground/png"

AUTHOR_PH = "$$AUTHOR$$"
TITLE_PH = "$$TITLE$$"
BALANCE_PH = "$$BALANCE$$"
DETAILS_PH = "$$DETAILS$$"
SECTION_PH = "$$SECTION$$"
TABLE_LINES_PH = "$$TABLE_LINES$$"
TABLE_TOTAL_PH = "$$TABLE_TOTAL$$"
PLOTS_PH = "$$PLOTS$$"
LONG_TABLE = "$$LONG_TABLE$$"
CAPTION_PH = "$$CAPTION$$"

AUTHOR = ""
TITLE_PREFIX = "Finanzen"


def create_finance_pdf(added_days=0):
    year = get_date(added_days).tm_year
    categories = dbi.select_yearly_exp_categories(str(year))
    latex_file_str = get_latex_file_str(
        year,
        categories
    )
    create_latex_pdf(latex_file_str, year)


def get_latex_file_str(year, categories):
    with open(BASE_TEMP_PATH, encoding="utf8") as file:
        file_str = file.read()

    balance_str = get_balance(
        year
    )

    details_str = get_monthly_content(
        year,
        categories
    )

    file_str = file_str.replace(TITLE_PH, TITLE_PREFIX + " " + str(year))
    file_str = file_str.replace(AUTHOR_PH, AUTHOR)
    file_str = file_str.replace(BALANCE_PH, balance_str)
    file_str = file_str.replace(DETAILS_PH, details_str)

    return file_str


def get_balance(year):
    with open(SECTION_PATH, encoding="utf8") as file:
        content = file.read().replace(SECTION_PH, "Bilanz")
    with open(MON_BAL_TEMP_PATH, encoding="utf8") as file:
        bal_temp = file.read()
    content += get_mon_bal_table_lines(bal_temp, year)
    content += get_cum_bal_table_lines(bal_temp, year)
    return content


def get_monthly_content(year, categories):
    with open(SECTION_PATH, encoding="utf8") as file:
        content = file.read().replace(SECTION_PH, "Ausgaben")
    yearly_plots = []
    for cat in categories[1:]:
        yearly_plots.append(get_yearly_cat_plots(year, cat))
    while len(yearly_plots) > 0:
        if len(yearly_plots) > 1:
            content += get_minipage(yearly_plots[0], yearly_plots[1])
            yearly_plots = yearly_plots[2:]
        else:
            content += get_minipage(yearly_plots[0], "")
            yearly_plots = yearly_plots[1:]
    with open(MON_EXP_TEMP_PATH, encoding="utf8") as file:
        mon_temp = file.read()
    for i, month in enumerate([x[0] for x in dat.months]):
        mon_content = mon_temp.replace(SECTION_PH, month)
        mon_content = mon_content.replace(
            TABLE_LINES_PH,
            get_mon_exp_table_lines(
                i + 1,
                year,
                categories
            )
        )
        mon_tot_exp = dbi.select_monthly_total_expenditure(str(i + 1), str(year))
        mon_content = mon_content.replace(
            TABLE_TOTAL_PH,
            "Gesamt&&" + mon_tot_exp
            )
        mon_content = mon_content.replace(
            PLOTS_PH,
            get_plots_by_month(i + 1, year, categories)
        )
        mon_content = mon_content.replace(
            LONG_TABLE,
            get_long_table(i + 1, year, categories)
        )

        content += mon_content
    return content


def get_long_table(month, year, categories):
    with open(LONG_TABLE_TEMP_PATH, "r", encoding="utf8") as file:
        long_table = file.read()
    table_lines = []
    for cat in categories:
        exp = dbi.select_mon_cat_sort_exp_list(str(month), str(year), cat)
        if len(exp) == 0:
            continue
        table_lines.append(get_long_table_line(cat, exp[0][0], exp[0][1], month, exp[0][2]))
        for entry in exp[1:]:
            table_lines.append(get_long_table_line("", entry[0], entry[1], month, entry[2]))
    long_table = long_table.replace(TABLE_LINES_PH, "\n".join(table_lines)[8:])
    return long_table


def get_saldo_plots(months, saldos, is_cumulative=False):
    fig, ax = plt.subplots()
    cumu_case = {
        True: ["Saldo kummuliert", "cumulative"],
        False: ["Saldo pro Monat", "per_month"]
    }
    bar_colors = list(map(lambda x: {True: "tab:blue", False: "tab:red"}[x > 0], saldos))
    if is_cumulative:
        months = [" "] + months
        saldos = [0] + saldos
        ax.plot(months, saldos, color="tab:grey")
        for i in range(len(months)):
            color = {
                1: "tab:blue",
                0: "tab:grey",
                -1:"tab:red"
            }[sign(saldos[i])]
            ax.scatter(months[i],
                       saldos[i],
                       color=color)
    else:
        ax.bar(months, saldos, color=bar_colors)
    ax.set_title(cumu_case[is_cumulative][0])
    plt.xticks(range(len(months)), months, rotation='vertical')
    # fig.subplots_adjust(bottom=0.22)
    file_name = cumu_case[is_cumulative][1] + ".png"
    plt.savefig(PNG_PATH + "/" + file_name)
    plt.close()
    return get_include_png_lines(PLOT_WIDTH_1, file_name)


def get_inc_exp_plots(months, incomes, expences, is_cumulative=False):
    fig, ax = plt.subplots()
    cumu_case = {
        True: ["Einnahmen & Ausgaben kummuliert", "inc_exp_cumulative"],
        False: ["Einnahmen & Ausgaben pro Monat", "inc_exp"]
    }
    if is_cumulative:
        months = [" "] + months
        ax.plot(months, [0] + incomes, marker="o")
        ax.plot(months, [0] + expences, color="tab:red", marker="o")
    else:
        expences = [-x for x in expences]
        ax.bar(months, incomes)
        ax.bar(months, expences, color="tab:red")
    ax.set_title(cumu_case[is_cumulative][0])
    plt.xticks(range(len(months)), months, rotation='vertical')
    # fig.subplots_adjust(bottom=0.22)
    file_name = cumu_case[is_cumulative][1] + ".png"
    plt.savefig(PNG_PATH + "/" + file_name)
    plt.close()
    return get_include_png_lines(PLOT_WIDTH_1, file_name)


def get_yearly_cat_plots(year, category):
    months = [x[1] for x in dat.months]
    expences = [float(dbi.select_monthly_category_expenditure(str(i + 1), str(year), category))
           for i in range(12)]
    fig, ax = plt.subplots()
    ax.bar(months, expences, color="tab:red")
    ax.set_title(category)
    plt.xticks(range(len(months)), months, rotation='vertical')
    file_name = category + ".png"
    plt.savefig(PNG_PATH + "/" + file_name)
    plt.close()
    return get_include_png_lines(1, file_name)


def get_plots_by_month(month, year, categories):
    categories = categories.copy()
    categories.remove("Fixkosten")
    expences = []
    for cat in categories:
        expences.append(float(dbi.select_monthly_category_expenditure(str(month), str(year), cat)))
    
    fig = plt.figure()
    plt.bar(categories, expences, color="tab:red")
    plt.title(dat.months[month - 1][0])
    plt.xticks(range(len(categories)), categories, rotation='vertical')
    fig.subplots_adjust(bottom=0.22)
    file_name =str(year) + "-" + str(month) + ".png"
    plt.savefig(PNG_PATH + "/" + file_name)
    plt.close()
    return get_include_png_lines(PLOT_WIDTH_2, file_name)


def get_bal_table_line(month, inc, exp):
    return ("        " +
            str(month) + "&" + 
            align_amount(inc) + "&" + 
            align_amount(exp) + "&" +
            align_amount(inc- exp) + "\\\\")

def get_long_table_line(category, name, day, month, amount):
    date = format_dm(day, month)
    return ("        " +
            string_to_tex(category) + "&" + 
            string_to_tex(name) + "&" + 
            date + "&" +
            align_amount(amount) + "\\\\")


def get_mon_bal_table_lines(lines: str, year: int):
    incomes = []
    expences = []
    table_rows = []
    for i, month in enumerate([x[0] for x in dat.months]):
        incomes.append(float(dbi.select_monthly_total_income(str(i + 1), str(year))))
        expences.append(float(dbi.select_monthly_total_expenditure(str(i + 1), str(year))))
        table_rows.append(get_bal_table_line(month, incomes[-1], expences[-1]))
    lines = lines.replace(TABLE_LINES_PH, "\n".join(table_rows)[8:])

    tot_inc = float(dbi.select_yearly_total_income(str(year)))
    tot_exp = float(dbi.select_yearly_total_expenditure(str(year)))
    lines = lines.replace(TABLE_TOTAL_PH, get_bal_table_line("Gesamt", tot_inc, tot_exp))
    lines = lines.replace(CAPTION_PH, "Bilanz pro Monat")

    months = [x[1] for x in dat.months]
    saldos = [incomes[i] - expences[i] for i in range(len(months))]
    plot_lines = get_inc_exp_plots(months, incomes, expences)
    plot_lines += get_saldo_plots(months, saldos)
    lines = lines.replace(PLOTS_PH, plot_lines)
    return lines


def get_minipage(first, second):
    with open(MINIPAGE_TEMP_PATH, "r", encoding="utf8") as file:
        minipage = file.read()
    minipage = minipage.replace("$$FIRST$$", first)
    minipage = minipage.replace("$$SECOND$$", second)
    return minipage


def get_cum_bal_table_lines(lines: str, year: int):
    incomes = []
    expences = []
    table_rows = []
    for i, month in enumerate([x[0] for x in dat.months]):
        incomes.append(float(dbi.select_cummulative_total_income(str(i + 1), str(year))))
        expences.append(float(dbi.select_cummulative_total_expenditure(str(i + 1), str(year))))
        table_rows.append(get_bal_table_line(month, incomes[-1], expences[-1]))
    lines = lines.replace(TABLE_LINES_PH, "\n".join(table_rows)[8:])

    tot_inc = float(dbi.select_yearly_total_income(str(year)))
    tot_exp = float(dbi.select_yearly_total_expenditure(str(year)))
    lines = lines.replace(TABLE_TOTAL_PH, get_bal_table_line("Gesamt", tot_inc, tot_exp))
    lines = lines.replace(CAPTION_PH, "Bilanz kummuliert")

    months = [x[1] for x in dat.months]
    saldos = [incomes[i] - expences[i] for i in range(len(months))]
    plot_lines = get_inc_exp_plots(months, incomes, expences, is_cumulative=True)
    plot_lines += "\n" + get_saldo_plots(months, saldos, is_cumulative=True)
    lines = lines.replace(PLOTS_PH, plot_lines)
    return lines


def get_mon_exp_table_lines(month, year, categories):
    table_rows = []
    for cat in categories:
        cat_exp = float(dbi.select_monthly_category_expenditure(str(month), str(year), cat))
        mon_total = float(dbi.select_monthly_total_expenditure(str(month), str(year)))
        percentage = "-"
        if mon_total > 0:
            percentage = str(round(cat_exp / mon_total * 100, 2))
        table_rows.append("        " + cat + "&" + percentage + "&" +
                          align_amount(cat_exp) + "\\\\")
    return "\n".join(table_rows)[8:]


def align_amount(value):
    value_str = str(round(value, 2))
    if value_str[-2] == ".":
        return value_str + "0"
    return value_str


def get_include_png_lines(width, file_name):
    with open(INCLUDE_PNG_PATH, "r", encoding="utf8") as file:
        text = file.read()
    text = text.replace("$$WIDTH$$", str(width))
    text = text.replace("$$FILE_NAME$$", str(file_name))
    return text


def create_latex_pdf(file_str, year):
    # create /latex/playground/latex.tex
    tex_file_path = TEX_PLAYGROUND_PATH + "/latex.tex"
    with open(tex_file_path, "w", encoding="utf8") as file:
        file.write(file_str)
    
    # build /latex/playground/latex.tex
    subprocess.run(["sh", "shell/build_tex.sh"])

    # copy and rename pdf
    source = TEX_PLAYGROUND_PATH + "/latex.pdf"
    sink = PDF_PATH + "/" + TITLE_PREFIX + "_" + str(year) + ".pdf"
    shutil.copyfile(source, sink)

    # clean up /latex/playground
    for file_name in os.listdir(TEX_PLAYGROUND_PATH):
        path_ = TEX_PLAYGROUND_PATH + "/" + file_name
        if not os.path.isdir(path_):
            os.unlink(path_)
    for file_name in os.listdir(TEX_PLAYGROUND_PATH + "/png"):
        path_ = TEX_PLAYGROUND_PATH + "/png/" + file_name
        if not os.path.isdir(path_):
            os.unlink(path_)

if __name__ == "__main__":
    create_finance_pdf()