# -*- coding: utf-8 -*-
"""
A complementary script to `sim_data_load', this module uses custom XML files
to create graphs from certain datasets that have been loaded into memory.

The graphs are saved both in png and pickled format to allow for later editing.

@author: elvd
"""

import os
import pickle
import lxml.etree as etree
import matplotlib.pyplot as plt


def construct_legend(legend_xml):
    legend_string = list()
    for entry in legend_xml:
        legend_string.append(entry.text)
    return legend_string


filename_list = os.listdir(os.getcwd())
filename_list = [filename for filename in filename_list if
                 os.path.splitext(filename)[1] == '.xml']

graph_counter = 0  # to help differentiate graphs from same XML file

for filename in filename_list:
    graph_info = etree.parse(filename)
    graph_info_root = graph_info.getroot()
    print 'Processing file: ', filename

    for graph in graph_info_root:
        # Find how to organise subgraphs
        subgraphs_separate = graph.find('.//*[@separate]').values()[0]

        graph_labels = graph.find('labels')

        if subgraphs_separate == 'yes':
            for subgraph in graph.find('subgraphs'):
                # uses same style as `elvd_tools.custom_plot'`
                fig = plt.figure()
                ax1 = fig.add_subplot(111)
                ax1.set_color_cycle(['r', 'k', 'b', 'g', 'c', 'm'])

                for data_key in graph.find('datasets'):
                    plot_entry = sim_results[data_key.text][int(subgraph.text)]
                    ax1.plot(plot_entry[:, 0], plot_entry[:, 1], lw=1.0)

                ax1.set_xlabel(graph_labels.find('xlabel').text)
                ax1.set_ylabel(graph_labels.find('ylabel').text)

                subgraph_title = ''.join([".//*[@subgraph='",
                                         subgraph.text, "']"])
                ax1.set_title(graph_labels.find(subgraph_title).text)

                ax1.legend(construct_legend(graph_labels.find('legend')),
                           loc='lower right')

                ax1.set_axisbelow(True)
                ax1.grid(which='both', axis='both', color='0.1', ls=':',
                         lw=0.2)
                ax1.tick_params(direction='out', top='off', right='off',
                                width=0.5)

                for spine in ['left', 'top', 'right', 'bottom']:
                    ax1.spines[spine].set_linewidth(0.5)

                plt.rc('font', family='serif')
                plt.rc('legend', fontsize=12)
                plt.rc('axes', titlesize=14)
                plt.rc('axes', labelsize=12)
                plt.rc('xtick', labelsize=12)
                plt.rc('ytick', labelsize=12)

                graph_filename = '_'.join([os.path.splitext(filename)[0],
                                           str(graph_counter)])
                graph_filename = '.'.join([graph_filename, 'pickle'])
                plt.savefig(graph_filename, dpi=300)
                pickle.dump(fig, file(graph_filename, 'w'))
                graph_counter += 1
                plt.close(fig)

        else:
            for data_key in graph.find('datasets'):
                fig = plt.figure()
                ax1 = fig.add_subplot(111)
                ax1.set_color_cycle(['r', 'k', 'b', 'g', 'c', 'm'])

                for subgraph in graph.find('subgraphs'):
                    plot_entry = sim_results[data_key.text][int(subgraph.text)]
                    ax1.plot(plot_entry[:, 0], plot_entry[:, 1], lw=1.0)

                ax1.set_xlabel(graph_labels.find('xlabel').text)
                ax1.set_ylabel(graph_labels.find('ylabel').text)
                subgraph_title = ''.join([".//*[@subgraph='",
                                         subgraph.text, "']"])
                ax1.set_title(graph_labels.find(subgraph_title).text)
                ax1.legend(construct_legend(graph_labels.find('legend')),
                           loc='lower right')

                ax1.set_axisbelow(True)
                ax1.grid(which='both', axis='both', color='0.1', ls=':',
                         lw=0.2)
                ax1.tick_params(direction='out', top='off', right='off',
                                width=0.5)

                for spine in ['left', 'top', 'right', 'bottom']:
                    ax1.spines[spine].set_linewidth(0.5)

                plt.rc('font', family='serif')
                plt.rc('legend', fontsize=12)
                plt.rc('axes', titlesize=14)
                plt.rc('axes', labelsize=12)
                plt.rc('xtick', labelsize=12)
                plt.rc('ytick', labelsize=12)

                graph_filename = '_'.join([os.path.splitext(filename)[0],
                                           str(graph_counter)])
                graph_filename = '.'.join([graph_filename, 'pickle'])
                plt.savefig(graph_filename, dpi=300)
                pickle.dump(fig, file(graph_filename, 'w'))
                graph_counter += 1
                plt.close(fig)
