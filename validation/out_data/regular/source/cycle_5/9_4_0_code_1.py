from sweetpea import *
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
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_4_0"))
### END