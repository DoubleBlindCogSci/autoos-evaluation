from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xmbiq= Factor("xmbiq", ["ztgrrw","xctwjz","thzl","tqd","ftwv","mlwv","xqojg"])
pap= Factor("pap", ["lnlw","qbvy","lcnfur","cgwsdi","chmye","uwwdtc","nvupej"])
def is_gas_zcp(xmbiq, pap):
    return xmbiq[-1] == "xqojg" and pap[-3] != "lcnfur"
def is_gas_mnoor(xmbiq, pap):
    return xmbiq[-1] != "xqojg" and pap[-3] == "lcnfur"
def is_gas_rhx(xmbiq, pap):
    return not (is_gas_zcp(xmbiq, pap) or is_gas_mnoor(xmbiq, pap))
gas= Factor("gas", [DerivedLevel("zcp", Window(is_gas_zcp, [xmbiq, pap], 4, 1)), DerivedLevel("mnoor", Window(is_gas_mnoor, [xmbiq, pap], 4, 1)), DerivedLevel("rhx", Window(is_gas_rhx, [xmbiq, pap], 4, 1))])

design=[xmbiq,pap,gas]
crossing=[gas]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_2"))

### END
