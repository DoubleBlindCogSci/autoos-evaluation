from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mrajg = Factor("mrajg", ["mfbp","iyoym","igq","liuw","expsg","btfs","jzclr"])
gvlcit = Factor("gvlcit", ["mfbp","iyoym","igq","liuw","expsg","btfs","jzclr"])
obi = Factor("obi", ["mfbp","iyoym","igq","liuw","expsg","btfs","jzclr"])
def yylf(mrajg, gvlcit, obi):
     return mrajg == gvlcit
def wrayup(mrajg, gvlcit, obi):
     return gvlcit != mrajg and obi == mrajg
def pngugw(mrajg, gvlcit, obi):
     return (mrajg != gvlcit) and (not wrayup(mrajg, gvlcit, obi))
sqcmon = Factor("bjc", [DerivedLevel("ggf", WithinTrial(yylf, [mrajg, gvlcit, obi])), DerivedLevel("jwysy", WithinTrial(wrayup, [mrajg, gvlcit, obi])),DerivedLevel("mdpjmz", WithinTrial(pngugw, [mrajg, gvlcit, obi]))])
### EXPERIMENT
design=[mrajg,gvlcit,obi,sqcmon]
crossing=[sqcmon]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)