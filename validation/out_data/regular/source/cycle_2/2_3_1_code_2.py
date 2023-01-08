from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kPX = Factor("kPX", ["RIXHSCRm]&w9", "BAv@xW"])
Sg_ = Factor("Sg_", ["zA7UZgVJKR", "wrMNGFRkex"])
Wd__D = Factor("Wd68D", ["AxgIH", "aiFdCWzYlwNNK"])

design=[kPX,Sg_,Wd__D]
crossing=[kPX,Sg_,Wd__D]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_3_1"))

### END
