import sys
import string

def main():
    words = list(filter(lambda x: len(x) >= 5 and (len(set(x)) == len(x)), [x.strip() for x in sys.stdin]))
    if words == []:
        print('neibb!')
    else:
        zipped = sorted(zip(words, map(wordScore, words)), reverse = True)
        print(zipped[0][0])

def wordScore(s):
    return sum([string.ascii_lowercase.index(x) for x in s])    

main()
