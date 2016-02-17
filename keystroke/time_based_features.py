'''
Module for Computing Time-based Features
----------------------------------------

Heuristic

1. read keystroke data with the metadata

2. preprocess data to subset only the keystroke obvservations that are
   associated with QuestionIDs.

3. group data by user

4. aggregate df from step 2 using the following functions:
   - function 1: handles the logic for grabbing time chunks per question
   - function 2: handles computing the aggregate features
'''

import pandas as pd
import numpy as np
from argparse import ArgumentParser


def GRLC(values):
    '''
    Calculate Gini index, Gini coefficient, Robin Hood index, and points of
    Lorenz curve based on the instructions given in:

    www.peterrosenmai.com/lorenz-curve-graphing-tool-and-gini-coefficient-calculator

    Lorenz curve values as given as lists of x & y points [[x1, x2], [y1, y2]]

    @param values: List of values
    @return: [Gini index, Gini coefficient, Robin Hood index, [Lorenz curve]]
    '''
    n = len(values)
    assert(n > 0), 'Empty list of values'
    sortedValues = sorted(values)  # Sort smallest to largest

    # Find cumulative totals
    cumm = [0]
    for i in range(n):
        cumm.append(sum(sortedValues[0:(i + 1)]))

    # Calculate Lorenz points
    LorenzPoints = [[], []]
    sumYs = 0           # Some of all y values
    robinHoodIdx = -1   # Robin Hood index max(x_i, y_i)
    for i in range(1, n + 2):
        x = 100.0 * (i - 1)/n
        y = 100.0 * (cumm[i - 1]/float(cumm[n]))
        LorenzPoints[0].append(x)
        LorenzPoints[1].append(y)
        sumYs += y
        maxX_Y = x - y
        if maxX_Y > robinHoodIdx:
            robinHoodIdx = maxX_Y
    giniIdx = 100 + (100 - 2 * sumYs)/n  # Gini index

    return [giniIdx, giniIdx/100, robinHoodIdx, LorenzPoints]


def compute_time_chunks(df):
    time_dict = {}
    previous_question = df['QuestionID'].iloc[0]
    min_timestamp = df['KeyStrokeTimeStamp'].iloc[0]
    time_dict[previous_question] = []
    length = df.shape[0] - 1

    # import ipdb; ipdb.set_trace()

    for i, row in df.iterrows():
        current_question = row['QuestionID']
        current_timestamp = row['KeyStrokeTimeStamp']

        # skip first row
        if i == 0:
            continue

        if (previous_question != current_question) or \
           (i == length and previous_question == current_question):

            time_dict[previous_question].append(
                current_timestamp - min_timestamp)
            # reinitialize values based on new question
            min_timestamp = current_timestamp
            previous_question = current_question
            if previous_question not in time_dict:
                time_dict[previous_question] = []

    return time_dict


def compute_time_stats(group_by_column, id_value, time_chunks_dict):
    '''
    This function outputs a dataframe with features (single row) associated
    with time spent on questions. Individual and aggregate features are
    outputed. A single row is outputed, with column group_by_column included.

    Inputs:
    - df: data frame input to calculate statistics on
    - group_by_column: name of column in df to subset on
    - id_value: ID to subset on
    - time_chunks_dict: output of compute_time_chunks

    Output
    - a dataframe with a single row representing features for one observation
    '''

    # compute time spent per question and number of times question revisited
    time_per_q = {}
    visits_per_q = {}
    for key in time_chunks_dict.keys():
        time_per_q[key] = sum(time_chunks_dict[key])
        visits_per_q[key] = len(time_chunks_dict[key])

    row = pd.Series({group_by_column: id_value})

    # aggregate features relating to visits
    row['agg_total_qs_answered'] = len(visits_per_q)
    row['agg_attempt_total'] = sum([visits_per_q[k] for k in visits_per_q])
    row['agg_attempt_max'] = max([visits_per_q[k] for k in visits_per_q])
    row['agg_attempt_std'] = np.std([visits_per_q[k] for k in visits_per_q])
    row['agg_attempt_mean'] = np.mean([visits_per_q[k] for k in visits_per_q])
    row['agg_attempt_gini'] = GRLC([visits_per_q[k] for k in visits_per_q])[1]

    # aggregate features relating to time spent per question
    row['agg_time_total'] = sum([time_per_q[k] for k in time_per_q])
    row['agg_time_min'] = min([time_per_q[k] for k in time_per_q])
    row['agg_time_max'] = max([time_per_q[k] for k in time_per_q])
    row['agg_time_std'] = np.std([time_per_q[k] for k in time_per_q])
    row['agg_time_mean'] = np.mean([time_per_q[k] for k in time_per_q])
    row['agg_time_gini'] = GRLC([time_per_q[k] for k in time_per_q])[1]
    row['agg_time_median'] = np.median([time_per_q[k] for k in time_per_q])

    # question applicant spent most/least time on (aggregate metric)
    row['agg_q_w_max_time'] = max(time_per_q, key=time_per_q.get)
    row['agg_q_w_min_time'] = min(time_per_q, key=time_per_q.get)

    return row.to_frame().transpose()


def compute_time_features_agg(df, group_by_column):
    '''
    This wraps around function 1, 2, and 3 to return a dataframe for
    aggregating time-based features across all users.

    Input: User Grouped Dataframe
    Output: Dataframe with time-based features
    '''
    id_value = df[group_by_column].iloc[0]
    time_chunks = compute_time_chunks(df)
    stats = compute_time_stats(group_by_column, id_value, time_chunks)
    return stats


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-i', help='input filepath')
    parser.add_argument('-o', help='output filepath')
    args = parser.parse_args()

    df = pd.read_csv(args.i, index_col=False)

    # Preprocessing
    df = df[df['QuestionID'].notnull()]
    df.loc[:, 'UserID'] = df['UserID'].astype(str)
    df.loc[:, 'QuestionID'] = df['QuestionID'].apply(lambda x: str(int(x)))

    # Groupby
    group_col = 'UserID'
    users = df.groupby(group_col)

    agg_df = users.apply(
        lambda g: compute_time_features_agg(g, group_col))

    agg_df.reset_index(drop=True).to_csv(args.o, index=False)
