from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jvsf = Factor("jvsf", ["kivh","kqagto","zqksk","xae","twyc","epq","rtxaw"])
def is_nfx_tngyia(jvsf):
    return jvsf[0] == "xae" and jvsf[-1] != "rtxaw"
def is_nfx_gemffy(jvsf):
    return jvsf[0] != "xae" and jvsf[-1] == "rtxaw"
def is_nfx_sspc(jvsf):
    return not (is_nfx_tngyia(jvsf) or is_nfx_gemffy(jvsf))
nfx = Factor("nfx", [DerivedLevel("tngyia", Transition(is_nfx_tngyia, [jvsf])), DerivedLevel("gemffy", Transition(is_nfx_gemffy, [jvsf])), DerivedLevel("sspc", Transition(is_nfx_sspc, [jvsf]))])

design=[jvsf,nfx]
crossing=[nfx]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_4"))

### END