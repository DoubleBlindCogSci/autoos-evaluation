from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
RBo= Factor("RBo", [Level("jOcz", 7), Level("YQILxAcQYra", 4), Level("$vqBxq", 7), "b$ZiSLoFmmg", "klXGVleXh", "OnwGa", "VsthfWm"])
ZcOY= Factor("ZcOY", [Level("VFeDO%4:", 4), Level("GDGohhXiJe;", 9), Level("m#eYvv<HIEwIN", 3), "TyNGASA$Ryheot", "JiUgRKF", "fvDDe", "BQmvXeGpYvev*M"])
nbgswoYdxzc_= Factor("nbgswoYdxzc?", [Level("6FnN HJhVlK", 7), Level("SNIarJ", 7), Level("wRx9kbOkRg", 3), "lLwGRqHP", "paE;uW", "EbgG "])

design=[RBo,ZcOY,nbgswoYdxzc_]
crossing=[RBo,ZcOY,nbgswoYdxzc_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/6_3_1"))

### END
