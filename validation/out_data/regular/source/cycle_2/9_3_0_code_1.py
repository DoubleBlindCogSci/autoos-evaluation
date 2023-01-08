from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
J675=['dCHIfB5IQmWo','epyeXa',"RDh$Prl",Level("gH|iRf",9),'vFVSSFIAzt',"5gUmG acaXL",Level("Nrvr",1)]
TDvEn=Factor("vTJkanPU",['VDs','MFD6j3?EYi6NFh','w!zPTtyn%co',J675[3],"soJNzQ","qdeggDx:&QBIR",'$DqZ',Level('bvbIM',6),Level('im_REOCUXNxC',4),'FcNn'])
VhETNNEQww=Factor("}XW)EkRXPUsH7E",[Level("yb@2Il:MSwMzm",7),"ze(x&ObX",'YM%j6wJBxNu',"Ll@FKdGT6bDX",Level("bmap",3),'TMaZm@GCy',"du%8kP?YfvAkG",'hsmp5qaZxq',Level("mzX",3)])
_LueMcPl=Level("yQ&Pf8jMZRbfM",9)
oQb3pt=Factor("utDl#",[Level("WHfo_WErI",4),'BsKTj!GBwvsNP',"d<C]",'h5eFN_a','fP#XIA~eQf[ulf','IJjFXxlODf',_LueMcPl,Level("pZ$mJS",1),'hcm(nSeI;A',"TNw2dblAjLMWtD"])

### EXPERIMENT
design=[TDvEn,VhETNNEQww,oQb3pt]
crossing=[TDvEn,VhETNNEQww,oQb3pt]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_3_0"))
### END