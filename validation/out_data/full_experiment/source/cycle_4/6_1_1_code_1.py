from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
edkiip = Factor("edkiip", ["ddtexz", "fecbd"])
mas = Factor("mas", ["zdqq", "chnyyz"])
erdzl = Factor("erdzl", ["ddtexz", "fecbd"])
odbrwn = Factor("odbrwn", ["zdqq", "chnyyz"])
egh = Factor("egh", ["oxg", "pbouw"])
ukmfq = Factor("ukmfq", ["lumokl", "rkahyg"])
def qfsm (ukmfq, mas):
    return ukmfq == mas
def eveixc (ukmfq, mas):
    return not qfsm(ukmfq, mas)
yhm = Factor("yhm", [DerivedLevel("jdmfqw", WithinTrial(qfsm, [ukmfq, mas])), DerivedLevel("det", WithinTrial(eveixc, [ukmfq, mas]))])
design=[yhm,edkiip,mas,erdzl,odbrwn,egh,ukmfq]
constraints=[ExactlyKInARow(3, odbrwn)]
crossing=[odbrwn,erdzl]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1_1"))
