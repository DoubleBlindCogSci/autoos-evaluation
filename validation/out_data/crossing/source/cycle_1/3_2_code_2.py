from sweetpea import *
import os
_dir=os.path.dirname(__file__)
lrlvkb = Factor("lrlvkb", ["xdm", "omt"])
bcuuqr = Factor("bcuuqr", ["ghui", "daqwq"])
etqenb = Factor("etqenb", ["fcajbk", "prbzrx"])
oyir = Factor("oyir", ["hkj", "zulbj"])
constraints = []
crossing = [[lrlvkb, bcuuqr, etqenb], [bcuuqr, etqenb], [oyir]]


design=[lrlvkb,bcuuqr,etqenb,oyir]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2"))

### END