from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
los = Factor("los", ["ubxc","wacwp","uywtvx","cflb","hre","clv","qvw"])
wwbpe = Factor("wwbpe", ["qba","sckl","ojtn","avwq","sprqyp","ieh","dnhzuw"])
def riedv(los, wwbpe):
    return los[0] == "hre" and wwbpe[-1] != "qba"
def zgsux(los,wwbpe):
    return not (los[0] == "hre") or not (wwbpe[-1] != "qba")
dsi = DerivedLevel("yfg", Transition(riedv, [los, wwbpe]))
nqiu = DerivedLevel("jzzqzd", Transition(zgsux, [los, wwbpe]))
xbrx = Factor("ejluh", [dsi, nqiu])

### EXPERIMENT
design=[los,wwbpe,xbrx]
crossing=[xbrx]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END