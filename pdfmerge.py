from PyPDF2 import PdfFileMerger
from tkinter import filedialog
import tkinter as tk
import uuid
import os

root = tk.Tk()
root.withdraw()


def pdf_concat():
    pdfs = []

    filePath = filedialog.askdirectory()
    destination = filePath + os.path.sep + 'merged'

    # load all ".pdf" files from the selected directory
    # and put them into a list
    for file in os.listdir(filePath):
        if file.endswith(".pdf"):
            pdfs.append(os.path.join(filePath, file))

    pdfs.sort()
    pdfLen = len(pdfs)

    print(f'Found {pdfLen} ".pdf" files in {filePath}')

    # return if directory was empty
    if (pdfLen < 1):
        return

    # create the destination folder
    if (os.path.isdir(destination) == False):
        os.mkdir(destination)
    else:
        # else clear the folder
        filelist = [f for f in os.listdir(destination) if f.endswith(".pdf")]
        for f in filelist:
            os.remove(os.path.join(destination, f))

    # how many pdfs will be generated
    length = int(len(pdfs) / 2) + 1
    x = 1

    # chunk the list into chunks of two and merge them
    for i in chunks(pdfs, 2):
        newFilename = f'{destination}{os.path.sep}{uuid.uuid4()}.pdf'

        merger = PdfFileMerger()

        for pdf in i:
            merger.append(pdf)

        merger.write(newFilename)
        merger.close()

        # give the user progress feedback
        progress = int((x / length) * 100)
        print(f'{newFilename} ({x} of {length}) {progress}%')

        x += 1

    # prevent automatic closing of the process
    input()


### php: array_chunk
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


if __name__ == '__main__':
    pdf_concat()
