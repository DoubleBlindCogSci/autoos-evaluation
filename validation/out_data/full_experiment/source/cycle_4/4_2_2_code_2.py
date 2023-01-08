from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
uwlh = Factor("uwlh", ["hhs", "ptiktj"])
uza = Factor("uza", ["uiq", "tmxav"])
bog = Factor("bog", ["hhs", "ptiktj"])
boh = Factor("boh", ["uiq", "tmxav"])
def is_znx_yjafe(uwlh, boh):
    return uwlh == boh
def is_znx_kndf(uwlh, boh):
    return not is_znx_yjafe(uwlh, boh)
znx = Factor("znx", [DerivedLevel("yjafe", WithinTrial(is_znx_yjafe, [uwlh, boh])), DerivedLevel("kndf", WithinTrial(is_znx_kndf, [uwlh, boh]))])
def is_dupc_duyj(uza, bog):
    return uza == bog
def is_dupc_ffiokh(uza, bog):
    return not is_dupc_duyj(uza, bog)
dupc = Factor("dupc", [DerivedLevel("duyj", WithinTrial(is_dupc_duyj, [uza, bog])), DerivedLevel("ffiokh", WithinTrial(is_dupc_ffiokh, [uza, bog]))])
constraints = [AtLeastKInARow(3, znx), ExactlyKInARow(3, boh)]
crossing = [bog, uza]

design=[uwlh,uza,bog,boh,znx,dupc]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2_2"))
