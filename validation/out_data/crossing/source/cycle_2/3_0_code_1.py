from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
txll = Factor("txll", ["giy", "nte"])
vixpp = Factor("vixpp", ["nfgin", "ifng"])
yvqrj = Factor("yvqrj", ["yalx", "gfuhfc"])
vov = Factor("vov", ["ewjum", "rnqopx"])
gbsiqh = Factor("gbsiqh", ["oetyi", "ezjdmx"])
nozc = Factor("nozc", ["hqou", "diqp"])
jorxj = Factor("jorxj", ["uuf", "glkebt"])
nqhae = Factor("nqhae", ["bspp", "fhflp"])
askrq = Factor("askrq", ["epwk", "blpq"])
sgzg = Factor("sgzg", ["iaz", "uht"])
bwnnbo = Factor("bwnnbo", ["dxh", "xfcd"])

### EXPERIMENT
design=[txll,vixpp,yvqrj,vov,gbsiqh,nozc,jorxj,nqhae,askrq,sgzg,bwnnbo]
crossing=[[txll,vixpp,yvqrj,vov],[gbsiqh,nozc,jorxj,nqhae],[askrq,sgzg,bwnnbo],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_0"))
### END