from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZdkRbRp_P = Factor("ZdkRbRp:P", [Level("Fb7dSvHvCg Ga", 8), Level("Eiy]ly", 1), Level("}3QL", 3)])
p_KMSdDk = Factor("p1KMSdDk", [Level("HONKDt", 3), Level("OHitE", 1), Level("YU f", 1)])
La__wTd__iQ = Factor("La^0wTd^4iQ", [Level("5zJZXXSWn", 1), Level("%J7MvI3", 9), Level("TspfX", 1)])

design=[ZdkRbRp_P,p_KMSdDk,La__wTd__iQ]
crossing=[ZdkRbRp_P,p_KMSdDk,La__wTd__iQ]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_3_1"))

### END
