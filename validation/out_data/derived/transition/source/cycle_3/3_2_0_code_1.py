from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
nyy = Factor("nyy", ["jjsaj","fzzu","nkgyi","paixu","wbgk","vwtci"])
eqgxv = Factor("eqgxv", ["wbz","ugcj","addimm","tidq","kfdsc","xuyt","vjgv"])
def vddugg(nyy, eqgxv):
     return "fzzu" == nyy[-1] and eqgxv[0] != "xuyt"
def sqq(nyy, eqgxv):
     return "fzzu" != nyy[-1] and eqgxv[0] == "xuyt"
def hda(nyy, eqgxv):
     return (not nyy[-1] == "fzzu") and (not sqq(nyy, eqgxv))
unrc = DerivedLevel("gzuju", Transition(vddugg, [nyy, eqgxv]))
mqdef = DerivedLevel("wvbiev", Transition(sqq, [nyy, eqgxv]))
iayp = DerivedLevel("iaqvaw", Transition(hda, [nyy, eqgxv]))
zfqw = Factor("roau", [unrc, mqdef, iayp])

### EXPERIMENT
design=[nyy,eqgxv,zfqw]
crossing=[zfqw]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END