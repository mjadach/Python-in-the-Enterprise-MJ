
words = " |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |"
new_words_list = words.split()
print(new_words_list)
symbols = "1234567890~!@#$%^&*()_+{}|:\"<>?,./;'[]\\-="
clean_word_list = []
for word in new_words_list:
    for i in range(0, len(symbols)):
        word = word.replace(symbols[i], "")
    if len(word) > 0:
        clean_word_list.append(word)
print (clean_word_list)