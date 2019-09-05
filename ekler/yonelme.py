# pylint: disable=invalid-name, missing-docstring
_INCE_HARFLER = "eiöü"


def ekle_yonelme(son_eslesen, kelime, son_karakter, ayir):
    """Iyelik Eki"""
    kaynastirma_harfi = "y"
    ek = "e" if son_eslesen in _INCE_HARFLER else "a"
    ayirma_eki = "'" if ayir else ""

    if son_karakter == son_eslesen:  # kelimenin sonu sesli harf
        sonuc = kelime + ayirma_eki + kaynastirma_harfi + ek
    else:
        sonuc = kelime + ayirma_eki + ek

    return sonuc
