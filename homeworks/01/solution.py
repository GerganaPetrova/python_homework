def such_much(x):
    if x % 15 == 0:
        return 'suchmuch'
    elif x % 3 == 0:
        return 'such'
    elif x % 5 == 0:
        return 'much'
    else:
        return str(x)


def wow_such_much(start, end):
    return [such_much(i) for i in range(start, end)]


def count_doge_words(sentence):
    parasites = ['wow', 'lol', 'so', 'such', 'much', 'very']
    words_in_sentence = sentence.split()
    return len([word for word in words_in_sentence if word in parasites])
