#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: app.py
Author: Giacomo Fagioli
Email: gf [AT] gfcyb [DOT] org
Date: 2024-09-11
Version: 0.1
License: GPL3
Repo: https://github.com/GFcyborg/test0
Credits: Alan Turing, Claude Shannon, Linus Torvalds, Guido van Rossum
Description: This header is called <obj>.__doc__
"""
__author__ = "Giacomo Fagioli"
__status__ = "Production"

import os
import datetime
import sys

print(f"Env: {sys.version} \n {sys.path}")
now = datetime.datetime.now()
print(f"Now it's: { now.strftime("%Y-%m-%d %H:%M:%S") }.")
