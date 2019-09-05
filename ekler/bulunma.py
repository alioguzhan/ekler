# pylint: disable=invalid-name, missing-docstring
_BULUNMA_GRUBU_1 = "aıou"
_BULUNMA_GRUBU_2 = "eiöü"


def ekle_bulunma(son_eslesen, kelime, son_karakter, ayir):
    """Bulunma Eki"""
    fistikci = "fstkçşhp"
    ek_ilk_harf = "d"  # d ya da t
    ek_son_harf = ""  # e ya da a
    if son_eslesen in _BULUNMA_GRUBU_1:
        ek_son_harf = "a"
    elif son_eslesen in _BULUNMA_GRUBU_2:
        ek_son_harf = "e"

    if son_karakter in fistikci:
        ek_ilk_harf = "t"

    ek = ek_ilk_harf + ek_son_harf
    ayirma_eki = "'" if ayir else ""
    sonuc = kelime + ayirma_eki + ek
    return sonuc
