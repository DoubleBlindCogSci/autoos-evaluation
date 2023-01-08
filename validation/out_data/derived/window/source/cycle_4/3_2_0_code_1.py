from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
iuuz = Factor("iuuz", ["qwvmh","keht","pfkmy","vdlw","sueuw","jahl"])
pfwafi = Factor("pfwafi", ["qwvmh","keht","pfkmy","vdlw","sueuw","jahl"])
dxcv = Factor("dxcv", ["qwvmh","keht","pfkmy","vdlw","sueuw","jahl"])
def qvk(iuuz, dxcv, pfwafi):
     return iuuz[0] == dxcv[-3] and iuuz[-3] != pfwafi[0]
def iabmzw(iuuz, dxcv, pfwafi):
     return dxcv[-3] != iuuz[0] and pfwafi[0] == iuuz[-3]
def hgyemc(iuuz, dxcv, pfwafi):
     return (not iuuz[0] == dxcv[-3]) and (iuuz[-3] != pfwafi[0])
hvya = DerivedLevel("uik", Window(qvk, [iuuz, pfwafi, dxcv],4,1))
duxon = DerivedLevel("rrqftz", Window(iabmzw, [iuuz, pfwafi, dxcv],4,1))
ciiwa = DerivedLevel("rxcigz", Window(hgyemc, [iuuz, pfwafi, dxcv],4,1))
sohqcv = Factor("ogak", [hvya, duxon, ciiwa])

### EXPERIMENT
design=[iuuz,pfwafi,dxcv,sohqcv]
crossing=[sohqcv]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END