def count_alphabets(fname):
    counts = [0]*26
    with open(fname) as f:
        for ch in f.read().lower():
            if 'a' <= ch <= 'z':
                counts[ord(ch)-97] += 1
    for i in range(26):
        print(chr(97+i), ":", counts[i])

count_alphabets('yourfile.txt')
