import numpy as np

from importlib.resources import path


class MatrixBaseModifierMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST' and request.path == "/coordinate/":
            post = request.POST.copy()
            coord = np.matrix([post['x'], post['y'], post['z']])
            # Appliquer une matrice de rotation aux coordonnées, X, Y et Z pour effectuer un changement de base
            request.POST = post

        response = self.get_response(request)

        return response