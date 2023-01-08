from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
onfbo = Factor("onfbo", ["nbqy","hluxjt","bgvex","kmcxj","oij","foyoxc","dyc"])
nbq = Factor("nbq", ["nbqy","hluxjt","bgvex","kmcxj","oij","foyoxc","dyc"])
rim = Factor("rim", ["nbqy","hluxjt","bgvex","kmcxj","oij","foyoxc","dyc"])
def suofw(onfbo, nbq, rim):
     return onfbo[-3] == nbq[-2] and onfbo[-2] != rim[-3]
def xfcew(onfbo, nbq, rim):
     return nbq[-2] != onfbo[-3] and onfbo[-2] == rim[-3]
def fgvx(onfbo, nbq, rim):
     return (not suofw(onfbo, nbq, rim)) and (not xfcew(onfbo, nbq, rim))
zdw = Factor("zfdgl", [DerivedLevel("chq", Window(suofw, [onfbo, nbq, rim],4)), DerivedLevel("zfnpyb", Window(xfcew, [onfbo, nbq, rim],4)),DerivedLevel("foaw", Window(fgvx, [onfbo, nbq, rim],4))])
### EXPERIMENT
design=[onfbo,nbq,rim,zdw]
crossing=[zdw]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)