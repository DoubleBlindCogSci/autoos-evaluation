from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cmidc = Factor("cmidc", ["dqqr", "iwueyv"])
fwwo = Factor("fwwo", ["bhzteu", "fnho"])
bjtwp = Factor("bjtwp", ["wakwup", "vofa"])
sjna = Factor("sjna", ["fjir", "vnkypq"])
sovdyj = Factor("sovdyj", ["msrpse", "stp"])
mwxs = Factor("mwxs", ["smoin", "ayrjfa"])

### EXPERIMENT
design=[cmidc,fwwo,bjtwp,sjna,sovdyj,mwxs]
crossing=[[cmidc,fwwo,bjtwp],[sjna,sovdyj],[mwxs],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_0"))
### END