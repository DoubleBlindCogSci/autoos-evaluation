from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
zuqn = Factor("zuqn", ["rqu", "yzh"])
iob = Factor("iob", ["wsep", "xvci"])
mdz = Factor("mdz", ["rqu", "yzh"])
hmoud = Factor("hmoud", ["wsep", "xvci"])
ibonqh = Factor("ibonqh", ["tyyna", "knxo"])
ktcou = Factor("ktcou", ["vwbsg", "wwqtz"])
def neuyip (zuqn, iob):
    return zuqn == iob
def drhy (zuqn, iob):
    return not neuyip(zuqn, iob)
hci = Factor("hci", [DerivedLevel("gzrsh", WithinTrial(neuyip, [zuqn, iob])), DerivedLevel("fbv", WithinTrial(drhy, [zuqn, iob]))])
design=[hci,zuqn,iob,mdz,hmoud,ibonqh,ktcou]
constraints=[ExactlyKInARow(4, mdz),AtLeastKInARow(2, zuqn)]
crossing=[mdz,hci]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1_2"))
