from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
U8ZQKvU6=['xuqvUI!QNWD','A1 apR:KOeUU',"BqBe;Uhi0%EyX","pKeu*C(Hrn","IG%qtiaBZ",'fBA}urKu',';chV']
NY3QxDQ_=Factor(":MJoBcljx",U8ZQKvU6)
Xt6Zi=["Wgqi4{kIhJV1)",'bTDHI',Level('rcSbkSrtNbBB',1),'oirf6Q']
dPSL0X=['uECHZECESk','TCQg','Z%Lb#6BOZbiQU',"%CWqrBAS*Uhu",Xt6Zi[1],'$lYKR','vwiNX',"uknjk"]
DdyM4=Factor("WTwbv",dPSL0X)
Km7tKgzr=Factor('fj%}(&xg',['AFgnPVcxla>w','h6JuFbxP<R','qwMx','Kr)XjtrZQhsF>P',"v%!So2AT F",'BEk ro',Level('^X81XESyrf:bf',4)])

### EXPERIMENT
design=[NY3QxDQ_,DdyM4,Km7tKgzr]
crossing=[NY3QxDQ_,DdyM4,Km7tKgzr]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_3_0"))
### END