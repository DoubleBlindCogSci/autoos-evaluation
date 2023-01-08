from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
mjsmfy = Factor("mjsmfy", ["zpc","lehda","nrfcn","hfb","hkva","hdzaoo"])
uubtu = Factor("uubtu", ["zpc","lehda","nrfcn","hfb","hkva","hdzaoo"])
jqdmb = Factor("jqdmb", ["zpc","lehda","nrfcn","hfb","hkva","hdzaoo"])
def jgw(mjsmfy, jqdmb, uubtu):
     return jqdmb[-1] == mjsmfy[-2]
def osjtug(mjsmfy, jqdmb, uubtu):
     return jqdmb[-1] != mjsmfy[-2] and mjsmfy[-1] == uubtu[-2]
def rqtw(mjsmfy, jqdmb, uubtu):
     return (not mjsmfy[-2] == jqdmb[-1]) and (mjsmfy[-1] != uubtu[-2])
bdq = Factor("lxcta", [DerivedLevel("wql", Window(jgw, [mjsmfy, uubtu, jqdmb],3)), DerivedLevel("byxd", Window(osjtug, [mjsmfy, uubtu, jqdmb],3)),DerivedLevel("rnzv", Window(rqtw, [mjsmfy, uubtu, jqdmb],3))])
### EXPERIMENT
design=[mjsmfy,uubtu,jqdmb,bdq]
crossing=[bdq]
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
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)