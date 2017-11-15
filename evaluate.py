#!/usr/bin/python3
import subprocess
import glob

def evaluate(path):
    output = subprocess.getoutput('./run.sh < ' + path + ' > /tmp/output && ./bin/score_evaluator ' + path + ' /tmp/output')
    _, score, max_score = output.split()
    score = int(score[:-1])
    max_score = int(max_score)
    return (score, max_score)

scores0 = [evaluate(p) for p in glob.glob("./input/0/*")]
scores1 = [evaluate(p) for p in glob.glob("./input/1/*")]
scores = scores0 + scores1

total_score = sum(x[0] for x in scores)
total_max_score = sum(x[1] for x in scores)

for score, max_score in scores:
    print('{} {} {:.2f}%'.format(
        score,
        max_score,
        score/max_score * 100.0
        ))

print('{} {} {:.2f}%'.format(
    total_score,
    total_max_score,
    total_score/total_max_score * 100.0
    ))
