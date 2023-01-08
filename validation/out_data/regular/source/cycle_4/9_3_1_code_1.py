from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ysJFTNQaiMP=Factor('qcAJmQDvCchZy',["oBb?PyBrQwz","YzVWSjq6LBaQ","FwqmKR6UlJ","YDFmv",'Cvzw F$[N^',">nRhVopm:V",'TCwsYOzc',"1bubPsYDrU","gC}zo("])
csMYxj=["Eho3Pc","fuHMjSx",'46:*JDvXtK',"jx__z$RlCJH{w",'Jxxd<abHW','JnB(8p']
NOdWdpG=Factor('w3biplTVb*3',['EnQLTyc1cIhZVR',"Gmw6NG]tuy",Level('AnHg8p;_ETEvI',3),"Q%jhzDfi",'dvFS FysnTvssH',csMYxj[1],Level("vqmam84?ywV",1),'Inkdkmy','C<Q&SVzkz','D[KG&E)$'])
it03uPXANH="AwKEEXQ"
InYXEu2ua=['GAaYNeC',"2BXkeLAoGbtxr!",'sVYs}',"HVw","AILkGi7TBMOn>L","{bQHUc]y","agN zv VPuTVQC",it03uPXANH,'FBaELRELNScp','SBc']
C34SCiRU=Factor("BAdA&N",InYXEu2ua)

### EXPERIMENT
design=[ysJFTNQaiMP,NOdWdpG,C34SCiRU]
crossing=[ysJFTNQaiMP,NOdWdpG,C34SCiRU]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_3_1"))
### END