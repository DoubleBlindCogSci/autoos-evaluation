from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wCitXyGU=Factor('gEA',[Level('GFaS0QA%gdsbWv',4),">UlJw","KL;yCKXPWgC?",Level("hecoSTDmd] VO",2),"RDmXG%O",'xIKE>heId','TWY(','exmdZoQ','uwGfZW;9r?Ko'])
yoap1Pl=Factor("(XOHTPtuI<du",[Level("PvDxbWU%URnODy",3),'hTVnnhiugkZ_EX','iyybcjPOq',"Szic!_A[bjvjs","rgaqZS","QZZVtoeXgyainT","RgZ_jAzDX",'WHYEWymX',"_ALziiuF"])

### EXPERIMENT
design=[wCitXyGU,yoap1Pl]
crossing=[wCitXyGU,yoap1Pl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_2_1"))
### END