from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
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
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_3_0_0.csv"))
nr_factors=3
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)