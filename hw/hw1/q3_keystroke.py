#!user/bin/env python3
# _*_ coding: utf-8 _*_

import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from functools import reduce

subjects_len = 51
sIdx_len = 8
rep_len = 47
N = 5
magic_number = 1.126
report_log = True


def init_data_dict(subject_idx):
    data = {}.fromkeys(subject_idx)
    for k in data.keys():
        data[k] = {}.fromkeys(range(1, sIdx_len + 1))
        for s in data[k].keys():
            data[k][s] = []
    return data


def load_data(u):
    data_df = pd.read_csv(u)
    subject_idx = sorted(list(set(data_df["subject"])))
    data = {s: {} for s in subject_idx}
    for s in data.keys():
        data[s] = {sIdx: np.array(data_df[data_df.subject == s][data_df.sessionIndex == sIdx].as_matrix())[:, 2:]
                   for sIdx in range(1, sIdx_len + 1)}
    return data, subject_idx


def load_test_data(u):
    data = []
    with open(u) as f:
        for lines in f.readlines():
            l = lines.split(',')
            data.append((l[0], np.array(l[3:], dtype=np.float32)))
    return data, len(data)


def split_data(data, subject_idx, n=5):
    train_data = init_data_dict(subject_idx)
    val_data = init_data_dict(subject_idx)

    for s in subject_idx:
        for sIdx in range(1, sIdx_len + 1):
            mask = random.sample(range(1, rep_len + 1), n)

            for r in range(0, rep_len):
                if (r + 1) in mask:
                    val_data[s][sIdx].append(data[s][sIdx][r][1:])
                else:
                    train_data[s][sIdx].append(data[s][sIdx][r][1:])
            val_data[s][sIdx] = np.array(val_data[s][sIdx], dtype=np.float32)
            train_data[s][sIdx] = np.array(train_data[s][sIdx], dtype=np.float32)

    return train_data, val_data


def format_val_data(data):
    val_data = {}.fromkeys(data.keys())
    for k in val_data.keys():
        val_data[k] = []

    for s in data.keys():
        for sIdx in range(1, sIdx_len + 1):
            for r in range(len(data[s][sIdx])):
                val_data[s].append(data[s][sIdx][r])
        val_data[s] = np.array(val_data[s], dtype=np.float32)
    return val_data


def manhattan_distance(a, b):
    return np.sum(abs(a - b))


def euclid_distance(a, b):
    pass


def mean_std_feature(data, subject_idx):
    mean_feature = init_data_dict(subject_idx)
    std_feature = init_data_dict(subject_idx)
    for s in subject_idx:
        for sIdx in range(1, 9):
            mean_feature[s][sIdx] = np.mean(data[s][sIdx], axis=0)
            std_feature[s][sIdx] = np.std(data[s][sIdx], axis=0)
    return mean_feature, std_feature


def the_one(mean, std, subject_idx):
    the_mean = {}.fromkeys(range(1, sIdx_len + 1))
    the_std = {}.fromkeys(range(1, sIdx_len + 1))
    for sIdx in range(1, 9):
        the_mean[sIdx] = sum(mean[s][sIdx] for s in subject_idx) / len(subject_idx)
        the_std[sIdx] = sum(std[s][sIdx] for s in subject_idx) / len(subject_idx)
    return the_mean, the_std


def manhattan(mean, std, the_mean, the_std, subject_idx):
    mean_manhattan = init_data_dict(subject_idx)
    std_manhattan = init_data_dict(subject_idx)
    for s in subject_idx:
        for sIdx in range(1, 9):
            mean_manhattan[s][sIdx] = manhattan_distance(mean[s][sIdx], the_mean[sIdx])
            std_manhattan[s][sIdx] = manhattan_distance(std[s][sIdx], the_std[sIdx])
    return mean_manhattan, std_manhattan


def check(r, mean_s, std_s, threshold):
    for sIdx in mean_s.keys():
        if manhattan_distance(r, mean_s[sIdx]) < threshold:
            return True
    return False


def log(the_time, fun_name):
    print("%f seconds, %s." % (time.time() - the_time, fun_name)) if report_log else None
    return time.time()


def main():
    start_time = the_time = time.time()

    data, subject_idx = load_data("KeyboardData.csv")
    train_data, val_data = split_data(data, subject_idx)
    val_data = format_val_data(val_data)
    test_data, test_len = load_test_data("KeyboardTestData.csv")
    the_time = log(the_time, "load split data")

    """Train Data Feature"""
    mean, std = mean_std_feature(train_data, subject_idx)
    # the_mean, the_std = the_one(mean, std, subject_idx)
    # mean_manhattan, std_manhattan = manhattan(mean, std, the_mean, the_std, subject_idx)
    the_time = log(the_time, "Train Data Feature")

    """VC Test"""
    # threshold_l = []
    # TPR_l = []
    # FPR_l = []
    #
    # for i in list(range(0, 240)):
    #     # threshold
    #     threshold = magic_number * i * 0.025
    #     threshold_l.append(threshold)
    #
    #     # TPR
    #     TP = 0
    #     P = subjects_len * sIdx_len * N  # 2040
    #     for s in val_data.keys():
    #         for r in val_data[s]:
    #             if check(r, mean[s], std[s], threshold):
    #                 TP += 1
    #     TPR = TP / P
    #     TPR_l.append(TPR)
    #
    #     # FPR
    #     FP = 0
    #     Neg = (subjects_len - 1) * subjects_len * sIdx_len * N  # 102000
    #     for s in val_data.keys():
    #         for r in val_data[s]:
    #             for ss in mean.keys():
    #                 if ss != s:
    #                     if check(r, mean[ss], std[ss], threshold):
    #                         FP += 1
    #     FPR = FP / Neg
    #     FPR_l.append(FPR)
    #
    #     the_time = log(the_time, str(i) + ' ' + str(threshold) + ' ' + str(TPR) + ' ' + str(FPR))
    #
    # plt.plot(threshold_l, TPR_l)
    # plt.title("Correct_Rate\nthreshold = 1.126*[0, 240]*0.025")
    # plt.savefig("correct_rate")
    # plt.cla()
    # plt.plot(FPR_l, TPR_l)
    # plt.title("ROC")
    # plt.savefig("ROC")
    # the_time = log(the_time, "VC")

    threshold = 1.8

    """Predict"""
    pre = [0] * test_len
    for i in range(test_len):
        s = test_data[i][0]
        if not check(test_data[i][1], mean[s], std[s], threshold):
            pre[i] = 1
    # print(pre)
    np.savetxt("answer.csv", pre, fmt='%d', delimiter=",")
    the_time = log(the_time, "Predict")

    print("\nTotal %f seconds" % (the_time - start_time))
    pass


if __name__ == "__main__":
    main()
