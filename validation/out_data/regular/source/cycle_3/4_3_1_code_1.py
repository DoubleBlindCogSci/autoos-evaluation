from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
znID=['guNcQia',Level("LCtiqhYJV",4),'RZKSouN&WZRt',"_EVgwS~BlrZ7p"]
qUNIUnsCPv=Factor(";ng",znID)
n0VCxbyyVmL=["~ujp*e","sczrjY$",")vAWn","zk}"]
mgEBdJLjSKd=Factor('cyX4srlXM_E',n0VCxbyyVmL)
oOp234=Factor("~Yw;u]PnGNb",['aOgLJ IhKxK','SThkrc',Level('ivYEax @Lnd{O6',3),"OcU>MhhCK4lod"])

### EXPERIMENT
design=[qUNIUnsCPv,mgEBdJLjSKd,oOp234]
crossing=[qUNIUnsCPv,mgEBdJLjSKd,oOp234]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_3_1"))
### END