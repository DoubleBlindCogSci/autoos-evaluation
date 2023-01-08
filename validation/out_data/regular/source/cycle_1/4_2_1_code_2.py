from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kNNU= Factor("kNNU", [">neZ(xRB", "YfzN", "xQTObpzFYMn", "UKKSPSrtiw"])
QnpjG= Factor("QnpjG", [Level("NO>", 1), Level("tvPqB{", 1), Level("ISbyAqOADENd v", 1), Level("IqzUUIBUNfCRu", 3), Level(" Fx", 1)])

design=[kNNU,QnpjG]
crossing=[kNNU,QnpjG]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/4_2_1"))

### END
