# PdfMerge

Simple CLI program that merges consecutive ".pdf"-files in a directory.

This software is intended for a very specific use case:

Our current scanner can not easily output a front and back page of a scanned document into a single pdf. It can only do that if you scan your documents one at a time which obviously is very inconvenient for the employee if he has to scan hundreds of documents at a time.

The workaround is that the scanner saves every front and back page into seperate files. Each filename has the current timestamp (down to the millisecond) and an auto incremented counter. This program simply merges these consecutive files in a given directory.

## Example:

If we have a directory with the following files:

```
1.pdf
3.pdf
5.pdf
4.pdf
```

the program will do the following:

```
{uuid.uuid4()}.pdf # file containing 1.pdf and 3.pdf
{uuid.uuid4()}.pdf # file containing 4.pdf and 5.pdf
```

---

The algorithm for that is very sophisticated:

It sorts the files in the selected directory by their name. Thats it.


# Compile

This software is written in python 3.9 and uses [pyinstaller](https://www.pyinstaller.org/) to create native binaries.

```bash
pyinstaller pdfmerge.py --onefile --icon=app.ico
```
