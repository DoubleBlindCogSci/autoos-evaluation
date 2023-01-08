from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ivtq = Factor("ivtq", ["zyb","wxozn","ksq","whzy","wvr","jvgipm","rqoj"])
def pomzz(ivtq):
    return ivtq[0] != "wxozn" or ivtq[-1] != "wvr"
def ooc(ivtq):
    return not pomzz(ivtq)
fgsq = DerivedLevel("eyixft", Transition(pomzz, [ivtq]))
ohxjnw = DerivedLevel("fijr", Transition(ooc, [ivtq]))
hmqz = Factor("mos", [fgsq, ohxjnw])

### EXPERIMENT
design=[ivtq,hmqz]
crossing=[hmqz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END