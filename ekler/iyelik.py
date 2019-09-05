# pylint: disable=invalid-name, missing-docstring
_IYELIK_GRUBU_1 = "aı"
_IYELIK_GRUBU_2 = "ei"
_IYELIK_GRUBU_3 = "ou"


def ekle_iyelik(son_eslesen, kelime, son_karakter, ayir):
    """Iyelik Eki"""
    kaynastirma_harfi = "n"
    if son_eslesen in _IYELIK_GRUBU_1:
        ek = "ın"
    elif son_eslesen in _IYELIK_GRUBU_2:
        ek = "in"
    elif son_eslesen in _IYELIK_GRUBU_3:
        ek = "un"
    else:
        ek = "ün"

    ayirma_eki = "'" if ayir else ""

    if son_karakter == son_eslesen:  # kelimenin sonu sesli harf
        sonuc = kelime + ayirma_eki + kaynastirma_harfi + ek
    else:
        sonuc = kelime + ayirma_eki + ek

    return sonuc
