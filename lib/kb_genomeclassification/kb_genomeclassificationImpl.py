# -*- coding: utf-8 -*-
#BEGIN_HEADER
# The header block is where all import statments should live
"""
import os
from Bio import SeqIO
from pprint import pprint, pformat
from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
from KBaseReport.KBaseReportClient import KBaseReport

    #here are some more imports for sklearn
#from sklearn import train_test_split
#from sklearn.grid_search import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import feature_selection
from sklearn.metrics import recall_score
from sklearn.model_selection import StratifiedKFold
#from sklearn.model_selection import StratifiedKFold 
#from sklearn import StratifiedKFold
#from sklearn.grid_search import StratifiedKFold

#fix later
import seaborn; seaborn.set()
#import matplotlib.pyplot as plt

#%matplotlib inlines    

    #here are imports for specific classifiers
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.neural_network import MLPClassifier

import numpy
import numpy as np
import pickle
"""

# The header block is where all import statments should live
#from __future__ import division
#from __future__ import absolute_import
import os
#from Bio import SeqIO
#from pprint import pprint, pformat
#from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
#from KBaseReport.KBaseReportClient import KBaseReport

    #here are some more imports for sklearn
#from sklearn import train_test_split
#from sklearn.grid_search import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import feature_selection
from sklearn.metrics import recall_score
from sklearn.model_selection import StratifiedKFold
#from sklearn.model_selection import StratifiedKFold
#from sklearn import StratifiedKFold
#from sklearn.grid_search import StratifiedKFold

#fix later
import seaborn as sns
#import matplotlib as mpl
#if os.environ.get('DISPLAY','') == '':
#    print('no display found. Using non-interactive Agg backend')
#    mpl.use('Agg')
#import matplotlib.pyplot as plt

#import matplotlib
#matplotlib.use('Agg')
#import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
plt.switch_backend('agg')
#plt.switch_backend('TkAgg')

#import matplotlib
#matplotlib.use('GTKAgg')  #I had to use GTKAgg for this to work, GTK threw errors
#import matplotlib.pyplot as plt

#%matplotlib inlines

    #here are imports for specific classifiers
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.neural_network import MLPClassifier

import numpy
import numpy as np
import pickle

import pandas as pd

from sklearn.tree import export_graphviz
import graphviz
import os
import re
import StringIO
import io
from io import open
import sys
from itertools import izip

#END_HEADER


class kb_genomeclassification:
    '''
    Module Name:
    kb_genomeclassification

    Module Description:
    A KBase module: kb_genomeclassification
This module build a classifier and predict phenotypes based on the classifier
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/sagoyal2/kb_genomeclassification.git"
    GIT_COMMIT_HASH = "5d29f72316e734318056ee489aad956f14e2af2e"

    #BEGIN_CLASS_HEADER
    # Class variables and functions can be defined in this block

    """
    def classiferTest(self, classifier, classifier_name, print_cfm):
        # so in this method we need to be returning a classifier instead of all the confusion matrices?
        # how do you return a classifier?

        if print_cfm:
            print(self.classifier_name)
        train_score = numpy.zeros(self.splits)
        validate_score = numpy.zeros(self.splits)
        cnf_matrix = numpy.zeros(shape=(3, 3))
        cnf_matrix_f = numpy.zeros(shape=(3, 3))
        for c in range(self.splits):
            X_train = self.full_attribute_array[self.train_index[c]]
            y_train = self.full_classification_array[self.train_index[c]]
            X_test = self.full_attribute_array[self.test_index[c]]
            y_test = self.full_classification_array[self.test_index[c]]
            classifier.fit(X_train, y_train)
            train_score[c] = classifier.score(X_train, y_train)
            validate_score[c] = classifier.score(X_test, y_test)
            y_pred = classifier.predict(X_test)
            cnf = confusion_matrix(y_test, y_pred)
            cnf_f = cnf.astype('float') / cnf.sum(axis=1)[:, numpy.newaxis]
            for i in range(len(cnf)):
                for j in range(len(cnf)):
                    cnf_matrix[i][j] += cnf[i][j]
                    cnf_matrix_f[i][j] += cnf_f[i][j]

        pickle_out = open("/kb/module/work/tmp/" + str(self.classifier_name) + ".pickle", "wb")
        pickle.dump(classifier.fit(self.full_attribute_array, self.full_classification_array), pickle_out, protocol=2)
        pickle_out.close()

        print("%6.3f\t%6.3f\t%6.3f\t%6.3f" % (
        numpy.average(train_score), numpy.std(train_score), numpy.average(validate_score), numpy.std(validate_score)))

        if print_cfm:
            cnf_av = cnf_matrix / self.splits
            print()
            print(cnf_av[0][0], cnf_av[0][1], cnf_av[0][2], )
            print(cnf_av[1][0], cnf_av[1][1], cnf_av[1][2], )
            print(cnf_av[2][0], cnf_av[2][1], cnf_av[2][2], )
            print()
            print(self.class_list[0])
            TP = cnf_av[0][0]
            TN = cnf_av[1][2] + cnf_av[1][2] + cnf_av[2][1] + cnf_av[2][2]
            FP = cnf_av[0][1] + cnf_av[0][2]
            FN = cnf_av[1][0] + cnf_av[2][0]
            self.cf_stats(TN, TP, FP, FN)

            print(self.class_list[1])
            TP = cnf_av[1][1]
            TN = cnf_av[0][0] + cnf_av[0][2] + cnf_av[2][0] + cnf_av[2][2]
            FP = cnf_av[1][0] + cnf_av[1][2]
            FN = cnf_av[0][1] + cnf_av[2][1]
            self.cf_stats(TN, TP, FP, FN)

            print(self.class_list[2])
            TP = cnf_av[2][2]
            TN = cnf_av[0][0] + cnf_av[0][1] + cnf_av[1][0] + cnf_av[1][1]
            FP = cnf_av[2][0] + cnf_av[2][1]
            FN = cnf_av[0][1] + cnf_av[0][2]
            self.cf_stats(TN, TP, FP, FN)

            print(classifier)
            print()

            print("Confusion matrix")
            for i in range(len(cnf_matrix)):
                print(self.class_list[i], end="  \t")
                for j in range(len(cnf_matrix[i])):
                    print(cnf_matrix[i][j] / self.splits, end="\t")
                print()
            print()
            for i in range(len(cnf_matrix_f)):
                print(self.class_list[i], end="  \t")
                for j in range(len(cnf_matrix_f[i])):
                    print("%6.1f" % ((cnf_matrix_f[i][j] / self.splits) * 100.0), end="\t")
                print()
            print()
            print("01", cnf_matrix[0][1])
            

            print("Confusion matrix")
            for i in range(len(cnf_matrix)):
                print(str(self.class_list[i]) + "  \t"),
                for j in range(len(cnf_matrix[i])):
                    print(str(cnf_matrix[i][j] / self.splits) + "\t"),
                print()
            print()
            for i in range(len(cnf_matrix_f)):
                print(str(self.class_list[i]) + "  \t"),
                for j in range(len(cnf_matrix_f[i])):
                    print(str("%6.1f" % ((cnf_matrix_f[i][j] / self.splits) * 100.0)) + "\t"),
                print()
            print()
            print("01", cnf_matrix[0][1])


            # plot_confusion_matrix(cnf_matrix/10,class_list,'Confusion Matrix')
            # plot_confusion_matrix(cnf_matrix_f/splits*100.0,class_list,'Confusion Matrix %',classifier_name)
        return ( numpy.average(train_score), numpy.std(train_score), numpy.average(validate_score), numpy.std(validate_score))
    """

    def classiferTest(self, classifier, classifier_name, print_cfm):
        # so in this method we need to be returning a classifier instead of all the confusion matrices?
        # how do you return a classifier?

        self.saved_name = classifier_name

        if print_cfm:
            print classifier_name
            self.list_name.extend([self.saved_name])
        train_score = numpy.zeros(self.splits)
        validate_score = numpy.zeros(self.splits)
        matrix_size = self.class_list.__len__()

        cnf_matrix = numpy.zeros(shape=(matrix_size, matrix_size))
        cnf_matrix_f = numpy.zeros(shape=(matrix_size, matrix_size))
        for c in xrange(self.splits):
            X_train = self.full_attribute_array[self.train_index[c]]
            y_train = self.full_classification_array[self.train_index[c]]
            X_test = self.full_attribute_array[self.test_index[c]]
            y_test = self.full_classification_array[self.test_index[c]]
            classifier.fit(X_train, y_train)
            train_score[c] = classifier.score(X_train, y_train)
            validate_score[c] = classifier.score(X_test, y_test)
            y_pred = classifier.predict(X_test)
            cnf = confusion_matrix(y_test, y_pred)
            cnf_f = cnf.astype(u'float') / cnf.sum(axis=1)[:, numpy.newaxis]
            for i in xrange(len(cnf)):
                for j in xrange(len(cnf)):
                    cnf_matrix[i][j] += cnf[i][j]
                    cnf_matrix_f[i][j] += cnf_f[i][j]

        if print_cfm:
            pickle_out = open(u"/kb/module/work/tmp/" + unicode(classifier_name) + u".pickle", u"wb")
            #pickle_out = open("/kb/module/work/tmp/" + str(self.classifier_name) + ".pickle", "wb")
            pickle.dump(classifier.fit(self.full_attribute_array, self.full_classification_array), pickle_out, protocol = 2)
            pickle_out.close()

        list_forDict = []

        if self.class_list.__len__() == 3:
            if print_cfm:
                cnf_av = cnf_matrix / self.splits
                print
                print cnf_av[0][0], cnf_av[0][1], cnf_av[0][2]
                print cnf_av[1][0], cnf_av[1][1], cnf_av[1][2]
                print cnf_av[2][0], cnf_av[2][1], cnf_av[2][2]
                print
                print self.class_list[0]
                TP = cnf_av[0][0]
                TN = cnf_av[1][2] + cnf_av[1][2] + cnf_av[2][1] + cnf_av[2][2]
                FP = cnf_av[0][1] + cnf_av[0][2]
                FN = cnf_av[1][0] + cnf_av[2][0]
                list_forDict.extend([None])
                list_forDict.extend(self.cf_stats(TN, TP, FP, FN))

                print self.class_list[1]
                TP = cnf_av[1][1]
                TN = cnf_av[0][0] + cnf_av[0][2] + cnf_av[2][0] + cnf_av[2][2]
                FP = cnf_av[1][0] + cnf_av[1][2]
                FN = cnf_av[0][1] + cnf_av[2][1]
                list_forDict.extend([None, None])
                list_forDict.extend(self.cf_stats(TN, TP, FP, FN))

                print self.class_list[2]
                TP = cnf_av[2][2]
                TN = cnf_av[0][0] + cnf_av[0][1] + cnf_av[1][0] + cnf_av[1][1]
                FP = cnf_av[2][0] + cnf_av[2][1]
                FN = cnf_av[0][1] + cnf_av[0][2]
                list_forDict.extend([None, None])
                list_forDict.extend(self.cf_stats(TN, TP, FP, FN))

                list_forDict.extend([(list_forDict[4] + list_forDict[10] + list_forDict[16])/3])

                self.list_statistics.append(list_forDict)

                # self.plot_confusion_matrix(cnf_matrix/10,class_list,'Confusion Matrix')
                self.plot_confusion_matrix(cnf_matrix_f/self.splits*100.0,self.class_list,u'Confusion Matrix',classifier_name)

        if self.class_list.__len__() == 2:
            if print_cfm:
                """
                Total = cnf[0][0] + cnf[0][1] + cnf[1][0] + cnf[1][1]
                TP = cnf[0][0] + cnf[1][1]

                FP_A = cnf[1][0]
                FN_A = cnf[0][1]
                TP_A = cnf[0][0]
                TN_A = cnf[1][1]
                AP = cnf[0][0] + cnf[0][1]
                AN = Total - AP

                print()
                print(newclass_list[0])
                print("Accuracy:\t\t%6.3f" % ((TP_A + TN_A) / Total))
                print("Misclassification Rate:\t%6.3f" % ((FN_A) / (FN_A + FP_A)))
                print("True Positive Rate:\t%6.3f" % (TP_A / (TP_A + FN_A)))
                print("False Positive Rate:\t%6.3f" % (FP_A / (FP_A + TN_A)))
                print("Specificity:\t\t%6.3f" % (TN_A / (TN_A + FP_A)))
                print("Precision:\t\t%6.3f" % (TP_A / (TP_A + FP_A)))
                print()
                """
                TP = cnf[0][0]
                TN = cnf[1][1]
                FP = cnf[0][1]
                FN = cnf[1][0]

                list_forDict.extend(self.cf_stats(TN, TP, FP, FN))
                self.list_statistics.append(list_forDict)

                self.plot_confusion_matrix(cnf_matrix_f/self.splits*100.0,self.class_list,u'Confusion Matrix',classifier_name)

        if print_cfm:
            print classifier
            print
            print u"Confusion matrix"
            for i in xrange(len(cnf_matrix)):
                print self.class_list[i],; sys.stdout.write(u"  \t")
                for j in xrange(len(cnf_matrix[i])):
                    print cnf_matrix[i][j] / self.splits,; sys.stdout.write(u"\t")
                print
            print
            for i in xrange(len(cnf_matrix_f)):
                print self.class_list[i],; sys.stdout.write(u"  \t")
                for j in xrange(len(cnf_matrix_f[i])):
                    print u"%6.1f" % ((cnf_matrix_f[i][j] / self.splits) * 100.0),; sys.stdout.write(u"\t")
                print
            print
            print u"01", cnf_matrix[0][1]

        print u"%6.3f\t%6.3f\t%6.3f\t%6.3f" % (
        numpy.average(train_score), numpy.std(train_score), numpy.average(validate_score), numpy.std(validate_score))

        return (numpy.average(train_score), numpy.std(train_score), numpy.average(validate_score), numpy.std(validate_score))

    """
    def cf_stats(self,TN,TP,FP,FN):
        AN = TN+FP
        AP = TN+FN
        PN = TN+FN
        PP = TP+FP
        Total = TN+TP+FP+FN
        Recall = (TP/(TP+FN))
        Precision = (TP/(TP+FP))
        print("Accuracy:\t\t%6.3f"%((TP+TN)/Total))
        print("Precision:\t\t%6.3f"%(Precision))
        print("Recall:\t\t%6.3f"%(Recall))
        print("F1 score::\t\t%6.3f"%(2*((Precision*Recall)/(Precision+Recall))))
        print()
    """
    def whichClassifier(self, name):
        if name == u"KNeighborsClassifier":
            return KNeighborsClassifier()
        elif name == u"GaussianNB":
            return GaussianNB()
        elif name == u"LogisticRegression":
            return LogisticRegression(random_state=0)
        elif name == u"DecisionTreeClassifier":
            return DecisionTreeClassifier(random_state=0)
        elif name == u"SVM":
            return svm.LinearSVC(random_state=0)
        elif name == u"NeuralNetwork":
            return MLPClassifier(random_state=0)
        else:
            return u"ERROR THIS SHOULD NOT HAVE REACHED HERE"

    def cf_stats(self, TN, TP, FP, FN):
        AN = TN + FP
        AP = TN + FN
        PN = TN + FN
        PP = TP + FP
        Total = TN + TP + FP + FN
        Recall = (TP / (TP + FN))
        Precision = (TP / (TP + FP))
        """
        print("Accuracy:\t\t%6.3f" % ((TP + TN) / Total))
        print("Precision:\t\t%6.3f" % (Precision))
        print("Recall:\t\t%6.3f" % (Recall))
        print("F1 score::\t\t%6.3f" % (2 * ((Precision * Recall) / (Precision + Recall))))
        print()
        """

        list_return=[((TP + TN) / Total), (Precision), (Recall), (2 * ((Precision * Recall) / (Precision + Recall)))]

        return list_return

    def to_HTML_Statistics(self, additional = False):

        #self.counter = self.counter + 1

        if not additional:

            print u"I am inside not additional"

            statistics_dict = {}

            #print(self.list_name)
            #print(self.list_statistics)

            for i, j in izip(self.list_name, self.list_statistics):
                statistics_dict[i] = j

            data = statistics_dict

            if self.class_list.__len__() == 3:
                my_index = [u'Facultative', u'Accuracy:', u'Precision:', u'Recall:', u'F1 score::', None, u'Aerobic', u'Accuracy:',
                        u'Precision:', u'Recall:', u'F1 score::', None, u'Anaerobic', u'Accuracy:', u'Precision:', u'Recall:',
                        u'F1 score::', u'Average F1']

            if self.class_list.__len__() == 2:
                my_index = [u'Accuracy:', u'Precision:', u'Recall:', u'F1 score::']

            df = pd.DataFrame(data, index=my_index)
            df.to_html(u'/kb/module/work/tmp/newStatistics.html')

        if additional:
            statistics_dict = {}

            neededIndex = [2, 3, self.list_name.__len__() - 2, self.list_name.__len__() -1]
            #neededIndex = [self.list_name.__len__() - 2, self.list_name.__len__() -1]
            sub_list_name = [self.list_name[i] for i in neededIndex]
            sub_list_statistics = [self.list_statistics[i] for i in neededIndex]

            for i, j in izip(sub_list_name, sub_list_statistics):
                statistics_dict[i] = j

            data = statistics_dict

            if self.class_list.__len__() == 3:
                my_index = [u'Facultative', u'Accuracy:', u'Precision:', u'Recall:', u'F1 score::', None, u'Aerobic', u'Accuracy:',
                        u'Precision:', u'Recall:', u'F1 score::', None, u'Anaerobic', u'Accuracy:', u'Precision:', u'Recall:',
                        u'F1 score::', u'Average F1']

            if self.class_list.__len__() == 2:
                my_index = [u'Accuracy:', u'Precision:', u'Recall:', u'F1 score::']

            df = pd.DataFrame(data, index=my_index)
            df.to_html(u'/kb/module/work/tmp/postStatistics.html')

        #df.to_html('statistics' + str(self.counter) + '.html')

    def plot_confusion_matrix(self,cm, classes, title,classifier_name):

        """
        plt.rcParams.update({'font.size': 18})
        #fig,ax= plt.subplots(figsize=(5,4))
        fig = plt.figure()
        ax = fig.add_subplot(figsize=(5,4))
        sns.set(font_scale=1.5)
        sns_plot = sns.heatmap(cm, annot=True, ax = ax, cmap="Blues"); #annot=True to annotate cells
        # labels, title and ticks
        ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels');
        ax.set_title(title);
        ax.xaxis.set_ticklabels(classes); ax.yaxis.set_ticklabels(classes);
        #fig.savefig(classifier_name+".png") #this may not be necessary as not necessary to save png file
        sns_plot.savefig(classifier_name+".png", format='png')
        """

        plt.rcParams.update({u'font.size': 18})
        fig = plt.figure()
        ax = fig.add_subplot(figsize=(5,4))
        sns.set(font_scale=1.5)
        sns_plot = sns.heatmap(cm, annot=True, ax = ax, cmap=u"Blues"); #annot=True to annotate cells
        ax = sns_plot
        ax.set_xlabel(u'Predicted labels'); ax.set_ylabel(u'True labels');
        ax.set_title(title);
        ax.xaxis.set_ticklabels(classes); ax.yaxis.set_ticklabels(classes);
        #ax.savefig(classifier_name+".png", format='png')

        fig = sns_plot.get_figure()
        #fig.savefig(u"./pics/" + classifier_name +u".png", format=u'png')
        fig.savefig(u"/kb/module/work/tmp/pics/" + classifier_name +u".png", format=u'png')

    def tree_code(self, optimized_tree, spacer_base=u"    "):
        """Produce psuedo-code for decision tree.
        Notes
        -----
        based on http://stackoverflow.com/a/30104792.
        """
        tree = optimized_tree #DecisionTreeClassifier(random_state=0, max_depth=3, criterion='entropy')
        #tree = DecisionTreeClassifier(random_state=0, max_depth=3, criterion='entropy')
        print u"Hello"

        tree.fit(self.full_attribute_array, self.full_classification_array)

        feature_names = self.attribute_list
        target_names = self.class_list

        left = tree.tree_.children_left
        right = tree.tree_.children_right
        threshold = tree.tree_.threshold
        features = [feature_names[i] for i in tree.tree_.feature]
        value = tree.tree_.value

        def recurse(left, right, threshold, features, node, depth):
            spacer = spacer_base * depth
            if (threshold[node] != -2):
                print spacer + u"if ( " + features[node] + u" <= " + \
                      unicode(threshold[node]) + u" ) {"
                if left[node] != -1:
                    recurse(left, right, threshold, features,
                                 left[node], depth + 1)
                print spacer + u"}\n" + spacer + u"else {"
                if right[node] != -1:
                    recurse(left, right, threshold, features,
                                 right[node], depth + 1)
                print spacer + u"}"
            else:
                target = value[node]
                for i, v in izip(numpy.nonzero(target)[1],
                                target[numpy.nonzero(target)]):
                    target_name = target_names[i]
                    target_count = int(v)
                    print spacer + u"return " + unicode(target_name) + \
                          u" ( " + unicode(target_count) + u" examples )"

        recurse(left, right, threshold, features, 0, 0)

        self.printTree(tree, u"NAMEmyTreeLATER")

    def tune_Decision_Tree(self):

        skf = StratifiedKFold(n_splits=self.splits, random_state=0, shuffle=True)
        for train_idx, test_idx in skf.split(self.full_attribute_array, self.full_classification_array):
            self.train_index.append(train_idx)
            self.test_index.append(test_idx)

        #below code is for gini-criterion
        val = numpy.zeros(12)
        test_av = numpy.zeros(12)
        test_std = numpy.zeros(12)
        val_av = numpy.zeros(12)
        val_std = numpy.zeros(12)
        for d in xrange(1, 12):
            val[d] = d
            (test_av[d], test_std[d], val_av[d], val_std[d]) = self.classiferTest(DecisionTreeClassifier(random_state=0, max_depth=d), u"DecisionTreeClassifier", False)

        fig, ax = plt.subplots(figsize=(6, 6))
        plt.errorbar(val[1:], test_av[1:], yerr=test_std[1:], fmt=u'o', label=u'Training set')
        plt.errorbar(val[1:], val_av[1:], yerr=val_std[1:], fmt=u'o', label=u'Testing set')
        ax.set_ylim(ymin=0.5, ymax=1.1)
        ax.set_title(u"Gini Criterion")
        plt.xlabel(u'Tree depth', fontsize=12)
        plt.ylabel(u'Accuracy', fontsize=12)
        plt.legend(loc=u'lower left')
        #plt.savefig(u"./pics/"+ self.global_target +u"_gini_depth-met.png")
        #fig.savefig(u"/kb/module/work/tmp/pics/" + classifier_name +u".png", format=u'png')
        plt.savefig(u"/kb/module/work/tmp/pics/"+ self.global_target +u"_gini_depth-met.png")

        gini_best_index = np.argmax(val_av)
        print gini_best_index
        gini_best = np.amax(val_av)

        #below code is for entropy-criterion
        val = numpy.zeros(12)
        test_av = numpy.zeros(12)
        test_std = numpy.zeros(12)
        val_av = numpy.zeros(12)
        val_std = numpy.zeros(12)
        for d in xrange(1, 12):
            val[d] = d
            (test_av[d], test_std[d], val_av[d], val_std[d]) = self.classiferTest(DecisionTreeClassifier(random_state=0, max_depth=d, criterion=u'entropy'), u"DecisionTreeClassifier",False)

        fig, ax = plt.subplots(figsize=(6, 6))
        plt.errorbar(val[1:], test_av[1:], yerr=test_std[1:], fmt=u'o', label=u'Training set')
        plt.errorbar(val[1:], val_av[1:], yerr=val_std[1:], fmt=u'o', label=u'Testing set')
        ax.set_ylim(ymin=0.5, ymax=1.1)
        ax.set_title(u"Entropy Criterion")
        plt.xlabel(u'Tree depth', fontsize=12)
        plt.ylabel(u'Accuracy', fontsize=12)
        plt.legend(loc=u'lower left')
        #plt.savefig(u"./pics/"+ self.global_target +u"_entropy_depth-met.png")
        plt.savefig(u"/kb/module/work/tmp/pics/"+ self.global_target +u"_entropy_depth-met.png")

        entropy_best_index = np.argmax(val_av)
        print entropy_best_index
        entropy_best = np.amax(val_av)


        gini_best_index = 4
        entropy_best_index = 3

        self.classiferTest(DecisionTreeClassifier(random_state=0, max_depth=gini_best_index, criterion=u'gini'), self.global_target + u"_DecisionTreeClassifier(gini)", True)
        self.classiferTest(DecisionTreeClassifier(random_state=0, max_depth=entropy_best_index, criterion=u'entropy'), self.global_target + u"_DecisionTreeClassifier(entropy)", True)

        self.to_HTML_Statistics(additional=True)

        if gini_best > entropy_best:
            self.tree_code(DecisionTreeClassifier(random_state=0, max_depth=gini_best_index, criterion=u'gini'))
        else:
            self.tree_code(DecisionTreeClassifier(random_state=0, max_depth=entropy_best_index, criterion=u'entropy'))


    def parse_lookNice(self,name):
        import re

        f = open(u"/kb/module/work/tmp/dotFolder/mydotTree.dot", u"r")
        allStr = f.read()
        f.close()
        new_allStr = allStr.replace(u'\\n', u'')

        first_fix = re.sub(ur'(\w\s\[label="[\w\s.,:()-]+)<=([\w\s.\[\]=,]+)("] ;)',
                           ur'\1 (Absent)" , color="0.650 0.200 1.000"] ;', new_allStr)
        second_fix = re.sub(ur'(\w\s\[label=")(.+?class\s=\s)', ur'\1', first_fix)

        # nominal fixes like color and shape
        third_fix = re.sub(ur'shape=box] ;', ur'shape=Mrecord] ; node [style=filled];', second_fix)

        if self.class_list.__len__() == 3:
            fourth_fix = re.sub(ur'(\w\s\[label="anaerobic")', ur'\1, color = "0.5176 0.2314 0.9020"', third_fix)
            fifth_fix = re.sub(ur'(\w\s\[label="aerobic")', ur'\1, color = "0.5725 0.6118 1.0000"', fourth_fix)
            sixth_fix = re.sub(ur'(\w\s\[label="facultative")', ur'\1, color = "0.5804 0.8824 0.8039"', fifth_fix)
            f = open(u"/kb/module/work/tmp/dotFolder/niceTree.dot", u"w")
            f.write(sixth_fix)
            f.close()

            os.system(u'dot -Tpng /kb/module/work/tmp/dotFolder/niceTree.dot >  '+ u"/kb/module/work/tmp/pics/"  + name + u'.png ')

        if self.class_list.__len__() == 2:
            fourth_fix = re.sub(ur'(\w\s\[label="N")', ur'\1, color = "0.5176 0.2314 0.9020"', third_fix)
            fifth_fix = re.sub(ur'(\w\s\[label="P")', ur'\1, color = "0.5725 0.6118 1.0000"', fourth_fix)
            f = open(u"/kb/module/work/tmp/dotFolder/niceTree.dot", u"w")
            f.write(fifth_fix)
            f.close()

            os.system(u'dot -Tpng /kb/module/work/tmp/dotFolder/niceTree.dot >  '+ u"/kb/module/work/tmp/pics/" + name + u'.png ')

    def printTree(self,tree, pass_name):
        """
        export_graphviz(tree, out_file="mytree.dot", feature_names=self.attribute_list,
                        class_names=self.class_list)
        with open("mytree.dot") as f:
            dot_graph = f.read()
        os.system('dot -Tpng mytree.dot >  ' + name + '.png ')
        """

        #dotfile = io.open(u"/kb/module/work/tmp/dotFolder/mydotTree.dot", u'w')
        not_dotfile = StringIO.StringIO()
        export_graphviz(tree, out_file=not_dotfile, feature_names=self.attribute_list,
                        class_names=self.class_list)
        #dotfile.close()

        #print(type(dotfile))
        #print(dotfile.getvalue())
        contents = not_dotfile.getvalue()
        not_dotfile.close()

        dotfile = open(u"/kb/module/work/tmp/dotFolder/mydotTree.dot", u'w')
        dotfile.write(contents)
        dotfile.close()

        self.parse_lookNice(pass_name)
        #os.system('dot -Tpng ./mytree.dot >  ' + name + '.png ')

    def _valid_params(self, params):

        pass

    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        
        """
        # Any configuration parameters that are important should be parsed and
        # saved in the constructor.
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']

        self.full_attribute_array = np.load("/kb/module/data/full_attribute_array.npy")
        self.full_classification_array = np.load("/kb/module/data/full_classification_array.npy")

        pickle_in = open("/kb/module/data/attribute_list.pickle", "rb")
        self.attribute_list = pickle.load(pickle_in)

        self.class_list = ['anaerobic', 'aerobic', 'facultative']

        self.train_index = []
        self.test_index = []

        self.splits = 10

        self.classifier_name = ""
        """
        which_target = u"Metabolism"

        print "I am right here"

        if which_target == u"Metabolism":
            self.full_attribute_array = np.load(u"/kb/module/data/full_attribute_array.npy")
            self.full_classification_array = np.load(u"/kb/module/data/full_classification_array.npy")
            self.class_list = [u'anaerobic', u'aerobic', u'facultative']

        if which_target == u"Gram_Stain":
            self.full_attribute_array = np.load(u"/kb/module/data/copyof_gram_full_attribute_array.npy")
            self.full_classification_array = np.load(u"/kb/module/data/copyof_gram_full_classification_array.npy")
            self.class_list = [u'N',u'P']


        pickle_in = open(u"/kb/module/data/attribute_list.pickle", u"rb")
        self.attribute_list = pickle.load(pickle_in)

        self.train_index = []
        self.test_index = []

        self.splits = 10
        self.global_target = which_target

        self.saved_name = u""
        self.list_name = []

        self.counter = 0

        self.list_statistics = []

        global output 
        output = {'jack': 4098, 'sape': 4139} #random dict

        #END_CONSTRUCTOR
        pass


    def build_classifier(self, ctx, params):
        """
        build_classifier: build_classifier
        requried params:
        ss
        :param params: instance of type "BuildClassifierInput" -> structure:
           parameter "phenotypeclass" of String, parameter "attribute" of
           String, parameter "workspace" of String, parameter
           "classifier_training_set" of mapping from String to type
           "ClassifierTrainingSet" (typedef string genome_id; typedef string
           phenotype;) -> structure: parameter "phenotype" of String,
           parameter "genome_name" of String, parameter "classifier_out" of
           String, parameter "target" of String, parameter "classifier" of
           String
        :returns: instance of type "ClassifierOut" -> structure: parameter
           "classifier_ref" of String, parameter "phenotype" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN build_classifier

        os.makedirs("/kb/module/work/tmp/pics/")
        os.makedirs("/kb/module/work/tmp/dotFolder/")

        print 'fdsafds'
        print params

        
        self._valid_params(params)

        classifier = params.get('classifier')
        target = params.get('target')

        # Add the block of code that reads in .txt file contain the annotations.
        # (Here my question is how to change this section so that it reads in the genomes files on the KBASE Narrative)


        skf = StratifiedKFold(n_splits=self.splits, random_state=0, shuffle=True)
        for train_idx, test_idx in skf.split(self.full_attribute_array, self.full_classification_array):
            self.train_index.append(train_idx)
            self.test_index.append(test_idx)

        if classifier == u"Default":
            self.classiferTest(KNeighborsClassifier(),target+u"_KNeighborsClassifier",True)
            self.classiferTest(GaussianNB(),target+u"_GaussianNB",True)
            self.classiferTest(LogisticRegression(random_state=0),target+u"_LogisticRegression",True)
            self.classiferTest(DecisionTreeClassifier(random_state=0),target+u"_DecisionTreeClassifier",True)
            self.classiferTest(svm.LinearSVC(random_state=0),target+u"_SVM",True)
            self.classiferTest(MLPClassifier(random_state=0),target+u"_NeuralNetwork", True)
        else:
            if target == u"Metabolism":
                self.classiferTest(self.whichClassifier(classifier), unicode(u"Metabolism_") + classifier, True)
            elif target == u"Gram_Stain":
                self.classiferTest(self.whichClassifier(classifier), unicode(u"Gram_Stain_") + classifier, True)
            else:
                print u"ERROR check spelling?"


        self.to_HTML_Statistics()
        
        #self.tune_Decision_Tree()
        #self.tree_code("doesn't matter")

        #END build_classifier

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method build_classifier return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def predict_phenotype(self, ctx, params):
        """
        :param params: instance of type "ClassifierPredictionInput" ->
           structure: parameter "workspace" of String, parameter
           "classifier_ref" of String, parameter "phenotype" of String
        :returns: instance of type "ClassifierPredictionOutput" -> structure:
           parameter "prediction_accuracy" of Double, parameter "predictions"
           of mapping from String to String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN predict_phenotype
        #END predict_phenotype

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method predict_phenotype return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
