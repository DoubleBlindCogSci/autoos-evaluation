### REGULAR FACTORS
zuqn = Factor("zuqn", ["rqu", "yzh"])
iob = Factor("iob", ["wsep", "xvci"])
mdz = Factor("mdz", ["rqu", "yzh"])
hmoud = Factor("hmoud", ["wsep", "xvci"])
ibonqh = Factor("ibonqh", ["tyyna", "knxo"])
ktcou = Factor("ktcou", ["vwbsg", "wwqtz"])
### DERIVED FACTORS
##
def neuyip (zuqn, iob):
    return zuqn == iob
def drhy (zuqn, iob):
    return not neuyip(zuqn, iob)
hci = Factor("hci", [DerivedLevel("gzrsh", WithinTrial(neuyip, [zuqn, iob])), DerivedLevel("fbv", WithinTrial(drhy, [zuqn, iob]))])
##
### EXPERIMENT
design=[hci,zuqn,iob,mdz,hmoud,ibonqh,ktcou]
constraints=[ExactlyKInARow(4, mdz),AtLeastKInARow(2, zuqn)]
crossing=[mdz,hci]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
