from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fso = Factor("fso", ["eyk", "qvyua"])
uqejrz = Factor("uqejrz", ["oqqufo","ula", "wxezs"])
ieu = Factor("ieu", ["mdkc","odfp","nwjzk", "stze"])
pvscuh = Factor("pvscuh", ["ube","dosaco", "lzckgw"])
zudx = Factor("zudx", ["gtwx", "mzxe"])

### EXPERIMENT
constraints=[AtMostKInARow(3,(fso,"qvyua")),ExactlyKInARow(3,(uqejrz,"wxezs"))]
design=[fso,uqejrz,ieu,pvscuh,zudx]
crossing=[ieu,pvscuh,zudx]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2"))
### END