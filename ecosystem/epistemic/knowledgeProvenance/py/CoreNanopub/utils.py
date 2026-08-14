import re


def _extractGCSID(gcs_uri):
    """
    Given a GCS uri, extracts the identifier of the GCS.

    :param gcs_uri: (str) URI of the considered GCS.
    :return: (str) Identifier of the considered GCS.
    """
    gcs_id = re.sub("http://gda.dei.unipd.it/cecore/resource/GCS#", "", gcs_uri)
    return gcs_id


def _extractSentenceID(sentence_uri):
    """
    Given a sentence uri, extracts the identifier of the sentence.

    :param sentence_uri: (str) URI of the considered sentence.
    :return: (str) Identifier of the considered sentence.
    """
    sentence_id = re.sub("http://gda.dei.unipd.it/cecore/resource/Sentence#", "", sentence_uri)
    return sentence_id


def process_gcs(gcs_df):
    """
    Filter out GCs with insufficient evidence
    :param self: self object.

    :return (list(str)) list of GCS id with insufficient evidence.
    """

    invalid_gcs = gcs_df.loc[(gcs_df["CCSNotInformativeLikelihood"] > 0.7) |
                             (gcs_df["PTNotInformativeLikelihood"] > 0.7)]

    return invalid_gcs.index.to_list()

