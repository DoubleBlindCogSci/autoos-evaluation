from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jfmjpo = Factor("jfmjpo", ["dffhaf","atlfu","nqg","frr","kapl","xoopg"])
krk = Factor("krk", ["dffhaf","atlfu","nqg","frr","kapl","xoopg"])
ktn = Factor("ktn", ["dffhaf","atlfu","nqg","frr","kapl","xoopg"])
def jarw(jfmjpo, ktn, krk):
     return jfmjpo[-3] == ktn[-1] and jfmjpo[-1] != krk[-3]
def vweea(jfmjpo, ktn, krk):
     return ktn[-1] != jfmjpo[-3] and krk[-3] == jfmjpo[-1]
def jxve(jfmjpo, ktn, krk):
     return (not jarw(jfmjpo, ktn, krk)) and (not vweea(jfmjpo, ktn, krk))
elohps = Factor("faobo", [DerivedLevel("uqcsr", Window(jarw, [jfmjpo, krk, ktn],4,1)), DerivedLevel("nrzqy", Window(vweea, [jfmjpo, krk, ktn],4,1)),DerivedLevel("bzlj", Window(jxve, [jfmjpo, krk, ktn],4,1))])
### EXPERIMENT
design=[jfmjpo,krk,ktn,elohps]
crossing=[elohps]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END