from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nvfINal2bE=Factor("IIAvEBEBnZqhA",["yNQKZrsUXCMb4h",'<MS9A',"bu5}iwBG)mu"])
lTwRq8wYj=[Level("HK4LftZdK",1),'@BZZomKQ','CDAjJy|veKYfMF']
cRHB=Factor('dCU%3hdNP>W?#x',lTwRq8wYj)
XZ9VWQnu=Factor("oeAtWT",[Level("ntz",10),Level('Ptbb',8),Level("8Ml",8)])

### EXPERIMENT
design=[nvfINal2bE,cRHB,XZ9VWQnu]
crossing=[nvfINal2bE,cRHB,XZ9VWQnu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/3_3_0"))
### END