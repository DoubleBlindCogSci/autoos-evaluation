from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mokqh = Factor("mokqh", ["tuoig","fji","rstfj","xdimx","byiuw","bxcy","tnmeod","kpaelj"])
rzgi = Factor("rzgi", ["tuoig","fji","rstfj","xdimx","byiuw","bxcy","tnmeod","kpaelj"])
oilv = Factor("oilv", ["tuoig","fji","rstfj","xdimx","byiuw","bxcy","tnmeod","kpaelj"])
def is_vgos_rypi(mokqh, rzgi, oilv):
    return mokqh == rzgi
def is_vgos_uidd(mokqh, rzgi, oilv):
    return mokqh != rzgi and mokqh == oilv
def is_vgos_cww(mokqh, rzgi, oilv):
    return mokqh != rzgi and mokqh != oilv
vgos = Factor("vgos", [DerivedLevel("rypi", WithinTrial(is_vgos_rypi, [mokqh, rzgi, oilv])), DerivedLevel("uidd", WithinTrial(is_vgos_uidd, [mokqh, rzgi, oilv])), DerivedLevel("cww", WithinTrial(is_vgos_cww, [mokqh, rzgi, oilv]))])

design=[mokqh,rzgi,oilv,vgos]
crossing=[vgos]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_2"))

### END