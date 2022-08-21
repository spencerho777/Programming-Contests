import collections
import random


# test = open("consistency1test.in", 'w')
# test.truncate(0)
# test.write("4500\n")
# for b in range(4500):
#     for a in range(100):
#         test.write(chr(random.randint(97, 122)).upper())
#     test.write("\n")



fin = open("consistency_chapter_1_input.txt", 'r')
fout = open("consistency1.txt", 'w')


n = int(fin.readline().strip())

def is_vowel(char):
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        return True
    return False

def num_most_common(string):
    if string == "": return 0
    print("most common: ", collections.Counter(string).most_common(1)[0])
    return collections.Counter(string).most_common(1)[0][1]

def solve(s):
    vowels = ""
    consonants = ""
    for char in s:
        if is_vowel(char):
            vowels += char
        else:
            consonants += char

    l_v = len(vowels)
    l_c = len(consonants)
    v_common = num_most_common(vowels)
    c_common = num_most_common(consonants)
    #print(vowels)
    #print(consonants)
    v2c = l_v + (2 * (l_c - c_common))
    c2v = l_c + (2 * (l_v - v_common))
    #print(v2c, c2v)
    return max(0, min(v2c, c2v))

for case in range(n):
    s = fin.readline().strip().lower()
    fout.write("Case #{}: {}\n".format( case + 1, solve(s) ))

fout.close()
    
    
