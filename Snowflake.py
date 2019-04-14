
import os
from turtle import Turtle

import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt


t = Turtle()
t.speed(0)
#a = 180
b = 180
for c in range(5):
 	a = 9*c
 	for i in range(100):
 		t.circle(i,a)
 		t.right(b)
 		t.circle(i,a)
 		t.right(b)
 		t.circle(i,a)
 		t.right(b)
 		t.circle(i,a)
input('Press any key to continue...')
