from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ivtq = Factor("ivtq", ["zyb","wxozn","ksq","whzy","wvr","jvgipm","rqoj"])
def is_mos_eyixft(ivtq):
    return ivtq[0] != "wxozn" or ivtq[-1] != "wvr"
def is_mos_fijr(ivtq):
    return not is_mos_eyixft(ivtq)
mos= Factor("mos", [DerivedLevel("eyixft", Transition(is_mos_eyixft, [ivtq])), DerivedLevel("fijr", Transition(is_mos_fijr, [ivtq]))])

design=[ivtq,mos]
crossing=[mos]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END