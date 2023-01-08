from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
V_wC = Factor("V_wC", [Level("dreaJwR:", 1), Level("aAzE", 1), Level("TTBhCQBnD", 1), Level("FES", 1), Level("^E%", 1), Level("iXcBfN", 1), Level("Ann", 1), Level("9FHNXzojhKn7(", 1)])
rDac_T_psjF = Factor("rDac*T}psjF", [Level("C lPvRRSmE", 2), Level("CqQOzlzkQvLa9", 1), Level("1e9|:", 1), Level("G<GWMf", 1), Level("N5VpbuLmFS", 1), Level("Pcq@zwY<F", 4), Level("ufxTm", 1), Level("KVl0YFN", 1)])
YuXmIWj__ = Factor("YuXmIWj9]", ["bpP8Gi3*3V", "cY~u?eU", "tRvOFbSdEI;r", "~3nN;*iC", "XFc68ekc", "Lv_k", "ROaVqfW&yqsUbI", "Ai ET@k"])
dgjWFM = Factor("dgjWFM", ["E4QVkD!Gn", "oZAEZFrCVSs", "L^ee", "vquv", "wO]hqOv&cAvAYo", "is*GNUE", "!vGVxnNeY", "rQT", "XH>Pn>j"])

design=[V_wC,rDac_T_psjF,YuXmIWj__,dgjWFM]
crossing=[V_wC,rDac_T_psjF,YuXmIWj__,dgjWFM]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_4_1"))

### END
