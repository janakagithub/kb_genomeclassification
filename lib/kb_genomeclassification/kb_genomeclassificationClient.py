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
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_genomeclassification(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
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
           parameter "phenotypeclass" of String, parameter "attribute" of
           String, parameter "workspace" of String, parameter
           "classifier_training_set" of mapping from String to type
           "ClassifierTrainingSet" (typedef string genome_id; typedef string
           phenotype;) -> structure: parameter "phenotype" of String,
           parameter "genome_name" of String, parameter "classifier_out" of
           String, parameter "target" of String, parameter "classifier" of
           String, parameter "shock_id" of String, parameter "list_name" of
           String, parameter "save_ts" of Long
        :returns: instance of type "ClassifierOut" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        return self._client.call_method(
            'kb_genomeclassification.build_classifier',
            [params], self._service_ver, context)

    def predict_phenotype(self, params, context=None):
        """
        :param params: instance of type "ClassifierPredictionInput" ->
           structure: parameter "workspace" of String, parameter
           "classifier_name" of String, parameter "phenotypeclass" of String,
           parameter "shock_id" of String, parameter "list_name" of String
        :returns: instance of type "ClassifierPredictionOutput" -> structure:
           parameter "prediction_accuracy" of Double, parameter "predictions"
           of mapping from String to String
        """
        return self._client.call_method(
            'kb_genomeclassification.predict_phenotype',
            [params], self._service_ver, context)

    def upload_trainingset(self, params, context=None):
        """
        :param params: instance of type "UploadTrainingSetInput" ->
           structure: parameter "phenotypeclass" of String, parameter
           "workspace" of String, parameter "classifier_training_set" of
           mapping from String to type "ClassifierTrainingSet" (typedef
           string genome_id; typedef string phenotype;) -> structure:
           parameter "phenotype" of String, parameter "genome_name" of
           String, parameter "training_set_out" of String, parameter "target"
           of String, parameter "shock_id" of String, parameter "list_name"
           of String
        :returns: instance of type "UploadTrainingSetOut" -> structure:
           parameter "report_name" of String, parameter "report_ref" of String
        """
        return self._client.call_method(
            'kb_genomeclassification.upload_trainingset',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('kb_genomeclassification.status',
                                        [], self._service_ver, context)
