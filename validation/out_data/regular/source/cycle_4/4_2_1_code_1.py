from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
KZWyz6Knu4=Factor('swjKQQwu2 B',["uJY0yz%JgV","%FZyYaF1","a]hoV","alaqU"])
dOfz1K_L5=Factor('qwJugPAWEC*',["ZDOC|u",Level('fGl7',4),"#D&eRI6OHf",'QQ]faO!CY&'])

### EXPERIMENT
design=[KZWyz6Knu4,dOfz1K_L5]
crossing=[KZWyz6Knu4,dOfz1K_L5]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_2_1"))
### END