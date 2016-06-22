#!/usr/bin/env python
#coding: utf8 

# Script Name	: extract_img.py
# Author	: Douglas Prado
# Created	: 22 June 2016 
# Last Modified	: 
# Version	: 1.0

# Modifications	: 

# Description	: Extract imagens from file pdf

import sys
import PyPDF2
import os.path
import io
from wand.image import Image

def ExtractImg(pdf_reader, n, out_path):
        writer = PyPDF2.PdfFileWriter()
        page = pdf_reader.getPage(n)
        writer.addPage(page)

        bytes = io.BytesIO()
        writer.write(bytes)
        bytes.seek(0)
	
        wand_img = Image(file = bytes)
	wand_img.format = 'jpg'
	jpg_bin = wand_img.make_blob()

	with open(out_path, 'wb') as temp_file:
		temp_file.write(jpg_bin)


print '    Extracting images:',
pdf_reader = PyPDF2.PdfFileReader(file('document.pdf', 'rb'))

print 'total', pdf_reader.getNumPages(), 'pages'

path_img = 'imgs'

if not os.path.exists(path_img):
    os.makedirs(path_img)

img_paths = []
for i in xrange(pdf_reader.getNumPages()):
    img_path = path_img+'/'+str(i+1)+'.jpg'
    img_paths.append(img_path)
    if not os.path.isfile(img_path):
        print '        '+str(i+1)+' :', img_path,
        sys.stdout.flush()
        ExtractImg(pdf_reader = pdf_reader, n = i, out_path = img_path)
        print '... done!'
