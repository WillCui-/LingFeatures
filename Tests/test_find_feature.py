# coding=utf-8
from unittest import TestCase

from LingFeatures.lingfeatures import find_feature


class TestFind_feature(TestCase):
    def test1(self):
        self.assertEqual([], find_feature([]))

    def test2(self):
        self.assertEqual([0, 11], find_feature(['p']))

    def test3(self):
        self.assertEqual(find_feature(['p', 'b']), [0, 11])

    def test4(self):
        self.assertEqual(find_feature(['p', 't']), [0])

    def test5(self):
        self.assertEqual(find_feature(['b', 'd', 'ɟ', 'n']), [0, 8])
