<p align="center">
<img src="ekler.png" width="300">
</p>

# Ekler
Turkce kelimelerin sonuna, fonetik yapilarina gore:

- `Iyelik` 
- `Yonelme`

eklerini ekler. 

## Kurulum & Kullanim 

    $ pip install ekler

Ornek Kullanim:

    from ekler import ekli, YONELME_EKI, IYELIK_EKI

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



## To Do

- ~~BUYUK HARF ve camelCase destegi~~
- `Bulunma` ve `Ayrilma` ekleri ( ali'de , ali'den )
- ~~Daha fazla test~~