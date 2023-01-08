from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ykmc = Factor("ykmc", ["vyle","yuvder","xxf","loup","hyh","fjptm","cgrl"])
okg = Factor("okg", ["lthe","oeru","pjzss","xtdg","mvmk","afop","pxg"])
def lee(ykmc, okg):
     return ykmc == "cgrl"
def mpk(ykmc, okg):
     return ykmc != "cgrl" and  okg == "lthe"
def tpxxht(ykmc, okg):
     return (not ykmc == "cgrl") and (okg != "lthe")
upfgtt = DerivedLevel("pxocro", WithinTrial(lee, [ykmc, okg]))
fsgc = DerivedLevel("xoqhut", WithinTrial(mpk, [ykmc, okg]))
hsezs = DerivedLevel("jgz", WithinTrial(tpxxht, [ykmc, okg]))
jghal = Factor("ncv", [upfgtt, fsgc, hsezs])

### EXPERIMENT
design=[ykmc,okg,jghal]
crossing=[jghal]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END