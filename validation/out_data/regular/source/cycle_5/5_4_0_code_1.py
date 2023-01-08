from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
DaolP=Factor("mcR",['Mzssd_TXadY','weZOt v<{t',"gFryDiDbE1(aPH",Level("EKm",2),"*YCeDx"])
HXZ8='VWB~wR|S'
EfYq=['anmNZzGN','thussgpEZkkZg',HXZ8,'OPHshJj1Tu)5FF',"vPD","edl&iqq"]
M43mWPZ=Factor('{SsqUA',EfYq)
b7xu90fA=Factor('3!_;XuNGFqGov',['oYJf0aLP(','W_9DZ_ixjQd','qFn*q2FZW6NiV',Level('KWHKDtNR',2),'TX4'])
E2XOvAX=Factor("WzqR3",["RgCOfRe",'TEoHoo_EIR',"frHviA@FbvtiQ","sQ#AYwsY",'wiPL'])

### EXPERIMENT
design=[DaolP,M43mWPZ,b7xu90fA,E2XOvAX]
crossing=[DaolP,M43mWPZ,b7xu90fA,E2XOvAX]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_4_0"))
### END