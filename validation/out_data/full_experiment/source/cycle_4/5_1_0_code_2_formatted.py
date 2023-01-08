### REGULAR FACTORS
emmn = Factor("emmn", ["zfeun", "ulfa"])
qoz = Factor("qoz", ["zoe", "qdaza"])
upqhqx = Factor("upqhqx", ["zfeun", "ulfa"])
gvpmo = Factor("gvpmo", ["zoe", "qdaza"])
hdjam = Factor("hdjam", ["uhe", "oulgv"])
### DERIVED FACTORS
##
def is_qus_mwsa(gvpmo, qoz):
    return gvpmo == qoz
def is_qus_oocxp(gvpmo, qoz):
    return not is_qus_mwsa(gvpmo, qoz)
qus = Factor("qus", [DerivedLevel("mwsa", WithinTrial(is_qus_mwsa, [gvpmo, qoz])), DerivedLevel("oocxp", WithinTrial(is_qus_oocxp, [gvpmo, qoz]))])
### EXPERIMENT
constraints = []
crossing = [qoz, hdjam]
design=[emmn,qoz,upqhqx,gvpmo,hdjam,qus]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
