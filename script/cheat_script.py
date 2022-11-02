from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pyperclip3 as pc
import numpy as np
import pandas as pd

print("running")
df = pd.read_csv("~/.cheat_code_folder/script/data/scrapping_solution.csv",index_col=0).dropna().reset_index(drop=True)
a_previous = pc.paste().decode("utf-8")

while True:

    a = pc.paste().decode("utf-8")

    if len(a)>0 and a != a_previous:
        array = np.append(np.array(df.description),a)
        vectorizer = TfidfVectorizer()
        desc_matrix = vectorizer.fit_transform(array)
        index = np.argmax(cosine_similarity(desc_matrix, desc_matrix[-1])[:-1])
        print("similarity :" + str(index))
        a_previous = a
        pc.copy(df.loc[index,"solution"])
