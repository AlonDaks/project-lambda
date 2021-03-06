from __future__ import print_function, division
import numpy as np
from scipy import stats
import itertools
import sys
from os.path import exists
import gc
from stat159lambda.config import REPO_HOME_PATH, NUM_VOXELS, SUBJECTS
from stat159lambda.utils import data_path as dp
import matplotlib.pyplot as plt

PERCENTILES = [0, 25, 50, 75, 90, 95, 99, 99.5, 100]


def get_pairwise_correlations():
    """
    Finds and returns the paths to the correlations of all possible pairs of
    subjects (if the paths exist)

    Parameters
    ----------
    None

    Returns
    -------
    paths : string array
    """
    subject_pairs = itertools.combinations(SUBJECTS, 2)
    return [np.load(dp.get_correlation_path(subj_a, subj_b))
            for subj_a, subj_b in subject_pairs]


def get_correlations(aggregation='pooled'):
    """
    Calculates correlations either using means or the pooled data, depending
    on specification

    Parameters
    ----------
    aggregation : string (optional)

    Returns
    -------
    correlations : array
    """
    correlations = np.concatenate(tuple(get_pairwise_correlations()))
    if aggregation == 'mean':
        correlations = get_pairwise_correlations()
        correlations = np.mean(np.matrix(correlations).T, axis=1)
        correlations = correlations[~np.isnan(correlations)]
        return np.squeeze(np.asarray(correlations))
    return correlations[~np.isnan(correlations)]


def save_correlation_histogram(aggregation):
    """
    Plots and saves the histogram of all correlations calculated by the
    specified aggregation into figures folder

    Parameters
    ----------
    aggregation : string

    Returns
    -------
    None
    """
    plt.hist(get_correlations(aggregation), bins=40)
    output_file_name = '{0}/figures/{1}_correlation_histogram.png'.format(
        REPO_HOME_PATH, aggregation)
    plt.savefig(output_file_name)
    print('Saved {0}'.format(output_file_name))
    plt.clf()


def save_correlation_percentiles(aggregation):
    """
    Calculates and saves the correlation percentiles calculated by the
    specified aggregation into figures folder

    Parameters
    ----------
    aggregation : string

    Returns
    -------
    None
    """
    correlations = get_correlations(aggregation)
    results = [[p, np.percentile(correlations, p)] for p in PERCENTILES]
    output_file_name = '{0}/figures/{1}_correlation_percentiles.txt'.format(
        REPO_HOME_PATH, aggregation)
    np.savetxt(output_file_name, results)
    print('Saved {0}'.format(output_file_name))


def main():
    save_correlation_histogram('mean')
    save_correlation_histogram('pooled')
    save_correlation_percentiles('mean')
    save_correlation_percentiles('pooled')


if __name__ == '__main__':
    main()
