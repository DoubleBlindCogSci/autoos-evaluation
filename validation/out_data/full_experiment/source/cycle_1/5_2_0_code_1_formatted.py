### REGULAR FACTORS
qwm = Factor("qwm", ["dfyept", "pfaqzf"])
qgau = Factor("qgau", ["ljmk", "bajuw"])
vztzuw = Factor("vztzuw", ["dfyept", "pfaqzf"])
upvxq = Factor("upvxq", ["ljmk", "bajuw"])
ykfncu = Factor("ykfncu", ["uzoatr", "ocup"])
### DERIVED FACTORS
##
def zswjux (qwm, upvxq):
    return qwm == upvxq
def wkfx (qwm, upvxq):
    return not zswjux(qwm, upvxq)
zklvsn = Factor("zklvsn", [DerivedLevel("dxvrh", WithinTrial(zswjux, [qwm, upvxq])), DerivedLevel("rxalmf", WithinTrial(wkfx, [qwm, upvxq]))])
##
def aqclgk (vztzuw, qgau):
    return vztzuw == qgau
def fdchco (vztzuw, qgau):
    return not aqclgk(vztzuw, qgau)
swopp = Factor("swopp", [DerivedLevel("airucu", WithinTrial(aqclgk, [vztzuw, qgau])), DerivedLevel("ekoc", WithinTrial(fdchco, [vztzuw, qgau]))])
### EXPERIMENT
design=[zklvsn,swopp,qwm,qgau,vztzuw,upvxq,ykfncu]
constraints=[]
crossing=[ykfncu,vztzuw]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
