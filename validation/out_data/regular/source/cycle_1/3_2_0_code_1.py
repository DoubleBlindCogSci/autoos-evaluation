from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
yqH1QEXLF=['z&F T',Level("Lkn",5),"wAvF("]
EQODmlAH=Factor("gVluEr",yqH1QEXLF)
sIvMzokurUU=Factor('Jo$YFb1gcut;0e',[Level("Wu}Fg:{V",10),"xbzPA",Level("b3EjP",2)])

### EXPERIMENT
design=[EQODmlAH,sIvMzokurUU]
crossing=[EQODmlAH,sIvMzokurUU]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/3_2_0"))
### END