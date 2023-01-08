from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
sgy = Factor("sgy", ["duftv","uao","elyd","nuvgkv","jdfnj","otnfn","bvjut","xdk"])
def vjyezz(sgy):
     return sgy[-2] == "elyd" and not sgy[0] == "elyd"
def poa(sgy):
     return not "elyd" == sgy[-2] and  "xdk" == sgy[0]
def mmw(sgy):
     return (sgy[-2] != "elyd") and (not sgy[0] == "xdk")
mhino = Factor("lav", [DerivedLevel("kllu", Window(vjyezz, [sgy],3,1)), DerivedLevel("ebjemp", Window(poa, [sgy],3,1)),DerivedLevel("dzrxzk", Window(mmw, [sgy],3,1))])
### EXPERIMENT
design=[sgy,mhino]
crossing=[mhino]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END