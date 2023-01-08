from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
FIwmlKbfbAp=['XNLjOyjDRJAlH',"DvKn8NIPWC","toWjGUON}SA@","^yS9fxXxesRw","Gd_WPJCWe!twW<","Z*YVlzmiVSqF9D",'R}{vy',"DqRjBdcAJwGq"]
fbOxAnkM=Factor("Wf@ql4o",["wggb",'Nvevg',FIwmlKbfbAp[3],'tnGXEIJ','x IdUyP;',"VTMVGMAolJVqE",'KKkC '])
OMqWJr=Factor("%bFav K&4H1MiP",[" JRfI",'UqnilJRjDc','v?WDCWNTMERzw',Level("okGvZByZyhG",1),'%JE(XnI','U7K1jEVBQANvFY'])
KtAb=['ORT<ZWaI@AP',"IVxM5B",'psBa',"hSOz{(IvCht?8",'FeaZkM',Level("yOQQ",3)]
mi2tdr=Factor("Qke_JgQ]upW",KtAb)

### EXPERIMENT
design=[fbOxAnkM,OMqWJr,mi2tdr]
crossing=[fbOxAnkM,OMqWJr,mi2tdr]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_3_0"))
### END