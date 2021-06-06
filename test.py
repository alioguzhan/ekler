"""Unit Tests"""
import unittest
from ekler import ekli, IYELIK_EKI, YONELME_EKI, BULUNMA_EKI, AYRILMA_EKI, COGUL_EKI, VASITA_EKI


class EkTestCase(unittest.TestCase):
    """ Tests for `ekli.py` """

    def __init__(self, methodName):
        self.bulunma_ekleri_map = {
            "antalya": "antalya'da",
            "Bursa": "Bursa'da",
            "Şule": "Şule'de",
            "gebze": "gebze'de",
            "eğerce": "eğerce'de",
            "Ağrı": "Ağrı'da",
            "ali": "ali'de",
            "mersin": "mersin'de",
            "istanbul": "istanbul'da",
            "kandilli": "kandilli'de",
            "ordu": "ordu'da",
            # Fistikci Sahap
            "gaziantep": "gaziantep'te",
            "sarp": "sarp'ta",
            "tokat": "tokat'ta",
            "kümes": "kümes'te",
            "dolap": "dolap'ta",
            "külah": "külah'ta",
            "Asıf": "Asıf'ta",
            "Muş": "Muş'ta",
            "Uşak": "Uşak'ta",
            "Kıraç": "Kıraç'ta",
        }
        super().__init__(methodName)

    def test_iyelik_ekleri(self):
        """ Testing iyelik ekleri"""
        iyelik_ekleri_map = {
            "ali": "alinin",
            "ayşe": "ayşenin",
            "onur": "onurun",
            "osman": "osmanın",
            "samet": "sametin",
            "gürsel": "gürselin",
            "nilüfer": "nilüferin",
            "mert": "mertin",
            "turgut": "turgutun",
            "fatih": "fatihin",
            "umut": "umutun",
            "barkın": "barkının",
            "utku": "utkunun",
            "can": "canın",
        }

        for isim, sonuc in iyelik_ekleri_map.items():
            modified = ekli(isim, IYELIK_EKI, False)
            self.assertEqual(sonuc, modified)

    def test_iyelik_ekleri_ozel(self):
        """Testing iyeli ekleri [ozel isim]"""
        iyelik_ekleri_ozel_map = {
            "ali": "ali'nin",
            "ayşe": "ayşe'nin",
            "onur": "onur'un",
            "osman": "osman'ın",
            "samet": "samet'in",
            "gürsel": "gürsel'in",
            "nilüfer": "nilüfer'in",
            "mert": "mert'in",
            "turgut": "turgut'un",
            "fatih": "fatih'in",
            "umut": "umut'un",
            "barkın": "barkın'ın",
            "utku": "utku'nun",
            "can": "can'ın",
        }

        for isim, sonuc in iyelik_ekleri_ozel_map.items():
            modified = ekli(isim, IYELIK_EKI)
            self.assertEqual(sonuc, modified)

    def test_yonelme_ekleri(self):
        """Testing yonelme ekleri"""
        yonelme_ekleri_map = {
            "ali": "aliye",
            "ayşe": "ayşeye",
            "onur": "onura",
            "osman": "osmana",
            "samet": "samete",
            "gürsel": "gürsele",
            "nilüfer": "nilüfere",
            "mert": "merte",
            "turgut": "turguta",
            "fatih": "fatihe",
            "umut": "umuta",
            "barkın": "barkına",
            "utku": "utkuya",
            "can": "cana",
        }

        for isim, sonuc in yonelme_ekleri_map.items():
            modified = ekli(isim, YONELME_EKI, False)
            self.assertEqual(sonuc, modified)

    def test_yonelme_ekleri_ozel(self):
        """Testing yonelme ekleri [ozel]"""
        yonelme_ekleri_ozel_map = {
            "ali": "ali'ye",
            "ayşe": "ayşe'ye",
            "onur": "onur'a",
            "osman": "osman'a",
            "samet": "samet'e",
            "gürsel": "gürsel'e",
            "nilüfer": "nilüfer'e",
            "mert": "mert'e",
            "turgut": "turgut'a",
            "fatih": "fatih'e",
            "umut": "umut'a",
            "barkın": "barkın'a",
            "utku": "utku'ya",
            "can": "can'a",
        }

        for isim, sonuc in yonelme_ekleri_ozel_map.items():
            modified = ekli(isim, YONELME_EKI)
            self.assertEqual(sonuc, modified)

    def test_vasita_ekleri(self):
        """Testing vasita ekleri"""
        vasita_ekleri_map = {
            "ali": "aliyle",
            "ayşe": "ayşeyle",
            "onur": "onurla",
            "osman": "osmanla",
            "samet": "sametle",
            "gürsel": "gürselle",
            "nilüfer": "nilüferle",
            "mert": "mertle",
            "turgut": "turgutla",
            "fatih": "fatihle",
            "umut": "umutla",
            "barkın": "barkınla",
            "utku": "utkuyla",
            "can": "canla",
        }

        for isim, sonuc in vasita_ekleri_map.items():
            modified = ekli(isim, VASITA_EKI, False)
            self.assertEqual(sonuc, modified)

    def test_vasita_ekleri_ozel(self):
        """Testing vasita ekleri [ozel]"""
        vasita_ekleri_ozel_map = {
            "ali": "ali'yle",
            "ayşe": "ayşe'yle",
            "onur": "onur'la",
            "osman": "osman'la",
            "samet": "samet'le",
            "gürsel": "gürsel'le",
            "nilüfer": "nilüfer'le",
            "mert": "mert'le",
            "turgut": "turgut'la",
            "fatih": "fatih'le",
            "umut": "umut'la",
            "barkın": "barkın'la",
            "utku": "utku'yla",
            "can": "can'la",
        }

        for isim, sonuc in vasita_ekleri_ozel_map.items():
            modified = ekli(isim, VASITA_EKI)
            self.assertEqual(sonuc, modified)

    def test_mixed_case_iyelik(self):
        """Testing mixed_case iyelik ekleri"""
        mixed_case_yonelme_map = {
            "alİ": "alİ'ye",
            "Ayşe": "Ayşe'ye",
            "ONUR": "ONUR'a",
            "osmAN": "osmAN'a",
            "samet": "samet'e",
            "gürsel": "gürsel'e",
            "nilüfer": "nilüfer'e",
            "mert": "mert'e",
            "turgut": "turgut'a",
            "faTİh": "faTİh'e",
            "umut": "umut'a",
            "BARKIN": "BARKIN'a",
            "utku": "utku'ya",
            "cAN": "cAN'a",
        }

        for isim, sonuc in mixed_case_yonelme_map.items():
            modified = ekli(isim, YONELME_EKI)
            self.assertEqual(sonuc, modified)

    def test_cogul_ekleri(self):
        """Testing cogul ekleri"""
        cogul_ekleri_ozel_map = {
            "ali": "aliler",
            "ayşe": "ayşeler",
            "onur": "onurlar",
            "osman": "osmanlar",
            "samet": "sametler",
            "gürsel": "gürseller",
            "nilüfer": "nilüferler",
            "mert": "mertler",
            "turgut": "turgutlar",
            "fatih": "fatihler",
            "umut": "umutlar",
            "barkın": "barkınlar",
            "utku": "utkular",
            "can": "canlar",
        }

        for isim, sonuc in cogul_ekleri_ozel_map.items():
            modified = ekli(isim, COGUL_EKI, False)
            self.assertEqual(sonuc, modified)

    def test_cogul_ekleri_ozel(self):
        """Testing cogul ekleri"""
        cogul_ekleri_ozel_map = {
            "ali": "ali'ler",
            "ayşe": "ayşe'ler",
            "onur": "onur'lar",
            "osman": "osman'lar",
            "samet": "samet'ler",
            "gürsel": "gürsel'ler",
            "nilüfer": "nilüfer'ler",
            "mert": "mert'ler",
            "turgut": "turgut'lar",
            "fatih": "fatih'ler",
            "umut": "umut'lar",
            "barkın": "barkın'lar",
            "utku": "utku'lar",
            "can": "can'lar",
        }

        for isim, sonuc in cogul_ekleri_ozel_map.items():
            modified = ekli(isim, COGUL_EKI)
            self.assertEqual(sonuc, modified)

    def test_silly_words_iyelik(self):
        """Testing silly words"""
        silly_words_map = {
            "asddfg": "asddfg'nin",
            "sndly": "sndly'nin",
            "eksry": "eksry'nin",
            "snr_srkbdy": "snr_srkbdy'nin",
        }

        for isim, sonuc in silly_words_map.items():
            modified = ekli(isim, IYELIK_EKI)
            self.assertEqual(sonuc, modified)

    def test_bulunma_ekleri(self):
        """Testing bulunma ekleri..."""
        for isim, sonuc in self.bulunma_ekleri_map.items():
            modified = ekli(isim, BULUNMA_EKI)
            self.assertEqual(sonuc, modified)

    def test_ayrilma_ekleri(self):
        """Testing ayrilma ekleri..."""
        for isim, sonuc in self.bulunma_ekleri_map.items():
            modified = ekli(isim, AYRILMA_EKI)
            self.assertEqual(sonuc + "n", modified)


if __name__ == "__main__":
    unittest.main(verbosity=2)
