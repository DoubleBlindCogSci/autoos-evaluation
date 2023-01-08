from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eIRV_I = Factor("eIRV%I", [Level("osUdJB&Edxl", 4), Level("hAimCiOE", 1), Level("XbB^LaV", 1), Level("pRW3HNV4FkK", 1), Level("lo@vVSx", 1), Level("!bPl:LIiQzwukG", 1), Level("#DzQ3", 1)])
Fxz_Uob_boxm_b = Factor("Fxz$Uob?boxm1b", ["&uypFVf", "IfOKO|", "~6ZvX*Hl|VI7NJ", "vdQPuaKTdc", "vMshw[HSHoJJhZ", "pqFGMs<"])
EwaZ_gw_b_ = Factor("EwaZ&gw;b4", [Level("oRyp", 4), Level("WQknLrt", 1), Level("zwlTSd", 1), Level("nD en:WCYHa6d", 1), Level("~wdw", 1), Level("|CUWyxo", 2), Level("XTb1X~ZLlgEe", 1)])

design=[eIRV_I,Fxz_Uob_boxm_b,EwaZ_gw_b_]
crossing=[eIRV_I,Fxz_Uob_boxm_b,EwaZ_gw_b_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_3_0"))

### END
