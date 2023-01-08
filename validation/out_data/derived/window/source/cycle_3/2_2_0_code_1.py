from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dnpj = Factor("dnpj", ["mrgi","kcr","nzdax","mpyl","selg"])
xgs = Factor("xgs", ["vsrm","sbf","vizxpk","gjcuqy","uue","fmedau","wwi"])
def xwbgnu(dnpj, xgs):
    return dnpj[0] != "mrgi" and xgs[-2] == "gjcuqy"
def fcqqvq(dnpj,xgs):
    return not xwbgnu(dnpj, xgs)
zbooyp = DerivedLevel("vxes", Window(xwbgnu, [dnpj, xgs],3,1))
lvb = DerivedLevel("rmfl", Window(fcqqvq, [dnpj, xgs],3,1))
chduc = Factor("rok", [zbooyp, lvb])

### EXPERIMENT
design=[dnpj,xgs,chduc]
crossing=[chduc]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END