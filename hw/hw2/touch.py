#!user/bin/env python3
# _*_ coding: utf-8 _*_

import time
import warnings
import numpy as np
import pandas as pd
from collections import Counter
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
np.set_printoptions(precision=6, suppress=True)

file = "feature.csv"
magic_number = 1.126
report_log = True
feature_name = []
FEATURES = 30
BINS = 50


def load_data(f):
    df = pd.read_csv(f)
    # remove useless feature
    df = df.drop(['change_of_finger_orientation'], axis=1)
    # remove +/-inf, NaN
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.dropna(axis=0, how='any')
    return df


def log(the_time, fun_name):
    print("%f seconds, %s." % (time.time() - the_time, fun_name)) if report_log else None
    return time.time()


def discrete_features(feature_pd, bins):
    for f in feature_pd.columns[:-2]:
        if f != "up_down_left_right_flag":
            b = np.floor((feature_pd[f] - bins[f][0]) / bins[f][2])
            b = np.where(b > -1, b, np.nan)
            b = np.where(b < BINS, b, np.nan)
            feature_pd[f] = b
    return feature_pd


def entropy(f_np):
    ent = 0
    for f in range(f_np.shape[1]):
        l = len(f_np[:, f])
        ff = f_np[:, f]
        c = Counter(ff[~np.isnan(ff)])
        for k in c.keys():
            p = c[k] / l
            ent -= p * np.log(p)
    return ent


def condition_entropy(discrete_features_pd, features, f_idx):
    condition_ent = 0
    l = len(discrete_features_pd[features[f_idx]])
    f = np.array(discrete_features_pd[features[f_idx]])
    c = Counter(f[~np.isnan(f)])
    for k in c.keys():
        cpd = discrete_features_pd.loc[discrete_features_pd[features[f_idx]] == k]
        cpd = cpd.drop([features[f_idx]], axis=1)
        e = entropy(np.array(cpd))
        condition_ent += e * c[k] / l
    return condition_ent


def f1_knn(data, label_np):
    k_f1 = []
    for k in range(1, 8):
        f1_list = []
        for u in np.sort(list(set(label_np))):
            label = [int(l == u) for l in label_np]
            neigh = KNeighborsClassifier(k)
            f1 = np.mean(cross_val_score(neigh, data, label, cv=10, scoring='f1'))
            f1_list.append(f1)
        k_f1.append([k, np.mean(f1_list)])
        print(k, np.mean(f1_list))

    best_idx = np.argmax(k_f1, axis=0)[1]
    k_best, f1_best = k_f1[best_idx][0], k_f1[best_idx][1]
    return k_best, f1_best


def f1_svm(data, label_np):
    f1_list = []
    for u in np.sort(list(set(label_np))):
        label = [int(l == u) for l in label_np]
        rbf = SVC(kernel='rbf')
        f1 = np.mean(cross_val_score(rbf, data, label, cv=10, scoring='f1'))
        print(u, f1)
        f1_list.append(f1)
    return np.mean(f1_list)


def main():
    start_time = the_time = time.time()

    """Load Data"""
    df = load_data(file)
    the_time = log(the_time, "Load Data")

    """Feature Label"""
    data_length = len(df.index)
    label_pd = df[["user_id", "doc_id", "phone_id"]]
    labels = np.array(label_pd.columns)
    feature_pd = df.drop(["user_id", "doc_id", "phone_id"], axis=1)
    features = np.array(feature_pd.columns)
    the_time = log(the_time, "Feature Label")

    """Corr"""
    # corr = feature_pd.corr()
    # corr.to_csv("corr.csv")
    # the_time = log(the_time, "Corr")

    """Bins"""
    # gaps = np.array(feature_pd.quantile([0.1, 0.9]), dtype=np.float32)
    # bins = {features[i]: (gaps[0][i], gaps[1][i], (gaps[1][i] - gaps[0][i]) / BINS) for i in range(FEATURES)}
    # discrete_features_pd = discrete_features(feature_pd, bins)
    # the_time = log(the_time, "Bins")

    """bins distribution"""
    # for f in discrete_features_pd.columns[:-2]:
    #     p = np.array(discrete_features_pd[f] < 0, dtype=int)
    #     print("-inf, 0    ", np.count_nonzero(p) / len(discrete_features_pd[f]))
    #     for i in range(0, 50):
    #         p = np.array((discrete_features_pd[f] == i), dtype=int)
    #         print(i, '    ', np.count_nonzero(p) / len(discrete_features_pd[f]))
    #     p = np.array(discrete_features_pd[f] > 49, dtype=int)
    #     print("49, +inf    ", np.count_nonzero(p) / len(discrete_features_pd[f]))
    #     break

    """Entropy"""
    # ent = entropy(np.array(discrete_features_pd))
    # print("entropy", ent)
    # the_time = log(the_time, "Entropy")

    """Information Gain, Mutual information, Top 10"""
    # f_ig = []
    # for f_idx in range(FEATURES):
    #     condition_ent = condition_entropy(discrete_features_pd, features, f_idx)
    #     ig = ent - condition_ent
    #     mutual_information = 1 - condition_ent / ent
    #     f_ig.append([f_idx, condition_ent, ig])
    #     print(f_idx+1, features[f_idx], condition_ent, ig, mutual_information)
    # the_time = log(the_time, "Info Gain")
    # f_ig = np.array(f_ig)
    # top = f_ig[np.argsort(f_ig[:, 2])[::-1]]
    # top_10_idx = top[:10, 0]
    # the_time = log(the_time, "Top 10")

    top_10_idx = [21, 9, 24, 12, 11, 1, 14, 7, 13, 17]
    top_features = features[top_10_idx]
    top_features_pd = feature_pd[top_features]

    feature_np = np.array(feature_pd)
    top_features_np = np.array(top_features_pd)
    label_np = np.array(label_pd)[:, 0]

    print("Top 10")
    print(f1_knn(top_features_np, label_np))
    # print(f1_svm(top_features_np, label_np))
    the_time = log(the_time, "Top 10")
    print("All 30")
    print(f1_knn(feature_np, label_np))
    # print(f1_svm(top_features_np, label_np))
    the_time = log(the_time, "All 30")

    print("\nTotal %f seconds" % (the_time - start_time))
    pass


if __name__ == "__main__":
    main()
