import json
import boto3

COMPREHEND = boto3.client('comprehend')


def lambda_handler(event, context):
    try:
        # Support API Gateway proxy integration (string body) and direct test events (dict)
        if isinstance(event, dict) and event.get('httpMethod'):
            body = event.get('body') or ''
            payload = json.loads(body) if body else {}
        else:
            payload = event if isinstance(event, dict) else {}

        text = payload.get('text')
        if not text:
            return _response(400, {'error': 'Missing field "text" in JSON payload'})

        lang = payload.get('language_code', 'en')
        resp = COMPREHEND.detect_sentiment(Text=text, LanguageCode=lang)

        result = {
            'Sentiment': resp.get('Sentiment'),
            'SentimentScore': resp.get('SentimentScore')
        }
        return _response(200, result)

    except Exception as e:
        return _response(500, {'error': str(e)})


def _response(status_code, body_dict):
    return {
        'statusCode': status_code,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(body_dict)
    }
