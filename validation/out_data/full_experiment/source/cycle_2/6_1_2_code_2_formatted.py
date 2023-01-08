### REGULAR FACTORS
zuqn = Factor("zuqn", ["rqu", "yzh"])
iob = Factor("iob", ["wsep", "xvci"])
mdz = Factor("mdz", ["rqu", "yzh"])
hmoud = Factor("hmoud", ["wsep", "xvci"])
ibonqh = Factor("ibonqh", ["tyyna", "knxo"])
ktcou = Factor("ktcou", ["vwbsg", "wwqtz"])
### DERIVED FACTORS
##
def is_hci_gzrsh(zuqn, iob):
    return zuqn == iob
def is_hci_fbv(zuqn, iob):
    return not is_hci_gzrsh(zuqn, iob)
hci= Factor("hci", [DerivedLevel("gzrsh", WithinTrial(is_hci_gzrsh, [zuqn, iob])), DerivedLevel("fbv", WithinTrial(is_hci_fbv, [zuqn, iob]))])
### EXPERIMENT
constraints = [AtLeastKInARow(2, (zuqn, "rqu")), ExactlyKInARow(4, (hci, "gzrsh"))]
crossing = [mdz, hci]
design=[zuqn,iob,mdz,hmoud,ibonqh,ktcou]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
