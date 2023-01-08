from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
h_mgDey = Factor("h(mgDey", [Level("9YgqDljcwqwl", 1), Level("T)aOsnFZxEDmw", 1), Level("c?Zadgj", 9), Level("ufVWhgu:AoyNB", 1), Level("Z_h", 1)])
Kh_ = Factor("Kh|", [Level("Zz9aSPy vcpErG", 6), Level("U5go", 9), Level("NcEzH[VNhmYptq", 1), Level("nU)MZuJk", 1), Level("xOHHoQGf", 1)])

design=[h_mgDey,Kh_]
crossing=[h_mgDey,Kh_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_2_1"))

### END
