#!/usr/bin/python

'''This module helps to creale LaTex files with python.
    Also there is an opportunity to create pdf file from tex file.'''

import os

class Document(object):
    def __init__(self, path = '', filename = 'integrals.tex', document_data = [], mode = ['math'], lang = ['english','russian']):
        self.path = path
        self.filename = filename
        self.document_data = document_data
        self.mode = mode
        self.language = lang
    def preamble(self):
        """This methods add initial data to document"""
        
        preamble_data = []
        #making \documentclass
        preamble_data.append('\\documentclass{article}\n')
        #enable math pocket
        if 'math' in self.mode:
            preamble_data.append('\\usepackage{mathtext}\n')
        #coding utf-8
        preamble_data.append('\\usepackage[utf8]{inputenc}\n')
        lang_string = ''
        #connecting languages
        for langs in self.language:
            lang_string += langs+','
        lang_string = lang_string[:-1]
        preamble_data.append('\\usepackage[' + lang_string + ']'+ '{babel}\n')
        #making \begin
        preamble_data.append('\\begin{document}\n')
        dont_fill = False
        if os.path.isfile('integrals.tex')==False:
            open(self.filename, 'a').close()
        print(preamble_data)
        with open(self.filename, 'r+') as f:
            for line in preamble_data:
                    f.write(line)

        pass
    def deltex(self):
        """This method delete old tex file if it is in directory"""
        try:
            import os
        except ImportError:
            print('No module \'os\' found. Please, make pip install os.')
            pass
        os.system('rm ' + self.filename)
        pass
    def append(self, data):
        """This method appends data to document list. To add this data to document you need to use Document().fill()"""
        if type(data) == list:
            for line in data:
                self.document_data.append(line + '\n')
        else:
            self.document_data.append(str(data))
        pass
    def fill(self, end_doc = False):
        """This method add data from document list to tex document"""
        
        with open(self.filename, 'r+') as f:
            data = f.readlines()
            data = data[:-1]
            for x in self.document_data:
                data.append(x)
            print(data)
            for lines in data:
                f.write(lines)
            if end_doc:
                f.write('\\end{document}\n')
    def Section(self, name):
        """This method creates Section by appending \section{name} to document list"""
        self.document_data.append('\\section{' + str(name) +'}\n')
        pass
    def Title(self, name):
        self.document_data.append('\\title{' + str(name) +'}\n')
        pass
    def Author(self, name):
        self.document_data.append('\\author{' + str(name) +'}\n')
        pass
    def Date(self):
        self.document_data.append('\\data{\\today}\n')


    def latex2pdf(self):
        """This method creates pdf file from latex file"""
        try: 
            import os
        except ImportError:
            print('No module \'os\' found. Please, make pip install os.')
            pass
        os.system('pdflatex ' + self.filename)
        pass


def StartTex(filename = 'integrals.tex', path = '', mode = ['math'], lang = ['english', 'russian'], date = True, title = None, author = None):
    document = Document(path, filename, [], mode, lang)
    document.preamble()
    return document
def makeTex():
        #remove old tex file
        try:
            import os
        except ImportError:
            print('No module \'os\' found. Please, make pip install os.')
        if os.path.isfile('integrals.tex'):
                os.system('rm ' + 'integrals.tex')
        #reading all the integrals from txt file
        integrals = []
        with open('integrals.txt', 'r+') as f:
            for line in f:
                integrals.append(line+'\n')
        integrals = list(set(integrals))   
        #creating new tex file
        document = StartTex()
        with open(document.filename, 'a') as f:
            for line in integrals:
                f.write(line)
            f.write('\\end{document}\n')   
        pass

def makePdf():
    os.system('pdflatex ' + 'integrals.tex')


