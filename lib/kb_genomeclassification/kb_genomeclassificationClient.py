# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except ImportError:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_genomeclassification(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://ci.kbase.us/services/auth/api/legacy/KBase/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def build_classifier(self, params, context=None):
        """
        build_classifier: build_classifier
        requried params:
        :param params: instance of type "BuildClassifierInput" -> structure:
           parameter "genome_attribute" of String, parameter "workspace" of
           String, parameter "training_set_name" of String, parameter
           "classifier_training_set" of mapping from String to type
           "ClassifierTrainingSet" -> structure: parameter "phenotype" of
           String, parameter "genome_name" of String, parameter
           "classifier_object_name" of String, parameter "description" of
           String, parameter "classifier_to_run" of String, parameter
           "logistic_regression" of type "LogisticRegressionOptions" ->
           structure: parameter "penalty" of String, parameter "dual" of type
           "boolean" ("True" or "False"), parameter "lr_tolerance" of Double,
           parameter "lr_C" of Double, parameter "fit_intercept" of type
           "boolean" ("True" or "False"), parameter "intercept_scaling" of
           Double, parameter "lr_class_weight" of String, parameter
           "lr_random_state" of Long, parameter "lr_solver" of String,
           parameter "lr_max_iter" of Long, parameter "multi_class" of
           String, parameter "lr_verbose" of type "boolean" ("True" or
           "False"), parameter "lr_warm_start" of Long, parameter "lr_n_jobs"
           of Long, parameter "decision_tree_classifier" of type
           "DecisionTreeClassifierOptions" -> structure: parameter
           "criterion" of String, parameter "splitter" of String, parameter
           "max_depth" of Long, parameter "min_samples_split" of Long,
           parameter "min_samples_leaf" of Long, parameter
           "min_weight_fraction_leaf" of Double, parameter "max_features" of
           String, parameter "dt_random_state" of Long, parameter
           "max_leaf_nodes" of Long, parameter "min_impurity_decrease" of
           Double, parameter "dt_class_weight" of String, parameter "presort"
           of String, parameter "gaussian_nb" of type "GaussianNBOptions" ->
           structure: parameter "priors" of String, parameter
           "k_nearest_neighbors" of type "KNearestNeighborsOptions" ->
           structure: parameter "n_neighbors" of Long, parameter "weights" of
           String, parameter "algorithm" of String, parameter "leaf_size" of
           Long, parameter "p" of Long, parameter "metric" of String,
           parameter "metric_params" of String, parameter "knn_n_jobs" of
           Long, parameter "support_vector_machine" of type
           "SupportVectorMachineOptions" -> structure: parameter "svm_C" of
           Double, parameter "kernel" of String, parameter "degree" of Long,
           parameter "gamma" of String, parameter "coef0" of Double,
           parameter "probability" of type "boolean" ("True" or "False"),
           parameter "shrinking" of type "boolean" ("True" or "False"),
           parameter "svm_tolerance" of Double, parameter "cache_size" of
           Double, parameter "svm_class_weight" of String, parameter
           "svm_verbose" of type "boolean" ("True" or "False"), parameter
           "svm_max_iter" of Long, parameter "decision_function_shape" of
           String, parameter "svm_random_state" of Long, parameter
           "neural_network" of type "NeuralNetworkOptions" -> structure:
           parameter "hidden_layer_sizes" of String, parameter "activation"
           of String, parameter "mlp_solver" of String, parameter "alpha" of
           Double, parameter "batch_size" of String, parameter
           "learning_rate" of String, parameter "learning_rate_init" of
           Double, parameter "power_t" of Double, parameter "mlp_max_iter" of
           Long, parameter "shuffle" of type "boolean" ("True" or "False"),
           parameter "mlp_random_state" of Long, parameter "mlp_tolerance" of
           Double, parameter "mlp_verbose" of type "boolean" ("True" or
           "False"), parameter "mlp_warm_start" of type "boolean" ("True" or
           "False"), parameter "momentum" of Double, parameter
           "nesterovs_momentum" of type "boolean" ("True" or "False"),
           parameter "early_stopping" of type "boolean" ("True" or "False"),
           parameter "validation_fraction" of Double, parameter "beta_1" of
           Double, parameter "beta_2" of Double, parameter "epsilon" of
           Double, parameter "ensemble_model" of type "EnsembleModelOptions"
           -> structure: parameter "k_nearest_neighbors_box" of Long,
           parameter "gaussian_nb_box" of Long, parameter
           "logistic_regression_box" of Long, parameter
           "decision_tree_classifier_box" of Long, parameter
           "support_vector_machine_box" of Long, parameter
           "neural_network_box" of Long, parameter "voting" of String,
           parameter "en_weights" of String, parameter "en_n_jobs" of Long,
           parameter "flatten_transform" of type "boolean" ("True" or "False")
        :returns: instance of type "ClassifierOut" -> structure: parameter
           "classifier_info" of list of type "classifierInfo" -> structure:
           parameter "classifier_name" of String, parameter "classifier_ref"
           of String, parameter "accuracy" of Double, parameter "report_name"
           of String, parameter "report_ref" of String
        """
        return self._client.call_method('kb_genomeclassification.build_classifier',
                                        [params], self._service_ver, context)

    def predict_phenotype(self, params, context=None):
        """
        :param params: instance of type "ClassifierPredictionInput" ->
           structure: parameter "workspace" of String, parameter
           "categorizer_name" of String, parameter "description" of String,
           parameter "file_path" of String, parameter "annotate" of Long
        :returns: instance of type "ClassifierPredictionOutput" -> structure:
           parameter "prediction_set" of mapping from String to type
           "PredictedPhenotypeOut" -> structure: parameter
           "prediction_probabilities" of Double, parameter "phenotype" of
           String, parameter "genome_name" of String, parameter "genome_ref"
           of String, parameter "report_name" of String, parameter
           "report_ref" of String
        """
        return self._client.call_method('kb_genomeclassification.predict_phenotype',
                                        [params], self._service_ver, context)

    def upload_trainingset(self, params, context=None):
        """
        :param params: instance of type "UploadTrainingSetInput" ->
           structure: parameter "phenotype" of String, parameter "workspace"
           of String, parameter "workspace_id" of String, parameter
           "description" of String, parameter "training_set_name" of String,
           parameter "file_path" of String, parameter "annotate" of Long
        :returns: instance of type "UploadTrainingSetOut" -> structure:
           parameter "classifier_training_set" of mapping from String to type
           "ClassifierTrainingSetOut" -> structure: parameter "phenotype" of
           String, parameter "genome_name" of String, parameter "genome_ref"
           of String, parameter "references" of list of String, parameter
           "evidence_types" of list of String, parameter "report_name" of
           String, parameter "report_ref" of String
        """
        return self._client.call_method('kb_genomeclassification.upload_trainingset',
                                        [params], self._service_ver, context)

    def rast_annotate_trainingset(self, params, context=None):
        """
        :param params: instance of type "RastAnnotateTrainingSetInput" ->
           structure: parameter "classifier_training_set" of mapping from
           String to type "ClassifierTrainingSetOut" -> structure: parameter
           "phenotype" of String, parameter "genome_name" of String,
           parameter "genome_ref" of String, parameter "references" of list
           of String, parameter "evidence_types" of list of String, parameter
           "workspace" of String, parameter "make_genome_set" of Long
        :returns: instance of type "RastAnnotateTrainingSetOutput" ->
           structure: parameter "classifier_training_set" of mapping from
           String to type "ClassifierTrainingSetOut" -> structure: parameter
           "phenotype" of String, parameter "genome_name" of String,
           parameter "genome_ref" of String, parameter "references" of list
           of String, parameter "evidence_types" of list of String, parameter
           "report_name" of String, parameter "report_ref" of String
        """
        return self._client.call_method('kb_genomeclassification.rast_annotate_trainingset',
                                        [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('kb_genomeclassification.status',
                                        [], self._service_ver, context)
