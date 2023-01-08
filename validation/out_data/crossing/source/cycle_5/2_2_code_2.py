from sweetpea import *
import os
_dir=os.path.dirname(__file__)
jxvn = Factor("jxvn", ["utg", "jssm"])
ureuaj = Factor("ureuaj", ["endd", "dkqdz"])
qubfnp = Factor("qubfnp", ["lvmdn", "glpr"])
constraints = []
crossing = [[jxvn, ureuaj], [qubfnp]]


design=[jxvn,ureuaj,qubfnp]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2"))

### END