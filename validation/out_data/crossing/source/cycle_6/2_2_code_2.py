from sweetpea import *
import os
_dir=os.path.dirname(__file__)
ymg = Factor("ymg", ["ukf", "yydyig"])
ipyed = Factor("ipyed", ["zeylg", "pywjvq"])
ttc = Factor("ttc", ["tjg", "oih"])
tirl = Factor("tirl", ["bwxhf", "qodosl"])
mhvvxa = Factor("mhvvxa", ["sdyc", "twesgh"])
zqvzs = Factor("zqvzs", ["ime", "gtvapc"])
lys = Factor("lys", ["fab", "qlel"])
constraints = []
crossing = [[ymg, ipyed, ttc], [tirl, mhvvxa, zqvzs, lys]]


design=[ymg,ipyed,ttc,tirl,mhvvxa,zqvzs,lys]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2"))

### END