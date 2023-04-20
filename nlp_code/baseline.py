# Python Draft for Baseline

import json

# Load simplify data


def main():
    dataset_dir = "./dataset/simplify_json"
    json_files = [dataset_dir + "/train_split.json", dataset_dir + "/valid_split.json"]
    data_files = []
    for json_file in json_files:
        with open(json_file, 'r') as f:
            data_files.append(json.load(f))

    # Get (X_train y_train), (X_valid, y_valid) from json file
    # covert big-5 ['Openness', 'Conscientiousness', 'Extraversion','Agreeableness', 'Neuroticism'] to 0:low 1:high
    for i in range(len(data_files)):
        for j in range(len(data_files[i])):
            data_files[i][j]['label'] = [0 if data_files[i][j]['Openness'] == 'low' else 1,
                                         0 if data_files[i][j]['Conscientiousness'] == 'low' else 1,
                                         0 if data_files[i][j]['Extraversion'] == 'low' else 1,
                                         0 if data_files[i][j]['Agreeableness'] == 'low' else 1,
                                         0 if data_files[i][j]['Neuroticism'] == 'low' else 1]



    X_train = []   # name, Utterance
    y_train = []   # big-5
    X_valid = []    # name, Utterance
    y_valid = []    # big-5
    speakers_train, speakers_valid = [],[]
    for i in range(len(data_files[0])):
        X_train.append((data_files[0][i]['Speaker'], data_files[0][i]['Utterance']))
        y_train.append(data_files[0][i]['label'])
        speakers_train.append(data_files[0][i]['Speaker'])
    speakers_train = list(set(speakers_train))
    print("There are {} speakers in train_data" .format(len(speakers_train)))

    for i in range(len(data_files[1])):
        X_valid.append((data_files[1][i]['Speaker'], data_files[1][i]['Utterance']))
        y_valid.append(data_files[1][i]['label'])
        speakers_valid.append(data_files[1][i]['Speaker'])
    speakers_valid = list(set(speakers_valid))
    print("There are {} speakers in valid_data" .format(len(speakers_valid)))


def combine_same_speaker_data(speakers, X, y):
    # combine same speaker data to one data and only keep different Utterance and one speaker name
    X_train_combine = []
    y_train_combine = []
    for speaker in speakers_train:
        X_train_combine.append({speaker:[]})
        y_train_combine.append({speaker:[]})



    for i in range(len(X_train)):
        for j in range(len(X_train_combine)):
            if X_train[i][0] in X_train_combine[j]:
                X_train_combine[j][X_train[i][0]].append(X_train[i][1])
                y_train_combine[j][X_train[i][0]].append(y_train[i])


    for i in range(len(y_train_combine)):
        for key in y_train_combine[i]:
            y_train_combine[i][key] = y_train_combine[i][key][0]
    return X_train_combine, y_train_combine

X_train_combined, y_train_combined = combine_same_speaker_data(speakers_train, X_train, y_train)
X_valid_combined, y_valid_combined = combine_same_speaker_data(speakers_valid, X_valid, y_valid)


# encoding=utf-8

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + " ".join(seg_list))  # Accruate Mode
# use jieba to cut sentence on x_valid_combined

for speaker in x_valid_combined:
    for key in speaker:
        for i in range(len(speaker[key])):
            seg_list = jieba.cut(speaker[key][i], cut_all=False)
            speaker[key][i] = " ".join(seg_list)

for speaker in X_train_combined:
    for i in range(1, len(speaker[key])):
        # combine all key's value to one value usse space to split
        speaker[key][0] = speaker[key][0] + " " + speaker[key][i]



for speaker in X_train_combined:
    for key in speaker:
        for i in range(1, len(speaker[key])):
            # delete other key's value
            del speaker[key][i]


# dat clean : convert all punctuation or multi-sapce to one space
for speaker in X_train_combined:
    for key in speaker:
        speaker[key][0] = re.sub(r'[^\w\s]','',speaker[key][0])
        speaker[key][0] = re.sub(r'\s+',' ',speaker[key][0])



# encoding=utf-8

if __name__ == "__main__":
    main()
              