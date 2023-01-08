from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
fphzla = Factor("fphzla", ["rmvin","vajjy","yzvo","fuaiq","uvnpv","xaboy","mwaro"])
def zcfkos(fphzla):
    return fphzla == "yzvo"
def cya(fphzla):
    return not zcfkos(fphzla)
hfdi = Factor("hehzh", [DerivedLevel("opdf", WithinTrial(zcfkos, [fphzla])), DerivedLevel("gxia", WithinTrial(cya, [fphzla]))])
### EXPERIMENT
design=[fphzla,hfdi]
crossing=[hfdi]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END