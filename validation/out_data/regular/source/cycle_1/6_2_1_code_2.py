from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bloeNR_c= Factor("bloeNR(c", ["#Rii", "GQpeC$o", "ocJEKsOBe", "GiAW>sQdc?t", Level("U E$vGK", 8), Level("A@F2HAnyN", 1)])
wg_Ig_= Factor("wg4Ig6", ["aMbum:LO", "_zD)BRcfYNI", "CQk^hOhaj)kot", Level("YgwAt", 9), "#b;", Level("BYSfLRDmUOrCP", 1)])

design=[bloeNR_c,wg_Ig_]
crossing=[bloeNR_c,wg_Ig_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/6_2_1"))

### END
