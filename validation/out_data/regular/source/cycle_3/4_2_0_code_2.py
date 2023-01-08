from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Houj_bCo_Do = Factor("Houj;bCo$Do", [Level("UkGodpK", 10), Level("XTl7;0ojFdtDkC", 1), Level("fTjX", 1), Level("rETujOKaOl", 1)])
CUA_WGwQ = Factor("CUA2WGwQ", [Level("xJvBbqaal?LMUD", 1), Level("Rrch?sDWbsC", 7), Level("sytZkHy", 1), Level("vAyCMFvWlmc}ef", 5)])

design=[Houj_bCo_Do,CUA_WGwQ]
crossing=[Houj_bCo_Do,CUA_WGwQ]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2_0"))

### END
