from sweetpea import *
import os
_dir=os.path.dirname(__file__)
jard = Factor("jard", ["tvmj", "eexu"])
ywdki = Factor("ywdki", ["tvdfyp", "otn"])
ufok = Factor("ufok", ["tckiob", "ddo"])
fjrkin = Factor("fjrkin", ["mun", "qzrsd"])
exz = Factor("exz", ["xcftfk", "zamg"])
constraints = []
crossing = [jard, ywdki, ufok, fjrkin, exz]


design=[jard,ywdki,ufok,fjrkin,exz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_1"))

### END