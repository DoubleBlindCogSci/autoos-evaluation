from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
OFScI=Factor("RDSEpr",["ZggI nf5aThntc","WziuObriIO",'ERd',"yl]DPGD","OfC4J","HWY8sY",'QWgAs',"oVtwy Nc[ ","AsKvEGHInx&B"])
ZFfZSAcb="IuHlLOFjeZD"
H6iLwMvVmFQ=Factor('[gbiy',[Level("jYyh&",2),ZFfZSAcb,'Edl',"E]lWG","Y5qkZW","!COqemf","$9DApcQO",'&yixbxzcOsE',"TSwfa",Level('(SQ?a 8LfVWO',4)])
Zsv1=Factor('X@pX',['pUWSzeHp','TFWMACuTiC4',"ntfVIgRC",'sSFM','LFk7B_e',"PExu",Level('uO1gGGkvBhMNqo',4),'GPUN?4u',"EcUgZTJV"])
_wR9A6=Factor("65E",["uPjIFDWiqNdeX",'rUrpr01Sv:',"UelMQN",'1QBt9HRsifg',Level('mjxEhahdbIQg',1),"PT$pn2JDit","RFnByR^YB","3d!",'uVTSouO7N'])

### EXPERIMENT
design=[OFScI,H6iLwMvVmFQ,Zsv1,_wR9A6]
crossing=[OFScI,H6iLwMvVmFQ,Zsv1,_wR9A6]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_4_0_0.csv"))
nr_factors=4
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_4_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)