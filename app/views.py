from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *

# Create your views here.



# FUNCTION BASED VIEW as  return the string
def fbv_string(request):
    return HttpResponse(' FUNCTION BASED VIEW as  return the string')

# CLASS BASED VIEW as  return the String
class CBV_string(View):
    def get(self, request):
        return HttpResponse(' CLASS CLASS BASED VIEW as return the string')


# FUNCTION BASED VIEW as  return the HTML_PAGE  
def fbv_html(request):
    return render(request,'fbv_html.html')

# CLASS BASED VIEW as  return the HTML_PAGE
class CBV_HTML(View):
    def get(self, request):
        return render(request,'CBV_HTML.html')
    
#FUNCTION BASED VIEW as return the HTML_PAGE TO FORM
def fbv_FORMS(request):
    SFD=StudentForm()
    d={'SFD':SFD}
    if request.method == 'POST':
        SFO=StudentForm(request.POST)
        if SFO.is_valid():
            SFO.save()
            return HttpResponse('Data Is Submitted Successfully')
    return render(request,'fbv_FORMS.html',d)

#CLASS BASED VIEW as return the HTML_PAGE TO FORM
class CBV_FORMS(View):
    def get(self, request):
        CSD=StudentForm()
        d={'CSD':CSD}
        return render(request,'CBV_FORMS.html',d)
    def post(self, request):
        if request.method == 'POST':
            SFD=StudentForm(request.POST)
            if SFD.is_valid():
                SFD.save()
                return HttpResponse('Data Is Saved')
