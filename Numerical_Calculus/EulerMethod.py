#Metodo de Euler para encontrar a solução aproximada de uma EDO de primeira ordem com PVI
from __future__ import division
from sympy import * 
from sympy.abc import x,y,t
from sympy.parsing.sympy_parser import *
from sympy.interactive import printing
import random
import sys
import os


print("insert the interval [a,b]")
a = float(input())
b = float(input())
print("insert the integer N")
N = int(input())
print("insert the first condition y(t) = w")
w = float(input())
expr = input("insert the function y': \n")
expr2 = sympify(expr)

h = (b-a)/N
s = a

for i in range(N):
	w = w + h * expr2.subs([(y, w), (t, s)]) #w = w + f(s,w) -> calcula Wi
	s = a + float((i+1) * h)#s = a + ih -> calcula Si
	print(s, w)#gerando pontos aproximados do grafico original
