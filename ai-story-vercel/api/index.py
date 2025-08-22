def handler(request):
    # Redirect to index.html in static
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": open("static/index.html").read()
    }
