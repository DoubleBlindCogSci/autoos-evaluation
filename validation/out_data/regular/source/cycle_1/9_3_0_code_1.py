from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
gMyTf=Factor('_HAzv',["gr&GSlM",'9xdOnDHGXf','UNOTTFk)AFMq0',"U1*mng J","BZysJvDInew",'FSHhEAThvq4','{{BS',"FtPqFz","AdpSV|TDjYLoN"])
qykWnECF=Factor("RabtMGmqX",[Level("ZgGspLf nfkGor",9),"*FChWzjw",'L}d',"QhJJMKxIbjFcEk",Level('uWf;kYbym#JIk',4),'CGC',"Mvd",Level('kMHQP',3),Level("{u3K EaIG",3)])
PPgDXh=Factor("LFsvlDVeGo$",["DSVIcFpZBQZ","utGw",Level("EZWxy>hD6h",3),'uzZQFDKw]WIe','OxkwKnHt?','rW>S&p','Y1TaFMKq tRA','bDJVif',Level('G7~sZf VBE$r',5)])

### EXPERIMENT
design=[gMyTf,qykWnECF,PPgDXh]
crossing=[gMyTf,qykWnECF,PPgDXh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/9_3_0"))
### END