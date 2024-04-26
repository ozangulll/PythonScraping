import os
import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


show_more_clicks = 0


driver = webdriver.Chrome()  
url = "https://www.excursionmarket.com/all-tours"
driver.get(url)


while show_more_clicks < 29:
    try:
        show_more_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "tourLoadBtn")))
        driver.execute_script("arguments[0].click();", show_more_button)
        time.sleep(3)  
        show_more_clicks += 1  
    except:
        print("No more tours to load.")
        break


soup = BeautifulSoup(driver.page_source, "html.parser")


tours = [a['href'] for a in soup.select('.tourCard__image a[href]')]


csv_file_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', "py", "faq.csv")
with open(csv_file_path, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Question', 'Answer'])
    
    for tour_url in tours:
        response = requests.get(tour_url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        faq_items = soup.find_all("div", class_="accordion__item")
        
        if not faq_items:
            print(f"No FAQ items found for {tour_url}")
            continue

        for faq_item in faq_items:
            question = faq_item.find("h3", class_="custom-h3-15")
            answer = faq_item.find("p", class_="text-15")

            if question and answer:
                question_text = question.text.strip()
                answer_text = answer.text.strip()
                writer.writerow([question_text, answer_text])
            else:
                print("Incomplete FAQ item found.")

print(f"CSV file saved to: {csv_file_path}")


print(f"Number of clicks on 'show more' button: {show_more_clicks}")


driver.quit()
