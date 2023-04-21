# -*- coding: utf-8 -*-

# just run py .\colocacoes_scraper.py in the terminal, after installing selenium
# takes about 7 minutes to run

import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

tic = time.perf_counter()

# Initialize the browser object
driver = webdriver.Firefox()

url_dict = {"2019_uni": "https://www.dges.gov.pt/coloc/2019/col1listas.asp?CodR=11&action=2"}

for key, value in url_dict.items():

    # Retrieve the webpage
    driver.get(value)

    # Get the select element
    select = Select(driver.find_element(By.NAME, 'CodEstab'))
    # Get the university options
    options = select.options
    options_values = [option.get_attribute("value") for option in options]
    options_names = [option.text for option in options]

    # index so we can print the university name
    index = 0

    with open(f'output{key}.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['NAME', 'COURSE', 'ESTABLISHMENT'])
        for value in options_values:
            # get the select element
            select = Select(driver.find_element(By.NAME, 'CodEstab'))
            # get the submit button
            submit = driver.find_element(By.CSS_SELECTOR, "input[name='listagem'][value='Lista de Colocados']")
            select.select_by_value(value)
            submit.click()
            # get the select element
            select_course = Select(driver.find_element(By.NAME, "CodCurso"))
            # get the options
            options_course = select_course.options

            options_course_values = [option.get_attribute("value") for option in options_course]
            options_course_names = [option.text for option in options_course]
            # index so we can print the course name
            index_course = 0
            
            for oc_value in options_course_values:
                select_course = Select(driver.find_element(By.NAME, "CodCurso"))
                select_course.select_by_value(oc_value)

                # find the continue button
                course_submit = driver.find_element(By.CSS_SELECTOR, "input[name='search'][value='Continuar']")
                course_submit.click()

                # get the table
                student_tables = driver.find_elements(By.CLASS_NAME, "caixa")
                # for some courses there are no students :(
                if len(student_tables) >= 3:
                    student_table = student_tables[2]
                else:
                    index_course += 1
                    driver.back()
                    continue
                student_table_rows = student_table.find_elements(By.TAG_NAME, "tr")

                for tr in student_table_rows:
                    td = tr.find_elements(By.TAG_NAME, "td")
                    student_name = td[1].text.strip()
                    writer.writerow([student_name, options_course_names[index_course], options_names[index]])
                index_course += 1

                # go back a page
                driver.back()
            index += 1
            driver.back()

driver.quit()
toc = time.perf_counter()
print(f"Finished in {toc - tic:0.4f} seconds")