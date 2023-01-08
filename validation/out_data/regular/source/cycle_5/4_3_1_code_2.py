from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
KsmmA_FQgwt = Factor("KsmmA5FQgwt", ["yZ9dZKM[EvG2yf", Level("@hbBa$M", 1), "Hbmmg", Level("}bxPZ$htn", 1)])
nXBtkb_r = Factor("nXBtkb3r", ["ufKzBs", "fhN@zhhckrEAP", "RRC", "kl&mms Ve", "4P>]cBEz"])
VKDnC_q = Factor("VKDnC;q", ["txzuaSdY", "cCFCaB@lnb1K@O", "[qRUT", "feMNa^Tbc<OgY"])

design=[KsmmA_FQgwt,nXBtkb_r,VKDnC_q]
crossing=[KsmmA_FQgwt,nXBtkb_r,VKDnC_q]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_3_1"))

### END
