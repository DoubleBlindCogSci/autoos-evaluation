from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jxvn = Factor("jxvn", ["utg", "jssm"])
ureuaj = Factor("ureuaj", ["endd", "dkqdz"])
qubfnp = Factor("qubfnp", ["lvmdn", "glpr"])

### EXPERIMENT
design=[jxvn,ureuaj,qubfnp]
crossing=[[jxvn,ureuaj],[qubfnp],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2"))
### END