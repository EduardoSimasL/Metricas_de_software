# -*- coding: iso-8859-1 -*-

from calculadora import Calculadora
from exception_calculadora import ExceptionCalculadora

if __name__ == "__main__":
    # Exemplo de uso
    calc = Calculadora()
    try:
        print("Soma:", calc.add(5, 3))
        print("Subtração:", calc.sub(5, 3))
        print("Multiplicação:", calc.mul(5, 3))
        print("Divisão:", calc.div(5, 3))
    except ExceptionCalculadora as e:
        print("Erro na calculadora:", e)

    try:
        raise ExceptionCalculadora.erroAoDividirPorZero()
    except ExceptionCalculadora as e:
        print("Erro:", e)

    try:
        raise ExceptionCalculadora.erroAoUsarInteiro()
    except ExceptionCalculadora as e:
        print("Erro:", e)
