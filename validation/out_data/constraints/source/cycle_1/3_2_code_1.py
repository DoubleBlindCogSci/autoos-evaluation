from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
sjrkg = Factor("sjrkg", ["iwgol","yics", "hez"])
lekrjk = Factor("lekrjk", ["hks","jyutsj", "agaw"])
sezqdj = Factor("sezqdj", ["djv","vdg", "cagt"])
tsgpzz = Factor("tsgpzz", ["avhx","krua","udhjcv", "lgtmhp"])
syu = Factor("syu", ["uvrmg","qsry","ipkb", "bdcn"])

### EXPERIMENT
constraints=[AtMostKInARow(2,(sjrkg,"hez")),ExactlyK(4,(lekrjk,"agaw")),MinimumTrials(48)]
design=[sjrkg,lekrjk,sezqdj,tsgpzz,syu]
crossing=[tsgpzz,syu]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2"))
### END