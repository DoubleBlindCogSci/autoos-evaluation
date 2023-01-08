from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
agpte = Factor("agpte", ["qcuk","ygfbs","nismk","hnuw","lli","ercbio","ijvwt"])
def cfal(agpte):
     return "nismk" == agpte
def zvahx(agpte):
     return agpte == "lli"
def mzehy(agpte):
     return (not cfal(agpte)) and (agpte != "lli")
hcyg = DerivedLevel("nmbkz", WithinTrial(cfal, [agpte]))
dar = DerivedLevel("vpq", WithinTrial(zvahx, [agpte]))
fbimtb = DerivedLevel("djrqu", WithinTrial(mzehy, [agpte]))
sioa = Factor("hcl", [hcyg, dar, fbimtb])

### EXPERIMENT
design=[agpte,sioa]
crossing=[sioa]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END