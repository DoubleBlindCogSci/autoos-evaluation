from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
F0ah=Factor("bxJb",[";PVCO$aWcbz",'ylo6Y}V',"BdY#FTkBv","rKo",'pZIl'])
ZsIFsAwet=Factor("VlJ",["AqzS}Bf",Level("r?Tjbj!MM",3),"T DkVkh^hG9","UuftnN ",'~eXNL5nuuW'])
czgH92ikH=["TpZUe",'FaJq8okZsp<','FpBVsTuVHl(:pE','Z$p','?gvaU']
t1Jit7t5F=Factor('MhQr',czgH92ikH)
rFei8IPkvLW=Factor('fPimoTeuEI{',['M$[LlIlc&0qii','4GK:qMKh','uvyeANtA','Tec*DFIour',"fiVqrMgCrZfq"])

### EXPERIMENT
design=[F0ah,ZsIFsAwet,t1Jit7t5F,rFei8IPkvLW]
crossing=[F0ah,ZsIFsAwet,t1Jit7t5F,rFei8IPkvLW]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_4_1"))
### END