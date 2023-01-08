### REGULAR FACTORS
edkiip = Factor("edkiip", ["ddtexz", "fecbd"])
mas = Factor("mas", ["zdqq", "chnyyz"])
erdzl = Factor("erdzl", ["ddtexz", "fecbd"])
odbrwn = Factor("odbrwn", ["zdqq", "chnyyz"])
egh = Factor("egh", ["oxg", "pbouw"])
ukmfq = Factor("ukmfq", ["lumokl", "rkahyg"])
### DERIVED FACTORS
##
def is_yhm_jdmfqw(ukmfq, mas):
    return ukmfq == mas
def is_yhm_det(ukmfq, mas):
    return not is_yhm_jdmfqw(ukmfq, mas)
yhm = Factor("yhm", [DerivedLevel("jdmfqw", WithinTrial(is_yhm_jdmfqw, [ukmfq, mas])), DerivedLevel("det", WithinTrial(is_yhm_det, [ukmfq, mas]))])
### EXPERIMENT
constraints = [ExactlyKInARow(3, (odbrwn, "jdmfqw"))]
crossing = [odbrwn, erdzl]
design=[edkiip,mas,erdzl,odbrwn,egh,ukmfq,yhm]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
