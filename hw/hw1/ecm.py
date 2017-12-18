#!user/bin/env python3
# _*_ coding: utf-8 _*_

import time
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from functools import reduce
from numpy import linalg as LA

path = "hw1/"
users_num = 50
L = 100  # a series of sequences
train_seq = 50
test_seq_begin = train_seq + 1
w = 6  # window size, accordance with paper
is_sub = True
report_log = True


def get_commands(user):
    with open(path + user) as f:
        return [c.split()[0] for c in f.readlines()]


def load_data():
    users = ["User" + str(u) for u in range(1, users_num + 1)]
    u_d = {u: get_commands(users[u - 1]) for u in range(1, users_num + 1)}
    return users, u_d


def load_ref():
    ref = np.loadtxt(path + "reference.txt")
    return ref.T


def err_01(y_pre, y):  # 1, -1
    return np.count_nonzero(y_pre != y) / len(y)


def total_commands(user_dict):
    seq = reduce((lambda x, y: x + y), [user_dict[u][:5000] for u in range(1, users_num + 1)])
    return list(set(seq)), Counter(seq)


def sub_commands(cmd_freq, top):
    return [_[0] for _ in cmd_freq.most_common(top)]


def observation_events(user_dict, user, seq):
    return user_dict[user][L * (seq - 1):L * seq]


# use for Qa
def co_occurrence_rm_ls(user_dict):
    cmd1 = "rm"
    cmd2 = "ls"
    co = []
    for u in [1, 2]:
        u_seq = []
        for s in range(1, 6):
            seq = observation_events(user_dict, u, s)
            c = sum(seq[_:_ + w].count(cmd2) if seq[_] == cmd1 else 0 for _ in range(len(seq)))
            u_seq.append(c)
        co.append(u_seq)
    return co


# train means seq length
def co_occurrence(user_dict, cmd, users, train, train_begin=1):
    m = len(cmd)
    co = []
    for u in range(1, users + 1):
        u_seq = []
        for s in range(train_begin, train_begin + train):
            seq = observation_events(user_dict, u, s)
            each_co = np.zeros((m, m))
            for i in range(m):
                for j in range(m):
                    c = sum(seq[_:_ + w].count(cmd[j]) if seq[_] == cmd[i] else 0 for _ in range(len(seq)))
                    each_co[i][j] = c
            u_seq.append(each_co.tolist())
        co.append(u_seq)
    return np.array(co)


def norm_co(co):
    mean = np.zeros(co[0][0].shape)
    for u in co:
        for s in u:
            mean += s
    mean = mean / (co.shape[0] * co.shape[1])
    for u in co:
        for s in u:
            s -= mean
    return co
    # return co - np.ones(co.shape) * np.mean(co)


def co_matrix(norm_co_occurrence):
    cmd_len = norm_co_occurrence.shape[-1]
    covariance_matrix = np.zeros((cmd_len ** 2, cmd_len ** 2))
    for u in norm_co_occurrence:
        for s in u:
            s = np.matrix(s.reshape(cmd_len ** 2))
            covariance_matrix += s.T * s
    return covariance_matrix


def eign(co_mat_sub, top_cmd):
    eigenvalues, eigenvectors = LA.eig(co_mat_sub)
    eigenvectors = np.array([v.reshape((top_cmd, top_cmd)) for v in eigenvectors])
    return eigenvalues.real, eigenvectors.real


def contribution_rate(eigenvalues, n):
    return sum(eigenvalues[:n]) / sum(eigenvalues)


def plot_contribution_rate(eigenvalues, top_cmd):
    rates = [contribution_rate(eigenvalues, N) for N in range(top_cmd)]
    plt.plot([N for N in range(top_cmd)], rates)
    plt.ylim(0, 1.1)
    plt.title("Contribution_Rate\nusers_num_sub=2 train_seq_sub=5 top_cmd=70")
    plt.savefig("contribution_rate")
    return rates


def feature_vector(user_dict, cmd_sub, user, top_cmd, N, train_begin, train_seq_sub=1):
    co_sub = co_occurrence(user_dict, cmd_sub, user, train_seq_sub, train_begin)
    co_mat_sub = co_matrix(co_sub)
    eigenvalues, eigenvectors = eign(co_mat_sub, top_cmd)

    fv = []
    a_hat = np.matrix(co_sub[0][0].reshape(top_cmd ** 2))
    for n in range(N):
        vi = np.matrix(eigenvectors[n].reshape(top_cmd ** 2))
        fv.append(float(vi * a_hat.T))
    return np.array(fv), eigenvectors[:N]


def user_fv(user_dict, cmd_sub, user, train_seq_sub, top_cmd, N):
    return np.array([feature_vector(user_dict, cmd_sub, user, top_cmd, N, tr)[0] for tr in range(1, train_seq_sub + 1)])


# train_seq_sub just means squ_sub length
def network(user_dict, cmd_sub, user, top_cmd, N, train_seq_sub, seq_begin=1):
    the_time = time.time()
    net = []
    for s in range(seq_begin, seq_begin + train_seq_sub):
        fv, eigenvectors = feature_vector(user_dict, cmd_sub, user, top_cmd, N, s)
        layer = np.array([fv[_] * eigenvectors[_] for _ in range(N)])
        net.append(layer)
        the_time = log(the_time, "network seq " + str(s))
    return sum(np.array(net))


def sim_layer(lay1, lay2, top_cmd):
    if np.sum(lay1) == 0 or np.sum(lay2) == 0:
        return 0
    else:
        return (lay1.reshape(top_cmd ** 2).dot(lay2.reshape(top_cmd ** 2))) / (np.sum(lay1) * np.sum(lay2))


# cosine similarity
def sim_net(h, N, top_cmd, net, net_test):
    net = np.where(net > h, 1, 0)
    net_test = np.where(net_test > h, 1, 0)
    sim = sum([sim_layer(net[n], net_test[n], top_cmd) for n in range(N)])
    return sim


def log(the_time, fun_name):
    print("%f seconds, %s." % (time.time() - the_time, fun_name)) if report_log else None
    return time.time()


def main():
    start_time = the_time = time.time()
    users, user_dict = load_data()
    cmd, cmd_freq = total_commands(user_dict)
    the_time = log(the_time, "total_commands")
    m = len(cmd)  # total # of commands
    reference = load_ref()

    """Qa Qb Qc"""
    # print("Qa\nm, total # of commands:", len(cmd))
    # co_rm_ls = co_occurrence_rm_ls(user_dict)
    # print("User1:", co_rm_ls[0], "\nUser2:", co_rm_ls[1])
    # print("Qb\nnorm co_occurrence\n", norm_co(co_rm_ls))
    # print("Qc\nCovariance Matrix:", co_matrix(norm_co(co_rm_ls)))

    # For performance reason: just test a VERY VERY smell data set
    if is_sub:
        users_num_sub, train_seq_sub, top_cmd = 2, 50, 50
    else:
        users_num_sub, train_seq_sub, top_cmd = users_num, train_seq, m

    cmd_sub = sub_commands(cmd_freq, top_cmd)
    the_time = log(the_time, "sub_commands")

    """Qd"""
    # co_sub = co_occurrence(user_dict, cmd_sub, users_num_sub, train_seq_sub)
    # norm_co_sub = norm_co(co_sub)
    # co_mat_sub = co_matrix(norm_co_sub)
    # eigenvalues, eigenvectors = eign(co_mat_sub, top_cmd)
    # rates = plot_contribution_rate(eigenvalues, top_cmd)
    # the_time = log(the_time, "plot_contribution_rate")
    N = top_cmd // 4

    """Qe"""
    # for u in [1, 2]:
    #     fv = user_fv(user_dict, cmd_sub, u, train_seq_sub, top_cmd, N)
    #     np.savetxt("user" + str(u) + "FV.csv", fv, fmt='%.4f', delimiter=",")

    """Qf Qg"""
    h = 0  # Threshold for positive and negative network models
    r = 0.03  # Threshold for cosine similarity

    # u = 2  # Just test User 2
    # net = network(user_dict, cmd_sub, u, top_cmd, N, train_seq_sub)
    # the_time = log(the_time, "network user " + str(u))
    #
    # tests = 100  # 100 test seqs, 1 seq per test, total,100 tests
    # sim = []
    # for t in range(tests):
    #     net_test = network(user_dict, cmd_sub, u, top_cmd, N, 1, test_seq_begin + t)
    #     sim.append(sim_net(h, N, top_cmd, net, net_test))
    #     the_time = log(the_time, "test " + str(t))
    # pre = np.where(np.array(sim) > r, 1, 0)
    # ref = reference[u - 1][:tests]
    # err_rate = err_01(pre, ref)

    """Qe"""
    u = 21
    r = 0.014
    # net = network(user_dict, cmd_sub, u, top_cmd, N, train_seq_sub)
    # the_time = log(the_time, "network user " + str(u))
    #
    # tests = 100
    # sim = []
    # for t in range(tests):
    #     net_test = network(user_dict, cmd_sub, u, top_cmd, N, 1, test_seq_begin + t)
    #     sim.append(sim_net(h, N, top_cmd, net, net_test))
    #     the_time = log(the_time, "test " + str(t + 1))
    # np.savetxt("user21rate.csv", np.array(sim), fmt='%.4f', delimiter=",")
    # pre = np.where(np.array(sim) > r, 1, 0)
    # np.savetxt("user21.csv", pre, fmt='%d', delimiter=",")

    print("\nTotal %f seconds" % (time.time() - start_time))
    pass


if __name__ == "__main__":
    main()
