from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
db5Uzw6=["rRxiqRvijWO",'TaVwXKOg8Dc',"Qb r<ai2bOAMA3","f;eDr",'vNdiWv',Level("GHrWJ#eCG}l9LR",9),Level("Hvuap",7)]
Wij1m=Factor("XqQI&BWrlDu>Pz",db5Uzw6)
LtBD=[Level("GIcBndwfp",3),"gENxv","II{(I","nBX2uSr{v","ksDKlX",Level('yMwP',5),Level("UZi",4)]
YeWMT3q=Factor("kWbbX?pmpLa",LtBD)
psJn_zMqnq=Factor('SRLeTbi',[Level("QXpmqmLEyd",4),Level('JiI',7),'@cntVPw#F F#N',"CIR",'mOcq',"plb{Wy#","T[pbrfa"])

### EXPERIMENT
design=[Wij1m,YeWMT3q,psJn_zMqnq]
crossing=[Wij1m,YeWMT3q,psJn_zMqnq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_3_0"))
### END