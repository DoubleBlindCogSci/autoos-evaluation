from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
FIwmlKbfbAp=['XNLjOyjDRJAlH',"DvKn8NIPWC","toWjGUON}SA@","^yS9fxXxesRw","Gd_WPJCWe!twW<","Z*YVlzmiVSqF9D",'R}{vy',"DqRjBdcAJwGq"]
fbOxAnkM=Factor("Wf@ql4o",["wggb",'Nvevg',FIwmlKbfbAp[3],'tnGXEIJ','x IdUyP;',"VTMVGMAolJVqE",'KKkC '])
OMqWJr=Factor("%bFav K&4H1MiP",[" JRfI",'UqnilJRjDc','v?WDCWNTMERzw',Level("okGvZByZyhG",1),'%JE(XnI','U7K1jEVBQANvFY'])
KtAb=['ORT<ZWaI@AP',"IVxM5B",'psBa',"hSOz{(IvCht?8",'FeaZkM',Level("yOQQ",3)]
mi2tdr=Factor("Qke_JgQ]upW",KtAb)

### EXPERIMENT
design=[fbOxAnkM,OMqWJr,mi2tdr]
crossing=[fbOxAnkM,OMqWJr,mi2tdr]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_3_0_0.csv"))
nr_factors=3
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)