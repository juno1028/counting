from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    text = request.GET['fulltext']
    textcount = len(text)
    splitted_text = text.split()
    text2 = "".join(splitted_text)
    text2count = len(text2)

    words = request.GET['fulltext']
    wordcounts = len(words.split())
    word_count = {}
    for word in words.split():
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1
    key_list = list(word_count.keys())
    value_list = []
    for char in key_list:
        value_list.append(word_count[char])
    result=[]
    for i in range(len(key_list)):
        result.append(str(key_list[i]) + ' : '+ str(value_list[i]))

    return render(request, 'result.html', {
        'text':text,
        'textcount':textcount,
        'text2count':text2count,
        'wordcounts':wordcounts,
        'result':result,
    })
    