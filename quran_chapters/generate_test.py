#! python3
import re

mainfile = open('quran_chapters.tex')

counter = 1

for surah in mainfile:
  if counter == 114: break

  counter = counter + 1