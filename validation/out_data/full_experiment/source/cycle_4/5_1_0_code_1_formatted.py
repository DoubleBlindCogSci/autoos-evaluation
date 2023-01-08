### REGULAR FACTORS
emmn = Factor("emmn", ["zfeun", "ulfa"])
qoz = Factor("qoz", ["zoe", "qdaza"])
upqhqx = Factor("upqhqx", ["zfeun", "ulfa"])
gvpmo = Factor("gvpmo", ["zoe", "qdaza"])
hdjam = Factor("hdjam", ["uhe", "oulgv"])
### DERIVED FACTORS
##
def xjhmo (gvpmo, qoz):
    return gvpmo == qoz
def ieja (gvpmo, qoz):
    return not xjhmo(gvpmo, qoz)
qus = Factor("qus", [DerivedLevel("mwsa", WithinTrial(xjhmo, [gvpmo, qoz])), DerivedLevel("oocxp", WithinTrial(ieja, [gvpmo, qoz]))])
### EXPERIMENT
design=[qus,emmn,qoz,upqhqx,gvpmo,hdjam]
constraints=[]
crossing=[qoz,hdjam]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
