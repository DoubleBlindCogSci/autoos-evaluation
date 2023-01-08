from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
HyBOCX6kp1B=['}GN^j{leK','R#U',Level("NWNYcy",2),"IHWk("]
o4MnidhDxx='vt;'
fa7c8ukdS=Factor('ZkX}tIBFirTJ',['gxuEEmGPjd','kg_YYOZ',"OQB",Level("#NHeid",3),'WJACKaffc<G',o4MnidhDxx,"E7QCPK","MTM","s>EN8htD",'yjoF^dSse',HyBOCX6kp1B[1]])
zOit3m=["XRkx5$JmVx",Level('TDpwahS#TACXo',1),'mWUEB[oovwzi','Q3F6I2a6tb5TF(',"jGa>L^3~r","OY$",'1fq<E(6 &JxBG','%a6UN)zmz_!a4',"fIIDMx^{iX46w["]
Z_bW=Factor('ayQBYUg%',zOit3m)

### EXPERIMENT
design=[fa7c8ukdS,Z_bW]
crossing=[fa7c8ukdS,Z_bW]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_2_1"))
### END