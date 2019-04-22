from unittest import TestCase

from LingFeatures.lingfeatures import find_sounds


class TestMain(TestCase):
    def test1(self):
        self.assertEqual([], find_sounds([]))

    def test2(self):
        self.assertEqual(['\xc9\xbd', '\xc9\xbe'], find_sounds(['tap']))

    def test3(self):
        self.assertEqual(['\xc9\xbe'], find_sounds(['tap', 'anterior']))

    def test4(self):
        self.assertEqual(['\xc9\xbe'], find_sounds(['anterior', 'tap']))

    def test5(self):
        self.assertEqual([], find_sounds(['nasal', 'approximant']))

    def test6(self):
        self.assertEqual(['\xca\x8e', 'l', '\xc9\xad'], find_sounds(['lateral', 'approximant']))

