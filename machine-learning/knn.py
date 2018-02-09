# k-近邻算法
from numpy import *
import operator
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    label = ['A', 'A', 'B', 'B']
    return group, label


def classify0(in_x, data_set, labels, k):
    data_set_size = data_set.shape[0]
    diff_mat = tile(in_x, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat ** 2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances ** 0.5
    sorted_dist_indices = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_i_label = labels[sorted_dist_indices[i]]
        class_count[vote_i_label] = class_count.get(vote_i_label, 0) + 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def file_to_matrix(filename):
    fr = open(filename)
    number_of_lines = len(fr.readlines())  # get the number of lines in the file
    return_mat = zeros((number_of_lines, 3))  # prepare matrix to return
    class_label_vector = []  # prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        list_from_line = line.split('\t')
        return_mat[index, :] = list_from_line[0:3]
        class_label_vector.append(int(list_from_line[-1]))
        index += 1
    return return_mat, class_label_vector


def auto_norm(data_set):
    min_vals = data_set.min(0)
    max_vals = data_set.max(0)
    ranges = max_vals - min_vals
    norm_data_set = zeros(shape(data_set))
    m = data_set.shape[0]
    norm_data_set = data_set - tile(min_vals, (m, 1))
    norm_data_set = norm_data_set / tile(ranges, (m, 1))  # element wise divide
    return norm_data_set, ranges, min_vals


def datingClassTest():
    hoRatio = 0.50  # hold out 10%
    datingDataMat, datingLabels = file_to_matrix('datingTestSet2.txt')  # load data setfrom file
    normMat, ranges, minVals = auto_norm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    print('total record is {}, classifier num is {}'.format(m, numTestVecs))
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print("the total error rate is: %f" % (errorCount / float(numTestVecs)))
    print(errorCount)


if __name__ == '__main__':
    group, label = createDataSet()
    # print(group, label)

    x = [item[0] for item in group]
    y = [item[1] for item in group]

    # print(classify0([0, 0], group, label, 3))
    dating_data_mat, dating_label = file_to_matrix('datingTestSet.txt')
    # print(dating_data_mat)
    # print(dating_label)

    norm_mat, ranges, min_vals = auto_norm(dating_data_mat)
    print(norm_mat)
    print(ranges)
    print(min_vals)
    # 显示散点
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # 冰淇淋公升与打游戏比例
    # ax.scatter(dating_data_mat[:, 1], dating_data_mat[:, 2])
    # plt.xlabel(u'玩游戏所耗时间')
    # plt.ylabel(u'每周消耗冰淇淋')
    # 里程与游戏百分比
    ax.scatter(dating_data_mat[:, 0], dating_data_mat[:, 1], 15.0 * array(dating_label), 15.0 * array(dating_label))
    plt.xlabel(u'飞行历程数')
    plt.ylabel(u'游戏百分比')
    # 里程与冰淇淋公升
    # ax.scatter(dating_data_mat[:, 0], dating_data_mat[:, 2])
    # plt.xlabel(u'飞行历程数')
    # plt.ylabel(u'冰淇淋升数')
    # plt.show()
    datingClassTest()
