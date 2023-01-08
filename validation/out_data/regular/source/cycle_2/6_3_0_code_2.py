from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ijDRyQgxkUTaL = Factor("ijDRyQgxkUTaL", [Level("TlK(U", 1), Level("ILnBfN", 4), "YlGhk{rRndt", "m#zU4$yXzyY", "xP(Kgw", "nlSTn2ltc^dA"])
fCdWJg_agY_t = Factor("fCdWJg[agY4t", ["X^y", Level("SsGnoU", 1), Level("HuylBEsNI", 3), "aDZ?kDGeN", "4rK", "Rs5HmgAl%1ze", "sZlUeBAUd4B"])
bby_IGB = Factor("bby<IGB", [Level("VuhAlkZJuMGo", 1), Level("M_vZsRG", 2), "XTyslcxc4;DvGU", "sG*iqB", "dni{DyCPDp", "GnXo"])

design=[ijDRyQgxkUTaL,fCdWJg_agY_t,bby_IGB]
crossing=[ijDRyQgxkUTaL,fCdWJg_agY_t,bby_IGB]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_3_0"))

### END
