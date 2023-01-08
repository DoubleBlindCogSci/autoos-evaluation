from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tievdi = Factor("tievdi", ["moo","wibvn","quqn","jkca","yifqp"])
def is_xbxua_qqfhbo(tievdi):
    return tievdi != "yifqp" or tievdi == "jkca"
def is_xbxua_wltdj(tievdi):
    return not is_xbxua_qqfhbo(tievdi)
xbxua = Factor("xbxua", [DerivedLevel("qqfhbo", WithinTrial(is_xbxua_qqfhbo, [tievdi])), DerivedLevel("wltdj", WithinTrial(is_xbxua_wltdj, [tievdi]))])

design=[tievdi,xbxua]
crossing=[xbxua]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END