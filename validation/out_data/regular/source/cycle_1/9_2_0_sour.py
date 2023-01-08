from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bIwD='kKQBbMoDy'
gGW1N=Factor("3yQfAn",['XX4',"wyf","2pcKqE! FL7e","OEnwYLpU",Level('Kip>;x',1),'PkY',bIwD,Level("RYyUHBNdcrYra",10),Level('adPD7VChaem',7),"RWthALArH1"])
nvfEcQK=Factor("dqmk7",[Level('RQZ5[aV!N9btRm',2),'%NcL','n]3Uq<AeizKA','wY)ph','ugu',"xkeXsnDX","xxRs$f[","uDPJZY{$knh9",Level("lt8",2)])

### EXPERIMENT
design=[gGW1N,nvfEcQK]
crossing=[gGW1N,nvfEcQK]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/9_2_0_0.csv"))
nr_factors=2
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/9_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)