from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
GSScI_jmaWctYX = Factor("GSScI~jmaWctYX", [Level("tTwoWeFW", 6), Level("J rI", 1), Level("b;jWYhx(d(6f0a", 1), Level("E$hF", 10), Level("qiW^xUhfBQSp", 1), Level(" YSRGOP", 1), Level("X9J", 1), Level("teg[IfqrC", 1), Level("wn~f*fAcLsXHoB", 1)])
QG GSw|WnW@Z = Factor("QG GSw|WnW@Z", [Level("WwSc", 1), Level("vFG 3gsAz", 1), Level("mDQPJMeH", 8), Level("Ntw", 1), Level("#|ijl9urNLDTt", 1), Level("TvJFdCQLTK", 1), Level("uoVl", 1), Level("LI2wpgDLviRhp", 1), Level("EYWswGzPq", 8)])
a_v_l_LvXU__uj = Factor("a2v|l!LvXU_)uj", [Level("kYReKIDGfJ9TPP", 1), Level("NJAdmPAJXQhVX", 1), Level("C$dEmqmYfta;so", 1), Level("fo[RQpd", 1), Level("kbQGPTj", 1), Level("ln|3|MZWbx", 1), Level("PljT)F", 1), Level(") Te(E~GeB", 1), Level("WFsTwhS", 1)])

design=[GSScI_jmaWctYX,a_v_l_LvXU__uj]
crossing=[GSScI_jmaWctYX,a_v_l_LvXU__uj]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_3_1"))

### END
