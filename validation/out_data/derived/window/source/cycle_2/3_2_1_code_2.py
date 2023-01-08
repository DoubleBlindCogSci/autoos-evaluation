from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eqhxp= Factor("eqhxp", ["oaylp","uisvq","mvc","trrtn","etz","vvixp"])
fkxb= Factor("fkxb", ["zqthl","eoxhfp","nipkq","fvud","sxndfe","teif","lzeks","brcsus"])
def is_url_tmu(eqhxp, fkxb):
    return eqhxp[0] == "etz" and fkxb[-1] != "teif"
def is_url_qdhzdb(eqhxp, fkxb):
    return eqhxp[0] != "etz" and fkxb[-1] == "teif"
def is_url_qkejh(eqhxp, fkxb):
    return not (is_url_tmu(eqhxp, fkxb) or is_url_qdhzdb(eqhxp, fkxb))
url= Factor("url", [DerivedLevel("tmu", Window(is_url_tmu, [eqhxp, fkxb], 2, 1)), DerivedLevel("qdhzdb", Window(is_url_qdhzdb, [eqhxp, fkxb], 2, 1)), DerivedLevel("qkejh", Window(is_url_qkejh, [eqhxp, fkxb], 2, 1))])

design=[eqhxp,fkxb,url]
crossing=[url]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END
