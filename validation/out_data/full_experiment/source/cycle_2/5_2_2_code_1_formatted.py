### REGULAR FACTORS
geo = Factor("geo", ["nifi", "dwc"])
jms = Factor("jms", ["krfi", "cwkx"])
mqhf = Factor("mqhf", ["nifi", "dwc"])
rqqs = Factor("rqqs", ["krfi", "cwkx"])
xocanv = Factor("xocanv", ["poqlbg", "gcr"])
### DERIVED FACTORS
##
def fubc (mqhf, xocanv):
    return mqhf == xocanv
def aud (mqhf, xocanv):
    return not fubc(mqhf, xocanv)
cvfre = Factor("cvfre", [DerivedLevel("tktwoa", WithinTrial(fubc, [mqhf, xocanv])), DerivedLevel("ljnw", WithinTrial(aud, [mqhf, xocanv]))])
##
def ahhql (jms, geo):
    return jms == geo
def gkv (jms, geo):
    return not ahhql(jms, geo)
nkd = Factor("nkd", [DerivedLevel("gzzjd", WithinTrial(ahhql, [jms, geo])), DerivedLevel("yan", WithinTrial(gkv, [jms, geo]))])
### EXPERIMENT
design=[cvfre,nkd,geo,jms,mqhf,rqqs,xocanv]
constraints=[AtMostKInARow(2, jms),MinimumTrials(25)]
crossing=[mqhf,xocanv]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
