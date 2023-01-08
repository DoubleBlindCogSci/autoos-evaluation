from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
BHeGJD3d08p='rLCR5h~NLcTLUu'
bsF20Us9hrS=[BHeGJD3d08p,'AFt','CWMql3]HUMVKrN',Level('ljt',2),'piqS#NWhxj',Level("g>BRsRvs",3),"9fusx2lFe GKOL","xQp",Level('hm9fxe(ofqgV',3),"91EmrhgBpu"]
wmV0eRlle=Factor('eIRa<mp<xhDb',bsF20Us9hrS)

### EXPERIMENT
design=[wmV0eRlle]
crossing=[wmV0eRlle]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_1_0"))
### END