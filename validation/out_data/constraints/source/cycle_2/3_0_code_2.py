from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jvrw = Factor("jvrw", ["zlebup","jgos", "pbzw"])
ipj = Factor("ipj", ["mrwhgp","vnbza","umgq", "tvibc"])
dqgb = Factor("dqgb", ["qjmic","lvfk", "awada"])
qdyr = Factor("qdyr", ["gkoqk","pmz", "norf"])
rnaqv = Factor("rnaqv", ["xeyirg","qivre","hrof", "soa"])
lit = Factor("lit", ["pvlfwy","idjr", "ihjkd"])


constraints = [MinimumTrials(47), ExactlyK(2, (ipj, "tvibc")), Exclude((dqgb, "awada"))]
crossing = [qdyr, rnaqv, lit]

design=[jvrw,ipj,dqgb,qdyr,rnaqv,lit]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_0"))

### END