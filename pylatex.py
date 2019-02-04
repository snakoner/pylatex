
#!/usr/bin/python

'''This module helps to creale LaTex files with python.
    Also there is an opportunity to create pdf file from tex file.'''

class Document:
    def __init__(self, path = '', filename = 'document.tex', document_data = []):
        self.path = path
        self.filename = filename
        self.document_data = document_data
    def delOld(self):
        os.system('rm ' + filename)
        pass
    def document_class(self):
        with open(self.filename, 'a') as f:
            f.write('\documentclass{article}\n')
        pass
    def begin_doc(self):
        with open(self.filename, 'a') as f:
            f.write('\\begin{document}\n')
        pass
    def end_doc(self):
        with open(self.filename, 'a') as f:
            f.write('\end{document}\n')
        pass
    def append(self, data):
        self.document_data.append(data + '\n')
        pass
    def latex2pdf(self):
        try: 
            import os
        except ImportError:
            print('No module \'os\' found. Please, make pip install os.')
            pass
        os.system('pdflatex ' + self.filename)
        pass
    def fill(self):
        with open(self.filename, 'a') as f:
            for lines in self.document_data:
                f.write(lines)
        pass




    