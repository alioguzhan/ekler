# pylint: disable=too-many-branches, invalid-name
""" EKLER:
Turkce kelimelerin sonuna, fonetik yapilarina gore:
 - iyelik
 - yonelme
 - bulunma
 - ayrilma
ekeri ekleyen module.

2019
Ali Oguzhan Yildiz
aoguzhanyildiz@gmail.com
"""
from .iyelik import ekle_iyelik
from .yonelme import ekle_yonelme
from .bulunma import ekle_bulunma
from .aykiri import ekle_aykiri
# upper ve lower islemi turkce icin duzgun calismiyor bu harflerde.
# kendimiz elle karsiliklarini vermemiz gerekiyor.
_LOWER_MAP = {ord(u"İ"): u"i", ord(u"I"): u"ı"}

_SESLI_HARFLER = "aeıioöuü"

IYELIK_EKI = 1  # Iyelik ekleri icin. Ornek: Ali'nin, Ayse'nin, Ahmet'in...
YONELME_EKI = 2  # Yonelme ekleri icin. Ornek: Ali'ye, Ayse'ye, Ahmet'e...
BULUNMA_EKI = 3  # Bulunma ekleri. Ornek: Ali'de, Paris'te, Maraş'ta, Reis Büfe'de...
AYRILMA_EKI = 4  # Ayrilma ekleri. Ornek: Ali'den, Paris'ten, Maraş'tan...


def ekli(kelime, ek_tipi, ayir=True):
    """Verilen kelimeyi belirtilen parametrelere gore sonuna ek halmis halde
    geri dondurur.

    kelime -> herhangi bir string.

    ek_tipi -> 1 ya da 2 olabilir.)
    1 -> IYELIK_EKI -> Ornek: Ali'nin, Ayse'nin, Ahmet'in...
    2 -> YONELME_EKI -> Ornek: Ali'ye, Ayse'ye, Ahmet'e...

    ayir -> Verilen kelime ozel isim ise sonuna gelen eki kesme isareti ile
    ayirir. Default olarak True. Ekin ayrilmasini istemiyorsaniz False olarak
    belirtmeniz gerekir.

    NOTE: Turkcedeki buyuk i / kucuk i ayriminda sorun oldugu icin,
    verilen kelime oncelikle kucuk harfe cevrilir. Yani kelimeniz buyuk harf
    iceriyorsa ya da komple buyuk harfse fonksiyondan donen sonucu tekrar
    istediginiz hale sokmaniz gerekir.

    TODO: Bunu aslinda otomatik hale getirebiliriz.
    """
    if not kelime or not ek_tipi:
        return None

    if not isinstance(kelime, str):
        raise Exception("kelime string olmali.")

    if ek_tipi not in [IYELIK_EKI, YONELME_EKI, BULUNMA_EKI, AYRILMA_EKI]:
        raise Exception("Ek tipi " + str(ek_tipi) + " gecerli degil.")

    kelime_fixed = str(kelime).translate(_LOWER_MAP).lower()

    son_karakter = kelime_fixed[-1]
    son_eslesen = None
    sonuc = None

    for index, karakter in enumerate(kelime_fixed[::-1]):
        if karakter in _SESLI_HARFLER and index < 3:
            # turkcede anlam ifade eden kelimelerde art arda 3 sessiz harf yok ??
            son_eslesen = karakter
            break

    if son_eslesen:
        if ek_tipi is IYELIK_EKI:
            sonuc = ekle_iyelik(son_eslesen, kelime, son_karakter, ayir)
        elif ek_tipi is YONELME_EKI:
            sonuc = ekle_yonelme(son_eslesen, kelime, son_karakter, ayir)
        elif ek_tipi is BULUNMA_EKI:
            sonuc = ekle_bulunma(son_eslesen, kelime, son_karakter, ayir)
        else:
            # ayrilma eki
            sonuc = ekle_bulunma(son_eslesen, kelime, son_karakter, ayir)
            sonuc = sonuc + "n"

    # icinde sesli harf olmayan, yani turkce kurallarina aykiri
    # herhangi bir kelimeyse buraya duser.
    else:
        sonuc = ekle_aykiri(ek_tipi, kelime, ayir)

    return sonuc
