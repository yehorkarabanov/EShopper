from .like import Like


def like(request):
    return {'like': Like(request)}
