#!/usr/bin/env python3
"""
Module for the Nganki project's classic portfolio analysis functions, pioneered
by Harry Markowitz.
REMEMBER TO REMOVE UNWANTED HASH MARKS AT THE END
"""

import pandas as pd

# Temporary data input to get some work done
from data_import import six_eq_yahoo

rets = six_eq_yahoo.pct_change().dropna(how='all')

if __name__ == '__main__':
    print(six_eq_yahoo)
    print(rets)
    pass
