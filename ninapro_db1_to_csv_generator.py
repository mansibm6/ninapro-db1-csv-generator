from scipy.io import loadmat
import pandas as pd
import os
import csv


# Access the mat file

count = 0
inputpath = 'D:/Machine Learning/Projects/sEMG based movement recognition/Datasets'
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


        # modify subject and convert it to numbers instead of lists

        element_subject = subject[0]
        for i in range(len(emg)) :
            subject.append(element_subject)

        for i in range(len(subject)):
            x = subject[i]
            y = x[0]
            subject[i] = y


        # modify repetition and convert it to numbers instead of lists

        element_repetition = repetition[0]
        for i in range(len(emg)) :
            repetition.append(element_repetition)

        for i in range(len(repetition)):
            x = repetition[i]
            y = x[0]
            repetition[i] = y


        # modify restimulus and convert it to numbers instead of lists

        element_restimulus = restimulus[0]
        for i in range(len(emg)) :
            restimulus.append(element_restimulus)

        for i in range(len(restimulus)):
            x = restimulus[i]
            y = x[0]
            restimulus[i] = y


        # modify rerepetition and convert it to numbers instead of lists

        element_rerepetition = rerepetition[0]
        for i in range(len(emg)) :
            rerepetition.append(element_rerepetition)

        for i in range(len(rerepetition)):
            x = rerepetition[i]
            y = x[0]
            rerepetition[i] = y


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


        # create 22 columns for glove data

        glove_0 = []
        for l in glove:
            glove_0.append(l[0])

        glove_1 = []
        for l in glove:
            glove_1.append(l[1])

        glove_2 = []
        for l in glove:
            glove_2.append(l[2])

        glove_3 = []
        for l in glove:
            glove_3.append(l[3])

        glove_4 = []
        for l in glove:
            glove_4.append(l[4])

        glove_5 = []
        for l in glove:
            glove_5.append(l[5])

        glove_6 = []
        for l in glove:
            glove_6.append(l[6])

        glove_7 = []
        for l in glove:
            glove_7.append(l[7])

        glove_8 = []
        for l in glove:
            glove_8.append(l[8])

        glove_9 = []
        for l in glove:
            glove_9.append(l[9])

        glove_10 = []
        for l in glove:
            glove_10.append(l[10])

        glove_11 = []
        for l in glove:
            glove_11.append(l[11])

        glove_12 = []
        for l in glove:
            glove_12.append(l[12])

        glove_13 = []
        for l in glove:
            glove_13.append(l[13])

        glove_14 = []
        for l in glove:
            glove_14.append(l[14])

        glove_15 = []
        for l in glove:
            glove_15.append(l[15])

        glove_16 = []
        for l in glove:
            glove_16.append(l[16])

        glove_17 = []
        for l in glove:
            glove_17.append(l[17])

        glove_18 = []
        for l in glove:
            glove_18.append(l[18])

        glove_19 = []
        for l in glove:
            glove_19.append(l[19])

        glove_20 = []
        for l in glove:
            glove_20.append(l[20])

        glove_21 = []
        for l in glove:
            glove_21.append(l[21])


        # convert the lists to dataframe (emg, exercise, stimulus)

        newData = list(zip(emg_0, emg_1, emg_2, emg_3, emg_4, emg_5, emg_6, emg_7, emg_8, emg_9, glove_0, glove_1, glove_2, glove_3, glove_4, glove_5, glove_6, glove_7, glove_8, glove_9, glove_10, glove_11, glove_12, glove_13, glove_14, glove_15, glove_16, glove_17, glove_18, glove_19, glove_20, glove_21, exercise, stimulus, restimulus, repetition, rerepetition, subject))
        columns = ['emg_0', 'emg_1', 'emg_2', 'emg_3', 'emg_4', 'emg_5', 'emg_6', 'emg_7', 'emg_8', 'emg_9', 'glove_0', 'glove_1', 'glove_2', 'glove_3', 'glove_4', 'glove_5', 'glove_6', 'glove_7', 'glove_8', 'glove_9', 'glove_10', 'glove_11','glove_12', 'glove_13', 'glove_14', 'glove_15', 'glove_16', 'glove_17', 'glove_18', 'glove_19', 'glove_20', 'glove_21', 'exercise', 'stimulus', 'restimulus', 'repetition', 'rerepetition', 'subject']
        dataset_df = pd.DataFrame(newData, columns=columns)


        # Merge all dataframes into one dataframe

        if count == 1:
            dataset_all_df = dataset_df
            continue
        else:
            frames = [dataset_all_df, dataset_df]
            dataset_all_df = pd.concat(frames)


# Convert dataframe to csv file

print(dataset_all_df.columns.tolist())
print(dataset_all_df.describe())
dataset_all_df.to_csv('Ninapro_DB1.csv')


