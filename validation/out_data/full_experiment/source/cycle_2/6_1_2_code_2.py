from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
zuqn = Factor("zuqn", ["rqu", "yzh"])
iob = Factor("iob", ["wsep", "xvci"])
mdz = Factor("mdz", ["rqu", "yzh"])
hmoud = Factor("hmoud", ["wsep", "xvci"])
ibonqh = Factor("ibonqh", ["tyyna", "knxo"])
ktcou = Factor("ktcou", ["vwbsg", "wwqtz"])
def is_hci_gzrsh(zuqn, iob):
    return zuqn == iob
def is_hci_fbv(zuqn, iob):
    return not is_hci_gzrsh(zuqn, iob)
hci= Factor("hci", [DerivedLevel("gzrsh", WithinTrial(is_hci_gzrsh, [zuqn, iob])), DerivedLevel("fbv", WithinTrial(is_hci_fbv, [zuqn, iob]))])
constraints = [AtLeastKInARow(2, (zuqn, "rqu")), ExactlyKInARow(4, (hci, "gzrsh"))]
crossing = [mdz, hci]

design=[zuqn,iob,mdz,hmoud,ibonqh,ktcou,hci]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_1_2"))
