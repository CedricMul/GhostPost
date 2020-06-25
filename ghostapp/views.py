from django.shortcuts import render, reverse, HttpResponseRedirect
from ghostapp.models import GPost
from ghostapp.forms import PostForm

def index(request):
    posts = GPost.objects.all()
    form = PostForm
    return render(request, 'index.html', {'posts': posts, 'form': form})

# def handle_recipe(request):
#     if request.method == 'POST':
#         form = recipe_form(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             Recipe.objects.create(
#                 title=data['title'],
#                 time_required=data['time_required'],
#                 description=data['description'],
#                 instructions=data['instructions'],
#                 author=data['author']
#             )
#             return HttpResponseRedirect(reverse('home'))

def gpost_submit(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GPost.objects.create(
                post_text = data['post_text'],
                is_boast = data['is_boast'],
                # up_votes = data['up_votes'],
                # down_votes = data['down_votes'],
                # date_and_time = data['date_and_time'],
                # total_votes = data['total_votes']
            )
            return HttpResponseRedirect(reverse('home'))

def boast_view(request):
    form = PostForm
    boasts = GPost.objects.filter(is_boast=True)
    return render(request, 'index.html', {'posts': boasts, 'form': form})

def roast_view(request):
    form = PostForm
    roasts = GPost.objects.filter(is_boast=False)
    return render(request, 'index.html', {'posts': roasts, 'form': form})

def sort_by_score(request):
    form = PostForm
    sorted_posts = GPost.objects.order_by('-total_votes')
    return render(request, 'index.html', {'posts': sorted_posts, 'form': form})

def sort_by_date(request):
    form = PostForm
    sorted_posts = GPost.objects.order_by('-date_and_time')
    return render(request, 'index.html', {'posts': sorted_posts, 'form': form})

def upvote_view(request, id):
    post = GPost.objects.get(id=id)
    post.up_votes += 1
    post.total_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('home'))

def downvote_view(request, id):
    post = GPost.objects.get(id=id)
    post.down_votes += 1
    post.total_votes -= 1
    post.save()
    return HttpResponseRedirect(reverse('home'))
