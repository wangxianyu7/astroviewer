import numpy as np
import matplotlib.pyplot as plt
import argparse
import os
import sys

def plot_data(filename, save, notshow):

    try:
        time,flux,flux_err = np.loadtxt(filename,unpack=True,delimiter=',')
    except:
        time,flux,flux_err = np.loadtxt(filename,unpack=True)

    plt.errorbar(time,flux,yerr=flux_err,fmt='.')

    if save:
        base_name = os.path.splitext(filename)[0]
        output_name = base_name + '.png'
        plt.savefig(output_name)

    if not notshow:
        plt.show()

def main():
    parser = argparse.ArgumentParser(description='Plot data from a file.')
    parser.add_argument('filename', type=str, help='The file to plot.')
    parser.add_argument('--save', action='store_true', help='Save the plot to a file.')
    parser.add_argument('--notshow', action='store_true', help='Do not display the plot.')
    args = parser.parse_args()

    plot_data(args.filename, args.save, args.notshow)

if __name__ == "__main__":
    main()
