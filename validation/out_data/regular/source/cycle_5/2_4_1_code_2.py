from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
CGJ_UZ_SM_Vw = Factor("CGJ UZ(SM]Vw", ["@ mxVsncjXSmU", "enhU|RVFM0", "GX;WW7"])
Udyvgb_c = Factor("Udyvgb*c", ["Bg6ynwjKGthO", "Hv9{2^3cf0"])
xEtS = Factor("xEtS", [Level("PYm", 2), Level("yJX", 1)])
mdqtqldTz = Factor("mdqtqldTz", ["oDE<XPpz", "DHA)cR"])

design=[CGJ_UZ_SM_Vw,Udyvgb_c,xEtS,mdqtqldTz]
crossing=[CGJ_UZ_SM_Vw,Udyvgb_c,xEtS,mdqtqldTz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_4_1"))

### END
