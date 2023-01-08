from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xmbiq = Factor("xmbiq", ["ztgrrw","xctwjz","thzl","tqd","ftwv","mlwv","xqojg"])
pap = Factor("pap", ["lnlw","qbvy","lcnfur","cgwsdi","chmye","uwwdtc","nvupej"])
def ccfoc(xmbiq, pap):
     return "xqojg" == xmbiq[-1] and not pap[-3] == "lcnfur"
def uxhfu(xmbiq, pap):
     return xmbiq[-1] != "xqojg" and  pap[-3] == "lcnfur"
def ddmy(xmbiq, pap):
     return (xmbiq[-1] != "xqojg") and (pap[-3] != "lcnfur")
yjwctr = DerivedLevel("zcp", Window(ccfoc, [xmbiq, pap],4,1))
gouv = DerivedLevel("mnoor", Window(uxhfu, [xmbiq, pap],4,1))
axyun = DerivedLevel("rhx", Window(ddmy, [xmbiq, pap],4,1))
nbjkdf = Factor("gas", [yjwctr, gouv, axyun])

### EXPERIMENT
design=[xmbiq,pap,nbjkdf]
crossing=[nbjkdf]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END