from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nnoj = Factor("nnoj", ["sqx", "glx"])
dbynih = Factor("dbynih", ["urhocr", "hjtod"])
ejwsu = Factor("ejwsu", ["gnlleu", "hjxt"])
iulyla = Factor("iulyla", ["qawc", "tndys"])
btk = Factor("btk", ["tsqztg", "yvfwf"])
tts = Factor("tts", ["mon", "ajyizx"])

### EXPERIMENT
design=[nnoj,dbynih,ejwsu,iulyla,btk,tts]
crossing=[[nnoj,dbynih,ejwsu,iulyla,btk,tts]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_4"))
### END