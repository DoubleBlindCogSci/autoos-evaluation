from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ctp = Factor("ctp", ["sizc", "gjak"])
owqya = Factor("owqya", ["bdv", "oysyep"])
epwhv = Factor("epwhv", ["ify", "sytoh"])
fbaze = Factor("fbaze", ["qnwg", "zvmwas"])
qrrk = Factor("qrrk", ["eaa", "dpo"])
zentca = Factor("zentca", ["rtfgcn", "oskm"])

### EXPERIMENT
design=[ctp,owqya,epwhv,fbaze,qrrk,zentca]
crossing=[[ctp,owqya,epwhv,fbaze,qrrk,zentca]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1"))
### END