from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ewFu25=["9YgqDljcwqwl",'T)aOsnFZxEDmw',Level("c?Zadgj",9),'ufVWhgu:AoyNB',"Z_h"]
xh7BeJvmnD_=Factor('h(mgDey',ewFu25)
u2d2iN=Factor("Kh|",[Level('Zz9aSPy vcpErG',6),Level("U5go",9),'NcEzH[VNhmYptq','nU)MZuJk','xOHHoQGf'])

### EXPERIMENT
design=[xh7BeJvmnD_,u2d2iN]
crossing=[xh7BeJvmnD_,u2d2iN]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_2_1"))
### END