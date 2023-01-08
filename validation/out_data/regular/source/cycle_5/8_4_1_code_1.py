from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mBMgkz0r=Factor('V_wC',['dreaJwR:',"aAzE","TTBhCQBnD",'FES',Level("^E%",1),'iXcBfN','Ann',"9FHNXzojhKn7("])
GyDP=Factor('rDac*T}psjF',[Level("C lPvRRSmE",2),'CqQOzlzkQvLa9',"1e9|:","G<GWMf","N5VpbuLmFS",Level('Pcq@zwY<F',4),"ufxTm","KVl0YFN"])
WE_E=Factor("YuXmIWj9]",["bpP8Gi3*3V",'cY~u?eU','tRvOFbSdEI;r','~3nN;*iC','XFc68ekc','Lv_k','ROaVqfW&yqsUbI',"Ai ET@k"])
xOijX='XH>Pn>j'
HwaMc=Factor('dgjWFM',['E4QVkD!Gn',"oZAEZFrCVSs","L^ee",'vquv','wO]hqOv&cAvAYo',"is*GNUE",'!vGVxnNeY','rQT',xOijX])

### EXPERIMENT
design=[mBMgkz0r,GyDP,WE_E,HwaMc]
crossing=[mBMgkz0r,GyDP,WE_E,HwaMc]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_4_1"))
### END