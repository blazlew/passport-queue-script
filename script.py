import time
from selenium import webdriver
from bs4 import BeautifulSoup
import os

options = webdriver.ChromeOptions()
# options.add_argument('headless')
driver = webdriver.Chrome(options=options)
driver.get('https://bezkolejki.eu/lodzkiuw')
time.sleep(2)

while True:
  driver.find_element_by_xpath("//*[contains(text(), 'Przyjmowanie wniosków')]").click()

  dalejButton = driver.find_element_by_xpath("//*[contains(text(), 'Dalej')]")
  driver.execute_script("arguments[0].click();", dalejButton)

  try:
    driver.find_element_by_xpath("//*[contains(text(), 'Brak dostępnych')]")
    driver.refresh()
    time.sleep(5)
  except:
    print('BOOKING AVAILABLE!')
    while True:
      os.system("afplay rooster.mp3") 
      os.system("say 'Znaleziono wolny termin' -v 'Zosia' -r 200") 


