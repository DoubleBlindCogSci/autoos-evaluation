from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Clbl_yEkS= Factor("Clbl#yEkS", [Level("X(AhOV}92WFgm", 5), Level("gtVJUIWy", 1), Level("PwCySm", 1), Level("yfdXy", 1), Level("eHsosCM9F{Ude", 1), Level(":y3myCEKIH", 1), Level("VjOd", 1), Level("WW}qiwP~e", 1)])
kBy__X_Hzqe= Factor("kBy)_X4Hzqe", [Level("QcS", 9), Level("aPBFuz", 1), Level("tqzmGY22HJEB", 1), Level("7EEOYi^EOMna8l", 10), Level("kV#hdR", 3), Level("OXgHrjGR;@nao", 1)])
o_KWHkza_OToog= Factor("o3KWHkza^OToog", [Level("SDSIwiqI?JlFk", 1), Level("xOJ", 1), Level("mkNGovUra2Xm", 1), Level("ZZkDSRH ;Aypo", 1), Level("W[&MuToGOvq", 9), Level("Pm|IQ", 1), Level("wMXYVAGALX", 1), Level("zb?yZ|yqDHlcRq", 1)])

design=[Clbl_yEkS,kBy__X_Hzqe,o_KWHkza_OToog]
crossing=[Clbl_yEkS,kBy__X_Hzqe,o_KWHkza_OToog]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/6_3_0"))

### END
