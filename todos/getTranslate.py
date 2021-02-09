import boto3
import json
import os

translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)
resultTx = translate.translate_text(Text='Hello, World', SourceLanguageCode='en', TargetLanguageCode='es')
