from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tmkwf= Factor("tmkwf", ["cjgub","usu","jajoct","jzpu","xepu","simzsx"])
def is_jmyrao_ucfyzp(tmkwf):
    return tmkwf[0] != "jzpu" and tmkwf[-1] == "simzsx"
def is_jmyrao_pca(tmkwf):
    return not is_jmyrao_ucfyzp(tmkwf)
jmyrao= Factor("jmyrao", [DerivedLevel("ucfyzp", Window(is_jmyrao_ucfyzp, [tmkwf], 3, 1)), DerivedLevel("pca", Window(is_jmyrao_pca, [tmkwf], 3, 1))])

design=[tmkwf,jmyrao]
crossing=[jmyrao]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END
