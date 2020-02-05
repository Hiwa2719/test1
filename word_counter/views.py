import re
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def counter(request):
    text = request.GET['text']
    words = re.findall('[a-zA-Z]+', text)
    words = [word.lower() for word in words]
    words_tuple = []
    for word in set(words):
        words_tuple.append((word, words.count(word)))
    words_tuple = sorted(words_tuple, key=lambda x: x[1], reverse=True)
    counter = len(words)
    return render(request, 'count.html', {'words': words_tuple, 'counter': counter})
