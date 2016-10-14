#!/usr/bin/env python

import sys
from bs4 import BeautifulSoup

soup = BeautifulSoup(open(sys.argv[1]), 'lxml')
model_location = lambda x: x.name == "Model"
model = soup(model_location)
print(model)
