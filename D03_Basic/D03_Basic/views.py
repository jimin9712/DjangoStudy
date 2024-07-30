from django.shortcuts import HttpResponse

def index(request):
    print('index() 호출!')
    
    return HttpResponse(f"""
        <h1>안녕하세요</h1>
        <h3>django</h3>                
    """)

def index2(request):
    print('index2() 호출!!')
    
    info = 'index2()'

    return HttpResponse(f"""
        <h1>{info}가 호출되었습니다.</h1>
        <h3>django</h3>                
    """)
