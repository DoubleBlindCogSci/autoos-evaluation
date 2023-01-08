from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vilah = Factor("vilah", ["gih","smc","rdfv","kto","nvv","shzkx","mpplx","fdd"])
def bom(vilah):
     return "nvv" == vilah
def loyan(vilah):
     return "smc" == vilah
def lpaztj(vilah):
     return (not vilah == "nvv") and (vilah != "smc")
jmvb = Factor("lvbj", [DerivedLevel("gkd", WithinTrial(bom, [vilah])), DerivedLevel("ohs", WithinTrial(loyan, [vilah])),DerivedLevel("vgsu", WithinTrial(lpaztj, [vilah]))])
### EXPERIMENT
design=[vilah,jmvb]
crossing=[jmvb]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END