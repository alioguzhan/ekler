# coding: utf-8
import unittest
from ekler import ekli, IYELIK_EKI, YONELME_EKI


class EkTestCase(unittest.TestCase):
    """ Tests for `ekli.py` """

    def test_iyelik_ekleri(self):
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
            "utku": "utkunun"
        }

        for isim, sonuc in iyelik_ekleri_map.items():
            modified = ekli(isim, IYELIK_EKI, False)
            self.assertEqual(sonuc, modified)

    def test_iyelik_ekleri_ozel(self):
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
            "utku": "utku'nun"
        }

        for isim, sonuc in iyelik_ekleri_ozel_map.items():
            modified = ekli(isim, IYELIK_EKI)
            self.assertEqual(sonuc, modified)

    def test_yonelme_ekleri(self):
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
            "utku": "utkuya"
        }

        for isim, sonuc in yonelme_ekleri_map.items():
            modified = ekli(isim, YONELME_EKI, False)
            self.assertEqual(sonuc, modified)

    def test_yonelme_ekleri_ozel(self):
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
            "utku": "utku'ya"
        }

        for isim, sonuc in yonelme_ekleri_ozel_map.items():
            modified = ekli(isim, YONELME_EKI)
            self.assertEqual(sonuc, modified)


if __name__ == '__main__':
    unittest.main()
