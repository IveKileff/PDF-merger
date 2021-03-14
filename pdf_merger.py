'''merges two pdfs called first.pdf and second.pdf, taking two pages
   from the first file and one from the second (then adding a blank
   page) and saves the merged file in \Documents\Merged File\ ready
   for printing double sided'''

import os

from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

# Read in first file
first_file = (Path.home()/'Documents'/'first.pdf')
first_pdf = PdfFileReader(str(first_file),strict=False)

# Read in second file
second_file = (Path.home()/'Documents'/'second.pdf')
second_pdf = PdfFileReader(str(second_file),strict=False)

# Ask user for the name to save the output file as
filename = input('What should I call the output file?: ')

# Initialise page size and counters
_, _, w, h = second_pdf.getPage(0)['/MediaBox']
no_of_pgs = first_pdf.getNumPages()
count = 0
v_count = 0

writer = PdfFileWriter()

for page in range(0,no_of_pgs):
    # add two pages from the first file to the output file
    pg_to_add = first_pdf.getPage(page)
    writer.addPage(pg_to_add)
    count = count + 1
    # if count is an even number - add one page from the second file 
    # interspersed with a blank page
    if count % 2 == 0:
        for v in range(0,1):
            v_pg = v_count + v
            pg_to_add = second_pdf.getPage(v_pg)
            writer.addPage(pg_to_add)
            writer.addBlankPage(w, h)
        v_count = v_count + 1
        
# Set working directory to where I want to save the output file
save_location = Path.home()/'Documents'/'Merged File'
os.chdir(save_location)

# Save PDF to file, wb for write binary
pdf_output = open(filename+'.pdf', 'wb')

# Outputting the PDF
writer.write(pdf_output)

# Closing the PDF writer
pdf_output.close()
print('Your file has been merged and saved')
