from __future__ import print_function
from __future__ import standard_library
standard_library.install_aliases()
from future.builtins import next
from future.builtins import object
import configparser                 # Py3-style import

class Upper(object):
    def __init__(self, iterable):
        self._iter = iter(iterable)
    def __next__(self):             # Py3-style iterator interface
        return next(self._iter).upper()
    def __iter__(self):
        return self

itr = Upper('hello')
print(next(itr), end=' ')           # Py3-style print function
for letter in itr:
    print(letter, end=' ')
