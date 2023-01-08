from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
XqQI_BWrlDu_Pz = Factor("XqQI&BWrlDu>Pz", [Level("rRxiqRvijWO", 1), Level("TaVwXKOg8Dc", 1), Level("Qb r<ai2bOAMA3", 1), Level("f;eDr", 1), Level("vNdiWv", 1), Level("GHrWJ#eCG}l9LR", 9), Level("Hvuap", 1)])
kWbbX_pmpLa = Factor("kWbbX?pmpLa", [Level("GIcBndwfp", 3), Level("gENxv", 1), Level("II{(I", 1), Level("nBX2uSr{v", 1), Level("ksDKlX", 1), Level("yMwP", 5), Level("UZi", 1)])
SRLeTbi = Factor("SRLeTbi", [Level("QXpmqmLEyd", 4), Level("JiI", 1), Level("@cntVPw#F F#N", 1), Level("CIR", 1), Level("mOcq", 1), Level("plb{Wy#", 1), Level("T[pbrfa", 1)])

design=[XqQI_BWrlDu_Pz,kWbbX_pmpLa,SRLeTbi]
crossing=[XqQI_BWrlDu_Pz,kWbbX_pmpLa,SRLeTbi]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_3_0"))

### END
