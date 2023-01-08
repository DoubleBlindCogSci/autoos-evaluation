from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ktmnf = Factor("ktmnf", ["tie", "zzxf"])
nncpy = Factor("nncpy", ["vdrklk", "enhbkm"])
cgflq = Factor("cgflq", ["cybcua", "xqlfqu"])
coxoc = Factor("coxoc", ["vvq", "oid"])
icpxef = Factor("icpxef", ["evovf", "vlh"])
knlto = Factor("knlto", ["caj", "oxgxq"])
cmsfp = Factor("cmsfp", ["qslgt", "lvj"])

### EXPERIMENT
design=[ktmnf,nncpy,cgflq,coxoc,icpxef,knlto,cmsfp]
crossing=[[ktmnf,nncpy,cgflq,coxoc,icpxef,knlto,cmsfp]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_4"))
### END