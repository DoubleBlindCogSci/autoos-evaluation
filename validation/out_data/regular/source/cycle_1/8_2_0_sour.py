from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
BxSpz=Factor('a1YxQGIoReR',[Level("kvW",7),'zYyMn5xpaCfo','OZTmyGNq','OTWjDg?Vqfm','*DzOIF:Hcp','ZMhHl:CEAooQ',Level("g:Vj#",8),"t^G@Ab[oMmpg4N"])
wZde=Factor('ooFs2z[qRGGH',["LjtFANUgqC2",Level('QSVsHULW',5),'UrVX'," g:6q",'ml|U[Vj9O',"gOcJjayZD) ",'OpmTm',"cfmcydLcF*jK"])

### EXPERIMENT
design=[BxSpz,wZde]
crossing=[BxSpz,wZde]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/8_2_0_0.csv"))
nr_factors=2
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/8_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)