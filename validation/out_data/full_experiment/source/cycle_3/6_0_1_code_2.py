from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
dgizf = Factor("dgizf", ["omekh", "jkt"])
imjtfj = Factor("imjtfj", ["gkhdp", "fyjb"])
amui = Factor("amui", ["omekh", "jkt"])
paanhe = Factor("paanhe", ["gkhdp", "fyjb"])
uirzmz = Factor("uirzmz", ["tdo", "gwtex"])
qhpc = Factor("qhpc", ["esaypj", "bps"])
constraints = [AtLeastKInARow(4, uirzmz)]
crossing = [dgizf, qhpc]

design=[dgizf,imjtfj,amui,paanhe,uirzmz,qhpc]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_0_1"))
