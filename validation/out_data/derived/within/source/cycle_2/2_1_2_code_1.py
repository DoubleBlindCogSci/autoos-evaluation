from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vzlmpb = Factor("vzlmpb", ["zws","hen","hpdf","uao","pcjx","nphqpl"])
def otuz(vzlmpb):
    return vzlmpb == "hpdf" or vzlmpb == "pcjx"
def iiu(vzlmpb):
    return vzlmpb != "hpdf" and not (vzlmpb == "pcjx")
tbfu = Factor("grgt", [DerivedLevel("rou", WithinTrial(otuz, [vzlmpb])), DerivedLevel("vod", WithinTrial(iiu, [vzlmpb]))])
### EXPERIMENT
design=[vzlmpb,tbfu]
crossing=[tbfu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END