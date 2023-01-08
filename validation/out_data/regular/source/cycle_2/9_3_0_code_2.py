from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vTJkanPU = Factor("vTJkanPU", [Level("VDs", 1), Level("MFD6j3?EYi6NFh", 1), Level("!zPTtyn%co", 1), Level("gH|iRf", 9), Level("vFVSSFIAzt", 1), Level("5gUmG acaXL", 1), Level("Nrvr", 1), Level("bvbIM", 6), Level("im_REOCUXNxC", 4), Level("FcNn", 1)])
_XW_EkRXPUsH_E = Factor("}XW)EkRXPUsH7E", [Level("yb@2Il:MSwMzm", 7), Level("ze(x&ObX", 1), Level("YM%j6wJBxNu", 1), Level("Ll@FKdGT6bDX", 1), Level("bmap", 1), Level("TMaZm@GCy", 1), Level("du%8kP?YfvAkG", 1), Level("hsmp5qaZxq", 1), Level("mzX", 1)])
utDl_ = Factor("utDl#", [Level("WHfo_WErI", 4), Level("BsKTj!GBwvsNP", 1), Level("d<C]", 1), Level("h5eFN_a", 1), Level("fP#XIA~eQf[ulf", 1), Level("IJjFXxlODf", 1), Level("yQ&Pf8jMZRbfM", 9), Level("pZ$mJS", 1), Level("hcm(nSeI;A", 1), Level("TNw2dblAjLMWtD", 1)])

design=[vTJkanPU,_XW_EkRXPUsH_E,utDl_]
crossing=[vTJkanPU,_XW_EkRXPUsH_E,utDl_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_3_0"))

### END
