from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zlm = Factor("zlm", ["zsj","ppg","wmzkcc","rfzzdx","ckmar","tmvzzn","isjyzz","fmu"])
enchxy = Factor("enchxy", ["iyhq","eqdxln","pqrqji","blu","pjccrq","dfejzk","kgz"])
def oexpc(zlm, enchxy):
     return "ppg" == zlm
def dgthhw(zlm, enchxy):
     return zlm != "ppg" and  enchxy == "iyhq"
def qpufhh(zlm, enchxy):
     return (not oexpc(zlm, enchxy)) and (enchxy != "iyhq")
gllguo = Factor("qkc", [DerivedLevel("dok", WithinTrial(oexpc, [zlm, enchxy])), DerivedLevel("uyctch", WithinTrial(dgthhw, [zlm, enchxy])),DerivedLevel("ypuao", WithinTrial(qpufhh, [zlm, enchxy]))])
### EXPERIMENT
design=[zlm,enchxy,gllguo]
crossing=[gllguo]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END