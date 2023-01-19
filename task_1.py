# Напишите программу, удаляющую из текста все слова содержащие "абв".
# В тексте используется разделитель пробел

from random import sample

#def list_rand_words(count: int, alp: str = 'абв'):
#    words_list = []
#    for i in range(count):
#        letters = sample(alp, k=3)
#        words_list.append(''.join(letters))
#    return ' '.join(words_list)


def list_rand_words(count: int, alp: str = 'абв'):
    return " ".join("".join(sample(alp, k=3)) for _ in range(count))

def simple_sentece(words: str):
    return " ".join(i for i in words.split() if i != 'абв')

list_1 = list_rand_words(int(input('введите кол-во слов ')))
list_2 = simple_sentece(list_1)
print(list_1)
print(list_2)