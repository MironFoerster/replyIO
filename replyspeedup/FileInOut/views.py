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
        problem_path = os.path.join(settings.MEDIA_ROOT, "FileInOut", str(request.POST['problem_id']))
        download_path = os.path.join("http://", request.get_host(), "media", "FileInOut", str(request.POST['problem_id']))
        context['path_out'] = os.path.join(download_path, "out.txt")
        context['path_source'] = os.path.join(download_path, "source.txt")
        for i in request.FILES['FileIn']:
            in_lines.append(i.decode('utf-8').replace('\r', '').replace('\n', ''))  #.split())  # z.B.: [['4'], ['1234', '7777'], ['1234', '4321'], ['helllo', 'strang', 'err']]

        in_lines.reverse()

        out_lines = []
        exec(open(os.path.join(problem_path, "run.py")).read(), {"in_lines": in_lines, "out_lines": out_lines})
        with open(os.path.join(problem_path, "out.txt"), 'w') as file_out:
            file_out.writelines(out_lines)
        
        print('algo completed, output file saved')

    else:
        print('no file or no algo selected')
    return render(request, 'FileInOut/index.html', context)

