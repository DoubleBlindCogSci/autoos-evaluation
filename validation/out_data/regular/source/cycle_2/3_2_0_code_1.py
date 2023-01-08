from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
IncbFT=["uEQEp",'zngvOgjInkCCe',"TbrhwXKm:QrEsR"]
OBu1n=Factor("cBEra",IncbFT)
ZMcPvXKX="aZXs"
cSQdpL=['XYf&f gEMX1',ZMcPvXKX,"jQKqc",Level('X|G(',2)]
ixtXIjB3=Factor('yX>wc',cSQdpL)

### EXPERIMENT
design=[OBu1n,ixtXIjB3]
crossing=[OBu1n,ixtXIjB3]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END