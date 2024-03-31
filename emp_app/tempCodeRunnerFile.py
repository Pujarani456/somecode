def all_emp(request):
    emps = Employee.objects.all()
    context={
        'emps':emps
    }