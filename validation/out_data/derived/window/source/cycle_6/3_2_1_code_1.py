from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mfrme = Factor("mfrme", ["joqydt","mobtn","kzjju","mevtp","crjhjs","wii"])
tnwi = Factor("tnwi", ["bvvwd","rqnix","courr","xwwdvb","kste","idonp"])
def qaylt(mfrme, tnwi):
     return "wii" == mfrme[0] and tnwi[-2] != "kste"
def xifu(mfrme, tnwi):
     return mfrme[0] != "wii" and  tnwi[-2] == "kste"
def nezdt(mfrme, tnwi):
     return (not mfrme[0] == "wii") and (not tnwi[-2] == "kste")
pwotnh = Factor("xlyjlo", [DerivedLevel("ztgo", Window(qaylt, [mfrme, tnwi],3,1)), DerivedLevel("rqcz", Window(xifu, [mfrme, tnwi],3,1)),DerivedLevel("qfujr", Window(nezdt, [mfrme, tnwi],3,1))])
### EXPERIMENT
design=[mfrme,tnwi,pwotnh]
crossing=[pwotnh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END