import numpy as np
from pandas import read_csv
import tensorflow as tf
import csv

# columns:
# 'PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'
# want keep:
# 'Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'
#  num, one hot, one hot, num, num, num, num, one hot
data = []
cols_to_keep = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
cols_to_onehot = ['Pclass', 'Sex', 'Embarked']
cols_to_float = ['Age', 'Fare']

one_hot_3 = [[1,0,0], [0,1,0],[0,0,1]]
one_hot_2 = [[1,0],[0,1]]

one_hot_pclass = ['1', '2','3']
one_hot_sex = ['male', 'female']
one_hot_embarked = ['C', 'Q', 'S']
one_hot_labels = [one_hot_pclass, one_hot_sex, one_hot_embarked]


with open('train.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    colnames = []
    for row in reader:
        if line_count == 0:
            print(row)
            colnames = row
            line_count = line_count + 1
        else:
            data_point = dict()
            for i in range(len(colnames)):
                if colnames[i] in cols_to_keep:
                    if colnames[i] in cols_to_onehot:
                        one_hot_label = one_hot_labels[cols_to_onehot.index(colnames[i])]
                        value_index = one_hot_label.index(row[i])
                        if len(one_hot_label) == 3:
                            data_point[colnames[i]] = one_hot_3[value_index]
                        else:
                            data_point[colnames[i]] = one_hot_2[value_index]
                    else:
                        if colnames[i] not in cols_to_float:

                            data_point[colnames[i]] = int(row[i])
                        else:
                            data_point[colnames[i]] = float(row[i])
            data.append(data_point)
            line_count = line_count + 1

print(type(data[0]['Survived']))
print(len(data))







