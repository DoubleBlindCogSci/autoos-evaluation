from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vinn = Factor("vinn", ["ocg","tyc","ajcqj","dwq","eixzwg"])
def gtz(vinn):
    return vinn[-3] != "ocg" or vinn[-2] == "eixzwg"
def zpj(vinn):
    return not (vinn[-3] != "ocg") and vinn[-2] != "eixzwg"
ozytaw = DerivedLevel("iyflel", Window(gtz, [vinn],4,1))
zcby = DerivedLevel("hnojgz", Window(zpj, [vinn],4,1))
sfqq = Factor("mktqr", [ozytaw, zcby])

### EXPERIMENT
design=[vinn,sfqq]
crossing=[sfqq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END