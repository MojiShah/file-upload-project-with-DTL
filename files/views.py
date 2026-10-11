from django.shortcuts import render,redirect,get_object_or_404
from django.http import FileResponse
from .models import File
from django.core.paginator import Paginator
from django.db.models import Q

IMAGE_EXTENSIONS = ( ".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg",)

# Create your views here.

def file_list(request):
    files = File.objects.all()
    
    #1. Search
    query = request.GET.get("q","").strip()
    if query:
        files = files.filter(file__icontains=query)
    
    #2. Filter by file type
    file_type = request.GET.get("type","all")
    image_query = Q()
    
    for extension in IMAGE_EXTENSIONS:
        image_query |= Q(file__iendswith=extension)
        
    if file_type == "image":
        files = files.filter(image_query)
    elif file_type == "other":
        files = files.exclude(image_query)
    else:
        file_type = "all"
        
    #3. ordering
    sort = request.GET.get("sort","newest")
    if sort == "oldest":
        files = files.order_by("uploaded_at","id")
    else:
        sort = "newest"
        files = files.order_by("-uploaded_at","-id")
    
    #4.pagination
    paginator = Paginator(files,5)
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        "page_obj" : page_obj,
        "query" : query,
        "file_type" : file_type,
        "sort" : sort
    }
    
    return render(request,"files/file_upload.html",context)

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

def file_download(request,file_id):
    file = get_object_or_404(File,id=file_id)
    file.file.open("rb")
    return FileResponse(file.file,as_attachment=True,filename=file.file.name.split("/")[-1])

def file_update(request,file_id):
    file = get_object_or_404(File,id=file_id)
    if request.method == "POST":
        uploaded_file = request.FILES.get("file")
        if uploaded_file:
            old_file_name = file.file.name
            file.file=uploaded_file
            file.save(update_fields=["file"])
            file.file.storage.delete(old_file_name)
        return redirect(file_detail,file_id=file.id)
    return render(request,'files/file-update.html',{"file":file})

def file_delete(request,file_id):
    file = get_object_or_404(File,id=file_id)
    if request.method == "POST":
        file.file.delete(save=False)
        file.delete()
    return redirect("file_list")

