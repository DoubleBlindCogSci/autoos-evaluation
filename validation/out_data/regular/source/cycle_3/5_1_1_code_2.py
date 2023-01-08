from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

Jkhzh_OB_OEnN = Factor("Jkhzh]OB)OEnN",  ["wa@Xvr", "iCW", "ibxB JhE!qT<", "ttaiJIhhY|4aer", "nE<Zp"])


design=[Jkhzh_OB_OEnN]
crossing=[Jkhzh_OB_OEnN]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_1_1"))

### END
