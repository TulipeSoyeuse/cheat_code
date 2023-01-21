from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pyperclip3 as pc
import numpy as np
import pandas as pd
import keyboard
from pynput.keyboard import Key, Listener
from threading import Lock

lock = Lock()


print("running")
df = pd.read_csv("script/data/scrapping_solution.csv",index_col=0).dropna().reset_index(drop=True)
a_previous = pc.paste().decode("utf-8")
paste_special=False
value_paste=None


def on_press(key):
    global value_paste
    global paste_special
    print(value_paste)
    print(paste_special)
    if paste_special and key == Key.ctrl:
        print("go")
        lock.acquire()
        keyboard.write(value_paste)
        lock.release()
        paste_special = False
def on_release(key):
    print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        return False


# Collect events until released

listener = Listener(on_press=on_press, on_release=on_release)
listener.start()

while True:

    a = pc.paste().decode("utf-8")

    if len(a)>0 and a != a_previous:
        array = np.append(np.array(df.description),a)
        vectorizer = TfidfVectorizer()
        desc_matrix = vectorizer.fit_transform(array)
        cos_sim_matrix = cosine_similarity(desc_matrix, desc_matrix[-1])[:-1]
        index = np.argmax(cos_sim_matrix)
        print("similarity :" + str(cos_sim_matrix[index]))
        soluce = df.loc[index,"solution"]
        if np.max(cos_sim_matrix[index]) > 0.5 :
            print(True)
            pc.copy(soluce)
            a_previous = soluce
            paste_special = True
            value_paste = soluce
        else :
            print("no match")
            pc.copy("no match")
            paste_special = False
            value_paste = None
            a_previous = "no match"
