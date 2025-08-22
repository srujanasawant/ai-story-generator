def handler(request):
    # Redirect to index.html in static
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": open("index.html").read()
    }
