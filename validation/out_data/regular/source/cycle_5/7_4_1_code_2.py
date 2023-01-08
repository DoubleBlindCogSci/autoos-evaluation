from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

_SZW_qT_Tzg = Factor("6SZW%qT Tzg", ["xgUOpw", "0Qom", "iLHXiPoR", "JIxzytPjOqTuY", "iYawESJhzUK", "wRSUcfICrWF", "LXAuu"])
dq_a_NaZ = Factor("dq!a9NaZ", [Level("ALVwPwmclY", 1), Level("QlKBf3$oQINl", 1), Level("PYvSbPnmN", 1), Level(":qMBD", 1), Level("w@FL", 3), Level("gIoZ*dLozIZz", 1), Level(">vttJxPu)U", 1), Level("fOmq", 1)])
rWXFXyC = Factor("rWXFXyC", [Level("bvX_DNsdXVQF", 4), Level("ZnpkjBJFFz Ae", 1), Level("b9MuBKmKOoB", 1), Level("coIO vpDL", 1), Level("JI<<bOrXx", 1), Level("mx]<JLXwSr qi", 1), Level("gNvQbD#yn", 1), Level("F5PyCazprMncUr", 1), Level("lND6}erUYKmK1", 1)])
K_JkN_xowZko = Factor("K7JkN6xowZko", ["MiH", "UkjGLPmv", "FGxdx]yZRV6qUf", "Nz0wrmt", "hDAU>hBT42njB<", "cRsglN[*G", "rhja8T[?QD", "yxB"])


design=[_SZW_qT_Tzg,dq_a_NaZ,rWXFXyC,K_JkN_xowZko]
crossing=[_SZW_qT_Tzg,dq_a_NaZ,rWXFXyC,K_JkN_xowZko]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_4_1"))

### END
