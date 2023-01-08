from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
aus= Factor("aus", ["joiup","gnnuy","alus","ijtzt","bpi","utz"])
def is_nsvlgj_yfwz(aus):
    return aus[0] == "bpi" or aus[-1] == "joiup"
def is_nsvlgj_mhpggi(aus):
    return not is_nsvlgj_yfwz(aus)
nsvlgj= Factor("nsvlgj", [DerivedLevel("yfwz", Transition(is_nsvlgj_yfwz, [aus])), DerivedLevel("mhpggi", Transition(is_nsvlgj_mhpggi, [aus]))])

design=[aus,nsvlgj]
crossing=[nsvlgj]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_3"))

### END
