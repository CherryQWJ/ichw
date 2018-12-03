#!/usr/bin/env/python3

"""Currency.py: Calculation for currency exchange.

__author__ = "QiuWeiJie"
__pkuid__  = "1800011802"
__email__  = "qiuweijie2000@pku.edu.cn"
"""
currency_from = input()
currency_to = input()
amount_from = input()
def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    from urllib.request import urlopen

    doc = urlopen("http://cs1110.cs.cornell.edu/2016fa/a1server.php?from="+currency_from+"&to="+currency_to+"&amt="+amount_from)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    print(jstr)
    jstr1 = jstr.split(" : ")
    if jstr1[-2] == ' false,"error" ':
        value = "Source currency code is invalid."
    else:
        jstr2 = jstr1[2].split('"')
        jstr3 = jstr2[1].split()
        value = float(jstr3[0])
    return value

print(exchange(currency_from, currency_to, amount_from))
def text_exchange(a):
    assert (exchange(USD, EUR, 2.5) == a)
    
text_exchange(2.1689225)   
    
    #以上代码是我和陈舒仪交流的成果
