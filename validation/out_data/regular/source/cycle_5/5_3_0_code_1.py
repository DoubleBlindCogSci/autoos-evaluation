from sweetpea import *
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
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_3_0"))
### END