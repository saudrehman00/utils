#!/usr/bin/python3
import PyPDF2
import os

import PyPDF2 

def merge_pdfs(pdfs,output):

    mergeFile = PyPDF2.PdfFileMerger()

    for pdf in pdfs:

        mergeFile.append(PyPDF2.PdfFileReader(pdf, 'rb'))

    mergeFile.write(output)

# Example usage
pdfs = [file for file in os.listdir() if file.endswith('.pdf')]
pdfs.sort()
output = 'merged.pdf'
merge_pdfs(pdfs, output)
