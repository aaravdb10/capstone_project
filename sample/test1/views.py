from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def file(request):
#     employees=[
#         {"name":"Rahul", "performance":90},
#         {"name":"Priya", "performance":72},
#     ]
#     total = len(empolyees)
#     return render(request, 'file.html', {"employees":employees, "total_employees":total})

def Set(request):
    response = HttpResponse("Cookie Value Set")
    response.set_cookie("Username", "name_value", max_age=600)
    response.set_cookie("Preference", "value_selected", max_age=600)
    response.set_cookie("Language", "language_selected", max_age=600)
    response.set_cookie("City", "city_selected", max_age=600)
    return response

def Get(request):
    value=request.COOKIES.get("Username")
    return HttpResponse(f"Cookie Value is: {value}")

def delete(request):
    response=HttpResponse("Cookies deleted successfully!")
    response.delete_cookie("Username")
    response.delete_cookie("language")
    response.delete_cookie("theme")
    response.delete_cookie("city")
    return response

def theme(request):
    response=HttpResponse("theme value is light")
    response.set_cookie("theme", "light", max_age=600)
    return response
def ctheme(request):
    if value=="dark":
        return render(request, "index.html", {"data":value})
    else:
        return render(request, "index.html", {"data":value})