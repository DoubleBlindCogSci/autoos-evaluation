from sweetpea import *
import os
_dir=os.path.dirname(__file__)
cuifi = Factor("cuifi", ["xmyzsu", "nlhh"])
miyu = Factor("miyu", ["zshea", "wdht"])
alkgs = Factor("alkgs", ["uia", "ndxara"])
ucn = Factor("ucn", ["vweh", "wuutz"])
ped = Factor("ped", ["ycsmkq", "uoqst"])
fxkg = Factor("fxkg", ["nunbpb", "nyvhp"])
sray = Factor("sray", ["vgvvo", "uuux"])
almiim = Factor("almiim", ["ybcgog", "quj"])
constraints = []
crossing = [[cuifi, miyu, alkgs], [ucn, ped, fxkg], [sray, almiim]]


design=[cuifi,miyu,alkgs,ucn,ped,fxkg,sray,almiim]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_4"))

### END