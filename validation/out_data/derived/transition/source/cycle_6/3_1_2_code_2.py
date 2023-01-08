from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xatn = Factor("xatn", ["zzmnb","zqjdqg","agwq","opkof","lpx","fwxt","rhk"])
def is_lpnq_ftgjj(xatn):
    return xatn[0] == "rhk" and xatn[-1] != "zqjdqg"
def is_lpnq_byul(xatn):
    return xatn[0] != "rhk" and xatn[-1] == "zqjdqg"
def is_lpnq_wuzutq(xatn):
    return not (is_lpnq_ftgjj(xatn) or is_lpnq_byul(xatn))
lpnq = Factor("lpnq", [DerivedLevel("ftgjj", Transition(is_lpnq_ftgjj, [xatn])), DerivedLevel("byul", Transition(is_lpnq_byul, [xatn])), DerivedLevel("wuzutq", Transition(is_lpnq_wuzutq, [xatn]))])

design=[xatn,lpnq]
crossing=[lpnq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_2"))

### END