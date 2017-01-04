#! python3
import linecache

f_nusoos = 'symbol_nass_list.txt'
f_keys = 'symbol_key_list.txt'
contentfile = open('content.tex', 'w+', encoding="utf-8")

theLine = " "

for x in range(96):
    contentfile.write('{} & {{\QPCSymbols\XeTeXglyph {}}}  & \\textarabic{{{}}} & \\texttt{{{}}} & \\verb$\XeTeXglyph {}$  \\\\'.format(x + 1, x + 2, linecache.getline(f_nusoos, x + 1).rstrip('\n'), linecache.getline(f_keys, x + 1).rstrip('\n'), x + 2))
    contentfile.write('\n')
    contentfile.write('\hline')
    contentfile.write('\n')
