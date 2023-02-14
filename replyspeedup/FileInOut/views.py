from django.shortcuts import render
from django.conf import settings
import os

def index(request):
    #algo = importlib.import_module('replyAlgo' + str(request.POST['algo_number']), package='.replyAlgos')

    #exec('from .replyAlgos import replyAlgo' + str(request.POST['algo_number']) + ' as algo')
    in_lines = []
    if ('FileIn' in request.FILES.keys()) and ('algo_number' in request.POST.keys()):
        from . import algos as algos
        for i in request.FILES['FileIn']:
            in_lines.append(i.decode('utf-8'))  #.split())  # z.B.: [['4'], ['1234', '7777'], ['1234', '4321'], ['helllo', 'strang', 'err']]

        in_lines.reverse()
        exec('global out_lines; out_lines = algos.algo_' + str(request.POST['algo_number']) + '(in_lines)')

        with open(settings.MEDIA_ROOT + '/FileInOut/fileOut.txt', 'w') as file_out:
            file_out.writelines(out_lines)
        print('algo completed, output file saved')

    else:
        print('no file or no algo selected')




    context = {'algos':range(1,6), 'path_fileOut':settings.MEDIA_URL + "FileInOut/fileOut.txt", 'path_source': settings.MEDIA_URL +  "FileInOut/source.txt"}
    return render(request, 'FileInOut/index.html', context)

