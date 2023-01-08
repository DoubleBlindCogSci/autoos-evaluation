from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
OMBWTW3_VTOT  = Factor("OMBWTW3$VTOT ", ["g0sUmwgnfwr", "(eJ"])
rUVsgeRdoGm = Factor("rUVsgeRdoGm", ["$DBdp", "BUc|c5bTF"])
fF_ = Factor("fF_", ["XoWq>jmLWIW", "Ke*fjQc&OdxAD_"])

design=[OMBWTW3_VTOT,rUVsgeRdoGm,fF_]
crossing=[OMBWTW3_VTOT,rUVsgeRdoGm,fF_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_3_0"))

### END
