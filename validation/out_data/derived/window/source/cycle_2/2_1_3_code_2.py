from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
elfx= Factor("elfx", ["zbydej","bpqtrb","vxtnpa","xfhmhy","qpilm","fzj"])
def is_ypqk_mxonf(elfx):
    return elfx[-1] == "vxtnpa" and elfx[-3] != "qpilm"
def is_ypqk_dhoai(elfx):
    return not is_ypqk_mxonf(elfx)
ypqk= Factor("ypqk", [DerivedLevel("mxonf", Window(is_ypqk_mxonf, [elfx], 4, 1)), DerivedLevel("dhoai", Window(is_ypqk_dhoai, [elfx], 4, 1))])

design=[elfx, ypqk]
crossing=[ypqk]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_3"))

### END
