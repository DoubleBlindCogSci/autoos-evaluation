from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
nit = Factor("nit", ["kxzzp","ypycp","laywua","sdotn","kvin","bfkgv"])
zaqgel = Factor("zaqgel", ["zuvwb","ebsp","xsw","fhkoez","tug","ltnvdy","toytrl"])
def efpic(nit, zaqgel):
    return nit == "ypycp" or zaqgel == "zuvwb"
def caygx(nit,zaqgel):
    return not efpic(nit, zaqgel)
fimvht = Factor("niy", [DerivedLevel("tybllc", WithinTrial(efpic, [nit, zaqgel])), DerivedLevel("asjj", WithinTrial(caygx, [nit, zaqgel]))])
### EXPERIMENT
design=[nit,zaqgel,fimvht]
crossing=[fimvht]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END