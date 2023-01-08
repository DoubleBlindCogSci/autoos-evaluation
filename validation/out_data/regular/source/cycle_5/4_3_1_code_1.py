from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
CfdBokIh=Factor('KsmmA5FQgwt',['yZ9dZKM[EvG2yf',Level('@hbBa$M',1),"Hbmmg",Level('}bxPZ$htn',1)])
zfVQdM=['ufKzBs',"fhN@zhhckrEAP",'RRC','kl&mms Ve',"4P>]cBEz","YRJQZH"]
pkZbwKMl=[zfVQdM[1],'7r1FVmGa','vu1zXk*ILeN',"dZXxThClg","ScRF<N"]
owh46qZ=Factor('nXBtkb3r',pkZbwKMl)
OT4PkgMYMz=Factor('VKDnC;q',['txzuaSdY','cCFCaB@lnb1K@O',"[qRUT","feMNa^Tbc<OgY"])

### EXPERIMENT
design=[CfdBokIh,owh46qZ,OT4PkgMYMz]
crossing=[CfdBokIh,owh46qZ,OT4PkgMYMz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_3_1"))
### END