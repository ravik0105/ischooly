from django.shortcuts import render
from django.http import HttpResponse


def home(request):
#    content = get_content_from_file('index.html')  # Implement your logic
#    return render(request, 'pages/index.html', {'content': content})
    return render(request, 'pages/index.html')


def item1(request):
#    content = get_content_from_file('index.html')  # Implement your logic
#    return render(request, 'pages/index.html', {'content': content})
    return render(request, 'pages/python/index.html')

def item2(request):
#    content = get_content_from_file('item2.html')  # Implement your logic
#    return render(request, 'pages/item2.html', {'content': content})
    return render(request, 'pages/python/item2.html')

def item3(request):
#    content = get_content_from_file('item3.html')  # Implement your logic
#    return render(request, 'pages/item3.html', {'content': content})
    return render(request, 'pages/python/item3.html')


def jitem1(request):
#    content = get_content_from_file('index.html')  # Implement your logic
#    return render(request, 'pages/index.html', {'content': content})
    return render(request, 'pages/java/index.html')

def jitem2(request):
#    content = get_content_from_file('item2.html')  # Implement your logic
#    return render(request, 'pages/item2.html', {'content': content})
    return render(request, 'pages/java/item2.html')

def jitem3(request):
#    content = get_content_from_file('item3.html')  # Implement your logic
#    return render(request, 'pages/item3.html', {'content': content})
    return render(request, 'pages/java/item3.html')

    
# You can define more views if needed

def get_content_from_file(filename):
    # Implement your logic to read and return content from the file
    # Handle file existence, permissions, etc.
    with open(filename, 'r') as f:
        return f.read()