from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
imgt = Factor("imgt", ["auik","ykvp","cnzw","ynk","cuzq","fwhui","rcuu","cdjwaz"])
ffi = Factor("ffi", ["sqx","dzsh","vgg","qnoc","pwdesb","wpsnra","nmsxqv","mbn"])
def vtmur(imgt, ffi):
     return "rcuu" == imgt[-1] and not ffi[0] == "mbn"
def ylup(imgt, ffi):
     return imgt[-1] != "rcuu" and ffi[0] == "mbn"
def yvtq(imgt, ffi):
     return (imgt[-1] != "rcuu") and (not ffi[0] == "mbn")
ryor = Factor("sfhdj", [DerivedLevel("kssc", Transition(vtmur, [imgt, ffi])), DerivedLevel("zaui", Transition(ylup, [imgt, ffi])),DerivedLevel("nqwa", Transition(yvtq, [imgt, ffi]))])
### EXPERIMENT
design=[imgt,ffi,ryor]
crossing=[ryor]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END