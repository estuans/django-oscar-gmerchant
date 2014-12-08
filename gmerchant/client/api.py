from oauth2client.client import SignedJwtAssertionCredentials
from httplib2 import Http


class APIScope(object):

    scope = ""

    def serverOAuthCredentials(self,app):

        #import pdb; pdb.set_trace()


        client_email = app.client_email
        with open(app.private_key_file.path) as f:
            private_key = f.read()

        credentials = SignedJwtAssertionCredentials(client_email, private_key,
        self.scope)

        return credentials

    def serverAuthorisation(self,app):
        creds = self.serverOAuthCredentials(app)
        http_auth = creds.authorize(Http())

        return http_auth


class Content(APIScope):
    scope = "https://www.googleapis.com/auth/content"
