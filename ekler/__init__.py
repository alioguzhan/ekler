# coding: utf-8
# upper ve lower islemi turkce icin duzgun calismiyor bu harflerde.
# kendimiz elle karsiliklarini vermemiz gerekiyor.
_LOWER_MAP = {
    ord(u'İ'): u'i',
    ord(u'I'): u'ı',
}

_SESLI_HARFLER = 'aeıioöuü'
_INCE_HARFLER = 'eiöü'
_IYELIK_GRUBU_1 = 'aı'
_IYELIK_GRUBU_2 = 'ei'
_IYELIK_GRUBU_3 = 'ou'
_IYELIK_GRUBU_4 = 'öü'

IYELIK_EKI = 1  # Iyelik ekleri icin. Ornek: Ali'nin, Ayse'nin, Ahmet'in...

YONELME_EKI = 2  # Yonelme ekleri icin. Ornek: Ali'ye, Ayse'ye, Ahmet'e...


def ekli(kelime, ek_tipi, ayir=True):
    """ Verilen kelimeyi belirtilen parametrelere gore sonuna ek halmis halde
    geri dondurur.

    kelime -> herhangi bir string. 

    ek_tipi -> 1 ya da 2 olabilir. 
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
        raise Exception('kelime string olmali.')

    if ek_tipi not in [IYELIK_EKI, YONELME_EKI]:
        raise Exception('Ek tipi ' + str(ek_tipi) + ' gecerli degil.')

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
            kaynastirma_harfi = 'n'
            if son_eslesen in _IYELIK_GRUBU_1:
                ek = 'ın'
            elif son_eslesen in _IYELIK_GRUBU_2:
                ek = 'in'
            elif son_eslesen in _IYELIK_GRUBU_3:
                ek = 'un'
            else:
                ek = 'ün'
        else:
            kaynastirma_harfi = 'y'
            if son_eslesen in _INCE_HARFLER:
                ek = 'e'
            else:
                ek = 'a'

        if son_karakter == son_eslesen:  # kelimenin sonu sesli harf
            if ayir:
                sonuc = kelime + "'" + kaynastirma_harfi + ek
            else:
                sonuc = kelime + kaynastirma_harfi + ek
        else:
            if ayir:
                sonuc = kelime + "'" + ek
            else:
                sonuc = kelime + ek

    # icinde sesli harf olmayan, yani turkce kurallarina aykiri
    # herhangi bir kelimeyse buraya duser.
    else:
        if ayir:
            if ek_tipi is IYELIK_EKI:
                sonuc = kelime + "'nin"
            else:
                sonuc = kelime + "'ye"
        else:
            if ek_tipi is IYELIK_EKI:
                sonuc = kelime + "nin"
            else:
                sonuc = kelime + "ye"

    return sonuc
