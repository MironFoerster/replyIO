from django.shortcuts import render, redirect
from django.conf import settings
import os

def upload(request):
    problem_id = str(request.FILES['FileUp'].name.split(".")[0])
    problem_path = os.path.join(settings.MEDIA_ROOT, "FileInOut", problem_id)

    with open(os.path.join(problem_path, "run.py"), 'w') as run_file:
        for line in request.FILES['FileUp']:
            run_file.write(line.decode('UTF-8')[:-1])
    with open(os.path.join(problem_path, "source.txt"), 'w') as source_file:
        for line in request.FILES['FileUp']:
            source_file.write(line.decode('UTF-8')[:-1])

    return redirect("FileInOut:index")

def index(request):
    context = {'algos': ["p"+str(i) for i in range(1,6)],
               'path_out': "",
               'path_source': ""}
    in_lines = []
    if ('FileIn' in request.FILES.keys()) and ('problem_id' in request.POST.keys()):
        print(request.POST)
        problem_path = os.path.join(settings.MEDIA_ROOT, "FileInOut", str(request.POST['problem_id']))

        context['path_out'] = os.path.join(problem_path, "out.txt")
        context['path_source'] = os.path.join(problem_path, "source.txt")

        for i in request.FILES['FileIn']:
            in_lines.append(i.decode('utf-8')[:-2])  #.split())  # z.B.: [['4'], ['1234', '7777'], ['1234', '4321'], ['helllo', 'strang', 'err']]
        in_lines.reverse()

        out_lines = []
        exec(open(os.path.join(problem_path, "run.py")).read())

        with open(os.path.join(problem_path, "out.txt"), 'w') as file_out:
            file_out.writelines(out_lines)

        
        print('algo completed, output file saved')

    else:
        print('no file or no algo selected')
    return render(request, 'FileInOut/index.html', context)

