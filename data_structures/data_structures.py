########################
# VERİ YAPILARI (DATA STRUCTURES)
##############################

# - Veri Yapılarına Giriş ve Hızlı Özet
# - Sayılar (Numbers): int, float, complex
# - Karakter Dizileri (Strings): str
# - Boolen (TRUE-FALSE): bool
# - Liste (List)
# - Sözlük (Dictionary)
# - Demet (Tuple)
# - Set

# Sayılar: complex
x = 2j + 1
type(x)

# Liste
x = ["btc", "eth", "xrp"]
type(x)

# Sözlük (dictionary)
# key: value
x = {"name": "Peter", "Age": 24}
type(x)
# Tuple (Demet)
x = ("python", "ml", "ds")
type(x)
# Set
# -> kümele işlemlerinde kullanılır.
x = {"python", "ml", "ds"}
type(x)

# Not: Liste, tuple, set ve dictionary veri yapıları aynı zamanda Python Collection (Arrays) olarak geçmektedir.

# Tipleri Değiştirmek
b = 10.5
int(b)
# out: 10
a = 5
float(a)
# out: 5.0

# Karakter Dizileri (Strings)
# tek çikft tırnak farketmez
# fonksiyonlar bir işlemde print kullanılır
print("John")
print('John')
"John"
# Çok Satırlı Karakter Dizileri

long_str = """
# - Veri Yapılarına Giriş ve Hızlı Özet
# - Sayılar (Numbers): int, float, complex
# - Karakter Dizileri (Strings): str
# - Boolen (TRUE-FALSE): bool
# - Liste (List)
# - Sözlük (Dictionary)
# - Demet (Tuple)
# - Set
"""
# Karakter Dizilerinin Elemanlarına Erişmek

name = "musa"
name[0]

# Karakter Dizilerinde Slice işlemi

# 0'dan başla 2ye kadar git 2 hariç
name[0:2]

## string içinde karakter sorgulama
"Set" in long_str
# set long_str'nin içinde mi?

# String (Karakter Dizisi)
## int ile ilgili kullanılabilecek metotlar:
dir(int)
## str ile ilgili kullanılabilecek metotlar:
dir(str)

# len
# string ifadesinin boyut bilgisini verir
name = "john"
len(name)

# Metot ve fonksyion aynı şeydir. Fakat farklılaştığı nokta fonksiyonların bağımsız
# metotların ise class yapısı içersinde tanımlanmış olmasıdır !!!

name.upper()

# replace: karakter değiştirir

hi = "Hello AI Era"
# l'yi p olarak değiştirir
hi.replace("l", "p")

# split: böler
"Hello AI Era".split()
## varsayılan olarak boşluğa göre böler
"Hello AI Era".split("o")

# capitalize: ilk harfi büyütür

"foo".capitalize()

# foo string ifadesi üzerinde yapabileceğimiz fonksiyonları döndürür:
dir("foo")

########################################################
# Liste (List)
########################################################

# - Değiştirilebilir
# - Sıralıdır. Index İşlemleri yapılabilir. (veri yapısının elemanlarına erişebilir)
# - Kapsayıcıdır. (birden fazla veri tipini içinde barıdırabilir.)

notes = [1, 2, 3, 3, 4]
type(notes)
not_nam = ["a", "b", "c", 1, 2, 3, True, [1, 2, 3]]


not_nam[7][1]
# out: 2
type(not_nam[7])
type(not_nam[7][2])

notes[0] = 99

not_nam[0:4]

dir(notes)
## apend: eleman ekler
notes.append(100)

## pop: indexe göre siler
notes.pop(0)

## insert: indexe göre ekler
notes.insert(1, 99)
# 1. indexe 99 edeğerei eklendi
######  self ifadesinden metot olduğu anlaşılır (self, ___index, __object)


#################################
# Sözlük (Dictionary)
#################################

# Değiştirilebilir.
# Sırasız (3.7 versiyonundan sonra sıralı)
# kapsayıcı.

# key-value
dictionary = {
    "reg": "regression",
    "log": "logictic regression",
    "cart": "classification and ref"
}
dictionary["reg"]
# out: regression

dictionary = {
    "reg": ["RMSE", 10],
    "log": "logictic regression",
    "cart": "classification and ref"
}

dictionary["reg"][1]

####################
# Key Sorgulama
####################

"reg" in dictionary

####################
# Key'e Göre Value'ya Erişmek
####################

dictionary["reg"]
dictionary.get("reg")

####################
# Value Değiştirmek
####################

dictionary["reg"] = ["YSA", 10]

###################
# Tüm Key'lere Erişmek
###################
dictionary.keys()

###################
# Tüm Value'lere Erişmek
###################

dictionary.values()

###################
# Tüm Çiftleri Tuple (Demet) Halinde Listeye Çevirme
###################

dictionary.items()
## out: dict_items([('reg', ['YSA', 10]), ('log', 'logictic regression'), ('cart', 'classification and ref')])

###################
# Key-Value Değerlerini Güncellemek
###################

dictionary.update({"reg": 11})

###################
# Demet (Tuple)
###################

# - Değiştirilemez
# - Sıralıdır.
# - Kapsayıcıdır. (birden farklı veri yapısının tutabilir.)

t = ("john", "mark", 1, 2)
type(t)
# out: tuple

t[0]
t[0:3]

t[0] = 9

t = list(t)
# tuple'ı list'e çevirdim.
t[0] = 9
# değişiklik yaptım
t = tuple(t)
# tekrar tuple'a dönüştürdüm.


###################
# Set
###################

# - Değiştirilemez
# - Sırasızdır + Eşsizdir.
# - Kapsayıcıdır. (birden farklı veri yapısının tutabilir.)
## küme işlemlerine benzer

###################
# difference(): İki kümenin farkı
###################

# köşeli parantez list'dir. List' üzerinde set oluşturuluyor
set1 = set([1, 3, 5])
set2 = set([1, 2, 3])


# set1'de olup set2'de olmayanlar.
# set1 - set2
set1.difference(set2)
set1 - set2
## out: 5

# set2'de olup set1'de olmayanlar.
set2.difference(set1)
set2 - set1

###################
# symmetric_difference(): İki kümede de birbirlerine göre olmayanlar
###################

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)
## out: 2,5

###################
# intersection(): İki kümenin kesişimi
###################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.intersection(set2)
set2.intersection(set1)

set1 & set2 # iiki kümenin kesişimi

###################
# union(): İki kümenin birleşimi
###################

set1.union(set2)
set2.union(set1)

###################
# isdisjoint(): İki kümenin kesişimi boş mu?
###################


set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

set1.isdisjoint(set2)
set2.isdisjoint(set1)

###################
# issubset(): Bir küme diğer kümenin alt kümesi mi?
###################

set1.issubset(set2)
## set1 set2'nin alt kümesi mi?

set2.issubset(set1)
## set1 set2'nin alt kümesi mi?

name = "VB0_BOOTCAMP"
type = "new_term"
f"Name:{name} type:{type}"













