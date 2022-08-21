

def solve(words):
    l = []
    end_s, end_e, mid = [], [], []
    for i in range(words):
        word = str(input())
        pieces = word.split("*")
        end_e.append(pieces[-1])
        end_s.append(pieces[0])
        if len(pieces) > 2:
            middle = []
            for p in range(1, len(pieces)):
                middle.append(pieces[p])
            mid.append(''.join(middle))
            l.append(word)
            
    end_s = sorted(end_s, key=lambda x: len(x), reverse=True)
    end_e = sorted(end_e, key=lambda x: len(x), reverse=True)
    mid = sorted(mid, key=lambda x: len(x), reverse=True)
    mid_word = ""
    word_s = end_s[0] if len(end_s) > 0 else ""
    word_e = end_e[0] if len(end_e) > 0 else ""
    #print(end_s,"-", mid, "-", end_e)
    for word in end_s:
        if word != "":
            w_len = len(word)
            #print(word, word_s[-w_len:])
            if word != word_s[:w_len]:
                #print("WORD BAD", word)
                return "*"
    for word in end_e:
        if word != "":
            w_len = len(word)
            #print(word, word_e[-w_len:])
            if word != word_e[-w_len:]:
                
                #print("WORD BAD", word)
                return "*"
    for word in mid:
        if word != "":
            if word not in word_e:
                mid_word += word
    #print(word_s, mid_word, word_e)
    final = word_s + mid_word + word_e
    return final


for case in range(int(input())):
    words = int(input())
    result = solve(words)
    print("Case #{}: {}".format( case + 1, result ))
