# Python Veri Yapıları
- ### [Numbers](#numbers)
  - #### [int](#int)
  - #### [float](#float)
  - #### [complex](#complex)
- ### [Strings](#strings)
- ### [Boolen](#boolen)
- ### [List](#list)
- ### [Dictionary](#dictionary)
- ### [Tuple](#tuple)
- ### [Set](#set)

## Numbers
Sayılar, pythonda 3 çeşide ayrılır. Bunlar integer, float ve complex'dir. 
### Int
Int, tamsayı anlamına gelir.
```python
a = -4
c = 23
m = 62
```
Yukarıda üç farklı değişkene int veri tipinde değerler atadık. Bunların tipini
görmek istersek
```python
type(a)
type(b)
type(m)
```
```
out: int
```
çıktısını alırız.

### Float
Float, pythonda ve çoğu programlama dillerinde ondaklılı sayıları temsil eder. 
Bazı kaynaklarda kayan sayı, kesikli sayı ifadesi de geçer. Bunların hepsi aynıdır.
Python'da ondalıklı ifade gösterimi "." nokta ile ifade edilir.
```python
a = -2.3
b = 5.3
c = 5.0
type(a)    # out: float
type(b)    # out: float
type(c)    # out: float
```
### Complex
Pythonda Karmaşık (complex) sayı oluşturmak sayının önüne katsayı katsayı
yazarak ifade edilir.

```python
x = 2j + 1
type(x)    # out: complex
```

### List
List(Liste)
- Değiştirilebilir
- Sıralıdır.
- Kapsayıcıdır.

Özellikleri Tanıyalım: 
* Değiştirilebilir: atama işlemi yapılabilir.
* Sıralıdır: Veride index işlemleri yapılabilir. Index kullanılarak verilere erişilebilir.
* Kapsayıcıdır: Birden fazla veri tipini içinde barıdırabilir.

```python
nxn = [1, 2, 3, 4, 5]
type(nxn)      # out: list 
nxn[0]         # out: 1
nxn[4]         # out: 5
```
Bir çok programlama dilinden aşina olduğumuz bir yapı. Genelde array(dizi) ile ifade edilen
bu yapı pythonda list şeklinde ifade ediliyor. Kullanış yapısı array ile aynıdır.

Kapsayıcı özelliğimize yönelik bir örnek:
```python
loveu = ["l", "o", "v", "u", 2, 3, 4, True, [1, 2, 3]]
loveu[0]    # out: l
loveu[7]    # out: True
loveu[8]    # out: [1, 2, 3]
loveu[8][1] # out: 2
```
Burada fark ediliyor ki birden fazla veri tipi list'in içerisinde barındırılabiliyor.
Bu da list'in kapsayıcı olduğu anlamına gelir.
Şimdi 'luveu' listesinin gelin ne kadar veri tipini taşıdığına bakalım.
1. str
2. int 
3. bool 
4. list -> [1, 2, 3]

Şimdi listemize bazı metotlar uygulayalım
```

```

