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
        cos_sim_matrix = cosine_similarity(desc_matrix, desc_matrix[-1])[:-1]
        index = np.argmax(cos_sim_matrix)
        print("similarity :" + str(cos_sim_matrix[index]))
        soluce = df.loc[index,"solution"]
        if np.max(cos_sim_matrix[index]) > 0.5 :
            print(True)
            pc.copy(soluce)
            a_previous = soluce
        else :
            print("no match")
            pc.copy("no match")
            a_previous = "no match"
