from sweetpea import *
import os
_dir=os.path.dirname(__file__)
kleet = Factor("kleet", ["wkfh", "kqe"])
mcalg = Factor("mcalg", ["rpu", "xmqp"])
qvyd = Factor("qvyd", ["bbt", "cpq"])
constraints = []
crossing = [kleet, mcalg, qvyd]


design=[kleet,mcalg,qvyd]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_6"))

### END