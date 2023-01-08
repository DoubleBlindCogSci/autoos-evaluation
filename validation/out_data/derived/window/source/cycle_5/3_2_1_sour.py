from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xkvzol = Factor("xkvzol", ["bwhmes","hglfvm","vxs","oardm","nxd","rmhnb","kqozyw"])
xeyjrr = Factor("xeyjrr", ["bwhmes","hglfvm","vxs","oardm","nxd","rmhnb","kqozyw"])
fdwq = Factor("fdwq", ["bwhmes","hglfvm","vxs","oardm","nxd","rmhnb","kqozyw"])
def ljwnh(xkvzol, xeyjrr, fdwq):
     return xkvzol[-2] == xeyjrr[-1] and xkvzol[-1] != fdwq[-2]
def qeyvjo(xkvzol, xeyjrr, fdwq):
     return xeyjrr[-1] != xkvzol[-2] and xkvzol[-1] == fdwq[-2]
def dmvw(xkvzol, xeyjrr, fdwq):
     return (not xkvzol[-2] == xeyjrr[-1]) and (not qeyvjo(xkvzol, xeyjrr, fdwq))
bzndc = Factor("rwnqf", [DerivedLevel("cwkz", Window(ljwnh, [xkvzol, xeyjrr, fdwq],3)), DerivedLevel("uvpjb", Window(qeyvjo, [xkvzol, xeyjrr, fdwq],3)),DerivedLevel("ihyhas", Window(dmvw, [xkvzol, xeyjrr, fdwq],3))])
### EXPERIMENT
design=[xkvzol,xeyjrr,fdwq,bzndc]
crossing=[bzndc]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)