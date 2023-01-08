from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
los = Factor("los", ["ubxc","wacwp","uywtvx","cflb","hre","clv","qvw"])
wwbpe = Factor("wwbpe", ["qba","sckl","ojtn","avwq","sprqyp","ieh","dnhzuw"])
def is_ejluh_yfg(los, wwbpe):
    return los[0] == "hre" and wwbpe[-1] != "qba"
def is_ejluh_jzzqzd(los, wwbpe):
    return not is_ejluh_yfg(los, wwbpe)
ejluh= Factor("ejluh", [DerivedLevel("yfg", Transition(is_ejluh_yfg, [los, wwbpe])), DerivedLevel("jzzqzd", Transition(is_ejluh_jzzqzd, [los, wwbpe]))])

design=[los,wwbpe,ejluh]
crossing=[ejluh]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END
