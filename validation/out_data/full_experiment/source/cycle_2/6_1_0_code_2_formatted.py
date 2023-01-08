### REGULAR FACTORS
aiq = Factor("aiq", ["dbjumx", "woafy"])
jefa = Factor("jefa", ["qkd", "zighty"])
leophp = Factor("leophp", ["dbjumx", "woafy"])
vwqn = Factor("vwqn", ["qkd", "zighty"])
zovw = Factor("zovw", ["qtjexx", "swxghh"])
qexm = Factor("qexm", ["ggxeg", "lbxnp"])
### DERIVED FACTORS
##
def is_pye_bqekyw(jefa, leophp):
    return jefa == leophp
def is_pye_ygfjnn(jefa, leophp):
    return not is_pye_bqekyw(jefa, leophp)
pye= Factor("pye", [DerivedLevel("bqekyw", WithinTrial(is_pye_bqekyw, [jefa, leophp])), DerivedLevel("ygfjnn", WithinTrial(is_pye_ygfjnn, [jefa, leophp]))])
### EXPERIMENT
constraints = []
crossing = [vwqn, aiq]
design=[aiq,jefa,leophp,vwqn,zovw,qexm]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
