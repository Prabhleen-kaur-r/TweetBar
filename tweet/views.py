from django.shortcuts import render, redirect, get_object_or_404
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):

    if request.user.is_authenticated:
        return redirect('tweet_list')

    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})


@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})


@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)

    return render(request, 'tweet_form.html', {'form': form})


@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')

    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})



@login_required
def like_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    
    if request.user in tweet.dislikes.all():
        tweet.dislikes.remove(request.user)
    
    if request.user in tweet.likes.all():
        tweet.likes.remove(request.user)  
    else:
        tweet.likes.add(request.user)  
    
    return HttpResponseRedirect(reverse('tweet_list'))


@login_required
def dislike_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    
    if request.user in tweet.likes.all():
        tweet.likes.remove(request.user)
    
    if request.user in tweet.dislikes.all():
        tweet.dislikes.remove(request.user)   
    else:
        tweet.dislikes.add(request.user)  
    
    return HttpResponseRedirect(reverse('tweet_list'))