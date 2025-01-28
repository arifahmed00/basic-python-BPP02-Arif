from collections import Counter
with open("read.txt", "r") as file:
    text = file.read()                  #read the text file

index = 0                                                # index for read all letter of text file one by one
num_word = 0                                             #counter for word
num_snt = 0                                              #counter for sentence
num_prg = 0                                              #counter for paragraph
chk = len(text)                                          #chaking length of text file
# Define punctuation for word and sentence counting
word_punc = [' ', ',', '.', '?', '!', ';']
sentence_punc = ['.', '?', '!', ';']

while chk != 0:
    # checking number of word in text file
    if text[index] in word_punc:
        num_word += 1

    # checking number of sentence in text file
    if text[index] in sentence_punc:
        num_snt += 1

    index += 1
    chk -= 1
#chaking paragraph in text file
paragraphs = text.split('\n\n')
for para in paragraphs:
    if para.strip():
        num_prg += 1               #chaking number of paragraphs in text file

#counting characters
num_chr = len(text)

#checking most frequent word in text file
fh =text.split()
cnt = Counter(fh)
mx = max(cnt)
#counting number of most frequent word in text file
un = []
tallies  =0

for ch in fh:
    if ch not in un:
        tallies+=1

print(f"Number of word in the text file is: {num_word}")
print(f"Number of characters in the text file is: {num_chr}")
print(f"Number of sentence in the text file is:{num_snt} ")
print(f"number of paragraph in the text file is:{num_prg}")
print(f"Most frequent word in text file is : {mx}:{tallies}")
