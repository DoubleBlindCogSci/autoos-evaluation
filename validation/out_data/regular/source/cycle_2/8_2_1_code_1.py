from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
d2g1q='ZxrHgV'
_f9AL0l2=Factor('Nu9hsR7)QRVyT',["XKlO:PTn",'iI)Jf2',"XALFi~H%HMIkby",'HVrd6cQVJP',d2g1q,"ndXyv",Level('?ZBCNvSe',6),'APKM#d','e8PrYt{v%JH *D'])
wrLypab=Factor("W!cIisM8FtnMmD",[Level('~BBHICUcD',7),"kScn0s","KypU",Level("<VVbyuZ4or",6),Level('BAfAY@ct)KUy',1),Level("ckxe3",3),'BfZFF',"ZKiVYkip"])

### EXPERIMENT
design=[_f9AL0l2,wrLypab]
crossing=[_f9AL0l2,wrLypab]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_2_1"))
### END