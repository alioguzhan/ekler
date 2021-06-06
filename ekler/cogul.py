# pylint: disable=invalid-name, missing-docstring
_BULUNMA_GRUBU_1 = "aıou"
_BULUNMA_GRUBU_2 = "eiöü"


def ekle_cogul(son_eslesen, kelime, ayir):
    """Cogul Eki"""
    ek_orta_harf = ""
    if son_eslesen in _BULUNMA_GRUBU_1:
        ek_orta_harf = "a"
    elif son_eslesen in _BULUNMA_GRUBU_2:
        ek_orta_harf = "e"

    ek = "l" + ek_orta_harf + "r"
    ayirma_eki = "'" if ayir else ""
    sonuc = kelime + ayirma_eki + ek
    return sonuc
