from django.http import JsonResponse

def respond(request):
    print(request.GET["query"])
    print(request.body)
    return JsonResponse({"message": "got your request"})
