import numpy as np


def load_data():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]


# 初始化项集(单项集)
def init_set0(data):
    set0 = []
    for tran in data:
        for item in tran:
            if not [item] in set0:
                set0.append([item])

    set0.sort()
    return map(frozenset, set0)


# 计算项集支持度，返回支持度合格的项集
def cal_supp(data, c_set, min_supp):
    support_dic = {}
    # 遍历完一次map后，会返回一个空列表，所以如果不事先将其存在另一个变量中，map只能访问一次。
    c_set = list(c_set)
    for curr_set in c_set:
        for curr_data in data:
            if curr_set.issubset(curr_data):
                if support_dic.get(curr_set, 0) == 0:
                    support_dic[curr_set] = 1
                else:
                    support_dic[curr_set] += 1

    new_set = []
    for curr_set in c_set:
        support_dic[curr_set] = support_dic[curr_set]/len(data)
        if support_dic[curr_set] >= min_supp:
            new_set.append(curr_set)

    return new_set, support_dic


# 遍历所有项集，合并项集产生新的项集
def apriori_gen(k, set_k):
    new_set = []
    len_set = len(set_k)
    for i in range(len_set):
        for j in range(i+1, len_set):
            set1 = list(set_k[i])[:k-2]
            set2 = list(set_k[j])[:k-2]
            set1.sort(); set2.sort()
            if set1 == set2:
                new_set.append(set_k[i] | set_k[j])

    return new_set


def apriori(data, min_support=0.5):
    set0 = init_set0(data)
    s1, support_dict = cal_supp(data, set0, min_support)
    s = [s1]
    k = 2
    while len(s[k-2]) > 0:
        new_set = apriori_gen(k, s[k-2])
        s2, support_s2 = cal_supp(data, new_set, min_support)
        support_dict.update(support_s2)
        s.append(s2)
        k += 1
    return s, support_dict


d = load_data()
s, supp = apriori(d)
print(s)
