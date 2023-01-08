from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Jtr6olMcw='vJYW'
eK21M6Kr=Factor('ZTTKcHt<I',[Level("OS|yv{[UpvDa",9),"UMWKNHvJdD","LzSMH","0fo",'$JU]GUA',Jtr6olMcw,"CsdovqHpChLd","gSgOSIT"])
VvQM54mWA3=[Level("tNfwIuKYoqvIFJ",9),'RtrQVwWj(pUY[',Level("aHoK7P",8)]
kw9HWt=['JYtSUk',Level("thgDE]Jp",9),'Mcd xm3e}B',Level('MrrRen$acYzgHf',7),"CuELFAwb",'Adi%G0VIDSaDy',VvQM54mWA3[0],Level('h}CZD',8)]
EMmB=Factor("bC@X",kw9HWt)

### EXPERIMENT
design=[eK21M6Kr,EMmB]
crossing=[eK21M6Kr,EMmB]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_2_0"))
### END