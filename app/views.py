from django.shortcuts import render

def home_view(request):
    nome_empresa{
        ["Shopeeamazo_nome_legal"]
    }

    return render(request, 'home.html')


def perfil_view(request):
    context{
        ['nome_funcionario': "haroldo", 'cargo': "Dev front-end", 'setor': "finança"]
    }
     
     return render(request, 'perfil.html', context)


def status_view(request):
    context{
        ['id_servidor': "Servidor Alpha-01", 'status_sistema': "Operacional"]
    }

    return render(request, 'Status.html', context)