from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
N_Bn = Factor("N6Bn", [Level("Ldm", 4), Level("chrUvnM|ZQvCS", 1), Level("j<QkW", 1), Level(">4lT7", 1), Level("vZHr", 1), Level("K2ghss<YwE[Q", 1), Level("Y8aTbwKWnph", 1), Level("mrJ", 9)])
hfm__ = Factor("hfm_3", [Level("fsEF", 6), Level(" pUWH", 1), Level("OTUOppP;VCi", 3), Level("hdurS", 1), Level("ISuXvoVCPDP", 9), Level("Qu2", 2), Level("#K#F}dLXUh&RI", 1)])
uPdZ_ygZP = Factor("uPdZ<ygZP", [Level("MFdi8MQhP[G", 1), Level("UijZHGvx", 1), Level("fltZe^8IxXIR", 2), Level("b(b7OhdQPuFKE", 1), Level("HOX6XppTGg", 1), Level("saLs{Ze8Bu$ ", 1), Level("os>jNIjMK", 1), Level("8SOhj[hhC", 1)])

design=[N_Bn,hfm__,uPdZ_ygZP]
crossing=[N_Bn,hfm__,uPdZ_ygZP]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_3_0"))

### END
