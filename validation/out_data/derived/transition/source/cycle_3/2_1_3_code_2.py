from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cpaotp = Factor("cpaotp", ["hsipy","lzfk","ygh","johine","qxb","sgyyen"])
def is_qweqys_hbk(cpaotp):
    return cpaotp[0] == "lzfk" or cpaotp[-1] != "johine"
def is_qweqys_bswz(cpaotp):
    return not is_qweqys_hbk(cpaotp)
qweqys= Factor("qweqys", [DerivedLevel("hbk", Transition(is_qweqys_hbk, [cpaotp])), DerivedLevel("bswz", Transition(is_qweqys_bswz, [cpaotp]))])

design=[cpaotp,qweqys]
crossing=[qweqys]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_3"))

### END
