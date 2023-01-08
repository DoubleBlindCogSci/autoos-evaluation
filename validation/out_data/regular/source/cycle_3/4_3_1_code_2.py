from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

_ng = Factor(";ng", [Level("guNcQia", 1), Level("LCtiqhYJV", 4), "RZKSouN&WZRt", "_EVgwS~BlrZ7p"])
cyX_srlXM_E = Factor("cyX4srlXM_E", ["~ujp*e", "sczrjY$", ")vAWn", "zk}"])
_Yw_u_PnGNb = Factor("~Yw;u]PnGNb", [Level("aOgLJ IhKxK", 1), Level("SThkrc", 1), Level("ivYEax @Lnd{O6", 3), "OcU>MhhCK4lod"])


design=[_ng,cyX_srlXM_E,_Yw_u_PnGNb]
crossing=[_ng,cyX_srlXM_E,_Yw_u_PnGNb]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_3_1"))

### END
