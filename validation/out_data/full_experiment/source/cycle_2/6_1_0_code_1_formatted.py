### REGULAR FACTORS
aiq = Factor("aiq", ["dbjumx", "woafy"])
jefa = Factor("jefa", ["qkd", "zighty"])
leophp = Factor("leophp", ["dbjumx", "woafy"])
vwqn = Factor("vwqn", ["qkd", "zighty"])
zovw = Factor("zovw", ["qtjexx", "swxghh"])
qexm = Factor("qexm", ["ggxeg", "lbxnp"])
### DERIVED FACTORS
##
def ypkh (jefa, leophp):
    return jefa == leophp
def znu (jefa, leophp):
    return not ypkh(jefa, leophp)
pye = Factor("pye", [DerivedLevel("bqekyw", WithinTrial(ypkh, [jefa, leophp])), DerivedLevel("ygfjnn", WithinTrial(znu, [jefa, leophp]))])
##
### EXPERIMENT
design=[pye,aiq,jefa,leophp,vwqn,zovw,qexm]
constraints=[]
crossing=[vwqn,aiq]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
