from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
GltTj47f0=["YzORK#Ylmpt",Level("kuO",7),Level("OaeQ!<GD2Hy",8),'PpMgMBMfTS','0ZwYyryh:Q6n']
mfAl5NlQ8=Factor("ZjRrH?",GltTj47f0)
b7BOq=Factor("Ql9PKY",[Level("QcmrORhdIb",6),Level(";#Gd",3),"GaTNPTp",'Nv#L^cxIB',"iXeRZYLa"])
NYucU=['pAf','Zc rtq;rscX',Level('lbhA&_(&Mz[',8),'zZTBiFQm',Level("pUwc",4)]
vtouic=Factor("VWCMH?L",NYucU)

### EXPERIMENT
design=[mfAl5NlQ8,b7BOq,vtouic]
crossing=[mfAl5NlQ8,b7BOq,vtouic]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_3_1"))
### END