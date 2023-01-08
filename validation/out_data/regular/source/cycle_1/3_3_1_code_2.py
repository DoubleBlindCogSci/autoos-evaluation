from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hHhjIT_Skj_Vr= Factor("hHhjIT#Skj)Vr", [Level("eL9{mhG8C{Zt", 5), Level("WPzItkve@!rEe", 1), Level("zaKrmGLbEGmzR", 1)])
kxY_r_= Factor("kxY!r8", ["]&UFD3tuiyS", "tGYmNS", "zClDUXWfp"])
t_vd_= Factor("t6vd;", ["aPFyndMROE", "TLzzbnYIIY", "DJXE&dfMaYT"])

design=[hHhjIT_Skj_Vr,kxY_r_,t_vd_]
crossing=[hHhjIT_Skj_Vr,kxY_r_,t_vd_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/3_3_1"))

### END
