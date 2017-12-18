#!user/bin/env python3
# _*_ coding: utf-8 _*_

import time
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib import ticker
from matplotlib import rc

warnings.filterwarnings("ignore")
np.set_printoptions(precision=6, suppress=True)

file = "server-log.csv"
magic_number = 1.126
gap = 600
step = 25
report_log = False


def load_data(f):
    df = pd.read_csv(f, sep=' ')
    df = df.drop(['idx', 'start_date'], axis=1)
    df["start_second"] = df["start_time"].apply(
        lambda t: sum([a * b for a, b in zip([3600, 60, 1], map(int, t.split(':')))]))
    df["duration_second"] = df["duration"].apply(
        lambda t: sum([a * b for a, b in zip([3600, 60, 1], map(int, t.split(':')))]))
    df["src_port"].replace('-', 0, inplace=True)
    df["dest_port"].replace('-', 0, inplace=True)
    return df


def entropy(f_np):
    ent = 0
    c = Counter(f_np)
    for k in c.keys():
        p = c[k] / len(f_np)
        ent -= p * np.log(p)
    return ent


def log(the_time, fun_name):
    print("%f seconds, %s." % (time.time() - the_time, fun_name)) if report_log else None
    return time.time()


def main():
    start_time = the_time = time.time()
    df = load_data(file)
    df = df.drop(["start_time", "duration", "start_second"], axis=1)

    l = int(np.floor(len(df) / step))

    for c in df.columns:
        min_list = []
        e_list = []
        for i in range(l):
            the_bin = step * i
            min_list.append(the_bin + gap / 2)
            s = df[str(c)]
            s = np.array(s[the_bin: the_bin + gap])
            e = entropy(s)
            e_list.append(e)

        rc('xtick', labelsize=8)
        fig, ax = plt.subplots(figsize=(40, 5))
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1000))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(100))
        ax.grid(True)
        ax.plot(min_list, e_list)
        plt.title(str(c))
        plt.savefig(str(c))
        plt.cla()

        the_time = log(the_time, str(c))

    print("\nTotal %f seconds" % (the_time - start_time))
    pass


if __name__ == "__main__":
    main()
