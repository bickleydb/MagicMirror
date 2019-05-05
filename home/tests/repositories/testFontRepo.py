from django.test import TestCase
from django.contrib.auth.models import User

import unittest
from home.shared.repositories.FontRepo import FontRepo
from home.models.FontModel import FontModel
from home.models.ApplicationDefinitionModel import ApplicationDefinitionModel


class EmptyFontTest(unittest.TestCase):
    def test_emptyFontList(self):
        repo = FontRepo()
        self.assertEqual(len(repo.load_fonts()), 0)


class SingleFontTest(TestCase):
    def setUp(self):
        FontModel.get_manager().create(
            name="TestFont",
            url=""
        )

    def testSingleFontTest(self):
        repo = FontRepo()
        self.assertEqual(len(repo.load_fonts()), 1)


class MultiFontTest(TestCase):
    def setUp(self):
        FontModel.get_manager().create(
            name="TestFont_0",
            url=""
        )
        FontModel.get_manager().create(
            name="TestFont_1",
            url=""
        )

    def testMultiFont(self):
        repo = FontRepo()
        self.assertEqual(len(repo.load_fonts()), 2)
