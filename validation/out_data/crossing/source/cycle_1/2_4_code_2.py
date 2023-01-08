from sweetpea import *
import os
_dir=os.path.dirname(__file__)
cvkizt = Factor("cvkizt", ["iyqtzz", "hikyaj"])
urm = Factor("urm", ["txrldj", "utm"])
stxg = Factor("stxg", ["rve", "mgz"])
wihk = Factor("wihk", ["vuxf", "rhm"])
rlxyvh = Factor("rlxyvh", ["wwpsc", "tszd"])
kpezd = Factor("kpezd", ["klyk", "bqc"])
knb = Factor("knb", ["opm", "lynvhh"])
constraints = []
crossing = [[cvkizt, urm, stxg], [wihk, rlxyvh, kpezd, knb]]


design=[cvkizt,urm,stxg,wihk,rlxyvh,kpezd,knb]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_4"))

### END