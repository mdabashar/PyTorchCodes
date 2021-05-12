# -*- coding: utf-8 -*-
"""
Created on Tue May 11 16:03:19 2021

@author: basharm
"""

from .mnist import get_mnist
from .usps import get_usps

__all__ = (get_usps, get_mnist)