from lambda_function import lambda_handler

if __name__ == '__main__':
    event = {"text": "This is fantastic!", "language_code": "en"}
    print(lambda_handler(event, None))
