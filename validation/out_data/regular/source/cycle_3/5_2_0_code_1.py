from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
njgu8eOcP=[Level('f_W]B<ZRuG',9),'rF]ZyO',"ctG:tUTxkTUNH*",'e|Kmp7hKAg0Bg']
iqyk=Level('fTd',1)
Z81FVfr=Factor('Tj2z',['vJLcHx','>a<Dstn',njgu8eOcP[3],'X:MifqeRNZxDL{',Level('MjfPLdhu',6),"ug(4)",iqyk])
Sl8qK3A1i=Factor(";DoQDv",[Level("xadYQNJsPQIE",9),Level("nPsPIw",7),"bIqzL",'ErKccNMuoym T{',Level("kvKzrxfWmLvzS",9)])

### EXPERIMENT
design=[Z81FVfr,Sl8qK3A1i]
crossing=[Z81FVfr,Sl8qK3A1i]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_2_0"))
### END