from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rywp_s_B_pNz = Factor("rywp9s)B;pNz", ["ol1SNL>urpCs", "ToZiajcDY;L", "U?HanBxlgxiyg", "SnZvzhVuD", "[ZSxI0yW "])
D_ZpVNQD = Factor("D1ZpVNQD", [Level(" nd1 wXhC]^H", 7), Level("~sKt_K[|", 1), Level("LQSA1zljHPc", 2), Level("XcrrEEQ&dzWJ~", 3), Level("WcGk", 9), Level("Yp(RKdbeg", 6), Level("psxeRCdwbOqyo", 1)])
W_bOaSC = Factor("W<bOaSC", ["[V&jJVtYY", "qtW", "w{U^N2Y(G", "wFHo", "mSNIXej*eKdjKD"])

design=[rywp_s_B_pNz,D_ZpVNQD,W_bOaSC]
crossing=[rywp_s_B_pNz,D_ZpVNQD,W_bOaSC]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_3_1"))

### END
