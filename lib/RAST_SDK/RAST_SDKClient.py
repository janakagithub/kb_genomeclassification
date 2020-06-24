# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################


# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from .baseclient import BaseClient as _BaseClient  # @Reimport
import time


class RAST_SDK(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login',
            service_ver='release',
            async_job_check_time_ms=100, async_job_check_time_scale_percent=150, 
            async_job_check_max_time_ms=300000):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = service_ver
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc,
            async_job_check_time_ms=async_job_check_time_ms,
            async_job_check_time_scale_percent=async_job_check_time_scale_percent,
            async_job_check_max_time_ms=async_job_check_max_time_ms)

    def _check_job(self, job_id):
        return self._client._check_job('RAST_SDK', job_id)

    def _annotate_genome_submit(self, params, context=None):
        return self._client._submit_job(
             'RAST_SDK.annotate_genome', [params],
             self._service_ver, context)

    def annotate_genome(self, params, context=None):
        """
        annotate genome
        params - a param hash that includes the workspace id and options
        :param params: instance of type "AnnotateGenomeParams" -> structure:
           parameter "workspace" of String, parameter "input_genome" of type
           "genome_id" (A string representing a genome id.), parameter
           "input_contigset" of type "contigset_id" (A string representing a
           ContigSet id.), parameter "genetic_code" of Long, parameter
           "domain" of String, parameter "scientific_name" of String,
           parameter "output_genome" of String, parameter
           "call_features_rRNA_SEED" of type "bool" (A binary boolean),
           parameter "call_features_tRNA_trnascan" of type "bool" (A binary
           boolean), parameter "call_selenoproteins" of type "bool" (A binary
           boolean), parameter "call_pyrrolysoproteins" of type "bool" (A
           binary boolean), parameter "call_features_repeat_region_SEED" of
           type "bool" (A binary boolean), parameter
           "call_features_insertion_sequences" of type "bool" (A binary
           boolean), parameter "call_features_strep_suis_repeat" of type
           "bool" (A binary boolean), parameter
           "call_features_strep_pneumo_repeat" of type "bool" (A binary
           boolean), parameter "call_features_crispr" of type "bool" (A
           binary boolean), parameter "call_features_CDS_glimmer3" of type
           "bool" (A binary boolean), parameter "call_features_CDS_prodigal"
           of type "bool" (A binary boolean), parameter
           "call_features_CDS_genemark" of type "bool" (A binary boolean),
           parameter "annotate_proteins_kmer_v2" of type "bool" (A binary
           boolean), parameter "kmer_v1_parameters" of type "bool" (A binary
           boolean), parameter "annotate_proteins_similarity" of type "bool"
           (A binary boolean), parameter "resolve_overlapping_features" of
           type "bool" (A binary boolean), parameter
           "call_features_prophage_phispy" of type "bool" (A binary boolean),
           parameter "retain_old_anno_for_hypotheticals" of type "bool" (A
           binary boolean)
        :returns: instance of type "AnnotateGenomeResults" -> structure:
           parameter "workspace" of type "workspace_name" (A string
           representing a workspace name.), parameter "id" of String,
           parameter "report_name" of String, parameter "report_ref" of String
        """
        job_id = self._annotate_genome_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _annotate_genomes_submit(self, params, context=None):
        return self._client._submit_job(
             'RAST_SDK.annotate_genomes', [params],
             self._service_ver, context)

    def annotate_genomes(self, params, context=None):
        """
        annotate genomes
        params - a param hash that includes the workspace id and options
        :param params: instance of type "AnnotateGenomesParams" -> structure:
           parameter "workspace" of String, parameter "genomes" of list of
           type "GenomeParams" -> structure: parameter "input_contigset" of
           type "contigset_id" (A string representing a ContigSet id.),
           parameter "input_genome" of type "genome_id" (A string
           representing a genome id.), parameter "output_genome" of type
           "genome_id" (A string representing a genome id.), parameter
           "genetic_code" of Long, parameter "domain" of String, parameter
           "scientific_name" of String, parameter "call_features_rRNA_SEED"
           of type "bool" (A binary boolean), parameter
           "call_features_tRNA_trnascan" of type "bool" (A binary boolean),
           parameter "call_selenoproteins" of type "bool" (A binary boolean),
           parameter "call_pyrrolysoproteins" of type "bool" (A binary
           boolean), parameter "call_features_repeat_region_SEED" of type
           "bool" (A binary boolean), parameter
           "call_features_insertion_sequences" of type "bool" (A binary
           boolean), parameter "call_features_strep_suis_repeat" of type
           "bool" (A binary boolean), parameter
           "call_features_strep_pneumo_repeat" of type "bool" (A binary
           boolean), parameter "call_features_crispr" of type "bool" (A
           binary boolean), parameter "call_features_CDS_glimmer3" of type
           "bool" (A binary boolean), parameter "call_features_CDS_prodigal"
           of type "bool" (A binary boolean), parameter
           "call_features_CDS_genemark" of type "bool" (A binary boolean),
           parameter "annotate_proteins_kmer_v2" of type "bool" (A binary
           boolean), parameter "kmer_v1_parameters" of type "bool" (A binary
           boolean), parameter "annotate_proteins_similarity" of type "bool"
           (A binary boolean), parameter "resolve_overlapping_features" of
           type "bool" (A binary boolean), parameter
           "call_features_prophage_phispy" of type "bool" (A binary boolean),
           parameter "retain_old_anno_for_hypotheticals" of type "bool" (A
           binary boolean)
        :returns: instance of type "AnnotateGenomesResults" -> structure:
           parameter "workspace" of type "workspace_name" (A string
           representing a workspace name.), parameter "report_name" of
           String, parameter "report_ref" of String
        """
        job_id = self._annotate_genomes_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def status(self, context=None):
        job_id = self._client._submit_job('RAST_SDK.status', 
            [], self._service_ver, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]
