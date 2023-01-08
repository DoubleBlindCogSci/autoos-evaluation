from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
edkiip = Factor("edkiip", ["ddtexz", "fecbd"])
mas = Factor("mas", ["zdqq", "chnyyz"])
erdzl = Factor("erdzl", ["ddtexz", "fecbd"])
odbrwn = Factor("odbrwn", ["zdqq", "chnyyz"])
egh = Factor("egh", ["oxg", "pbouw"])
ukmfq = Factor("ukmfq", ["lumokl", "rkahyg"])
def is_yhm_jdmfqw(ukmfq, mas):
    return ukmfq == mas
def is_yhm_det(ukmfq, mas):
    return not is_yhm_jdmfqw(ukmfq, mas)
yhm = Factor("yhm", [DerivedLevel("jdmfqw", WithinTrial(is_yhm_jdmfqw, [ukmfq, mas])), DerivedLevel("det", WithinTrial(is_yhm_det, [ukmfq, mas]))])
constraints = [ExactlyKInARow(3, odbrwn)]
crossing = [odbrwn, erdzl]

design=[edkiip,mas,erdzl,odbrwn,egh,ukmfq,yhm]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_1_1"))
