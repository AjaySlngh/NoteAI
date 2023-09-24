# This example requires environment variables named "LANGUAGE_KEY" and "LANGUAGE_ENDPOINT"
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
key = os.environ.get('AZURE_LANGUAGE_KEY')
endpoint = os.environ.get('AZURE_LANGUAGE_ENDPOINT')


# Authenticate the client using your key and endpoint

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=ta_credential)
    return text_analytics_client


# Example method for summarizing text


def sample_extractive_summarization(client):
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import (
        TextAnalyticsClient,
        ExtractiveSummaryAction
    )

    client = authenticate_client()

    file = open("transcription.txt", "r")
    file_s = file.read()

    document = [file_s]
    file.close()

    file = open("extractive_summary.txt", "w")

    poller = client.begin_analyze_actions(
        document,
        actions=[
            ExtractiveSummaryAction(max_sentence_count=15)
        ],
    )

    document_results = poller.result()
    for result in document_results:
        extract_summary_result = result[0]  # first document, first result
        if extract_summary_result.is_error:
            print("...Is an error with code '{}' and message '{}'".format(
                extract_summary_result.code, extract_summary_result.message
            ))
            file.write("...Is an error with code '{}' and message '{}'".format(
                extract_summary_result.code, extract_summary_result.message
            ))
        else:
            print("Summary extracted: \n{}".format(
                " ".join([sentence.text for sentence in extract_summary_result.sentences]))
            )
            file.write("{}".format(
                " ".join([sentence.text for sentence in extract_summary_result.sentences]))
            )
