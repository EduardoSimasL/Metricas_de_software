# -*- coding: iso-8859-1 -*-

class ExceptionCalculadora(Exception):
    def __init__(self, message):
        super().__init__(message)

    @staticmethod
    def erroAoDividirPorZero():
        return ExceptionCalculadora("Não posso dividir por zero")

    @staticmethod
    def erroAoUsarInteiro():
        return ExceptionCalculadora("Esta calculadora só utiliza números naturais")
