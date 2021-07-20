try:
    new_words = open("words.txt", "w")
except:
    exit(1)
with open("text.txt", "r") as text:
    while True:
        line = text.readline()
        if not line:
            break
        if len(line) and ('A' <= line[0] <= 'Я'):
            word = line.split(sep=',')[0]
            if len(word) > 3:
                skip = False
                for c in word:
                    if c < 'А' or c > 'Я':
                        skip = True
                        break
                if not skip:
                    new_words.write('"' + word + '",' + '\n')

new_words.close()
