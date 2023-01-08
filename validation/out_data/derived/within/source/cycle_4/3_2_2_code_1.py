from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mokqh = Factor("mokqh", ["tuoig","fji","rstfj","xdimx","byiuw","bxcy","tnmeod","kpaelj"])
rzgi = Factor("rzgi", ["tuoig","fji","rstfj","xdimx","byiuw","bxcy","tnmeod","kpaelj"])
oilv = Factor("oilv", ["tuoig","fji","rstfj","xdimx","byiuw","bxcy","tnmeod","kpaelj"])
def tgaup(mokqh, rzgi, oilv):
     return mokqh == rzgi
def imvlj(mokqh, rzgi, oilv):
     return rzgi != mokqh and mokqh == oilv
def arpqcs(mokqh, rzgi, oilv):
     return (not mokqh == rzgi) and (mokqh != oilv)
mwmdzj = DerivedLevel("rypi", WithinTrial(tgaup, [mokqh, rzgi, oilv]))
jvv = DerivedLevel("uidd", WithinTrial(imvlj, [mokqh, rzgi, oilv]))
kuua = DerivedLevel("cww", WithinTrial(arpqcs, [mokqh, rzgi, oilv]))
pwnyi = Factor("vgos", [mwmdzj, jvv, kuua])

### EXPERIMENT
design=[mokqh,rzgi,oilv,pwnyi]
crossing=[pwnyi]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END