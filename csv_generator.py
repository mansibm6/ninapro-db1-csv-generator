from scipy.io import loadmat
import pandas as pd
import os
import csv


# Access the mat file

count = 0
inputpath = 'D:/Machine Learning Mastery/Projects/sEMG based movement recognition/Datasets'
listdir = os.listdir(inputpath)
for file in listdir:
    if file.endswith('mat'):
        file_path = os.path.join(inputpath, file)
        dataset = loadmat(file_path)
        count = count + 1


        # convert all columns to list

        emg = [[element for element in upperElement] for upperElement in dataset['emg']]
        stimulus = [[element for element in upperElement] for upperElement in dataset['stimulus']]
        glove =  [[element for element in upperElement] for upperElement in dataset['glove']]
        subject =  [[element for element in upperElement] for upperElement in dataset['subject']]
        exercise =  [[element for element in upperElement] for upperElement in dataset['exercise']]
        repetition =  [[element for element in upperElement] for upperElement in dataset['repetition']]
        restimulus = [[element for element in upperElement] for upperElement in dataset['restimulus']]
        rerepetition = [[element for element in upperElement] for upperElement in dataset['rerepetition']]


        # modify stimulus and convert it to numbers instead of lists

        element_stimulus = stimulus[0]
        for i in range(len(emg)) :
            stimulus.append(element_stimulus)

        for i in range(len(stimulus)):
            x = stimulus[i]
            y = x[0]
            stimulus[i] = y


        # modify exercise and convert it to numbers instead of lists

        element_exercise = exercise[0]
        for i in range(len(emg)):
            exercise.append(element_exercise)

        for i in range(len(exercise)):
            x = exercise[i]
            y = x[0]
            exercise[i] = y


        # create 101014 rows and 10 columns of emg data and convert them to numbers instead of lists

        emg_0 = []
        for l in emg:
            emg_0.append(l[0])

        emg_1 = []
        for l in emg:
            emg_1.append(l[1])

        emg_2 = []
        for l in emg:
            emg_2.append(l[2])

        emg_3 = []
        for l in emg:
            emg_3.append(l[3])

        emg_4 = []
        for l in emg:
            emg_4.append(l[4])

        emg_5 = []
        for l in emg:
            emg_5.append(l[5])

        emg_6 = []
        for l in emg:
            emg_6.append(l[6])

        emg_7 = []
        for l in emg:
            emg_7.append(l[7])

        emg_8 = []
        for l in emg:
            emg_8.append(l[8])

        emg_9 = []
        for l in emg:
            emg_9.append(l[9])


        # convert the lists to dataframe (emg, exercise, stimulus)

        newData = list(zip(emg_0, emg_1, emg_2, emg_3, emg_4, emg_5, emg_6, emg_7, emg_8, emg_9, exercise, stimulus))
        columns = ['emg_0', 'emg_1', 'emg_2', 'emg_3', 'emg_4', 'emg_5', 'emg_6', 'emg_7', 'emg_8', 'emg_9', 'exercise', 'stimulus']
        dataset_df = pd.DataFrame(newData, columns=columns)


        # Merge all dataframes into one dataframe

        if count == 1:
            dataset_all_df = dataset_df
            continue
        else:
            frames = [dataset_all_df, dataset_df]
            dataset_all_df = pd.concat(frames)


# Convert dataframe to csv file

print(dataset_all_df)
dataset_all_df.to_csv('sEMG_exercise_stimulus_DB1.csv')


