# -*- coding: iso-8859-1 -*-

import logging

class Calculadora:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def add(self, par1, par2):
        return par1 + par2

    def sub(self, par1, par2):
        if (par1 - par2) < 0:
            raise ExceptionCalculadora("Esta calculadora só utiliza números naturais")
        return par1 - par2

    def mul(self, par1, par2):
        return par1 * par2

    def div(self, par1, par2):
        if par2 == 0:
            raise ExceptionCalculadora("Não posso dividir por zero")
        return par1 / par2
