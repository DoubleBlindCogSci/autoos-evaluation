from sweetpea import *
import os
_dir=os.path.dirname(__file__)
knqgp = Factor("knqgp", ["ocs", "pdgniz"])
mnz = Factor("mnz", ["jav", "zjpv"])
agam = Factor("agam", ["nhhm", "nfdz"])
constraints = []
crossing = [knqgp, mnz, agam]


design=[knqgp,mnz,agam]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_4"))

### END