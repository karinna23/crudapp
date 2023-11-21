from django.shortcuts import render, redirect, get_object_or_404
from .models import Faculty
from .forms import FacultyAddForm, FacultyEditForm

def list(request):
    faculties = Faculty.objects.all()
    return render(request, 'myapp/list.html', {'faculties': faculties})

def add(request):
    if request.method == 'POST':
        form = FacultyAddForm(request.POST)
        if form.is_valid():
            # Find the next available faculty_number
            next_faculty_number = get_next_available_faculty_number()
            form.instance.faculty_number = next_faculty_number
            form.save()
            return redirect('myapp:list')
    else:
        form = FacultyAddForm()
    return render(request, 'myapp/add.html', {'form': form})

def get_next_available_faculty_number():
    # Find the highest existing faculty_number
    highest_faculty_number = Faculty.objects.order_by('-faculty_number').first()
    if highest_faculty_number is None:
        # No faculty members exist, start from 1
        return 1
    else:
        # Increment the highest faculty_number by 1
        return highest_faculty_number.faculty_number + 1

def edit(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == "POST":
        form = FacultyEditForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('myapp:list')
    else:
        form = FacultyEditForm(instance=faculty)
    return render(request, 'myapp/edit.html', {'form': form})

def delete(request, pk):
    faculty = Faculty.objects.get(pk=pk)
    faculty_number = faculty.faculty_number
    faculty.delete()
    mark_faculty_number_as_available(faculty_number)
    return redirect('myapp:list')

def mark_faculty_number_as_available(faculty_number):
    # You can implement logic here to track and make faculty numbers available again.
    # This might involve updating a separate model or data structure to keep track of available numbers.
    pass
