from django.shortcuts import render

services=[
    {
        'service_name' : 'EC2',
        'service_type' : 'Compute',
        'AVailable_resources' : 'Linux,Windows' 
    },
        {
        'service_name' : 'RDS',
        'service_type' : 'Database',
        'Available_resources' : 'PostgreSQL,MariaDB,MySQL' 
    }
]

def home(request):
    context={
        'srvcs' : services
    }
    return render(request,'clouds/home.html',context)

def about(request):
    return render(request,'clouds/about.html')