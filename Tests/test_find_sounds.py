# coding=utf-8
from unittest import TestCase

import LingFeatures.lingfeatures


class TestFind_sounds(TestCase):
    def test1(self):
        self.assertEqual([], LingFeatures.lingfeatures.find_sounds([]))

    def test2(self):
        self.assertEqual(['\xc9\xbd', '\xc9\xbe'], LingFeatures.lingfeatures.find_sounds(['tap']))

    def test3(self):
        self.assertEqual(['\xc9\xbe'], LingFeatures.lingfeatures.find_sounds(['tap', 'anterior']))

    def test4(self):
        self.assertEqual(['\xc9\xbe'], LingFeatures.lingfeatures.find_sounds(['anterior', 'tap']))

    def test5(self):
        self.assertEqual([], LingFeatures.lingfeatures.find_sounds(['nasal', 'approximant']))

    def test6(self):
        self.assertEqual(['\xca\x8e', 'l', '\xc9\xad'], LingFeatures.lingfeatures.find_sounds(['lateral', 'approximant']))
