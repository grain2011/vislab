import numpy as np
import matplotlib.pyplot as plt


def plot_df_bar(df, columns=None):
    """
    Used to plot AP vs MCC for a single feature, or AP between features.
    """
    fig = plt.figure(figsize=(16, 4))
    ax = fig.add_subplot(111)
    if columns is not None:
        df = df[columns]
    df.plot(ax=ax, kind='bar')
    ax.set_ylim([0, 1])
    ax.set_yticks(np.arange(11) / 10.)
    fig.autofmt_xdate()
    return fig


def plot_top_k_accuracies(accuracies_df, top_k=5):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    accuracies_df.ix[range(top_k + 1)].plot(ax=ax, style='s--')
    ax.set_xlim([1, top_k])
    ax.set_xticks(range(1, top_k + 1))
    ax.set_xlabel('K')
    ax.set_ylim([0, 1])
    ax.set_ylabel('Top-K Accuracy')
    return fig


def plot_curve_with_area(x, y, area, xlabel, ylabel, area_label, title=None):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    ax.plot(x, y, 'k-')
    ax.bar(0, area, 1, alpha=0.2)
    ax.text(.05, area - 0.05, '{}: {:.3f}'.format(area_label, area))
    ax.set_xticks([0, .25, .5, .75, 1])
    ax.set_yticks([0, .25, .5, .75, 1])
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if title is not None:
        ax.set_title(title)
    return fig
