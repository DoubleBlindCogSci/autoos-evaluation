from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
dnuay = Factor("dnuay", ["mrja", "aoeg"])
khuiq = Factor("khuiq", ["mvda", "jfwow"])
yqs = Factor("yqs", ["mrja", "aoeg"])
mtarj = Factor("mtarj", ["mvda", "jfwow"])
mhibz = Factor("mhibz", ["eroq", "irtmb"])
def xen (mhibz, khuiq):
    return mhibz == khuiq
def lql (mhibz, khuiq):
    return not xen(mhibz, khuiq)
cbgvt = Factor("cbgvt", [DerivedLevel("nxfjfi", WithinTrial(xen, [mhibz, khuiq])), DerivedLevel("dge", WithinTrial(lql, [mhibz, khuiq]))])
design=[cbgvt,dnuay,khuiq,yqs,mtarj,mhibz]
constraints=[]
crossing=[dnuay,yqs]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1_0"))
