from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
EZJJ_VpVz_wUQ = Factor("EZJJ(VpVz7wUQ", ["yJYk3K", "MKjjJD3r"])
PZ_n_ = Factor("PZ}n1", [Level("{NrQk)Sy", 1), Level("#EZV", 10)])
jmhDcwuB_Xs = Factor("jmhDcwuB|Xs", ["Y eGKV*W", "KwO>F"])

design=[EZJJ_VpVz_wUQ,PZ_n_,jmhDcwuB_Xs]
crossing=[EZJJ_VpVz_wUQ,PZ_n_,jmhDcwuB_Xs]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_3_1"))

### END
