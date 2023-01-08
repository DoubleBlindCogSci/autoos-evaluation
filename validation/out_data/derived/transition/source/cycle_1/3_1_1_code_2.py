from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vksj= Factor("vksj", ["zmzan","cfohyl","vafjcn","lojc","quu","rfqmb","qydd"])
def is_etwf_pkxzmq(vksj):
    return vksj[0] == "cfohyl"
def is_etwf_aman(vksj):
    return vksj[0] == "quu"
def is_etwf_zuttft(vksj):
    return not (is_etwf_pkxzmq(vksj) or is_etwf_aman(vksj))
etwf= Factor("etwf", [DerivedLevel("pkxzmq", Transition(is_etwf_pkxzmq, [vksj])), DerivedLevel("aman", Transition(is_etwf_aman, [vksj])), DerivedLevel("zuttft", Transition(is_etwf_zuttft, [vksj]))])

design=[vksj,etwf]
crossing=[etwf]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END
