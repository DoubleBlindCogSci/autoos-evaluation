from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

_rY_eZI_Oc_ = Factor(">rY@eZI}Oc)", [Level("SoWBiQ&YTqQzcT", 1), Level("sfQt", 7), Level("y6^Cq_", 1), Level("EPLv:JMYYMK", 1)])
M_UTjqP_VUHvE = Factor("M3UTjqP0VUHvE", ["fp{G", "mEWV^bB}WiGkl", "1jI9QflgLp", "PYtvC_ZbJlo"])
dtD_MQkuKXy = Factor("dtD^MQkuKXy", ["eClU}ThYb", "LpYI~oVWxscLTg", "YlYn zR{gfVehn"])


design=[_rY_eZI_Oc_,M_UTjqP_VUHvE,dtD_MQkuKXy]
crossing=[_rY_eZI_Oc_,M_UTjqP_VUHvE,dtD_MQkuKXy]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_3_1"))

### END
