from django.http import HttpResponse


def home_page(request):
    print("home page requested")
    friends = [
        'Ankit',
        'ravi'
    ]
    return HttpResponse("<h1>This is home page<h1>")
    # return JsonResponse(friends, safe=False)