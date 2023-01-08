from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vlzwOE4I=Factor("6SZW%qT Tzg",['xgUOpw','0Qom','iLHXiPoR',"JIxzytPjOqTuY","iYawESJhzUK",'wRSUcfICrWF',"LXAuu"])
AtXEUTZ=":qMBD"
ZUh6LY5eF=['ALVwPwmclY','QlKBf3$oQINl','PYvSbPnmN',AtXEUTZ,Level('w@FL',3),'gIoZ*dLozIZz','>vttJxPu)U',"fOmq"]
DLDa0jauV=Factor("dq!a9NaZ",ZUh6LY5eF)
AYElMPIv=["mx]<JLXwSr qi",'gNvQbD#yn',Level('F5PyCazprMncUr',1),"coIO vpDL",'JI<<bOrXx']
esBjPvZN=Factor('rWXFXyC',[Level("bvX_DNsdXVQF",4),"ZnpkjBJFFz Ae","b9MuBKmKOoB",AYElMPIv[2],'px5bt','M6OodBmiuMWg#R','yxB',"lND6}erUYKmK1"])
lsMJ76E=Factor('K7JkN6xowZko',['MiH','UkjGLPmv',"FGxdx]yZRV6qUf",'Nz0wrmt','hDAU>hBT42njB<',"cRsglN[*G",'rhja8T[?QD'])

### EXPERIMENT
design=[vlzwOE4I,DLDa0jauV,esBjPvZN,lsMJ76E]
crossing=[vlzwOE4I,DLDa0jauV,esBjPvZN,lsMJ76E]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_4_1"))
### END