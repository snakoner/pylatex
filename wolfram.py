import wolframalpha
import requests
import random
import re
from pylatex import Document, StartTex, makeTex, makePdf

appId = 'ER4JAQ-UYALREV432'

def get_picture(result):
	for res in result:
		res = res['img']
		res = res['@src']
		f = open(str(random.randint(0,100))+'.jpg','wb')
		f.write(requests.get(res).content)
		f.close()
	pass

def prepareForTex(result):
	result = re.split('\'plaintext\':', str(result))[-1]
	result = result[2:-2]
	print(result)
	lines = re.split('=', result)
	#result = result[:-2]
	#working with integral
	result = re.split(' ', lines[0])
	print(result[0])
	a_lim, b_lim = 0, 0
	b_lim = re.split('\^', result[0])[-1]
	a_lim = re.split('\^',re.split('_', result[0])[-1])[0]
	final_string = '$$\int_{' + str(a_lim) + '}^{' + str(b_lim) + '} ' + result[1] + ' ' + result[2]
	for number, line in enumerate(lines):
		if number >= 1:
			final_string += ' =' + line
	final_string += '$$'
	final_string = re.sub('≈', '=', final_string)
	print(final_string)
	return final_string

def addIntToFile(result):
	with open('integrals.txt', 'a') as f:
		f.write(result + '\n')
	pass

def getIntTex(result):
	return result['plaintext']
def parseData(res, intType):
	answer = []	
	for pod in res.pods:
		for sub in pod.subpods:
			answer.append(sub)
	return answer[0] if intType else answer[2]
def getDataFromWolframAlpha():
	client = wolframalpha.Client()
	res = client.query('int logx from 0 to 1')
	return res

def makeRequest(request, appId):
	client = setConnection(appId)
	result = client.query(request)
	return result


def setConnection(appId):
	client = wolframalpha.Client(appId)
	return client
def selectIntType(request):
	return True if 'from' in request else False 

	








	