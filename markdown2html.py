#!/usr/bin/python3
"""Markdown converter script"""
import os
import sys

headings = {
    '#': 'h1',
    '##': 'h2',
    '###': 'h3',
    '####': 'h4',
    '#####': 'h5',
    '######': 'h6'
}


def markDownConverter(line):
    """Converter"""
    markHeading = line.split()[0]
    htmlHeading = headings[markHeading]
    text = line.replace(markHeading + ' ', '')
    return '<{}>{}</{}>\n'.format(htmlHeading, text, htmlHeading)


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

    with open(markdownFile, 'r+') as f:
        lines = f.readlines()
        convLines = ''
        for line in lines:
            convLines += markDownConverter(line[: -1])

    with open(outputFile, 'w+') as f:
        f.write(convLines)
