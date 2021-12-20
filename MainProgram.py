import tkinter as tk
import TextClean as tc
import TubesStrago as tb
from tkinter import filedialog
from tkinter import *
from Stopwords import stopword_list

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
                            # print(f"{i}")
                            j = j - 1;
                            i = i - 1;
                        else:
                            list_found.append(i)
                            # print(f"{i}")
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

def select_file():
    text_box3.delete(1.0, END)
    text_box.delete(1.0, END)
    browse_text.set("File Opened")
    file =  filedialog.askopenfilename(initialdir = "D:\pythoncoba\TugasBesarStrago",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    TextClean = tc.TextClean(file)
    text_box.insert(tk.END, TextClean.get_string_of_words())
    text_box.tag_configure("center" , justify='center')
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(row=1, column=3,  rowspan=3)
    tes = "Panjang text tanpa stopword : "+str(len(TextClean.get_list_string_without_stopwords()))+"\n" + "Panjang text dengan stopword : "+str(len(TextClean.get_list_string_of_words()))+"\n"
    text_box3.insert(tk.END, tes)
    text_box3.tag_configure("center" , justify='center')
    text_box3.tag_add("center", 1.0, "end")
    text_box3.grid(row=5, column=0,  rowspan=3, columnspan=2)
    # text_box_teks_asli2 = tk.Text(root, height=2, width=10, padx=10, pady=10)
    # text_box_teks_asli2.insert(tk.END, len(TextClean.get_list_string_of_words()))
    # text_box_teks_asli2.tag_configure("center" , justify='center')
    # text_box_teks_asli2.tag_add("center", 1.0, "end")
    # text_box_teks_asli2.grid(row=3, column=0)
    # text_box_teks_asli = tk.Text(root, height=2, width=10, padx=10, pady=10)
    # text_box_teks_asli.insert(tk.END, len(TextClean.get_list_string_of_words()))
    # text_box_teks_asli.tag_configure("center" , justify='center')
    # text_box_teks_asli.tag_add("center", 1.0, "end")
    # text_box_teks_asli.grid(row=4, column=0)
    # text_box_teks_noStopword = tk.Text(root, height=2, width=10, padx=10, pady=10)
    # text_box_teks_noStopword.insert(tk.END, len(TextClean.get_list_string_without_stopwords()))
    # text_box_teks_noStopword.tag_configure("center" , justify='center') 
    # text_box_teks_noStopword.tag_add("center", 1.0, "end")
    # text_box_teks_noStopword.grid(row=4, column=1)
    

def cari_pola():
    
    string_text = {}
    text_box2.delete(1.0, END)
    text_box2.tag_configure("center" , justify='center')
    text_box2.tag_add("center", 1.0, "end")
    text_box2.grid(row=5, column=3,  rowspan=3)
    INPUT = input_text.get("1.0", "end-1c")
    pola = INPUT.split()
    for kata in list(pola):
        if kata in stopword_list:
            print(f"{kata} adalah stopword, maka kata ini tidak akan dicari")
            pola.remove(kata)
    list_pola = list(pola)
    pola_set = set(pola)
    pola = list(pola_set)
    print(pola)
    text = text_box.get("1.0", "end-1c")
    checker = False
    i = 0
    while i<len(pola): 
        hasil = SearchBM(text,pola[i])
        if hasil != -1:
            for j in hasil:
                   
                # print(hasil)
                # print(f"{pola[i]} ditemukan pada index {j}")
                akhir_kata = j + len(pola[i])
                text_box.tag_config("start", foreground="red")
                text_box.tag_config("end", foreground="blue")
                text_box.tag_add("start", "1."+str(j), "1."+str(akhir_kata))
        string_text[pola[i]] = len(hasil) 
        i+=1



    list_pola = " ".join(list_pola)
    print(list_pola)
    hasil = SearchBM(text,list_pola)
    if hasil != -1:
        string_text[list_pola] = len(hasil) 
        for j in hasil:
            # print(hasil)
            # print(f"{list_pola} ditemukan pada index {j}")
            akhir_kata = j + len(list_pola)
            text_box.tag_config("start", foreground="blue")
            text_box.tag_add("start", "1."+str(j), "1."+str(akhir_kata))
    text_box2.insert(tk.END, string_text)
        
         


    
  

root = tk.Tk()
root.title("Main Program")

canvas = tk.Canvas(root, width=1000, height=400)
canvas.grid(columnspan=15, rowspan=8)

tes = ""

text_box = tk.Text(root, height=20, width=70, padx=10, pady=10)
text_box2 = tk.Text(root, height=20, width=70, padx=10, pady=10)
text_box3 = tk.Text(root, height=20, width=70, padx=10, pady=10)

instructions = tk.Label(root, text="Select data text", font=("Helvetica", 16))
instructions.grid(row=1, column=0)

input_text = Text(root, height=2, width=25, bg="light yellow")
input_text.grid(row=2, column=0)

browse_text = tk.StringVar()
browse_text.set("Browse")
browse_btn = tk.Button(root, textvariable=browse_text, height=2, width=15, fg="white", bg="black", command=select_file)
browse_btn.grid(column=1, row=1)
search_text = tk.StringVar()
search_text.set("Cari Pola!")
search_btn = tk.Button(root, textvariable=search_text, height = 2, width = 15, fg="white", bg="black", command=cari_pola)
search_btn.grid(column=1, row=2)


canvas = tk.Canvas(root, width=400, height=400)
canvas.grid(columnspan=12, rowspan=3)

root.mainloop()
