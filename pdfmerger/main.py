#!/usr/bin/python3
import PyPDF2
import os

def merge_pdfs(pdfs, output):
    # Create a PDF object to store the merged PDF
    merger = PyPDF2.PdfFileMerger()
    
    # Loop through each PDF in the list
    for pdf in pdfs:
        # Open each PDF and add it to the merger
        with open(pdf, 'rb') as file:
            merger.append(file)
    
    # Write the merged PDF to the output file
    with open(output, 'wb') as file:
        merger.write(file)

# Example usage
pdfs = [file for file in os.listdir() if file.endswith('.pdf')]
pdfs.sort()
output = 'merged.pdf'
merge_pdfs(pdfs, output)
