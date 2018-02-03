#!/home/fy/.virtualenvs/spider_py2/bin/python2.7
# coding=utf-8
import weibo
import time


class myAPIClient(weibo.APIClient):

    def __init__(self, app_key, app_secret, redirect_uri, access_token):
        weibo.APIClient.__init__(self, app_key, app_secret,
                                 redirect_uri, access_token)

    def request_access_token_info(self, access_token):
        r = weibo._http_post(
            '%s%s' % (self.auth_url, 'get_token_info'), access_token=access_token)
        current = int(time.time())
        expires = r.expire_in + current
        return weibo.JsonDict(expires_in=expires)


def get_client(appkey, appsecret, callback, access_token):
    client = myAPIClient(appkey, appsecret, callback, access_token)
    r = client.request_access_token_info(access_token)
    expires_in = r.expires_in
    client.set_access_token(access_token, expires_in)
    return client
