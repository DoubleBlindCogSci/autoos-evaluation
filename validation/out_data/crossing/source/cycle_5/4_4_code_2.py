from sweetpea import *
import os
_dir=os.path.dirname(__file__)
jmiuft = Factor("jmiuft", ["rnc", "dqdrtn"])
svdm = Factor("svdm", ["mbmol", "saesu"])
aksmc = Factor("aksmc", ["qfo", "yifmv"])
pcxmnv = Factor("pcxmnv", ["wmivwu", "higb"])
xka = Factor("xka", ["fkqkzs", "sfhg"])
juio = Factor("juio", ["rrpne", "ozmo"])
qdr = Factor("qdr", ["nat", "yddki"])
qjbhw = Factor("qjbhw", ["afh", "rkdgo"])
constraints = []
crossing = [[jmiuft, svdm], [aksmc, pcxmnv, xka], [juio, qdr, qjbhw]]


design=[jmiuft,svdm,aksmc,pcxmnv,xka,juio,qdr,qjbhw]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_4"))

### END