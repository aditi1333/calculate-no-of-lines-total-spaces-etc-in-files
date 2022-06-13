#program2
import string
file = open("temp.txt","r")
text = file.read()
file.close()
word_list = text.lower().split(None)
word_freq = {}
for word in word_list:
    word_freq[word] = word_freq.get(word,0)+1
    keys = sorted(word_freq.keys())
#display freq of words
for word in keys:
    print("%s %d" %(word, word_freq[word]))

