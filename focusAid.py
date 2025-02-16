from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def focusAid():
    links = [
        "https://www.youtube.com/watch?v=JSnbUouPS1k",
        "https://www.youtube.com/watch?v=bRlaxFTxxs8",
        "https://www.youtube.com/watch?v=aWh8j7rcQNE",
        "https://www.youtube.com/watch?v=MmONqKigHEs",
        "https://www.youtube.com/watch?v=1zyyb4be8n4",
        "https://www.youtube.com/watch?v=9xG6DGrsd5E"
    ]

    random_int = random.randint(0,5)
    driver = webdriver.Chrome()

    driver.get(links[random_int])
    wait = WebDriverWait(driver,10)
    theater_mode = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ytp-size-button")))
    play = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ytp-play-button")))
    play.click()
    theater_mode.click()
    total_time = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ytp-time-duration"))).text


    while True:
        try:
            curr_time = driver.find_element(By.CLASS_NAME, "ytp-time-current").text

            if curr_time == total_time:
                break
            
            time.sleep(1)
        except Exception:
            break

    driver.quit()




