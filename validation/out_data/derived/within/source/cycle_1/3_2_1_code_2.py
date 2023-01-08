from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
taaa= Factor("taaa", ["filhdf","zmdo","nexxd","fpsq","ysn","gjlyl","cspkuu","msxd"])
vcz= Factor("vcz", ["uwleue","xuceqb","abux","dtfovj","bio","fus","uxtm"])
def is_djwavc_ajplpx(taaa):
    return taaa == "filhdf"
def is_djwavc_mlkbl(taaa, vcz):
    return taaa != "filhdf" and vcz == "bio"
def is_djwavc_dosx(taaa, vcz):
    return not (is_djwavc_ajplpx(taaa) or is_djwavc_mlkbl(taaa, vcz))
djwavc= Factor("djwavc", [DerivedLevel("ajplpx", WithinTrial(is_djwavc_ajplpx, [taaa])), DerivedLevel("mlkbl", WithinTrial(is_djwavc_mlkbl, [taaa, vcz])), DerivedLevel("dosx", WithinTrial(is_djwavc_dosx, [taaa, vcz]))])

design=[taaa,vcz,djwavc]
crossing=[djwavc]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END
