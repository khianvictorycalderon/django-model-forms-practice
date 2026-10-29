from django.shortcuts import render, redirect
from .forms import StudentForm

# Create your views here.
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("add_student")
    else:
        form = StudentForm

    return render(
        request,
        'add_student.html',
        {
            "form": form
        }
    )