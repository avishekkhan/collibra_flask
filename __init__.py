import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('OAuth callback received.')

    code = req.params.get('code')
    state = req.params.get('state')

    if code:
        return func.HttpResponse(f"Login successful. Auth code: {code}", status_code=200)
    else:
        return func.HttpResponse("Login failed. No authorization code received.", status_code=400)
