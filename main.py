from itertools import permutations
import pickle

file_path = r'C:/Users/weineja/Documents/Words//'

def binarysearch(sequence, value):
    lo, hi = 0, len(sequence) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sequence[mid] < value:
            lo = mid + 1
        elif value < sequence[mid]:
            hi = mid - 1
        else:
            return mid
    return None

def hash(word):

    _hash = 5381

    for i in xrange(0, len(word)):
        _hash = ((_hash << 5) + _hash) + ord(word[i])
    return _hash

def create_dict():
    file_name = r'wordsEn.txt'
    word_dict = {}

    with open(file_path + file_name,'U') as fp:
        for line in fp:
            word_dict[hash(line[:-1])] = line[:-1]

    with open(file_path + 'word_dict.pkl', 'wb') as fp:
        pickle.dump(word_dict, fp)

def main():
    create_dict()
    word = 'ERCRDATTE'
    perms = [''.join(p) for p in permutations(word.lower())]
    perms_unique = set(perms)
    with open(file_path + 'word_dict.pkl', 'rb') as fp:
        word_dict = pickle.load(fp)

    for perm in perms_unique:
        try:
            print word_dict[hash(perm)]
            break
        except KeyError:
            continue

if __name__ == "__main__":
    main()
