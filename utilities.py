# some useful functions

import os
import nltk
import re
from xml.etree import ElementTree

def load_entire_directory(directory_path):
    files = os.listdir(directory_path)
    corpus = {}
    for f in files:
        if f[0] != ".":
            file = open(directory_path + '/' + f)
            corpus[f] = file.read()
            file.close()
    return corpus

def read_and_tokenize(filename):
    myfile = open('corpora/' + filename)
    raw_string = myfile.read()
    word_list = nltk.word_tokenize(raw_string)
    return word_list


class ListTable(list):
    def _repr_html_(self):
        html = ["<table style= 'border: 1px solid black;''>"]
        for row in self:
            html.append("<tr>")
            for col in row:
                html.append("<td align='left' style='border: .5px solid gray;''>{0}</td>".format(col))
            
            html.append("</tr>")
        html.append("</table>")
        return ''.join(html)
