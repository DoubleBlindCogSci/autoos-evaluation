from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cZ96y2=Factor('hHhjIT#Skj)Vr',[Level("eL9{mhG8C{Zt",5),'WPzItkve@!rEe','zaKrmGLbEGmzR'])
oioDbqbFCmV=Factor('kxY!r8',[']&UFD3tuiyS','tGYmNS','zClDUXWfp'])
yHirkFY=Factor("t6vd;",["aPFyndMROE","TLzzbnYIIY",'DJXE&dfMaYT'])

### EXPERIMENT
design=[cZ96y2,oioDbqbFCmV,yHirkFY]
crossing=[cZ96y2,oioDbqbFCmV,yHirkFY]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/3_3_1_0.csv"))
nr_factors=3
nr_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/3_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)