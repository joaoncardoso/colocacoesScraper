# -*- coding: utf-8 -*-

import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# URL of the website
url = "https://www.dges.gov.pt/coloc/2020/col1listas.asp?CodR=11&action=2"

# Initialize the browser object
driver = webdriver.Firefox()

# Retrieve the webpage
driver.get(url)

# Get the select element
select = Select(driver.find_element(By.NAME, 'CodEstab'))
# Get the options
options = select.options
options_values = [option.get_attribute("value") for option in options]


for value in options_values:
    submit = driver.find_element(By.CSS_SELECTOR, "input[name='listagem'][value='Lista de Colocados']")
    select.select_by_value(value)
    submit.click()
    select_course = Select(driver.find_element(By.NAME, "CodCurso"))
    #get the select element
    # get the options
    options_course = select_course.options

    options_course_values = [option.get_attribute("value") for option in options_course]
    
    for oc_value in options_course_values:
        select_course = Select(driver.find_element(By.NAME, "CodCurso"))
        select_course.select_by_value(oc_value)
    
        course_submit = driver.find_element(By.CSS_SELECTOR, "input[name='search'][value='Continuar']")
        course_submit.click()

        # get the table: <table class="caixa" width="700" cellspacing="0" cellpadding="2" border="0">
        student_tables = driver.find_elements(By.CLASS_NAME, "caixa")
        student_table = student_tables[2]
        student_table_rows = student_table.find_elements(By.TAG_NAME, "tr")

        #print web element text for each row
        for tr in student_table_rows:
            print(tr.text)

        # go back a page
        driver.back()
    break

    """
        for tr in student_table_rows:
            td = tr.find_elements(By.TAG_NAME, "td")
            student_name = td[1].text.strip()
            print("NAME:", student_name)

        # go back through link with text "Voltar"
        back_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Voltar')]")
        back_link.click()
    break

"""
        
driver.quit()