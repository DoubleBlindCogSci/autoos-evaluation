from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rnmqww = Factor("rnmqww", ["jas","drhz","jglx","deji","jqshvt","zktr","mhm"])
vhln = Factor("vhln", ["adqrok","yha","bij","jeilkw","iamwb"])
def is_qgpn_xiarzr(rnmqww, vhln):
    return rnmqww[0] == "jas" and vhln[-1] != "jeilkw"
def is_qgpn_mmf(rnmqww, vhln):
    return not is_qgpn_xiarzr(rnmqww, vhln)
qgpn = Factor("qgpn", [DerivedLevel("xiarzr", Transition(is_qgpn_xiarzr, [rnmqww, vhln])), DerivedLevel("mmf", Transition(is_qgpn_mmf, [rnmqww, vhln]))])

design=[rnmqww,vhln,qgpn]
crossing=[qgpn]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END