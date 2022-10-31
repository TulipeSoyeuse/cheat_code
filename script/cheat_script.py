import pyperclip3 as pc
import pandas as pd
import nltk
import os

nltk.download('punkt')

def process_string(df, input_string,cpt):
    input_string = " ".join(nltk.word_tokenize(input_string.lower()))
    row_ = df["description"].apply(lambda x : str(x).find(input_string))

    if len(df.loc[row_ != -1]["solution"].to_list()) == 0 or len(df.loc[row_ != -1]["solution"].to_list()) > 1 :
        return "no match dumbass"
    else :
        return str(df.loc[row_ != -1]["solution"].to_list()[0])

df = pd.read_csv("scrapping_solution.csv")
a_previous=pc.paste().decode("utf-8")
last_past=""
cpt_changes=0
print("running")

while True:
    a = pc.paste().decode("utf-8")

    if len(a)>0 and str(a) != str(a_previous):
        cpt_changes +=1
        a = pc.paste().decode("utf-8")
        to_clip = process_string(df, a, cpt_changes)
        if to_clip != "no match dumbass":
            pc.copy(to_clip)
            a_previous = str(to_clip)
        else :
            print("no match")
