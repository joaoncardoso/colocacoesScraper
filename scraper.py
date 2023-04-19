# -*- coding: utf-8 -*-

import csv
import mechanicalsoup

# URL of the website
url = "https://www.dges.gov.pt/coloc/2020/col1listas.asp?CodR=11&action=2"

# Initialize the browser object
mainBrowser = mechanicalsoup.StatefulBrowser()

# Retrieve the webpage

mainBrowser.open(url)
page = mainBrowser.get_current_page()

# Get the select element
select = page.find("select", {"name": "CodEstab"})
# Get the options
options = select.find_all("option")


for option in options:
    browser = mechanicalsoup.StatefulBrowser()
    # open browser on page page. 
    browser.open(url)
    # select form
    form = browser.select_form()
    submit = page.find("input", {"name": "listagem", "value": "Lista de Colocados"})

    select_option = option["value"]
    browser["CodEstab"] = select_option
    browser.submit_selected(submit)


    course_page = browser.get_current_page()

    #get the select element
    select_course = course_page.find("select", {"name": "CodCurso"})
    # get the options
    options_course = select_course.find_all("option")
    # print(options_course)


    for oc in options_course:
        browser.select_form()
        select_course_option = oc["value"]
        course_submit = course_page.find("input", {"name": "search", "value": "Continuar"})
        browser["CodCurso"] = select_course_option
        browser.submit_selected(course_submit)

        student_page = browser.get_current_page()
        # get the table: <table class="caixa" width="700" cellspacing="0" cellpadding="2" border="0">
        student_tables = student_page.find_all("table", {"class": "caixa"})
        student_table = student_tables[2]
        student_table_rows = student_table.find_all("tr")
        for tr in student_table_rows:
            td = tr.find_all("td")
            student_name = td[1].text.strip()
            print("NAME:", student_name)
        # go back through link with text "Voltar"
        back_link = student_page.find("a", string="Voltar")
        print(back_link)
        browser.follow_link(back_link)
        break
            # Row: ['\r\n\t\t\t153(...)01   \r\n\t\t', '\r\n\t\t\tSTUDENTNAME\r\n\t\t']
            # get STUDENTNAME
            #student_name = row[1].split("\r\n\t\t\t")[1]
            #print("NAME:", student_name.encode("utf-8"))

    break
"""
    course_page = response.soup
    # get the select element
    select_course = course_page.find("select", {"name": "CodCurso"})
    # get the options
    options_course = select_course.find_all("option")
    print(options_course)
    break

url2 = "https://www.google.com/imghp?hl=en"

response = browser.get(url2)

browser.select_form()
browser.get_current_form().print_summary()
"""
    