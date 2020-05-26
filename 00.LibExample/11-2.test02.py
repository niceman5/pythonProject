"""
주어진 인수에 데해 a/b를 실행하는 함수
>>> div(5,2)
2.5
"""


def div(a, b):
    """
    답은 소수로 반환됩니다.
    >>> [div(n, 2) for n in range(5)]
    [0.0, 0.5, 1.0, 1.5, 2.0]
    """

    return a/b


if __name__ == "__main__":
    import doctest

    doctest.testmod()