#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from mosaicomponents.codefield import CodeField
# Se for usar o py.test:
# Comentar a linha acima, e descomentar a de baixo
#from mosaicomponents.mosaicomponents.codefield import CodeField

class TestCodeField(TestCase):

    def setUp(self):
        """Do the test basic setup."""
        data = {"label": ("Type"), "name":"type", "value": "True"}
        self.codefield = CodeField(data, self)

    # ----------------------------------------------------------------------
    def test_get_value(self):
        self.assertTrue(self.codefield.get_value())

    # ----------------------------------------------------------------------
    def test_set_value(self):
        value = "Teste"
        self.assertIsNone(self.codefield.set_value(value))
        value = "True"
        self.assertIsNone(self.codefield.set_value(value))
        value = ""
        self.assertIsNone(self.codefield.set_value(value))
        value = "Algo"
        self.assertIsNone(self.codefield.set_value(value))

    # ----------------------------------------------------------------------
    def test_insert_at_cursor(self):
        value = "Teste"
        self.assertIsNone(self.codefield.set_value(value))
        value = "True"
        self.assertIsNone(self.codefield.set_value(value))
        value = ""
        self.assertIsNone(self.codefield.set_value(value))
        value = "Algo"
        self.assertIsNone(self.codefield.set_value(value))
