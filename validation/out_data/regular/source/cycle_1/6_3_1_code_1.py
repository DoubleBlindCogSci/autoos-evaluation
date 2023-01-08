from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
X1ee='klXGVleXh'
DGHM8aSU_Wq=Factor("RBo",['b$ZiSLoFmmg',X1ee,"OnwGa",Level('jOcz',7),'VsthfWm',Level("YQILxAcQYra",4),Level("$vqBxq",7)])
zBr61X=Level("m#eYvv<HIEwIN",3)
brcdIMF=['TyNGASA$Ryheot',Level("VFeDO%4:",4),"JiUgRKF",'fvDDe',"BQmvXeGpYvev*M",Level('GDGohhXiJe;',9),zBr61X]
kWGVK8yDjo=Factor('ZcOY',brcdIMF)
OdlKtz5jKH=Factor('nbgswoYdxzc?',[Level('6FnN HJhVlK',7),'lLwGRqHP',"paE;uW",Level("SNIarJ",7),'EbgG ',Level("wRx9kbOkRg",3)])

### EXPERIMENT
design=[DGHM8aSU_Wq,kWGVK8yDjo,OdlKtz5jKH]
crossing=[DGHM8aSU_Wq,kWGVK8yDjo,OdlKtz5jKH]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/6_3_1"))
### END