import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)


def task2(name):
    data = pd.read_csv(name)
    print(data[:10])
    print(data['Agency'][:10])
    print(data[['Agency', 'Business Title', 'Work Location 1']])


def task3(name):
    data = pd.read_csv(name)
    data['Agency'].value_counts(sort=True).plot(kind='bar')
    plt.show()


def task4(name):
    data = pd.read_csv(name)
    data['median'] = data.groupby('Salary Range From')['Salary Range To'].transform(np.median)
    gb = data.groupby('Agency')
    data1 = pd.DataFrame([data.loc[gb.groups[n], 'median'].values for n in gb.groups], index=gb.groups.keys())
    data1 = data1.median(axis=1)
    data1.plot(kind='bar')
    plt.show()

    gb = data.groupby('Work Location')
    data1 = pd.DataFrame([data.loc[gb.groups[n], 'median'].values for n in gb.groups], index=gb.groups.keys())
    data1 = data1.median(axis=1)
    data1[:100].plot(kind='bar')
    plt.show()


#task2('NYC_Jobs.csv')
#task3('NYC_Jobs.csv')
task4('NYC_Jobs.csv')
