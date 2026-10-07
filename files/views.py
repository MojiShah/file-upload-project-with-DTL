from django.shortcuts import render,redirect,get_object_or_404
from .models import File

# Create your views here.

def file_list(request):
    files = File.objects.all().order_by("-uploaded_at")
    return render(request,"files/file_upload.html",{"files": files})

# def file_upload(request):
#     if request.method == "POST":
#         uploaded_file = request.FILES.get('file');
#         if uploaded_file:
#             File.objects.create(file=uploaded_file)
            
#         return redirect('file_upload')
    
#     files = File.objects.all().order_by('-uploaded_at');
#     return render(request=request,template_name='files/file_upload.html',context={"files":files})
    
# def delete_file(request,file_id):
#     if request.method == "POST":
#         file = File.objects.get(id=file_id);
#         # remove from media folder
#         file.file.delete(save=False);
#         #remove from db
#         file.delete();
#     return redirect('file_upload')

def file_create(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get("file")
        if uploaded_file:
            File.objects.create(file=uploaded_file)
        return redirect('file_list')
    return redirect('file_list')

def file_detail(request,file_id):
    file = get_object_or_404(File,id=file_id)
    return render(request,'files/file_detail.html',{'file':file})