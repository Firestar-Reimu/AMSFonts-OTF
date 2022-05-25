import os
import fontforge as ff

os.chdir('amsfonts')
files = os.listdir("./")

for font in files:
    if font.endswith('.pfb'):
        f = ff.open(font)
        fname = f.fontname + '.otf'
        f.familyname = f.fontname
        f.generate(fname, flags=("TeX-table",))
