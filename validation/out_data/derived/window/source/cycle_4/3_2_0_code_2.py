from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
iuuz = Factor("iuuz", ["qwvmh","keht","pfkmy","vdlw","sueuw","jahl"])
pfwafi = Factor("pfwafi", ["qwvmh","keht","pfkmy","vdlw","sueuw","jahl"])
dxcv = Factor("dxcv", ["qwvmh","keht","pfkmy","vdlw","sueuw","jahl"])
def is_ogak_uik(iuuz, pfwafi, dxcv):
    return iuuz[0] == dxcv[-3] and iuuz[-3] != pfwafi[0]
def is_ogak_rrqftz(iuuz, pfwafi, dxcv):
    return dxcv[-3] != iuuz[0] and iuuz[-3] == pfwafi[0]
def is_ogak_rxcigz(iuuz, pfwafi, dxcv):
    return not (is_ogak_uik(iuuz, pfwafi, dxcv) or is_ogak_rrqftz(iuuz, pfwafi, dxcv))
ogak= Factor("ogak", [DerivedLevel("uik", Window(is_ogak_uik, [iuuz, pfwafi, dxcv], 4, 1)), DerivedLevel("rrqftz", Window(is_ogak_rrqftz, [iuuz, pfwafi, dxcv], 4, 1)), DerivedLevel("rxcigz", Window(is_ogak_rxcigz, [iuuz, pfwafi, dxcv], 4, 1))])

design=[iuuz,pfwafi,dxcv,ogak]
crossing=[ogak]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END