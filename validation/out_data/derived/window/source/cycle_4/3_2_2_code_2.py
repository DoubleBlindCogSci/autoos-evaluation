from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zgwty = Factor("zgwty", ["lrxps","evaz","dor","ncxhe","apsexc","hhcc","cbkgpp"])
muz = Factor("muz", ["lrxps","evaz","dor","ncxhe","apsexc","hhcc","cbkgpp"])
isi = Factor("isi", ["lrxps","evaz","dor","ncxhe","apsexc","hhcc","cbkgpp"])
def is_knehq_lfnwwo(zgwty, muz, isi):
    return zgwty[0] == isi[-3] and zgwty[-3] != muz[0]
def is_knehq_sdddpo(zgwty, muz, isi):
    return isi[-3] != zgwty[0] and zgwty[-3] == muz[0]
def is_knehq_vyjx(zgwty, muz, isi):
    return not (is_knehq_lfnwwo(zgwty, muz, isi) or is_knehq_sdddpo(zgwty, muz, isi))
knehq = Factor("knehq", [DerivedLevel("lfnwwo", Window(is_knehq_lfnwwo, [zgwty, muz, isi], 4, 1)), DerivedLevel("sdddpo", Window(is_knehq_sdddpo, [zgwty, muz, isi], 4, 1)), DerivedLevel("vyjx", Window(is_knehq_vyjx, [zgwty, muz, isi], 4, 1))])

design=[zgwty,muz,isi,knehq]
crossing=[knehq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_2"))

### END