from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
EPg1E7Nuci=['NCxmd','PteBpv','nNg',"tpD^5R",'!A&']
er_H=Factor("acN",EPg1E7Nuci)
kzmviuON=["pA;b)<luxgDWs",'zVuz9K>H)rdwcB',"{7xhelWGHSNd!Y"]
Ji2sUYFWQw=["WXRcPM%MU5YSzC",'hKaRwnnoDeWXX',"hr?",'ioNKmC',"a{WDu4U8Pz(Xd",'1V*']
c6183=["mjLE",kzmviuON[0],'&RYMao','kpZnk',Ji2sUYFWQw[4],'TluwzyyoIavu',"ylYLeo"]
Q2zzUJCFG=Factor('qnqYg',c6183)
Pb8VCzLcUuO=Factor(";9YO?NIn",[Level("2KPeoV0NsF*AGf",4),'jpGSx',"XP1b","8a*WJXla)",'mctOo'])

### EXPERIMENT
design=[er_H,Q2zzUJCFG,Pb8VCzLcUuO]
crossing=[er_H,Q2zzUJCFG,Pb8VCzLcUuO]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_3_0_0.csv"))
nr_factors=3
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)