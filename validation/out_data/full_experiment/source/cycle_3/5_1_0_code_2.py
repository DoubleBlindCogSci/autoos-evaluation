from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
dnuay = Factor("dnuay", ["mrja", "aoeg"])
khuiq = Factor("khuiq", ["mvda", "jfwow"])
yqs = Factor("yqs", ["mrja", "aoeg"])
mtarj = Factor("mtarj", ["mvda", "jfwow"])
mhibz = Factor("mhibz", ["eroq", "irtmb"])
def is_cbgvt_nxfjfi(mhibz, khuiq):
    return mhibz == khuiq
def is_cbgvt_dge(mhibz, khuiq):
    return not is_cbgvt_nxfjfi(mhibz, khuiq)
cbgvt = Factor("cbgvt", [DerivedLevel("nxfjfi", WithinTrial(is_cbgvt_nxfjfi, [mhibz, khuiq])), DerivedLevel("dge", WithinTrial(is_cbgvt_dge, [mhibz, khuiq]))])
constraints = []
crossing = [dnuay, yqs]

design=[dnuay,khuiq,yqs,mtarj,mhibz,cbgvt]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_1_0"))
