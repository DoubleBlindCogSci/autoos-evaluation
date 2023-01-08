from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
O7wieF=Factor('jUf;GSNjsdU<E?',['wsnZnqLWlD','a$tmZO',"EL(zDtnWikAAw","TMm5ZB",'CzhjVwxjc1?cbV',Level('rPfCErTNe',3)])
ljl8Kseo0=[']^F',"8bdJ",'w_e};^C@NPhWM',Level('TnOQoUDtN',5),']QCdmJ',';gMlwG']
tPvnBVZuD0U=Factor("BRpwg n",ljl8Kseo0)

### EXPERIMENT
design=[O7wieF,tPvnBVZuD0U]
crossing=[O7wieF,tPvnBVZuD0U]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/6_2_0"))
### END