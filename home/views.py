from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
students = []


def HomePage(request):
    if request.method == 'POST':
        # Creating a variable in which we store the contents that we received from the POST method of the form in index.html
        form_data = request.POST
        # Creating a variable name that will capture the field names {student_name} from the form
        name = form_data['student_name']
        # Creating a variable name that will capture the second field {lucky_number} from the form
        luck_number = form_data['lucky_number']

        # Below indicates what we want to do with the data received from the form.
        new_student = {
            'name': name,
            'lucky_number': luck_number,
        }
        students.append(new_student)
        total_students = len(students)
        print("Total Students: "+str(total_students))

        return redirect('/')
    else:
        return render(request, 'index.html', {'students': students})


def ContextPage(request):
    my_context = {
        'name': "Hilda"
    }

    return render(request, 'context.html', my_context)


def profilepage(request):
    age = 2025-1967
    context = {
        'profile': "Joanna's Profile",
        'name': "Joanna",
        'nin': "CF67890655GTHD78",
        'course': "CSE Python",
        'age': age
    }
    return render(request, 'profile.html', context)
