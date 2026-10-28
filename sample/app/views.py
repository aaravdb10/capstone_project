from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import HttpRequest

# Create views that render the project-level templates folder.
def home(request):
    username="virjil van dijk"
    course="django"
    fees=1200
    name=None
    description="every cloud has a silver lining!"
    return render(request, 'home.html', {"username":username, "course":course, "fees":fees, "name":name, "description": description})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
def page_not_found(request):
    return render(request, '404.html')
def first(request):
    name="kushal"
    course="btech"
    city="haryana"
    return render(request, 'first.html',{"username":name, "course_name":course, "city_name":city})
def second(request):
    # course=["django", "php", "laravel", "html"]
    context = {"name": "parv",
            "course": "bba",
            "fees": 800000,
            "duration":"3 months"}
    return render(request, 'second.html', {"context":context})
def conditions(request):
    num=10
    char="b"
    course={"html", "css", "js"}
    return render(request, 'conditional_statement.html', {"number":num, "character":char, "courses":course})

def image(request):
    img = 'app/images/img1.png'
    return render(request, 'image.html', {"img": img})
def question(request):
    student="rahul"
    marks=75
    return render(request, 'question.html', {"student":student, "marks":marks})

def question2(request):
    student=[
        {"id":101, "name":"rahul", "course":"bca", "marks":75},
        {"id":102, "name":"aman", "course":"bca", "marks":35},
        {"id":103, "name":"priya", "course":"mca", "marks":93},
        {"id":104, "name":"neha", "course":"mca", "marks":23},
        {"id":105, "name":"sam", "course":"bca", "marks":43}
    ]
    return render(request, 'question2.html', {"students": student})

def file(request):
    employees=[
        {"name":"Rahul", "performance":90},
        {"name":"Priya", "performance":72},
    ]
    return render(request, 'file.html', {"employees":employees})