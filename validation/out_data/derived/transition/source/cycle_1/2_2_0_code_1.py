from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ekav = Factor("ekav", ["gdouen","hnajd","ltruym","vbfv","ltssjd"])
dway = Factor("dway", ["gdouen","hnajd","ltruym","vbfv","ltssjd"])
auik = Factor("auik", ["gdouen","hnajd","ltruym","vbfv","ltssjd"])
def rdlx(ekav, dway, auik):
    return ekav[0] == dway[-1]
def amxvlo(ekav, dway, auik):
    return not (ekav[0] == dway[-1])
puut = DerivedLevel("dzw", Transition(rdlx, [ekav, dway, auik]))
dxtn = DerivedLevel("tkf", Transition(amxvlo, [ekav, dway, auik]))
wlbupb = Factor("bfsf", [puut, dxtn])

### EXPERIMENT
design=[ekav,dway,auik,wlbupb]
crossing=[wlbupb]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END