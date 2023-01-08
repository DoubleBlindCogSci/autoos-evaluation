from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ybxlxi = Factor("ybxlxi", ["tvzo","zlobz","kauhfp","vazzo","qlwxy","nxhhsi"])
def is_byjy_jlkvr(ybxlxi):
    return ybxlxi[-2] == "zlobz" or ybxlxi[-3] == "kauhfp"
def is_byjy_hlpzh(ybxlxi):
    return not is_byjy_jlkvr(ybxlxi)
byjy= Factor("byjy", [DerivedLevel("jlkvr", Window(is_byjy_jlkvr, [ybxlxi], 4, 1)), DerivedLevel("hlpzh", Window(is_byjy_hlpzh, [ybxlxi], 4, 1))])

design=[ybxlxi,byjy]
crossing=[byjy]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END
