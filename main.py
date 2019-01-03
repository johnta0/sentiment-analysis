import pandas as pd
import mecab

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
    return dic[word]

def 

def main():
    # set up dictionary
    dic = dicfile_to_dict()
    # set up data to analyze
    text = 'ありがとうございました。好きです。'
    # morphological analysic by mecab

if __name__ == '__main__':
