from django.shortcuts import render

from tasks.models import Task


# Create your views here.
# FBV
def index(request):
    print("In the view")
    # if come from request in URL with ?descr_filter="wash"
    descr_filter = request.GET.get('descr_filter', "")
    if descr_filter:
        tasks = Task.objects.filter(description__icontains=descr_filter.lower())
    else:
        tasks = Task.objects.all()

    # object
    context = {
        "name": "Emily",
        "tasks": tasks,
        "tasks_count": tasks.count(),
        "descr_filter": descr_filter,
    }
    return render(request, "tasks/index.html", context)

# from Logging:
# SELECT "tasks_task"."id",
#        "tasks_task"."title",
#         "tasks_task"."description",
#         "tasks_task"."done"
# FROM "tasks_task"
# WHERE UPPER("tasks_task"."description"::text) LIKE UPPER('%wash%');
# args=('%wash%',); alias=default
# [11/Jan/2024 18:33:53] "GET / HTTP/1.1" 200 289
#
# """
