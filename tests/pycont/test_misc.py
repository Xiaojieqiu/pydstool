#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest

from PyDSTool.errors import (
    PyDSTool_ValueError,
)
from PyDSTool.PyCont.misc import (
    monotone,
)


def test_monotone_raises_exception():
    for n in [-1, 0, 1]:
        with pytest.raises(PyDSTool_ValueError):
            monotone([], num=n)
