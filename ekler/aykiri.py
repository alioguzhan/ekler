# pylint: disable=invalid-name, missing-docstring
IYELIK_EKI = 1
YONELME_EKI = 2
BULUNMA_EKI = 3
AYRILMA_EKI = 4


def ekle_aykiri(ek_tipi, kelime, ayir):
    ayirma_eki = "'" if ayir else ""

    if ek_tipi is IYELIK_EKI:
        sonuc = kelime + ayirma_eki + "nin"
    elif ek_tipi is YONELME_EKI:
        sonuc = kelime + ayirma_eki + "ye"
    elif ek_tipi is BULUNMA_EKI:
        sonuc = kelime + ayirma_eki + "de"
    else:
        sonuc = kelime + ayirma_eki + "den"

    return sonuc
