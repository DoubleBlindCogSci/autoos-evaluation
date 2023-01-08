from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zgwty = Factor("zgwty", ["lrxps","evaz","dor","ncxhe","apsexc","hhcc","cbkgpp"])
muz = Factor("muz", ["lrxps","evaz","dor","ncxhe","apsexc","hhcc","cbkgpp"])
isi = Factor("isi", ["lrxps","evaz","dor","ncxhe","apsexc","hhcc","cbkgpp"])
def bwz(zgwty, isi, muz):
     return zgwty[0] == isi[-3] and zgwty[-3] != muz[0]
def xhuz(zgwty, isi, muz):
     return isi[-3] != zgwty[0] and zgwty[-3] == muz[0]
def aul(zgwty, isi, muz):
     return (not zgwty[0] == isi[-3]) and (not zgwty[-3] == muz[0])
hio = Factor("knehq", [DerivedLevel("lfnwwo", Window(bwz, [zgwty, muz, isi],4,1)), DerivedLevel("sdddpo", Window(xhuz, [zgwty, muz, isi],4,1)),DerivedLevel("vyjx", Window(aul, [zgwty, muz, isi],4,1))])
### EXPERIMENT
design=[zgwty,muz,isi,hio]
crossing=[hio]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END