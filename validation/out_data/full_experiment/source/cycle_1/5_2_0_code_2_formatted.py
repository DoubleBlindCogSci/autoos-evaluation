### REGULAR FACTORS
qwm = Factor("qwm", ["dfyept", "pfaqzf"])
qgau = Factor("qgau", ["ljmk", "bajuw"])
vztzuw = Factor("vztzuw", ["dfyept", "pfaqzf"])
upvxq = Factor("upvxq", ["ljmk", "bajuw"])
ykfncu = Factor("ykfncu", ["uzoatr", "ocup"])
### DERIVED FACTORS
##
def is_zklvsn_dxvrh(qwm, upvxq):
    return qwm == upvxq
def is_zklvsn_rxalmf(qwm, upvxq):
    return not is_zklvsn_dxvrh(qwm, upvxq)
zklvsn= Factor("zklvsn", [DerivedLevel("dxvrh", WithinTrial(is_zklvsn_dxvrh, [qwm, upvxq])), DerivedLevel("rxalmf", WithinTrial(is_zklvsn_rxalmf, [qwm, upvxq]))])
##
def is_swopp_airucu(vztzuw, qgau):
    return vztzuw == qgau
def is_swopp_ekoc(vztzuw, qgau):
    return not is_swopp_airucu(vztzuw, qgau)
swopp= Factor("swopp", [DerivedLevel("airucu", WithinTrial(is_swopp_airucu, [vztzuw, qgau])), DerivedLevel("ekoc", WithinTrial(is_swopp_ekoc, [vztzuw, qgau]))])
### EXPERIMENT
constraints = []
crossing = [ykfncu, vztzuw]
design=[qwm,qgau,vztzuw,upvxq,ykfncu]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
