from django.shortcuts import render
from .models import Video
from .forms import VideoForm


def video_list(request):
    return render(request,'video/video_list.html',{
        'video_list' : Video.objects.all(),
    })

def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'video/video_detail.html', {
        'video' : video,
    })

def video_new(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save()
            return redirect('video:list')
    else:
        form = VideoForm()
    return render(request, 'video/video_new.html',{
        'form' : form,
    })
# Create your views here.
