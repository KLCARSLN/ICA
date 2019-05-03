# coding:utf-8

import base64
import requests
from bs4 import BeautifulSoup
import datetime

today = str(datetime.date.today())
print(""" \033[1;32;1m 

8888888  .d8888b.         d8888 
  888   d88P  Y88b       d88888 
  888   888    888      d88P888 
  888   888            d88P 888 
  888   888           d88P  888 
  888   888    888   d88P   888 
  888   Y88b  d88P  d8888888888 
8888888  "Y8888P"  d88P     888 \033[0;32;1m """)

print("")
print("\x1b[1;33;1mIn Cipher (A) decoder \x1b[0;33;1m")
print("\x1b[1;33;1mby KILIÇ aka K.A.\x1b[0;33;1m")
print("\x1b[1;33;1mTwitter.com/MHMMD_KLC \x1b[0;33;1m")
print("\x1b[1;33;1mSonuçları sonuc.txt'ye kaydeder \x1b[0;33;1m")
print("")

cryptic = input("\x1b[1;31;1mŞifrelenmiş Metin: \033[1;37;1m")

dosyaappend = open("Sonuc.txt", "a")

todayy = "**************************" + today + "**************************"

dosyaappend.write("\n")
dosyaappend.write(todayy)
dosyaappend.write("\n")
dosyaappend.write("Şifreli Metin:" + cryptic)
dosyaappend.write("\n")

# hex
ii = cryptic
ii = ii.replace(",", "")
ii = ii.replace("\\x", "")
ii = ii.replace("0x", "")

try:
    asc = "hex: " + bytes.fromhex(ii).decode('utf-8')
    print("\x1b[1;36;1mhex: \033[1;37;1m" + bytes.fromhex(ii).decode('utf-8'))
except:
    asc = "Bu şifrelenmiş text kesin olarak hexlenmemiştir!"
    print("\x1b[1;31;1mBu şifrelenmiş text kesin olarak hexlenmemiştir!\033[1;37;1m")

dosyaappend.write("\n")
dosyaappend.write(asc)
dosyaappend.write("\n")

# Binary Yıldırım
try:
    binali = cryptic.replace(" ", "")
    n = int(binali, 2)
    binary = "Binary: " + n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    print("\x1b[1;36;1mBinary: \033[1;37;1m" + n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
except:
    binary = "Bu şifrelenmiş text kesin olarak binary ile şifrelenmemiştir!"
    print("\x1b[1;31;1mBu şifrelenmiş text kesin olarak binary ile şifrelenmemiştir!\033[1;37;1m")
dosyaappend.write("\n")
dosyaappend.write(str(binary))
dosyaappend.write("\n")

# decimal
cry = cryptic.replace(",", " ")
decimalist = cry.split()
deci = ""
try:
    for decim in decimalist:
        decim = int(decim)
        deci1 = chr(decim)
        deci = deci + deci1
    deciA = "Decimal: " + deci
    print("\x1b[1;36;1mDecimal: \033[1;37;1m" + deci)
except:
    deciA = "Bu şifrelenmiş text kesin olarak Decimal ile şifrelenmemiştir."
    print("\x1b[1;31;1mBu şifrelenmiş text kesin olarak Decimal ile şifrelenmemiştir.\033[1;37;1m")

dosyaappend.write("\n")
dosyaappend.write(str(deciA))
dosyaappend.write("\n")

# md5
murl = "http://hashtoolkit.com/decrypt-md5-hash/"
mdurl = murl + cryptic
m = requests.get(mdurl)
d = BeautifulSoup(m.content, "html.parser")

try:
    emdi = d.find_all("span", {"title": "decrypted md5 hash"})
    emdifayf = "MD5: " + emdi[0].text
    print("\x1b[1;36;1mMD5: \033[1;37;1m" + emdi[0].text)
except:
    emdifayf = "Bu şifrelenmiş text ya MD5 ile şifrelenmemiştir ya da veritabanında bulunmuyordur."
    print("\x1b[1;31;1mBu şifrelenmiş text ya MD5 ile şifrelenmemiştir ya da veritabanında bulunmuyordur.\033[1;37;1m")

dosyaappend.write("\n")
dosyaappend.write(str(emdifayf))
dosyaappend.write("\n")

# sha1
try:
    sha = d.find_all("span", {"title": "decrypted sha1 hash"})
    sha1 = "SHA1: " + sha[0].text
    print("\x1b[1;36;1mSHA1: \033[1;37;1m" + sha[0].text)
except:
    sha1 = "Bu şifrelenmiş text ya SHA1 ile şifrelenmemiştir ya da veritabanında bulunmuyordur."
    print("\x1b[1;31;1mBu şifrelenmiş text ya SHA1 ile şifrelenmemiştir ya da veritabanında bulunmuyordur.\033[1;37;1m")

dosyaappend.write("\n")
dosyaappend.write(str(sha1))
dosyaappend.write("\n")

# sha256
try:
    sha2 = d.find_all("span", {"title": "decrypted sha256 hash"})
    sha256 = "SHA256: " + sha2[0].text
    print("\x1b[1;36;1mSHA256: \033[1;37;1m" + sha2[0].text)
except:
    sha256 = "Bu şifrelenmiş text ya SHA256 ile şifrelenmemiştir ya da veritabanında bulunmuyordur."
    print("\x1b[1;31;1mBu şifrelenmiş text ya SHA256 ile şifrelenmemiştir ya da veritabanında bulunmuyordur.\033[1;37;1m")

dosyaappend.write("\n")
dosyaappend.write(str(sha256))
dosyaappend.write("\n")

# sha384
try:
    sha3 = d.find_all("span", {"title": "decrypted sha384 hash"})
    sha384 = "SHA384: " + sha3[0].text
    print("\x1b[1;36;1mSHA384: \033[1;37;1m" + sha3[0].text)
except:
    sha384 = "Bu şifrelenmiş text ya SHA384 ile şifrelenmemiştir ya da veritabanında bulunmuyordur."
    print("\x1b[1;31;1mBu şifrelenmiş text ya SHA384 ile şifrelenmemiştir ya da veritabanında bulunmuyordur.\033[1;37;1m")

dosyaappend.write("\n")
dosyaappend.write(str(sha384))
dosyaappend.write("\n")

# sha512
try:
    sha5 = d.find_all("span", {"title": "decrypted sha512 hash"})
    sha512 = "SHA512: " + sha5[0].text
    print("\x1b[1;36;1mSHA512: \033[1;37;1m" + sha5[0].text)
except:
    sha512 = "Bu şifrelenmiş text ya SHA512 ile şifrelenmemiştir ya da veritabanında bulunmuyordur."
    print("\x1b[1;31;1mBu şifrelenmiş text ya SHA512 ile şifrelenmemiştir ya da veritabanında bulunmuyordur.\033[1;37;1m")

dosyaappend.write("\n")
dosyaappend.write(str(sha512))
dosyaappend.write("\n")

# Base64
try:
    bssixty = base64.b64decode(cryptic)
    bssixtydort = str(bssixty)
    bssixtydort = bssixtydort[2:-1]

    baswrt = str("Base64: " + bssixtydort)
    print("\x1b[1;36;1mBase64: \033[1;37;1m" + bssixtydort)
except:
    baswrt = "Bu şifrelenmiş text kesin olarak base64 ile şifrelenmemiştir!"
    print("\x1b[1;31;1mBu şifrelenmiş text kesin olarak base64 ile şifrelenmemiştir!\033[1;37;1m")

dosyaappend.write("\n")
dosyaappend.write(str(baswrt))
dosyaappend.write("\n")

# Rot13
rotone = "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
rotthree = "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz"
rotcevir = cryptic.maketrans(rotone, rotthree)
Rot13sonuc = cryptic.translate(rotcevir)

rotwrt = "Rot13: " + str(Rot13sonuc)
print("\x1b[1;36;1mRot13: \033[1;37;1m" + str(Rot13sonuc))
dosyaappend.write("\n")
dosyaappend.write(rotwrt)
dosyaappend.write("\n")


# Tersine
def rvrs(x):
    return x[::-1]


tersinesonuc = rvrs(cryptic)
trsnwrt = "Tersine / Reverse: " + tersinesonuc
print("\x1b[1;36;1mTersine / Reverse: \033[1;37;1m" + tersinesonuc)
dosyaappend.write("\n")
dosyaappend.write(trsnwrt)
dosyaappend.write("\n")

# Sezar Bey
# Şifreli text'e göre 'harflerr' değişkenini ayarlayın.
# Eğer şifreli textte küçük harf veya sayı gibi eklenmesi gereken şeyler varsa ekleyin veya çıkarın
# aksi takdirde doğru sonuç alamazsınız.

mesaj = cryptic
harflerr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

for csrmrq in range(len(harflerr)):
    translated = ""
    for symbl in mesaj:
        if symbl in harflerr:
            num = harflerr.find(symbl)
            num = num - csrmrq
            if num < 0:
                num = num + len(harflerr)
            translated = translated + harflerr[num]
        else:
            translated = translated + symbl
        szrwrt = 'Sezar #%s: %s' % (csrmrq, translated)
    print("\x1b[1;36;1mSezar #%s:\033[1;37;1m %s" % (csrmrq, translated))
    dosyaappend.write("\n")
    dosyaappend.write(szrwrt)
dosyaappend.write("\n")

# Affine harekatı
dosyaappend.write("\n")

cod = cryptic
sitringuzunluk = len(cod)
i_i = 0
a = 2
mod = int(26)

while a < mod:
    b = 0
    a1 = 1
    a_li = a
    mod_lu = mod

    while mod_lu != 0:
        a_li %= mod_lu
        (a_li, mod_lu) = (mod_lu, a_li)

    if a_li == 1:
        while a1 * a % mod != 1:
            a1 += 1

        while b < mod:
            i_i = 0
            ca = "Affine a= " + str(a) + " b= " + str(b)
            dosyaappend.write("Affine: " + ca + ": \n")
            print("\x1b[1;36;1m"+ ca + "\033[1;37;1m")
            while i_i < sitringuzunluk:
                karakter = cod[i_i]
                y = ord(karakter) - 97
                x = (a1 * (y - b)) % mod
                aff = chr(x + 97)
                print(aff, end="")
                i_i += 1
                dosyaappend.write(aff)
            dosyaappend.write("\n")
            print()
            dosyaappend.write(" ")
            b += 1

        print()
        dosyaappend.write(" ")
    a += 1

# Vinegere
v = cryptic
v = v.replace(" ", "")
if v.isalpha():
    e = input("Vinegere için key giriniz: ")
else:
    print("\x1b[1;31;1mVinegere şifrelemesi sayı içermez!\033[1;37;1m")
harfler = "abcdefghijklmnopqrstuvwxyz"


def vinegere(v, e):
    vin = ""
    vineg = []
    for i in e:
        vineg.append(harfler.find(i))
    x = 0
    for i in v:
        if x == len(vineg):
            x = 0
        pos = harfler.find(i.lower()) - vineg[x]
        if pos < 0:
            pos = pos + 26
        vin += harfler[pos].lower()
        x += 1
    return vin

try:
    vin = vinegere(v, e)
    vinA = "Vinegere: " + vin
    print("\x1b[1;36;1mVinegere: \033[1;37;1m" + vin)
except:
    vinA = "Bu şifrelenmiş text kesin olarak vinegere ile şifrelenmemiştir!"
    print("\x1b[1;31;1mBu şifrelenmiş text kesin olarak vinegere ile şifrelenmemiştir!\033[1;37;1m")

dosyaappend.write("\n")
dosyaappend.write(vinA)
dosyaappend.write("\n")
dosyaappend.close()
