from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mR_oSR= Factor("mR#oSR", [Level("Qcux", 3), Level("mtnbsZU", 1), Level("HTkhTRh>*GQn", 1), Level("CAhqRP", 6), Level("fpaeaYph[", 1), Level("b@FCjC", 1), Level("M8xlMpWVkYW]B", 1), Level("uv@Z*lKW>Sy", 8)])

design=[mR_oSR]
crossing=[mR_oSR]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/8_1_1"))

### END
