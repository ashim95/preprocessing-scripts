import langid
import pickle, sys

from langid import LanguageIdentifier, model
from joblib import Parallel, delayed

identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)

def create_n_splits(total, n):

    list_idx = [i for i in range(total)]

    tuples = []
    start = 0
    s = total / n

    for i in range(n):
        stop = start + s

        if i == n-1:
            stop = total
        tuples.append((start, stop))
        start = stop

    return tuples

def process_lines(start, stop, dir_id):

    fp = open("parallel_runs/" + str(dir_id + 1) + "/test.txt", 'r')

    dic = {}

    i = 0
    for line in fp:
        if i >= start:
            text = line.strip()
            out_langid = identifier.classify(unicode(text, "utf-8"))
            dic[i] = (text, out_langid)
            i +=1
            if i == stop:
                break
        else:
            i +=1

    fp.close()
    with open("parallel_runs/" +str(dir_id + 1) + "/langid_en_" + str(start) + "_" + str(stop) + ".pkl", 'w') as fpk:
        pickle.dump(dic, fpk)

    print "Exiting for direcory Id "  + str(dir_id + 1)

if __name__ == "__main__":

    total_lines = int(sys.argv[1])
    n_jobs = int(sys.argv[2])

    split_tuples = create_n_splits(total_lines, n_jobs)
    print split_tuples

    Parallel(n_jobs=n_jobs)(delayed (process_lines)(t[0], t[1], i) for i, t in enumerate(split_tuples))
