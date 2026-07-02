"""
Calculadora Científica — template de trabalho em grupo.

Cada membro do grupo fica responsável por uma seção de funções.
Leia o README para ver a distribuição e os requisitos.
"""

import math


# ─── Seção 1: Operações básicas ──────────────────────────────────────────────

def add(a, b):
    """Retorna a + b."""
    raise NotImplementedError("Implemente esta função")


def subtract(a, b):
    """Retorna a - b."""
    raise NotImplementedError("Implemente esta função")


def multiply(a, b):
    """Retorna a * b."""
    raise NotImplementedError("Implemente esta função")


def divide(a, b):
    """Retorna a / b. Lança ValueError se b == 0."""
    raise NotImplementedError("Implemente esta função")


# ─── Seção 2: Potência e raiz ────────────────────────────────────────────────

def power(base, exp):
    """Retorna base ** exp."""
    raise NotImplementedError("Implemente esta função")


def sqrt(n):
    """Retorna a raiz quadrada de n. Lança ValueError se n < 0."""
    raise NotImplementedError("Implemente esta função")


def cbrt(n):
    """Retorna a raiz cúbica de n (suporta negativos)."""
    raise NotImplementedError("Implemente esta função")


# ─── Seção 3: Trigonometria ──────────────────────────────────────────────────

def sin(x):
    """Retorna o seno de x (em radianos)."""
    raise NotImplementedError("Implemente esta função")


def cos(x):
    """Retorna o cosseno de x (em radianos)."""
    raise NotImplementedError("Implemente esta função")


def tan(x):
    """Retorna a tangente de x (em radianos)."""
    raise NotImplementedError("Implemente esta função")


def degrees_to_radians(d):
    """Converte graus para radianos."""
    raise NotImplementedError("Implemente esta função")


def radians_to_degrees(r):
    """Converte radianos para graus."""
    raise NotImplementedError("Implemente esta função")


# ─── Seção 4: Logaritmos ─────────────────────────────────────────────────────

def log(x):
    """Retorna o logaritmo natural de x. Lança ValueError se x <= 0."""
    raise NotImplementedError("Implemente esta função")


def log10(x):
    """Retorna log na base 10 de x. Lança ValueError se x <= 0."""
    raise NotImplementedError("Implemente esta função")


def log_base(x, base):
    """Retorna log na base 'base' de x. Lança ValueError para entradas inválidas."""
    raise NotImplementedError("Implemente esta função")


# ─── Seção 5: Estatística ────────────────────────────────────────────────────

def mean(values):
    """Retorna a média aritmética. Lança ValueError se a lista for vazia."""
    raise NotImplementedError("Implemente esta função")


def median(values):
    """Retorna a mediana. Lança ValueError se a lista for vazia."""
    raise NotImplementedError("Implemente esta função")


def mode(values):
    """Retorna o valor mais frequente. Lança ValueError se a lista for vazia."""
    raise NotImplementedError("Implemente esta função")


def std_dev(values):
    """Retorna o desvio padrão amostral. Lança ValueError se len(values) < 2."""
    raise NotImplementedError("Implemente esta função")
