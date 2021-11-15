def doctest_tb_plain():
    """
In [18]: xmode plain
Exception reporting mode: Plain

In [19]: run simpleerr.py
Traceback (most recent call last):
    ...line ..., in <module>
    bar(mode)
    ...line ..., in bar
    div0()
    ...line ..., in div0
    x/y
ZeroDivisionError: ...
    """


empty = 1
