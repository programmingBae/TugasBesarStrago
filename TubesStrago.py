from Stopwords import stopword_list
from TextClean import string_of_words, list_string_of_words


def lastO(pola):
    last = [None]*128
    for i in range(0,128,1):
        last[i] = -1
    for i in range(0, len(pola), 1):
        last[ord(pola[i])] = i
    return last

def searchBM(T,P):
    last = lastO(P)
    n = len(T)
    m = len(P)
    i = m-1
    if (i > n-1):
    #pola > text
        hasil = -1
    else:
        j = m-1
        Found = False
        while (i < n) and (not Found):
            if (P[j] == T[i]):
                if (j == 0):
                    Found = True
                else:
                    j = j - 1;
                    i = i - 1;
            else: #character jump
                lo = last[ord(T[i])]
                i = i + m - min(j,1+lo)
                j = m-1 #back to rightmost
    if (Found):
        hasil = i
    else:
        hasil = -1
    return hasil

def main():
    print(f"Banyak kata dalam file text : {len(list_string_of_words)}")
    pola = ""
    if pola in stopword_list:
        print("Pola tidak boleh stopword")
    else:
        hasil = searchBM(string_of_words, pola)
        print(hasil)


if __name__ == "__main__":
    main()