from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
vpq = Factor("vpq", ["pgn","wuubg","ajwvvn","pntjpx","ozh","koznz","rhz"])
ovkmj = Factor("ovkmj", ["pgn","wuubg","ajwvvn","pntjpx","ozh","koznz","rhz"])
ezejn = Factor("ezejn", ["pgn","wuubg","ajwvvn","pntjpx","ozh","koznz","rhz"])
def vwa(vpq, ovkmj, ezejn):
    return vpq != ovkmj or vpq != ezejn
def sremcz(vpq, ovkmj, ezejn):
    return vpq == ovkmj and vpq == ezejn
fuwwh = DerivedLevel("rsja", WithinTrial(vwa, [vpq, ovkmj, ezejn]))
tbqvcc = DerivedLevel("zbfi", WithinTrial(sremcz, [vpq, ovkmj, ezejn]))
gvihfx = Factor("kdrz", [fuwwh, tbqvcc])

### EXPERIMENT
design=[vpq,ovkmj,ezejn,gvihfx]
crossing=[gvihfx]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0, "levels":False}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)