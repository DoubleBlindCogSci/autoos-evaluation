from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
gEA = Factor("gEA", [Level("GFaS0QA%gdsbWv", 4), Level("hecoSTDmd] VO", 2), ">UlJw", "KL;yCKXPWgC?", "RDmXG%O", "xIKE>heId", "TWY(", "exmdZoQ", "uwGfZW;9r?Ko"])
_XOHTPtuI_du = Factor("(XOHTPtuI<du", [Level("PvDxbWU%URnODy", 3), "hTVnnhiugkZ_EX", "iyybcjPOq", "Szic!_A[bjvjs", "rgaqZS", "QZZVtoeXgyainT", "RgZ_jAzDX", "WHYEWymX", "_ALziiuF"])

design=[gEA,_XOHTPtuI_du]
crossing=[gEA,_XOHTPtuI_du]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_2_1"))

### END
