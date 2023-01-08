from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
BxSpz=Factor('a1YxQGIoReR',[Level("kvW",7),'zYyMn5xpaCfo','OZTmyGNq','OTWjDg?Vqfm','*DzOIF:Hcp','ZMhHl:CEAooQ',Level("g:Vj#",8),"t^G@Ab[oMmpg4N"])
wZde=Factor('ooFs2z[qRGGH',["LjtFANUgqC2",Level('QSVsHULW',5),'UrVX'," g:6q",'ml|U[Vj9O',"gOcJjayZD) ",'OpmTm',"cfmcydLcF*jK"])

### EXPERIMENT
design=[BxSpz,wZde]
crossing=[BxSpz,wZde]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/8_2_0"))
### END