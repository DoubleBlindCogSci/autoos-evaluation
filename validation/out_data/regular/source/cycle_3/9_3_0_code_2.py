from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
UHiOjqnbU = Factor("UHiOjqnbU", [Level("rp1lOL#evEP3x", 7), Level("T]Tjhxzd~", 1), Level("hGqjd?wPSNcdq", 1), Level("znsmPHpfA", 1), Level("^f;!", 1), Level("oE]lhEJxf", 1), Level("lVUpk", 1), Level("hJBMJ|g", 1), Level("AJbGE", 1)])
NjyastzmSRtAD = Factor("NjyastzmSRtAD", [Level("BJSEyvvX", 1), Level("OkJ{O", 1), Level("_QsjOpSwu(", 2), Level("PpzE#N99U^RSMB", 1), Level("FnUpZw5aO%", 1), Level("FfMi", 7), Level("I%n", 1), Level("VMyuf}:$TQW", 1), Level("YWy&]", 1), Level("xKWkchXMInY", 2)])
HpsJeGNB = Factor("HpsJeGNB", [Level("8WM)BAZKaV", 1), Level("&OfvK{", 1), Level("TYZ", 7), Level("Vz3X3yXZcA", 1), Level("i_B", 1), Level("DEAFokd", 1), Level("wZJuZQSMLLOrgt", 1), Level("CYwOs e]Rb", 1), Level("|k9z WS*VG~", 1)])

design=[UHiOjqnbU,NjyastzmSRtAD,HpsJeGNB]
crossing=[UHiOjqnbU,NjyastzmSRtAD,HpsJeGNB]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_3_0"))

### END
