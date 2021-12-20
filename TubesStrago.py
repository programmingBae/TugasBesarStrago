


def LastO(pola):
    last = [None]*128
    for i in range(0,128,1): last[i] = -1
    for i in range(0, len(pola), 1): last[ord(pola[i])] = i
    return last

def SearchBM(T,P):
    list_found = []
    last = LastO(P)
    n = len(T)
    m = len(P)
    i = m-1
    if (i > n-1):
    #pola > text
        hasil = -1
    else:
        j = m-1
        Found = False
        index = 0
        while (i < n) :
            if (P[j] == T[i]):
                if (j == 0):
                    if (i<n):
                        list_found.append(i)
                        print(f"{i}")
                        j = j - 1;
                        i = i - 1;
                    else:
                        list_found.append(i)
                        print(f"{i}")
                else:
                    j = j - 1;
                    i = i - 1;
            else: #character jump
                lo = last[ord(T[i])]
                i = i + m - min(j,1+lo)
                j = m-1 #back to rightmost
    if len(list_found)>0:
        hasil = list_found
    else:
        hasil = -1
    return hasil

def main():
    string_of_words = "Abed aku adalah aku yang abed adalah aku dengan aku abed adalh"
    pola = "aku"
    hasil = SearchBM(string_of_words, pola)
    print(hasil)
 


if __name__ == "__main__":
    main()