from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
llppou = Factor("llppou", ["kwx","vpznh","cacm","pmvgq","rromj","wnvo"])
buff = Factor("buff", ["mtp","tegfon","rawjzc","ganf","cgukfq","gbjs","llq","qmkzto"])
def ydd(llppou, buff):
     return "pmvgq" == llppou[0] and not buff[-1] == "rawjzc"
def drf(llppou, buff):
     return "pmvgq" != llppou[0] and  buff[-1] == "rawjzc"
def wnsdrx(llppou, buff):
     return (not ydd(llppou, buff)) and (not drf(llppou, buff))
pbjt = DerivedLevel("odx", Window(ydd, [llppou, buff],2,1))
wdyckx = DerivedLevel("eqe", Window(drf, [llppou, buff],2,1))
cdk = DerivedLevel("qygv", Window(wnsdrx, [llppou, buff],2,1))
mpe = Factor("jwu", [pbjt, wdyckx, cdk])

### EXPERIMENT
design=[llppou,buff,mpe]
crossing=[mpe]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END