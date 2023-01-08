from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kleet = Factor("kleet", ["wkfh", "kqe"])
mcalg = Factor("mcalg", ["rpu", "xmqp"])
qvyd = Factor("qvyd", ["bbt", "cpq"])

### EXPERIMENT
design=[kleet,mcalg,qvyd]
crossing=[[kleet,mcalg,qvyd]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_6"))
### END