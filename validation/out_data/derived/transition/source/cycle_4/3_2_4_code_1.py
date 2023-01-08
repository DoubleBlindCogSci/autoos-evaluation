from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
swxrom = Factor("swxrom", ["indmsy","yrf","cwqp","ziaw","vhjh","irj","mdfvvh","cirqwl"])
hfo = Factor("hfo", ["rmn","jusbu","fyc","qcqre","uukbjl","akcut"])
def vld(swxrom, hfo):
     return "cwqp" == swxrom[-1] and not hfo[0] == "uukbjl"
def pedq(swxrom, hfo):
     return swxrom[-1] != "cwqp" and hfo[0] == "uukbjl"
def slvout(swxrom, hfo):
     return (not vld(swxrom, hfo)) and (not hfo[0] == "uukbjl")
aufk = Factor("ybt", [DerivedLevel("asygc", Transition(vld, [swxrom, hfo])), DerivedLevel("cgb", Transition(pedq, [swxrom, hfo])),DerivedLevel("chx", Transition(slvout, [swxrom, hfo]))])
### EXPERIMENT
design=[swxrom,hfo,aufk]
crossing=[aufk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END