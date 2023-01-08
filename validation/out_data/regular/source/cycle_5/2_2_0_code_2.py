from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
QzCcJJyQWm_jh = Factor("QzCcJJyQWm&jh", ["Ub#", "INmFAsImU"])
_He_oHGjgzz = Factor("<He[oHGjgzz", ["uHx 5wkPFW", ";s 4MSSLBSac"])

design=[QzCcJJyQWm_jh,_He_oHGjgzz]
crossing=[QzCcJJyQWm_jh,_He_oHGjgzz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END
