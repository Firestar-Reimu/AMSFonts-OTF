import os
import glob
import fontforge as ff

os.chdir('./amsfonts-otf')
files = glob.glob('../amsfonts/fonts/type1/public/amsfonts/*/*.pfb')

for font in files:
    f = ff.open(font)
    fname = f.fontname + '.otf'
    f.familyname = f.fontname
    f.generate(fname, flags=("TeX-table",))
