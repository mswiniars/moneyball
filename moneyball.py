import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_histograms(data_frame):
    f, ax = plt.subplots(2, 2)
    ax[0, 0].hist(data_frame.RS, bins=50)
    ax[0, 0].set_title("Runs Scored")
    ax[0, 1].hist(data_frame.RA, bins=50)
    ax[0, 1].set_title("Runs Allowed")
    ax[1, 0].hist(data_frame.OBP, bins=50)
    ax[1, 0].set_title("On Base Percentage")
    ax[1, 1].hist(data_frame.SLG, bins=50)
    ax[1, 1].set_title("Slugging Percentage")
    f.subplots_adjust(hspace=0.2)
    f.set_figheight(7)
    f.set_figwidth(9)
    plt.show()


def plot_scatters(in_offs, out_of_offs):
    plt.figure(figsize=(9,7))
    plt.scatter(in_offs.W, in_offs.RD, c='r')
    plt.scatter(out_of_offs.W, out_of_offs.RD, c='b')
    plt.xlabel('Wins')
    plt.ylabel('Runs Difference')
    plt.axvline(99, 0, 1, color='Black', ls='--')
    plt.show()


df = pd.read_csv('baseball.csv')
df = df[df['Year'] < 2002]
pd.options.display.max_rows = df.shape[0]
pd.options.display.max_columns = 20
pd.options.display.width = 1000
df['RD'] = df['RS'] - df['RA']
list_of_columns = list(df.columns.values)
list_of_columns.insert(5, list_of_columns.pop(-1))
df = df[list_of_columns]

print(np.random.rand(3,))
print(np.random.randint(0, 255, 3))
print(df)

in_playoffs = df[df['Playoffs'] == 1]
out_of_playoffs = df[df['Playoffs'] == 0]
plot_scatters(in_playoffs, out_of_playoffs)
