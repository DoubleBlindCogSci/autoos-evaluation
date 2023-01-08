from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
pohbz = Factor("pohbz", ["bpev", "kiujoc"])
edcx = Factor("edcx", ["tyc", "yunio"])
yoma = Factor("yoma", ["bpev", "kiujoc"])
wmhjq = Factor("wmhjq", ["tyc", "yunio"])
wegj = Factor("wegj", ["mbg", "xpjjgv"])
fdhif = Factor("fdhif", ["atcbho", "ziqlyq"])
constraints = [AtLeastKInARow(3, (fdhif, "atcbho")), MinimumTrials(50)]
crossing = [yoma, edcx]

design=[pohbz,edcx,yoma,wmhjq,wegj,fdhif]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/6_0_2"))
