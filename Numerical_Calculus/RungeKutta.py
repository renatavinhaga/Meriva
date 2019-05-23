from __future__ import division
from sympy import * 
from sympy.abc import x,y,t
from sympy.parsing.sympy_parser import *
from sympy.interactive import printing
import random
import sys
import os

#Metodo de Runge-Kutta para encontrar a solução aproximada de uma EDO de primeira ordem com PVI
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
s = a #s=t


for i in range(N):
	K1 = h * expr2.subs([(y, w), (t, s)]) 
	K2 = h * expr2.subs([(y, w + (K1/2)), (t, s + (h/2))]) 
	K3 = h * expr2.subs([(y, w + (K2/2)), (t, s + (h/2))]) 
	K4 = h * expr2.subs([(y, w + K3), (t, s + h)]) 

	w = w + (K1 + 2 * K2 + 2 * K3 + K4)/6
	s = a + float((i + 1) * h)
	print(s, w)#gerando pontos aproximados do grafico original