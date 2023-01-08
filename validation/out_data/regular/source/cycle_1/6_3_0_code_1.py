from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
IT7gl3Bbb_W=['wWsddqrAY','hILzm','aVUbVYYhm','X(AhOV}92WFgm',Level('qAgNvRGMe',3),'zDiYDkye',"WW}qiwP~e"]
pSNLq=Factor('Clbl#yEkS',[IT7gl3Bbb_W[3],'gtVJUIWy',"PwCySm",Level('yfdXy',5),'eHsosCM9F{Ude',':y3myCEKIH',Level("VjOd",1)])
VcEiSHLw=Factor("kBy)_X4Hzqe",[Level('QcS',9),'aPBFuz',Level('tqzmGY22HJEB',5),Level("7EEOYi^EOMna8l",10),Level('kV#hdR',3),"OXgHrjGR;@nao"])
aIw3NVE6='ZZkDSRH ;Aypo'
HjPzCn2Aq="xOJ"
xkZXVlpt=['SDSIwiqI?JlFk',HjPzCn2Aq,'mkNGovUra2Xm',aIw3NVE6,Level("W[&MuToGOvq",9),"Pm|IQ",'wMXYVAGALX',Level("zb?yZ|yqDHlcRq",2)]
Yypl=Factor('o3KWHkza^OToog',xkZXVlpt)

### EXPERIMENT
design=[pSNLq,VcEiSHLw,Yypl]
crossing=[pSNLq,VcEiSHLw,Yypl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/6_3_0"))
### END