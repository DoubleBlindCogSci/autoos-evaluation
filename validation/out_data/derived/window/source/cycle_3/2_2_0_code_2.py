from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dnpj = Factor("dnpj", ["mrgi","kcr","nzdax","mpyl","selg"])
xgs = Factor("xgs", ["vsrm","sbf","vizxpk","gjcuqy","uue","fmedau","wwi"])
def is_rok_vxes(dnpj, xgs):
    return dnpj[0] != "mrgi" and xgs[-2] == "gjcuqy"
def is_rok_rmfl(dnpj, xgs):
    return not is_rok_vxes(dnpj, xgs)
rok= Factor("rok", [DerivedLevel("vxes", Window(is_rok_vxes, [dnpj, xgs], 3, 1)), DerivedLevel("rmfl", Window(is_rok_rmfl, [dnpj, xgs], 3, 1))])

design=[dnpj,xgs,rok]
crossing=[rok]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END
