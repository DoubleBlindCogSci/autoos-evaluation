from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
gudpr = Factor("gudpr", ["tpxk","mzxlux","eneif","vxp","enjsv"])
iqmtg = Factor("iqmtg", ["ygi","hwpanh","bfkbl","smrsqk","qdfvn","ldgwb","xqni"])
def jqfs(gudpr, iqmtg):
    return gudpr[-1] != "mzxlux" and iqmtg[0] != "qdfvn"
def frmwzg(gudpr,iqmtg):
    return not jqfs(gudpr, iqmtg)
cggu = DerivedLevel("bizxs", Window(jqfs, [gudpr, iqmtg],2,1))
fise = DerivedLevel("jyvte", Window(frmwzg, [gudpr, iqmtg],2,1))
jqqg = Factor("htfb", [cggu, fise])

### EXPERIMENT
design=[gudpr,iqmtg,jqqg]
crossing=[jqqg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END