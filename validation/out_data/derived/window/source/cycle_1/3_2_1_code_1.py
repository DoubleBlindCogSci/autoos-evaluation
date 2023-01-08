from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
bsy = Factor("bsy", ["pccj","drl","bzlogf","qtctr","bsz","msu","itl"])
nopd = Factor("nopd", ["pccj","drl","bzlogf","qtctr","bsz","msu","itl"])
fhq = Factor("fhq", ["pccj","drl","bzlogf","qtctr","bsz","msu","itl"])
def vjzjb(bsy, nopd, fhq):
     return bsy[0] == nopd[-3]
def yst(bsy, nopd, fhq):
     return nopd[-3] != bsy[0] and fhq[0] == bsy[-3]
def ang(bsy, nopd, fhq):
     return (not vjzjb(bsy, nopd, fhq)) and (not yst(bsy, nopd, fhq))
esxqjs = DerivedLevel("xkn", Window(vjzjb, [bsy, nopd, fhq],4,1))
kza = DerivedLevel("bxvp", Window(yst, [bsy, nopd, fhq],4,1))
ferqf = DerivedLevel("ylwc", Window(ang, [bsy, nopd, fhq],4,1))
zzuvq = Factor("nsaqy", [esxqjs, kza, ferqf])

### EXPERIMENT
design=[bsy,nopd,fhq,zzuvq]
crossing=[zzuvq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END