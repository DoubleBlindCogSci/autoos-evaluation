from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Wf_ql_o = Factor("Wf@ql4o", ["wggb", "Nvevg", "^yS9fxXxesRw", "Gd_WPJCWe!twW<", "Z*YVlzmiVSqF9D", "R}{vy", "DqRjBdcAJwGq"])
_bFav_K__H_MiP = Factor("%bFav K&4H1MiP", [" JRfI", "UqnilJRjDc", "v?WDCWNTMERzw", "okGvZByZyhG", "%JE(XnI", "U7K1jEVBQANvFY"])
Qke_JgQ_upW = Factor("Qke_JgQ]upW", [Level("yOQQ", 3), "ORT<ZWaI@AP", "IVxM5B", "psBa", "hSOz{(IvCht?8", "FeaZkM"])

design=[Wf_ql_o,_bFav_K__H_MiP,Qke_JgQ_upW]
crossing=[Wf_ql_o,_bFav_K__H_MiP,Qke_JgQ_upW]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_3_0"))

### END
