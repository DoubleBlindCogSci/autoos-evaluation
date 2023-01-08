### REGULAR FACTORS
edkiip = Factor("edkiip", ["ddtexz", "fecbd"])
mas = Factor("mas", ["zdqq", "chnyyz"])
erdzl = Factor("erdzl", ["ddtexz", "fecbd"])
odbrwn = Factor("odbrwn", ["zdqq", "chnyyz"])
egh = Factor("egh", ["oxg", "pbouw"])
ukmfq = Factor("ukmfq", ["lumokl", "rkahyg"])
### DERIVED FACTORS
##
def qfsm (ukmfq, mas):
    return ukmfq == mas
def eveixc (ukmfq, mas):
    return not qfsm(ukmfq, mas)
yhm = Factor("yhm", [DerivedLevel("jdmfqw", WithinTrial(qfsm, [ukmfq, mas])), DerivedLevel("det", WithinTrial(eveixc, [ukmfq, mas]))])
##
### EXPERIMENT
design=[yhm,edkiip,mas,erdzl,odbrwn,egh,ukmfq]
constraints=[ExactlyKInARow(3, odbrwn)]
crossing=[odbrwn,erdzl]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
