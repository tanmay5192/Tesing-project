from django.shortcuts import render
from project import forms


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

# def contact(request):
#     return render(request,'contact.html')

def student_form(request):
    form=forms.studentform()
    if request.method =='POST':
        form=forms.studentform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('form data inserted into database successfully')
            return render(request, 'thanks.html', {'name': form.cleaned_data['name']})
    return render (request,'contact.html',{'form':form})