from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
TZ_xjZ = Factor("TZ3xjZ", [Level("DtolflCM5fYCAH", 1), Level("QPS2N", 1), Level("4|w", 1), Level("vYf:", 1), Level("seJSMA%]f", 1), Level("Mt<kW", 1), Level(")CSgqmV:", 4), Level("nmba", 1), Level("a6brMZG", 1)])
_R_cXdnjV_X = Factor("8R6cXdnjV#X", [Level("GW|aFAYOPC", 1), Level("SYiCIPX", 1), Level("bow", 1), Level("YVjSmyWA", 1), Level("GWmycbs|iLn", 3), Level("iKkfMFi{", 1), Level("OTZRBVtp", 1), Level("]Gp;a", 1)])
MmlzVP_o = Factor("MmlzVP}o", [Level("hUNKjllG<UP2Gb", 1), Level(" QgeiT7CLEEh", 1), Level("2ygr ZjMz&_DJ", 1), Level("ZgA&CIRN", 1), Level("!TUHih", 1), Level("Amsfx<LUOm", 1), Level("y:Q", 1), Level("QbtPzLZ|[", 1)])

design=[TZ_xjZ,_R_cXdnjV_X,MmlzVP_o]
crossing=[TZ_xjZ,_R_cXdnjV_X,MmlzVP_o]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_3_0"))

### END
