from django.shortcuts import render

def index(request):
    """
        The idea here is that the U when redirected to index, it will be first checked if:
            they are logged in;
            they are management role or not;
            they are the admin managing the shifts of employees;

        based on that a different path of return will be shown,
        as per right now it will be render only the employee path
    """
    return render(request, 'employee/index.html')
