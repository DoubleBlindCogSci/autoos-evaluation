from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZjRrH_ = Factor("ZjRrH?", [Level("YzORK#Ylmpt", 1), Level("kuO", 7), Level("OaeQ!<GD2Hy", 8), Level("PpMgMBMfTS", 1), Level("0ZwYyryh:Q6n", 1)])
Ql_PKY = Factor("Ql9PKY", [Level("QcmrORhdIb", 6), Level(";#Gd", 1), Level("GaTNPTp", 1), Level("Nv#L^cxIB", 1), Level("iXeRZYLa", 1)])
VWCMH_L = Factor("VWCMH?L", [Level("pAf", 1), Level("Zc rtq;rscX", 1), Level("lbhA&_(&Mz[", 8), Level("zZTBiFQm", 1), Level("pUwc", 4)])

design=[ZjRrH_,Ql_PKY,VWCMH_L]
crossing=[ZjRrH_,Ql_PKY,VWCMH_L]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_3_1"))

### END
