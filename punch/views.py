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


def punch_history(request):
    """
        This function will be returning the page in which we will display all the past punches of and employee. If the employee have worked all the hours that was shceduled it will show up as a Green line, otherwise red.
    """
    return render(request, 'employee/history.html')


def schedule(request):
    """
        This function should return the schedule of the employee so that it could be checked in the app.
    """
    return render(request, 'employee/schedule.html')