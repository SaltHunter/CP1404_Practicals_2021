wordscount = {}
text = input("Text: ")
# text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
for word in words:
    frequency = wordscount.get(word, 0)
    wordscount[word] = frequency + 1
words = list(wordscount.keys())
words.sort()
maxlength = max(len(word) for word in words)
for word in words:
    print("{:{}} : {}".format(word, maxlength, wordscount[word]))