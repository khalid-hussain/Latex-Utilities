#! python3
import re

mainfile    = open('../quran_chapters.tex')
contentfile = open('content.tex', 'w+')

counter = 0

for surah in mainfile:
  if counter == 114: break
  shortcut = re.search('(newcommand)({)(.*)(})({)', surah)
  # print('\item ', shortcut.group(3), '\n', sep='')
  writeLine = '\item ' + shortcut.group(3) + '\n'
  contentfile.write(writeLine)
  counter = counter + 1