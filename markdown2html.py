#!/usr/bin/python3
"""Markdown converter script"""
import os
import sys

if __name__ == '__main__':
    filesName = sys.argv[1:]

    if len(filesName) < 2:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        exit(1)
    else:
        markdownFile, outputFile = filesName[0], filesName[1]
        if not os.path.exists(markdownFile):
            sys.stderr.write('Missing {}\n'.format(markdownFile))
            exit(1)
        else:
            exit(0)
