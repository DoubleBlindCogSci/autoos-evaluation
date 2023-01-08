from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
XNDPvbMGi='cW{Ilk~y~POT'
thtynil6=['WZpwSCHq','ImrE]lduw{Qksl',"$e&Q",'PNeqBHUqsIG','Q<o',XNDPvbMGi,'lH;EzXs',Level('nnIiGKcue',3),'vXOuPJKKz']
hT362k=Factor('cqM',thtynil6)
UyuPUlN4='i<vBBQxdFIr'
MUTWfc4l=Factor('cyANfIZJpQOgh$',[Level('?VIecNgjZ!>',2),'DRD',Level("epr@z:NXTgrVVw",3),'iZiVT','6#mpkRrIqrf',UyuPUlN4,"UnCC>jMoA","OqnmMYNff>U","eQ1|T{I^"])
v_GdC7U=["JHWoN",'rFMlkftlF','wG YzNeGxuJvE',"ID?se7vmMz",'SVJgykI',"5PrE?z jT",'Oh<DPIgw',"JBGdUQ8LX"]
ggbxk=Factor("Dkk{DvU^",v_GdC7U)

### EXPERIMENT
design=[hT362k,MUTWfc4l,ggbxk]
crossing=[hT362k,MUTWfc4l,ggbxk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_3_1"))
### END