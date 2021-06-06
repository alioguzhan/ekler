<p align="center">
<img src="https://raw.githubusercontent.com/alioguzhan/ekler/master/ekler.jpg" width="300">
</p>

# Ekler

[![PyPI](https://img.shields.io/pypi/v/ekler?color=blue)](https://pypi.org/project/ekler/)
[![Run Tests](https://github.com/alioguzhan/ekler/actions/workflows/test.yml/badge.svg)](https://github.com/alioguzhan/ekler/actions/workflows/test.yml)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ekler)
![PyPI - Downloads](https://img.shields.io/pypi/dm/ekler?color=blue)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://opensource.org/licenses/MIT)

Turkce kelimelerin sonuna, fonetik yapilarina gore:

- `Iyelik`
- `Yonelme`
- `Bulunma`
- `Ayrılma`
- `Çoğul`
- `Vasıta`

eklerini ekler.

## Kurulum & Kullanim

```bash
pip install ekler
```

Ornek Kullanim:

```py
from ekler import ekli, YONELME_EKI, IYELIK_EKI, BULUNMA_EKI, AYRILMA_EKI, VASITA_EKI

isim = 'ali'
ekli(isim, IYELIK_EKI)
## ali'nin

ekli(isim, YONELME_EKI)
## ali'ye

isim = "Ahmet"
ekli(isim, IYELIK_EKI)
## ahmet'in

ekli(isim, YONELME_EKI)
## ahmet'e

ekli(isim, YONELME_EKI, False) # kesme isareti yok
## ahmete

isim = "Istanbul"
ekli(isim, BULUNMA_EKI)
## Istanbul'da

ekli(isim, AYRILMA_EKI)
## Istanbul'dan

isim = "Gaziantep"
ekli(isim, BULUNMA_EKI) # sertlesme var. de -> te
## Gaziantep'te

ekli(isim, AYRILMA_EKI) # sertlesme var. den -> ten
## Gaziantep'ten

isim = "kitap"
ekli(isim, COGUL_EKI)
## kitaplar

isim = "kalem"
ekli(isim, COGUL_EKI)
## kalemler

isim = "Leyla"
ekli(isim, VASITA_EKI)
## Leyla'yla
```

## Sınırlamalar

Kutuphaneyi gelistirme amacim `sahis`, `cografi yer`, `kullanici adi (username)` kelimelerinde kullanilmasidir. Bu tarz kelimelerde duzgun calismaktadir. (**istisna ya da hata bulursaniz lutfen belirtin**)

Ancak; kurum, mekan gibi sonuna gelecek eklerin bir standardi olmayan yerlerde hatali sonuclar verecektir. Mesela; `Ziraat Bankasi` kelimesine bulunma eki kullanmak istediginizde `Ziraat Bankasi'nda` yerine `Ziraat Bankasi'da` seklinde sonuc verecektir.

Ama mesela `Akbank` kelimesinde bu durum gecerli degil. Duzgun bir sekilde `Akbank'ta` ve `Akbank'tan` seklinde sonuc verecektir.

Dedigim gibi sorunsuz calismasi icin basta bahsettigim durumlarda kullanabilirsiniz.

## Katkıda Bulunanlar

- [@midorikocak](https://github.com/midorikocak)
