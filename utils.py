import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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
    f.show()


def plot_scatters(in_offs, out_of_offs, RDxline=True, label='RD'):
    plt.figure(figsize=(9,7))
    if RDxline:
        plt.scatter(in_offs.W, in_offs[label], c='r')
        plt.scatter(out_of_offs.W, out_of_offs[label], c='b')
        plt.xlabel('Wins')
        plt.ylabel(label)
        plt.axvline(99, 0, 1, color='Black', ls='--')
    else:
        plt.scatter(in_offs[label], in_offs.W, c='r')
        plt.scatter(out_of_offs[label], out_of_offs.W, c='b')
        plt.ylabel('Wins')
        plt.xlabel(label)
        plt.axhline(99, 0, 1, color='Black', ls='--')
    plt.show()


def plot_deriving_slope(x, y):
    # Deriving slope,intercept values
    slope, intercept = np.polyfit(x, y, 1)
    abline_values = [slope * i + intercept for i in x]
    # Plotting the figure
    plt.figure(figsize=(10, 8))
    plt.scatter(x, y)
    plt.plot(x, abline_values, 'b')
    plt.title("Slope = %s" % (slope))
    plt.xlabel("Run Difference")
    plt.ylabel("Wins")
    plt.show()


def set_up_display(data_frame):
    pd.options.display.max_rows = data_frame.shape[0]
    pd.options.display.max_columns = 20
    pd.options.display.width = 1000
