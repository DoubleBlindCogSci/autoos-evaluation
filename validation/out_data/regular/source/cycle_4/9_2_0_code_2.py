from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xeT_sUVeZ = Factor("xeT8sUVeZ", [Level("x0jozyEr", 1), Level("N ?x[i AC", 1), Level("C}eWW%UuhVy", 1), Level("J~odOQmitm", 1), Level("dzIh]EyV:ls1nI", 1), Level("H0CpB", 1), Level("oAt[QoOzW xm", 1), Level("BJKUev4xH", 1), Level("eHV", 2), Level("tLGjZGyva", 2), Level("tfhpM{TBq", 1)])
hF_y_l = Factor("hF]y:l", [Level("QzWHb<dLIKacrh", 1), Level("woC%sL", 1), Level("kQQDyLn{o", 1), Level("UK1q?", 1), Level("cqZ8L}SZVT_O", 1), Level("eN51vNrQQ", 1), Level("zGT<yFyyNZ", 1), Level("AypcOqde", 1)])

design=[xeT_sUVeZ,hF_y_l]
crossing=[xeT_sUVeZ,hF_y_l]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_2_0"))

### END
