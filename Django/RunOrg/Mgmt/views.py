from django.shortcuts import render

locations = [
    {
        'name' : 'Loc1', 'status' : 'Active'
    },
    {
        'name' : 'Loc2', 'status' : 'Active'
    },
    {
        'name' : 'Loc3', 'status' : 'Closed'
    }
]

volunteers = [
    {
        'name' : 'Daniel', 'role' : '', 'phone' : '0721723444'
    }

]

def home(request):
    context = {'locations' : locations, 'volunteers' : volunteers}
    return render(request, 'Mgmt/home.html', context)

def about(request):
    return render(request, 'Mgmt/about.html')