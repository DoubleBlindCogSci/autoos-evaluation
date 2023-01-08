from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
LtyWZBaaSD=Factor('Jkhzh]OB)OEnN',["wa@Xvr",'iCW',"ibxB JhE!qT<","ttaiJIhhY|4aer","nE<Zp"])

### EXPERIMENT
design=[LtyWZBaaSD]
crossing=[LtyWZBaaSD]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1_1"))
### END