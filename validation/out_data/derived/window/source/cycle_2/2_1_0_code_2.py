from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jux= Factor("jux", ["jvpa","oxp","vgfogi","swxoq","xwmy","rceiym","szd"])
def is_koux_nct(jux):
    return jux[-1] != "oxp" or jux[0] != "jvpa"
def is_koux_xfgem(jux):
    return not is_koux_nct(jux)
koux= Factor("koux", [DerivedLevel("nct", Window(is_koux_nct, [jux], 4, 1)), DerivedLevel("xfgem", Window(is_koux_xfgem, [jux], 4, 1))])

design=[jux, koux]
crossing=[koux]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END
