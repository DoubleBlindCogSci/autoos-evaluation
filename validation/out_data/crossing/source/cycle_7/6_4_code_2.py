from sweetpea import *
import os
_dir=os.path.dirname(__file__)
nnoj = Factor("nnoj", ["sqx", "glx"])
dbynih = Factor("dbynih", ["urhocr", "hjtod"])
ejwsu = Factor("ejwsu", ["gnlleu", "hjxt"])
iulyla = Factor("iulyla", ["qawc", "tndys"])
btk = Factor("btk", ["tsqztg", "yvfwf"])
tts = Factor("tts", ["mon", "ajyizx"])
constraints = []
crossing = [nnoj, dbynih, ejwsu, iulyla, btk, tts]


design=[nnoj,dbynih,ejwsu,iulyla,btk,tts]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_4"))

### END