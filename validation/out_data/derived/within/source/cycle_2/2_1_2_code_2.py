from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vzlmpb= Factor("vzlmpb", ["zws","hen","hpdf","uao","pcjx","nphqpl"])
def is_grgt_rou(vzlmpb):
    return vzlmpb == "hpdf" or vzlmpb == "pcjx"
def is_grgt_vod(vzlmpb):
    return not is_grgt_rou(vzlmpb)
grgt= Factor("grgt", [DerivedLevel("rou", WithinTrial(is_grgt_rou, [vzlmpb])), DerivedLevel("vod", WithinTrial(is_grgt_vod, [vzlmpb]))])

design=[vzlmpb, grgt]
crossing=[grgt]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END
