from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nit = Factor("nit", ["kxzzp","ypycp","laywua","sdotn","kvin","bfkgv"])
zaqgel = Factor("zaqgel", ["zuvwb","ebsp","xsw","fhkoez","tug","ltnvdy","toytrl"])
def is_niy_tybllc(nit, zaqgel):
    return nit == "ypycp" or zaqgel == "zuvwb"
def is_niy_asjj(nit, zaqgel):
    return not is_niy_tybllc(nit, zaqgel)
niy = Factor("niy", [DerivedLevel("tybllc", WithinTrial(is_niy_tybllc, [nit, zaqgel])), DerivedLevel("asjj", WithinTrial(is_niy_asjj, [nit, zaqgel]))])

design=[nit,zaqgel,niy]
crossing=[niy]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END