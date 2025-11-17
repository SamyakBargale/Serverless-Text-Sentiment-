#!/usr/bin/env bash
set -e

STACK_NAME=serverless-sentiment-api
REGION=us-east-1
S3_BUCKET=your-deployment-bucket-name-$(date +%s) # replace with your s3 bucket name

if ! command -v sam >/dev/null 2>&1; then
  echo "sam CLI not found. Install it: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html"
  exit 1
fi

# create S3 bucket
aws s3 mb s3://$S3_BUCKET --region $REGION || true

# package & deploy
sam package --template-file template.yaml --s3-bucket $S3_BUCKET --output-template-file packaged.yaml
sam deploy --template-file packaged.yaml --stack-name $STACK_NAME --capabilities CAPABILITY_IAM --region $REGION

echo "Deployed stack $STACK_NAME to region $REGION"
