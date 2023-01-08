from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dikfjs = Factor("dikfjs", ["nyx","bma","petkz","gyap","fgw"])
def is_ygkt_bgkms(dikfjs):
    return dikfjs[-1] == "nyx" or dikfjs[0] != "petkz"
def is_ygkt_dzzqz(dikfjs):
    return not is_ygkt_bgkms(dikfjs)
ygkt = Factor("ygkt", [DerivedLevel("bgkms", Transition(is_ygkt_bgkms, [dikfjs])), DerivedLevel("dzzqz", Transition(is_ygkt_dzzqz, [dikfjs]))])

design=[dikfjs,ygkt]
crossing=[ygkt]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END