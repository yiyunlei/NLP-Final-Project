import os
import sys
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
import numpy as np
import json
import gzip
import csv, re
import string
from tqdm import tqdm
import codecs
import argparse
from collections import Counter
from spacy.lang.en import English
 

# Convenient for debugging but feel free to comment out

# Hard-wired variables
input_speechfile   = "./speeches2020_jan_to_jun.jsonl.gz"
stopwords_file     = "./mallet_en_stoplist.txt"

train_csv_file     = "./dataset/CPED/train_split.csv"
valid_csv_file     = "./dataset/CPED/valid_split.csv"
test_csv_file      = "./dataset/CPED/test_split.csv"
csv_files         = [train_csv_file, valid_csv_file, test_csv_file]

train_json_file    = "./dataset/json/train_split.json"
valid_json_file    = "./dataset/json/valid_split.json"
test_json_file     = "./dataset/json/test_split.json"
json_files        = [train_json_file, valid_json_file, test_json_file]

train_simplify_json_file    = "./dataset/simplify_json/train_split.json"
valid_simplify_json_file    = "./dataset/simplify_json/valid_split.json"
test_simplify_json_file     = "./dataset/simplify_json/test_split.json"
simplify_json_files        = [train_simplify_json_file, valid_simplify_json_file, test_simplify_json_file]



# Covert csv file to json file
def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii = False)
    print("Convert successfully".format(csv_file, json_file))


# Simplify and clean data
def simplify_data(json_file, simplify_json_file):
    # Use order OCEAN 
    keys = ['Openness', 'Conscientiousness', 'Extraversion','Agreeableness', 'Neuroticism', 'Speaker', 'Utterance']
    new_data = []
    with open(json_file, 'r') as f:
        data = json.load(f)
    for obj in data:
        new_data.append({key: obj[key] for key in keys})
    with open(simplify_json_file, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii = False)

# Clean data and one hot encoding 
# low - 0
# high - 1
def clean_data(json_file):
    count = 0
    keys = ['Openness', 'Conscientiousness', 'Extraversion','Agreeableness', 'Neuroticism', 'Speaker', 'Utterance']
    # print rows that have Unknown value
    with open(json_file, 'r') as f:
        data = json.load(f)
    updated_data = []
    for obj in data:
        if obj['Speaker'] != '其他' and all(obj[key] != 'unknown' for key in keys):
            updated_data.append(obj)
            count += 1
    print("count:", count)
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(updated_data, f, ensure_ascii = False)
    

# Get (X_train y_train), (X_valid, y_valid, X_test, y_test) from json file
def get_X_y(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    X = []
    y = []
    for i in range(len(data)):
        X.append(data[i]['name, Utterance'])
        y.append(data[i]['label'])
    return X, y

def validate_unique_big5_of_speaker(simplify_json_file):
    with open(simplify_json_file, 'r') as f:
        data = json.load(f)
    speakers = []
    for obj in data:
        speakers.append(obj['Speaker'])
    speakers = list(set(speakers))
    print("There are {} speakers in {}" .format(len(speakers), simplify_json_file))
    for speaker in speakers:
        data_of_same_speaker = []
        for obj in data:
            if obj['Speaker'] == speaker:
                data_of_same_speaker.append(obj)
        # print("Speaker {} has {} data" .format(speaker, len(data_of_same_speaker)))
        if not validate_unique_big5(data_of_same_speaker):
            print("Speaker {} has different big5 in {}" .format(speaker, simplify_json_file))
            return False
    return True

def validate_unique_big5(data_of_same_speaker):
    # print("datase:", data_of_same_speaker[0])
    """Validate that the big5 for each speaker is unique"""
    keys = ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism']
    big5 = {key: data_of_same_speaker[0][key] for key in keys}
    for data in data_of_same_speaker[1:]:
        current_big5 = {key: data[key] for key in keys}
        if current_big5 != big5:
            return False
    return True

def main():
    # preprocess data
    for csv_file, json_file, simplify_json_file in zip(csv_files, json_files, simplify_json_files):
        # print('current covert {} file to {}:' .format(csv_file, json_file))
        # csv_to_json(csv_file,json_file)
        # simplify_data(json_file, simplify_json_file)
        # clean_data(simplify_json_file)
        # validation unique big5 for each speaker
        if not validate_unique_big5_of_speaker(simplify_json_file):
            print("There are different big5 for same speaker in {}" .format(simplify_json_file))
        print("There are no different big5 for same speaker in {}" .format(simplify_json_file))


if __name__ == "__main__":
    main()
    