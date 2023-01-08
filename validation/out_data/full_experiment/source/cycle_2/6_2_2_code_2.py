from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
cxac = Factor("cxac", ["alpai", "mdiei"])
byvob = Factor("byvob", ["juc", "bzdi"])
ayfgq = Factor("ayfgq", ["alpai", "mdiei"])
tnd = Factor("tnd", ["juc", "bzdi"])
uwgbrp = Factor("uwgbrp", ["gnyajh", "bqg"])
phb = Factor("phb", ["mjyfwo", "jea"])
def is_funv_jrhlqv(phb, uwgbrp):
    return phb == uwgbrp
def is_funv_axyuo(phb, uwgbrp):
    return not is_funv_jrhlqv(phb, uwgbrp)
funv= Factor("funv", [DerivedLevel("jrhlqv", WithinTrial(is_funv_jrhlqv, [phb, uwgbrp])), DerivedLevel("axyuo", WithinTrial(is_funv_axyuo, [phb, uwgbrp]))])
def is_bkcnhy_cfae(cxac, tnd):
    return cxac == tnd
def is_bkcnhy_ljbbi(cxac, tnd):
    return not is_bkcnhy_cfae(cxac, tnd)
bkcnhy= Factor("bkcnhy", [DerivedLevel("cfae", WithinTrial(is_bkcnhy_cfae, [cxac, tnd])), DerivedLevel("ljbbi", WithinTrial(is_bkcnhy_ljbbi, [cxac, tnd]))])
constraints = [AtLeastKInARow(3, (byvob, "juc")), AtMostKInARow(4, (uwgbrp, "gnyajh"))]
crossing = [cxac, byvob]

design=[cxac,byvob,ayfgq,tnd,uwgbrp,phb,funv,bkcnhy]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_2_2"))
