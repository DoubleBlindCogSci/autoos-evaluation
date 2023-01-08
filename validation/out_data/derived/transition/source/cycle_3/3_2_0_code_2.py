from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nyy = Factor("nyy", ["jjsaj","fzzu","nkgyi","paixu","wbgk","vwtci"])
eqgxv = Factor("eqgxv", ["wbz","ugcj","addimm","tidq","kfdsc","xuyt","vjgv"])
def is_roau_gzuju(nyy, eqgxv):
    return nyy[-1] == "fzzu" and eqgxv[0] != "xuyt"
def is_roau_wvbiev(nyy, eqgxv):
    return nyy[-1] != "fzzu" and eqgxv[0] == "xuyt"
def is_roau_iaqvaw(nyy, eqgxv):
    return not (is_roau_gzuju(nyy, eqgxv) or is_roau_wvbiev(nyy, eqgxv))
roau= Factor("roau", [DerivedLevel("gzuju", Transition(is_roau_gzuju, [nyy, eqgxv])), DerivedLevel("wvbiev", Transition(is_roau_wvbiev, [nyy, eqgxv])), DerivedLevel("iaqvaw", Transition(is_roau_iaqvaw, [nyy, eqgxv]))])

design=[nyy,eqgxv,roau]
crossing=[roau]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END
