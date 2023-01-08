from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dNhiegChdNK=[Level("o20tcr",4),"E#K"]
JBBXBZ_Y=[dNhiegChdNK[0],"bkZgz[q:HF8hxt",Level('TRdM$5L',2),"nqlL?&XL",'rbvEa',Level("vqg",4),"7^QxENEOxB",'YeaGAaZv5M']
MzQCR3KEeh4=Factor("QpxkUz~vdhp",JBBXBZ_Y)

### EXPERIMENT
design=[MzQCR3KEeh4]
crossing=[MzQCR3KEeh4]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_1_1"))
### END