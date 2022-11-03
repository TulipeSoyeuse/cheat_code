from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import subprocess
import numpy as np
import pandas as pd

print("running")
df = pd.read_csv("~/.cheat_code_folder/script/data/scrapping_solution.csv",index_col=0).dropna().reset_index(drop=True)
a_previous = "\n".join(subprocess.run("powershell.exe -noprofile Get-Clipboard",shell=True))

while True:

    a = "\n".join(subprocess.run("powershell.exe -noprofile Get-Clipboard",shell=True))

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
            subprocess.run(f"clip.exe {soluce}",shell=True)
            a_previous = soluce
        else :
            print("no match")
            subprocess.run("clip.exe 'no match'",shell=True)
            a_previous = "no match"
