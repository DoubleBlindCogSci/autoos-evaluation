from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
o9CIQ=Factor('GSScI~jmaWctYX',[Level('tTwoWeFW',6),Level('J rI',3),"b;jWYhx(d(6f0a",Level('E$hF',10),"qiW^xUhfBQSp",' YSRGOP','X9J','teg[IfqrC',"wn~f*fAcLsXHoB"])
LQ6I85=['WwSc','vFG 3gsAz',Level('mDQPJMeH',8),Level('Ntw',3),'#|ijl9urNLDTt',"TvJFdCQLTK",'uoVl','LI2wpgDLviRhp',Level('EYWswGzPq',8)]
WmKIypq45=Factor("QG GSw|WnW@Z",LQ6I85)
TvtdLMRA=Factor('a2v|l!LvXU_)uj',['kYReKIDGfJ9TPP',"NJAdmPAJXQhVX","C$dEmqmYfta;so",'fo[RQpd','kbQGPTj',"ln|3|MZWbx","PljT)F",') Te(E~GeB','WFsTwhS'])

### EXPERIMENT
design=[o9CIQ,WmKIypq45,TvtdLMRA]
crossing=[o9CIQ,WmKIypq45,TvtdLMRA]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_3_1"))
### END