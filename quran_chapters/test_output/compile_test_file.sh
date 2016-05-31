# Generate item list of all Suwar
py generate_enumerate_list.py

# Combine header, footer and content file
cat header.tex\
    content.tex\
    footer.tex > test_file.tex

pdflatex test_file.tex

rm test_file.aux\
   content.tex\
   test_file.tex\
   test_file.log