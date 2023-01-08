from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
geo = Factor("geo", ["nifi", "dwc"])
jms = Factor("jms", ["krfi", "cwkx"])
mqhf = Factor("mqhf", ["nifi", "dwc"])
rqqs = Factor("rqqs", ["krfi", "cwkx"])
xocanv = Factor("xocanv", ["poqlbg", "gcr"])
def fubc (mqhf, xocanv):
    return mqhf == xocanv
def aud (mqhf, xocanv):
    return not fubc(mqhf, xocanv)
cvfre = Factor("cvfre", [DerivedLevel("tktwoa", WithinTrial(fubc, [mqhf, xocanv])), DerivedLevel("ljnw", WithinTrial(aud, [mqhf, xocanv]))])
def ahhql (jms, geo):
    return jms == geo
def gkv (jms, geo):
    return not ahhql(jms, geo)
nkd = Factor("nkd", [DerivedLevel("gzzjd", WithinTrial(ahhql, [jms, geo])), DerivedLevel("yan", WithinTrial(gkv, [jms, geo]))])
design=[cvfre,nkd,geo,jms,mqhf,rqqs,xocanv]
constraints=[AtMostKInARow(2, jms),MinimumTrials(25)]
crossing=[mqhf,xocanv]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_2_2"))
