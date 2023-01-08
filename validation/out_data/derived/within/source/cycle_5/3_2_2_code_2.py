from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zlm = Factor("zlm", ["zsj","ppg","wmzkcc","rfzzdx","ckmar","tmvzzn","isjyzz","fmu"])
enchxy = Factor("enchxy", ["iyhq","eqdxln","pqrqji","blu","pjccrq","dfejzk","kgz"])
def is_qkc_dok(zlm, enchxy):
    return zlm == "ppg"
def is_qkc_uyctch(zlm, enchxy):
    return zlm != "ppg" and enchxy == "iyhq"
def is_qkc_ypuao(zlm, enchxy):
    return not (is_qkc_dok(zlm) or is_qkc_uyctch(zlm, enchxy))
qkc = Factor("qkc", [DerivedLevel("dok", WithinTrial(is_qkc_dok, [zlm])), DerivedLevel("uyctch", WithinTrial(is_qkc_uyctch, [zlm, enchxy])), DerivedLevel("ypuao", WithinTrial(is_qkc_ypuao, [zlm, enchxy]))])

design=[zlm,enchxy,qkc]
crossing=[qkc]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_2"))

### END