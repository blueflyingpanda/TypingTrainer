max_len = -1
max_line = ""

with open("words.txt", "r") as words:
    while True:
        line = words.readline()
        if not line:
            break
        if len(line) > max_len:
            max_len = len(line)
            max_line = line

print(max_len)
print(max_line)
print(len("ЧЕЛОВЕКОНЕНАВИСТНИЧЕСТВО"))