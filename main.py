import pandas as pd
import MeCab

def dicfile_to_dict():
    # fuck shift-jis encoding :middle_finger:
    dic = pd.read_csv(
        './pn_ja.dic',
        sep=':',
        encoding='shift-jis',
        names=('Tango', 'Yomi', 'Hinshi', 'Score'),
    )
    words = dic['Tango']
    score = dic['Score']
    return dict(zip(words, score))

def calc_score(word, dic):
    if not word in dic:
        return None
    return dic[word]

def main():
    # set up dictionary
    dic = dicfile_to_dict()
    # set up data to analyze
    text = '何らかの文章'
    # morphological analysic by mecab
    tagger = MeCab.Tagger("-Ochasen")
    parsed_arr = tagger.parse(text).splitlines()
    parsed_arr.pop()    

    total = 0
    for word in parsed_arr:
        # split by tab
        tab = word.split('\t')
        # use word, which is the 0th element of tab(array)
        score = calc_score(tab[0], dic)
        if score is None:
            total += 0
            print('Word not found in the library')
        else:
            print('Score: ', end="")
            print(score)
            total += score
    print('Total Score: ')
    print(total)

if __name__ == '__main__':
    main()