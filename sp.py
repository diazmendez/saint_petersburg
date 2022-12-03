from random import random
import numpy as np
import pandas as pd

'''
def create_trials_sequence(length):
    sequence = []
    for _ in range(length):
        n=1
        while random()>0.5:
            n+=1
        sequence.append(n)
    return(np.array(sequence))
    
def outcomes(bid, min_N_for_average):
'''

def sp_trial():
    n=1
    while random()>0.5:
        n+=1
    return(n, 2**(n-1))

def sp_session(trials, bids):
    sequence_gains = 0
    for i in range(trials):
        n, trial_outcome = sp_trial()
        sequence_gains += trial_outcome
    gains = sequence_gains - (trials * bids)
    return (gains)

def estimation(trials_set=np.logspace(1,3,num=3), bids=np.array(list(range(1,11))), runs=10000):
    columns=['trials','bid','s_rate','gains_m','gains_std','losses_m','losses_std']
    df = pd.DataFrame(columns=columns)
    for trials in trials_set:
        final_outcomes=np.transpose(np.array([sp_session(int(trials),bids) for _ in range(runs)]))
        for i, bid in enumerate(bids):
            out = final_outcomes[i]
            wins = out[out>=0]
            losses = out[out<0]
            success_rate = round(len(wins)/len(out), 2)
            wins_mean = round(np.mean(wins), 2) if any(wins) else 0
            wins_std = round(np.std(wins), 2) if any(wins) else 0
            losses_mean = round(np.mean(losses), 2) if any(losses) else 0
            losses_std = round(np.std(losses), 2) if any(losses) else 0
            df_add = pd.DataFrame([[int(trials),bid,success_rate,wins_mean,wins_std,
                                                            losses_mean,losses_std]],columns=columns)
            #print(f'{int(trials)}\t{bid}\t{success_rate}\t{wins_mean}\t{wins_std}\t{losses_mean}\t{losses_std}')
            df = pd.concat([df,df_add], ignore_index=True)
    return(df)

if __name__ == '__main__':
    runs = 100000
    max_bid = 16
    df = estimation(trials_set=np.logspace(1,3,num=3), bids=np.array(list(range(1,max_bid))), runs=runs)

