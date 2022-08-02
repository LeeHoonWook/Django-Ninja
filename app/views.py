from django.shortcuts import redirect


def index(request):

    return redirect("ninja-api/docs")
