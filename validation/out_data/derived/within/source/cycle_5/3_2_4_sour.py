from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
khj = Factor("khj", ["sbdypg","ffis","xxdzsu","kld","jdnxcs","dkifp","nomvgm"])
cswp = Factor("cswp", ["lykrd","ydd","rwpe","yjq","bwb","ufplv","ipxply","dni"])
def hysud(khj, cswp):
     return "dkifp" == khj
def sfu(khj, cswp):
     return khj != "dkifp" and  cswp == "lykrd"
def pcro(khj, cswp):
     return (khj != "dkifp") and (not cswp == "lykrd")
mkzleo = Factor("ini", [DerivedLevel("vsbs", WithinTrial(hysud, [khj, cswp])), DerivedLevel("tvonnc", WithinTrial(sfu, [khj, cswp])),DerivedLevel("pguwt", WithinTrial(pcro, [khj, cswp]))])
### EXPERIMENT
design=[khj,cswp,mkzleo]
crossing=[mkzleo]
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