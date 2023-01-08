from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
MoghVZR=Factor('dPsIbBsXpE',['pPRUvEyTvE',"jxlzg}LvS$QelF",'CtG6z5qtQ0GPK','YE*aR','M4qy&Lm6x',"ZJVQThen",'QFD WY}bgsolVL','SfM;p'])
KlPDz=["i|YL7bJytpW","BxwMlgclUw"," wl","vASM~cpB",Level("1znnBJir#k:anj",2)]
vdNqzfTr0L=['D;vqqfmDlaG8',"QdO*m9DVjw",'LT}w^F2(','{3egwQj','0pB?G','zzn',"YBzuuR",KlPDz[1],'NycuKWQGvd']
IyUad=Factor("&pWH",vdNqzfTr0L)

### EXPERIMENT
design=[MoghVZR,IyUad]
crossing=[MoghVZR,IyUad]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_2_1"))
### END