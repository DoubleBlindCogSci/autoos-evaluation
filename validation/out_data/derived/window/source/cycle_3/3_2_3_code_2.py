from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xzar = Factor("xzar", ["czr","kradd","einxyr","anxmad","yrfr","xdmei","jhpjrv","jix"])
fnhg = Factor("fnhg", ["ooollz","zrxn","brvdut","fybb","whgo","zigtjm","toz"])
def is_svpnhe_vkj(xzar, fnhg):
    return xzar[-1] == "jhpjrv" and fnhg[-2] != "zigtjm"
def is_svpnhe_xkghzg(xzar, fnhg):
    return xzar[-1] != "jhpjrv" and fnhg[-2] == "zigtjm"
def is_svpnhe_dxo(xzar, fnhg):
    return not (is_svpnhe_vkj(xzar, fnhg) or is_svpnhe_xkghzg(xzar, fnhg))
svpnhe= Factor("svpnhe", [DerivedLevel("vkj", Window(is_svpnhe_vkj, [xzar, fnhg], 3, 1)), DerivedLevel("xkghzg", Window(is_svpnhe_xkghzg, [xzar, fnhg], 3, 1)), DerivedLevel("dxo", Window(is_svpnhe_dxo, [xzar, fnhg], 3, 1))])

design=[xzar,fnhg,svpnhe]
crossing=[svpnhe]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_3"))

### END
