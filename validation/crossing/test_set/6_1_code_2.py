from sweetpea import *
import os
_dir=os.path.dirname(__file__)
ctp = Factor("ctp", ["sizc", "gjak"])
owqya = Factor("owqya", ["bdv", "oysyep"])
epwhv = Factor("epwhv", ["ify", "sytoh"])
fbaze = Factor("fbaze", ["qnwg", "zvmwas"])
qrrk = Factor("qrrk", ["eaa", "dpo"])
zentca = Factor("zentca", ["rtfgcn", "oskm"])
constraints = []
crossing = [ctp, owqya, epwhv, fbaze, qrrk, zentca]


design=[ctp,owqya,epwhv,fbaze,qrrk,zentca]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_1"))

### END