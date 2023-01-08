from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
EURYH__ = Factor("EURYH68", [Level("SxYEA", 1), Level("rGtQrRKtSF", 1), Level("pHEp)RWpyZ", 1), Level("sMSo2F;!", 8), Level("nx6GulJ", 1), Level("c{Oeo<QF", 1), Level("bON", 1), Level("vEMO {FwTRQH", 1), Level("71s", 1)])
wX__laii = Factor("wX#^laii", [Level("0mjNr", 5), Level("fPET", 1), Level("Hb)", 9), Level("yuJOaLEA", 1), Level("o]jJ9g%MLYfZC", 1), Level("TPNi2trc}hy", 6), Level("lRsU6vwOQJa4", 1), Level("p6b$hq[A", 1), Level("*Lf|!Ft~zG3QF", 1), Level("hiEuuxnMoB7I", 1)])

design=[EURYH__,wX__laii]
crossing=[EURYH__,wX__laii]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_2_1"))

### END
