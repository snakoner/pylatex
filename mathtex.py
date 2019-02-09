import math

def sum(equation, xfrom=0, xto = 'infty'):
	return '$\sum_{n='+str(xfrom)+'}^{\\' + str(xto) + '} ' + str(equation) + '$' \
		if xto == 'infty' else  '$\sum_{n='+str(xfrom)+'}^{' + str(xto) + '} ' + str(equation) + '$'
def equat(equation):
	return '$' + str(equation) + '$'
def integral(equation, a = 0, b = 'infty'):
	return '$$\int_{'+str(a)+'}^{\\'+str(b) + '} ' +str(equation)+'dx$$' \
		if b == 'infty' else '$$\int_{'+str(a)+'}^{'+str(b)+'} '+str(equation)+'dx$$'
def frac(a, b):
	return '$\\frac{' + str(a) +'}{' + str(b) + '}$'
def xfrac(equation):
	return '$\\frac{' + equation.split('/')[0] +'}{' + equation.split('/')[1] + '}$'
def binomial_coefficient(n, k):
	return '$C_'+str(n)+'^'+str(k)+'$'
