from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jyvygh = Factor("jyvygh", ["vwaya", "kdy"])
zprvzb = Factor("zprvzb", ["hdo","rhn", "njzbtb"])
wjspxt = Factor("wjspxt", ["jcx", "jyptk"])
srbpq = Factor("srbpq", ["jlky","fydqm","kdjxb", "zyw"])
zbe = Factor("zbe", ["emwa","ftndk", "ycfd"])

### EXPERIMENT
constraints=[AtMostKInARow(4,(jyvygh,"kdy")),MinimumTrials(18)]
design=[jyvygh,zprvzb,wjspxt,srbpq,zbe]
crossing=[wjspxt,srbpq,zbe]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_4"))
### END