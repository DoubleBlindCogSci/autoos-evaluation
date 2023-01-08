from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
taaa = Factor("taaa", ["filhdf","zmdo","nexxd","fpsq","ysn","gjlyl","cspkuu","msxd"])
vcz = Factor("vcz", ["uwleue","xuceqb","abux","dtfovj","bio","fus","uxtm"])
def uhjc(taaa, vcz):
     return taaa == "filhdf"
def barkmp(taaa, vcz):
     return taaa != "filhdf" and  vcz == "bio"
def ynb(taaa, vcz):
     return (taaa != "filhdf") and (not barkmp(taaa, vcz))
hxjww = DerivedLevel("ajplpx", WithinTrial(uhjc, [taaa, vcz]))
wmeygd = DerivedLevel("mlkbl", WithinTrial(barkmp, [taaa, vcz]))
wpqxo = DerivedLevel("dosx", WithinTrial(ynb, [taaa, vcz]))
woyyf = Factor("djwavc", [hxjww, wmeygd, wpqxo])

### EXPERIMENT
design=[taaa,vcz,woyyf]
crossing=[woyyf]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END