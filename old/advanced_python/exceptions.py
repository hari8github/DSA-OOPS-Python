#exceptions and error.

#filenotfounderror
#zerodivisionerror
#modulenotfounderror
#valueerror
#indexerror
#assertionerror etc.....

"""try:
    a = 100/0
except:
    print("error da")

try:
    b = 1/0
    c = 5*1
    print(b+c)
    print(c)
except Exception as e: #or except ZeroDivisionError as e:
    print(e)
else:
    print("summa da")
finally:
    print("this is exception da")"""

"""class ValueTooHigh(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test(x):
    if x > 100:
        raise ValueTooHigh('value is too high bro and your value is: ', x)

try:
    test(200)
except ValueTooHigh as e:
    print(e.message, e.value)"""

"""import logging
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

import loggings"""