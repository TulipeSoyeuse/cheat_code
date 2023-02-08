from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pyperclip3 as pc
import numpy as np
import pandas as pd
import keyboard
from pynput.keyboard import Key, Listener, Controller
from threading import Lock
import time
lock = Lock()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://tournament.lewagon.com/games")
print("running")
keyboard2 = Controller()
try :
    df = pd.read_csv("script/data/scrapping_solution.csv",index_col=0).dropna().reset_index(drop=True)
except:
    df =  pd.read_csv("data/scrapping_solution.csv",index_col=0).dropna().reset_index(drop=True)
a_previous = pc.paste().decode("utf-8")
value_paste=None

def on_press(key):
    if key == Key.ctrl :
        time.sleep(0.3)
        prompt = driver.find_element(By.XPATH,"//div[@id='instructions']/p").text
        array = np.append(np.array(df.description),prompt)
        vectorizer = TfidfVectorizer()
        desc_matrix = vectorizer.fit_transform(array)
        cos_sim_matrix = cosine_similarity(desc_matrix, desc_matrix[-1])[:-1]
        index = np.argmax(cos_sim_matrix)
        print("similarity :" + str(cos_sim_matrix[index]))
        soluce = df.loc[index,"solution"]
        # target_code = driver.find_element(By.XPATH,"//div[@class='CodeMirror cm-s-monokai']")
        # target_code.click()
        lock.acquire()
        keyboard.write(soluce)
        lock.release()

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

listener = Listener(on_press=on_press, on_release=on_release)
listener.start()

while True:
    pass
