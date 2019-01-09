import pickle
import os, sys


def load_dictionary(filename):

    dic = {}

    with open(filename, 'r') as fp:
        dic = pickle.load(fp)

    return dic

def merge_with_large(large_dic, dic):

    count = 0
    for key, val in dic.iteritems():
        if key in large_dic:
            count +=1
        large_dic[key] = val

    print "Total common : " + str(count)


if __name__ == "__main__":

    total_lines = int(sys.argv[1])
    n_jobs = int(sys.argv[2])

    large_dic = {}

    for i in range(n_jobs):
        for file in os.listdir("parallel_runs/" + str(i + 1)):
            if "langdetect" in file:
                filename = os.path.join("parallel_runs/" + str(i + 1) + "/", file)
                break
        dic = load_dictionary(filename)
        merge_with_large(large_dic, dic)

    print len(large_dic)
    print total_lines

    with open("langid_collection_dic.pkl", 'w') as fp:
        pickle.dump(large_dic, fp)


