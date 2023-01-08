from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
geo = Factor("geo", ["nifi", "dwc"])
jms = Factor("jms", ["krfi", "cwkx"])
mqhf = Factor("mqhf", ["nifi", "dwc"])
rqqs = Factor("rqqs", ["krfi", "cwkx"])
xocanv = Factor("xocanv", ["poqlbg", "gcr"])
def is_cvfre_tktwoa(mqhf, xocanv):
    return mqhf == xocanv
def is_cvfre_ljnw(mqhf, xocanv):
    return not is_cvfre_tktwoa(mqhf, xocanv)
cvfre= Factor("cvfre", [DerivedLevel("tktwoa", WithinTrial(is_cvfre_tktwoa, [mqhf, xocanv])), DerivedLevel("ljnw", WithinTrial(is_cvfre_ljnw, [mqhf, xocanv]))])
def is_nkd_gzzjd(jms, geo):
    return jms == geo
def is_nkd_yan(jms, geo):
    return not is_nkd_gzzjd(jms, geo)
nkd= Factor("nkd", [DerivedLevel("gzzjd", WithinTrial(is_nkd_gzzjd, [jms, geo])), DerivedLevel("yan", WithinTrial(is_nkd_yan, [jms, geo]))])
constraints = [AtMostKInARow(2, jms), MinimumTrials(25)]
crossing = [mqhf, xocanv]

design=[geo,jms,mqhf,rqqs,xocanv,cvfre,nkd]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_2_2"))
