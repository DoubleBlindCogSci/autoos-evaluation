from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
llppou= Factor("llppou", ["kwx","vpznh","cacm","pmvgq","rromj","wnvo"])
buff= Factor("buff", ["mtp","tegfon","rawjzc","ganf","cgukfq","gbjs","llq","qmkzto"])
def is_jwu_odx(llppou, buff):
    return llppou[0] == "pmvgq" and buff[-1] != "rawjzc"
def is_jwu_eqe(llppou, buff):
    return llppou[0] != "pmvgq" and buff[-1] == "rawjzc"
def is_jwu_qygv(llppou, buff):
    return not (is_jwu_odx(llppou, buff) or is_jwu_eqe(llppou, buff))
jwu= Factor("jwu", [DerivedLevel("odx", Window(is_jwu_odx, [llppou, buff], 2, 1)), DerivedLevel("eqe", Window(is_jwu_eqe, [llppou, buff], 2, 1)), DerivedLevel("qygv", Window(is_jwu_qygv, [llppou, buff], 2, 1))])

design=[llppou,buff,jwu]
crossing=[jwu]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_3"))

### END
