from channels.middleware import BaseMiddleware


class AuthSocketMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        return await super().__call__(scope, receive, send)