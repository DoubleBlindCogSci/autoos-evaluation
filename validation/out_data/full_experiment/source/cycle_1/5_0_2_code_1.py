from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
kbj = Factor("kbj", ["jnhscz", "enmgky"])
npycyx = Factor("npycyx", ["xbz", "pjtbin"])
ltjqdz = Factor("ltjqdz", ["jnhscz", "enmgky"])
dbb = Factor("dbb", ["xbz", "pjtbin"])
tdpseh = Factor("tdpseh", ["zgn", "sfu"])
design=[kbj,npycyx,ltjqdz,dbb,tdpseh]
constraints=[AtLeastKInARow(3, tdpseh),MinimumTrials(26)]
crossing=[npycyx,tdpseh]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/5_0_2"))
