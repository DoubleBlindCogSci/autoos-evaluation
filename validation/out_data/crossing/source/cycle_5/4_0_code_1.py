from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pjnbo = Factor("pjnbo", ["nlcks", "mtq"])
hte = Factor("hte", ["harjg", "izaae"])
kjeta = Factor("kjeta", ["bazf", "oeg"])
yqp = Factor("yqp", ["ggmwfy", "oloni"])
tsl = Factor("tsl", ["ubsx", "wpfgfv"])
pbis = Factor("pbis", ["wosbek", "ziwy"])
tzmhx = Factor("tzmhx", ["qnxkxp", "ntjpn"])
rfc = Factor("rfc", ["aob", "nyw"])
zmukm = Factor("zmukm", ["oey", "nle"])

### EXPERIMENT
design=[pjnbo,hte,kjeta,yqp,tsl,pbis,tzmhx,rfc,zmukm]
crossing=[[pjnbo],[hte,kjeta,yqp],[tsl,pbis,tzmhx],[rfc,zmukm],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_0"))
### END