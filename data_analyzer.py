with open("read.txt", "r") as file:
    text = file.read()
    print(text)
num_word = 0
num_chr = 0
num_snt = 0
num_prg = 0
# np = text.split('\n''\n')
# uniValues = []
index = 0
chk = len(text)

tallies = []
punc = [' ', ',', '.', '?']
sprt = ['.', '?']
while chk > 0:
    if text[index] in punc:
        num_word += 1
    if text[index] in punc:
        num_chr += chk-1
    if text[index] in sprt:
        num_snt += 1

    # if uniValues not in text[index]:
    #     spl = text.split(',')
    #     uniValues.append(text)
    #     tallies.append(1)

    index += 1
    chk -= 1


print(f"Number of word in the text file is: {num_word}")
print(f"Number of characters in the text file is: {num_chr}")
print(f"Number of sentence in the text file is:{num_snt} ")
print(f"number of paragraph in the text file is:{num_prg}")
#print(f"Number of unique values is: {uniValues}:{tallies}")



