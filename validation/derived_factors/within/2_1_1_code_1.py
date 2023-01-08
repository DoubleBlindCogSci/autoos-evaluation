from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
tievdi = Factor("tievdi", ["moo","wibvn","quqn","jkca","yifqp"])
def pwln(tievdi):
    return tievdi != "yifqp" or tievdi == "jkca"
def ivtm(tievdi):
    return not pwln(tievdi)
igwwsj = Factor("xbxua", [DerivedLevel("qqfhbo", WithinTrial(pwln, [tievdi])), DerivedLevel("wltdj", WithinTrial(ivtm, [tievdi]))])
### EXPERIMENT
design=[tievdi,igwwsj]
crossing=[igwwsj]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END