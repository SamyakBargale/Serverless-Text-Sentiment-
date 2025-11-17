
A small serverless project demonstrating AWS Lambda + API Gateway + AWS Comprehend to return sentiment for input text.

## Features
- POST `/sentiment` endpoint
- Uses AWS Comprehend `DetectSentiment`
- Minimal IAM policy example included

## Files
- `lambda_function.py` — Lambda handler
- `template.yaml` — (optional) SAM template
- `deploy.sh` — helper deployment script
- `sample_request.json` — example input
- `iam_policy.json` — least-privilege example

## Quickstart (console)
1. Create an IAM role for Lambda with `AWSLambdaBasicExecutionRole` and the policy in `iam_policy.json`.
2. Create a Lambda function (Python 3.9+) and paste `lambda_function.py`.
3. Create an HTTP API in API Gateway (or REST API) with a POST `/sentiment` route integrated to the Lambda.
4. Test with `curl`:

```bash
curl -X POST '<API_URL>/sentiment' -H 'Content-Type: application/json' -d @sample_request.json
