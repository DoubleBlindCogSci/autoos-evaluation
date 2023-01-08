from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rtnhuu= Factor("rtnhuu", ["qaplpa","xrxe","iiz","mmack","nif","rnwtsk"])
tabde= Factor("tabde", ["ufjmg","elr","rwngi","qsttxo","iuxn","btxr","oue","lbx"])
def is_lpqj_totap(rtnhuu):
    return rtnhuu == "xrxe"
def is_lpqj_pebd(rtnhuu, tabde):
    return rtnhuu != "xrxe" and tabde == "oue"
def is_lpqj_jaut(rtnhuu, tabde):
    return not (is_lpqj_totap(rtnhuu) or is_lpqj_pebd(rtnhuu, tabde))
lpqj= Factor("lpqj", [DerivedLevel("totap", WithinTrial(is_lpqj_totap, [rtnhuu])), DerivedLevel("pebd", WithinTrial(is_lpqj_pebd, [rtnhuu, tabde])), DerivedLevel("jaut", WithinTrial(is_lpqj_jaut, [rtnhuu, tabde]))])

design=[rtnhuu,tabde,lpqj]
crossing=[lpqj]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_3"))

### END
