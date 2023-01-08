from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
knqgp = Factor("knqgp", ["ocs", "pdgniz"])
mnz = Factor("mnz", ["jav", "zjpv"])
agam = Factor("agam", ["nhhm", "nfdz"])

### EXPERIMENT
design=[knqgp,mnz,agam]
crossing=[[knqgp,mnz,agam]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_4"))
### END