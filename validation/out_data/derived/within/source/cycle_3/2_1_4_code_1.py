from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
aeckdg = Factor("aeckdg", ["rhdi","uslq","jauqo","tiydi","gpj"])
def aod(aeckdg):
    return aeckdg != "jauqo"
def eccgo(aeckdg):
    return aeckdg == "jauqo"
yarz = Factor("tpax", [DerivedLevel("auu", WithinTrial(aod, [aeckdg])), DerivedLevel("rurk", WithinTrial(eccgo, [aeckdg]))])
### EXPERIMENT
design=[aeckdg,yarz]
crossing=[yarz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END