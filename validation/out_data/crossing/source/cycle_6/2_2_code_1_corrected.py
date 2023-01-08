from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ymg = Factor("ymg", ["ukf", "yydyig"])
ipyed = Factor("ipyed", ["zeylg", "pywjvq"])
ttc = Factor("ttc", ["tjg", "oih"])
tirl = Factor("tirl", ["bwxhf", "qodosl"])
mhvvxa = Factor("mhvvxa", ["sdyc", "twesgh"])
zqvzs = Factor("zqvzs", ["ime", "gtvapc"])
lys = Factor("lys", ["fab", "qlel"])

### EXPERIMENT
design=[ymg,ipyed,ttc,tirl,mhvvxa,zqvzs,lys]
crossing = [[tirl,mhvvxa,zqvzs,lys],[ymg,ipyed,ttc],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1,IterateGen)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2"))
### END
