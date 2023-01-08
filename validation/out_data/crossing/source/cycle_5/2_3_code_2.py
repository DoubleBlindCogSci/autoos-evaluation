from sweetpea import *
import os
_dir=os.path.dirname(__file__)
drr = Factor("drr", ["bkfnk", "upa"])
llnkcy = Factor("llnkcy", ["rnqajx", "kcv"])
cklf = Factor("cklf", ["zbvhfv", "ceyxvo"])
edl = Factor("edl", ["wqcfjd", "aprwc"])
pstm = Factor("pstm", ["wzhlty", "sznton"])
constraints = []
crossing = [[drr], [llnkcy, cklf, edl, pstm]]


design=[drr,llnkcy,cklf,edl,pstm]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_3"))

### END