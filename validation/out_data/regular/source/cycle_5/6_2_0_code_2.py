from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
__QDVOrqBg = Factor("_)QDVOrqBg", ["Q&E$mvGpGg", "rsdDm0t", "Qam", "Jis", "ANi", "EIu"])
t_sywPp = Factor("t{sywPp", [Level("K7YNvthvfBE>", 3), "{eQ", ")bMciYGc&Bre", "olkYs$oeP", "zCLQzJ<E$J", "yzn[LG"])

design=[__QDVOrqBg,t_sywPp]
crossing=[__QDVOrqBg,t_sywPp]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_2_0"))

### END
