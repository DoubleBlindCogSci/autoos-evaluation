from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
gudpr = Factor("gudpr", ["tpxk","mzxlux","eneif","vxp","enjsv"])
iqmtg = Factor("iqmtg", ["ygi","hwpanh","bfkbl","smrsqk","qdfvn","ldgwb","xqni"])
def is_htfb_bizxs(gudpr, iqmtg):
    return gudpr[-1] != "mzxlux" and iqmtg[0] != "qdfvn"
def is_htfb_jyvte(gudpr, iqmtg):
    return not is_htfb_bizxs(gudpr, iqmtg)
htfb = Factor("htfb", [DerivedLevel("bizxs", Window(is_htfb_bizxs, [gudpr, iqmtg], 2, 1)), DerivedLevel("jyvte", Window(is_htfb_jyvte, [gudpr, iqmtg], 2, 1))])

design=[gudpr,iqmtg,htfb]
crossing=[htfb]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END