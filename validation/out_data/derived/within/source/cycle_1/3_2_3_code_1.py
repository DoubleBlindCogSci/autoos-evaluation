from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rtnhuu = Factor("rtnhuu", ["qaplpa","xrxe","iiz","mmack","nif","rnwtsk"])
tabde = Factor("tabde", ["ufjmg","elr","rwngi","qsttxo","iuxn","btxr","oue","lbx"])
def lrvbo(rtnhuu, tabde):
     return "xrxe" == rtnhuu
def hnkj(rtnhuu, tabde):
     return rtnhuu != "xrxe" and  tabde == "oue"
def rbcp(rtnhuu, tabde):
     return (not rtnhuu == "xrxe") and (not tabde == "oue")
jeyb = DerivedLevel("totap", WithinTrial(lrvbo, [rtnhuu, tabde]))
fuc = DerivedLevel("pebd", WithinTrial(hnkj, [rtnhuu, tabde]))
bsyaea = DerivedLevel("jaut", WithinTrial(rbcp, [rtnhuu, tabde]))
ednt = Factor("lpqj", [jeyb, fuc, bsyaea])

### EXPERIMENT
design=[rtnhuu,tabde,ednt]
crossing=[ednt]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END