import numpy as np
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Membuka file Dokumen Latihan1.txt yang berisi artikel pada latihan1
file = open("Dokumen Latihan1.txt", "r")
read_file = file.read()
print("Artikel asli:\n", read_file, "\n")

# Memisahkan kalimat artikel dengan 'spasi' sebagai pemisahnya, hingga menjadi perkata (tokenisasi)
split_file = read_file.split(" ")
print("Artikel per kata (tokenisasi):\n", split_file, "\n")

# Menghapus tanda baca pada tiap kata, dengan tanda baca yang dhapus dikumpulkan pada variabel punc
punc = """!"#$%&'(1234567890)*+,-./:;<=>?@[\]^_`{|}~"""

file_no_punc = ["".join(char for char in string if char not in punc) for string in split_file]
print("Artikel per kata tanpa tanda baca:\n", file_no_punc, "\n")

# Mengubah semua huruf yang ada menjadi huruf kecil (casefolding)
file_casefold = [x.lower() for x in file_no_punc]
print("Artikel per kata tanpa tanda baca dengan huruf kecil (casefolding):\n", file_casefold, "\n")

# Membuka file stopword tala dan mengelompokkannya dalam bentuk list dengan 'enter' sebagai pemisahnya
stopword_tala = open("stopword_tala.txt", "r")
read_stopword = stopword_tala.read()

split_stopword = read_stopword.split("\n")

# Penghapusan kata yang ada pada stopword tala (filtering)
new_words = [word for word in file_casefold if word not in split_stopword]
print("Kata-kata yang sudah dilakukan filtering:\n", new_words, "\n")

# Mengubah bentuk kata menjadi kata dasar (stemming)
factory = StemmerFactory()
stemmer = factory.create_stemmer()
documents = [stemmer.stem(word) for word in new_words]
print("Kata-kata yang sudah diubah kedalam kata dasar (stemming):\n", documents, "\n")

# Mencari kata-kata yang unik saja, atau tidak terdapat duplikasi (term)
kata_unik = np.unique(documents)
print("Kata-kata unik (term):\n", kata_unik, "\n")

# Karena masih terdapat kata yang termasuk kedalam stopword (karena proses perubahan kata dasar), maka dilakukan kembali proses filtering kedua.
final_term = [word for word in kata_unik if word not in split_stopword]
print("Kata-kata yang sudah dilakukan filtering pada term:\n", final_term, "\n")


