from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
agpte = Factor("agpte", ["qcuk","ygfbs","nismk","hnuw","lli","ercbio","ijvwt"])
def is_hcl_nmbkz(agpte):
    return agpte == "nismk"
def is_hcl_vpq(agpte):
    return agpte == "lli"
def is_hcl_djrqu(agpte):
    return agpte != "nismk" and agpte != "lli"
hcl = Factor("hcl", [DerivedLevel("nmbkz", WithinTrial(is_hcl_nmbkz, [agpte])), DerivedLevel("vpq", WithinTrial(is_hcl_vpq, [agpte])), DerivedLevel("djrqu", WithinTrial(is_hcl_djrqu, [agpte]))])

design=[agpte,hcl]
crossing=[hcl]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_2"))

### END