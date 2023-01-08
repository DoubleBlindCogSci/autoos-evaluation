from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vinn= Factor("vinn", ["ocg","tyc","ajcqj","dwq","eixzwg"])
def is_mktqr_iyflel(vinn):
    return vinn[-3] != "ocg" or vinn[-2] == "eixzwg"
def is_mktqr_hnojgz(vinn):
    return not is_mktqr_iyflel(vinn)
mktqr= Factor("mktqr", [DerivedLevel("iyflel", Window(is_mktqr_iyflel, [vinn], 4, 1)), DerivedLevel("hnojgz", Window(is_mktqr_hnojgz, [vinn], 4, 1))])

design=[vinn, mktqr]
crossing=[mktqr]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END
