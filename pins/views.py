from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CreatePinForm, EditPinForm , SaveToBoard, CommentForm
from .models import Pin, Comment
from boards.models import Board
from accounts.forms import EditProfileForm
from accounts.models import User, Follow
from django.urls import reverse_lazy, reverse
from django.template.defaultfilters import slugify
from django.db.models import Q









class PinCreateView(LoginRequiredMixin, CreateView):
    form_class=CreatePinForm
    template_name='create_pin.html'
    success_url=reverse_lazy('pinterest:home')

    
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        form.instance.slug=slugify(form.instance.title)
        return super().form_valid(form)



@login_required
def edit_pin(request, id):
    pin = get_object_or_404(Pin, id=id)
    if request.method == 'POST' and request.user == pin.user:
        form = EditPinForm(request.user, request.POST, instance=pin)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            board = Board.objects.filter(id=instance.board.id).first()
            instance.save()
            board.pins.add(instance)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def delete_pin(request, id):
    pin = get_object_or_404(Pin, id=id)
    if request.user == pin.user:
        pin.delete()
    return redirect('accounts:profile', request.user.username)


@login_required
def add_comment(request, id):
    pin = get_object_or_404(Pin, id=id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.pin = pin
            instance.user = request.user
            instance.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id).delete()
    return redirect(request.META.get('HTTP_REFERER'))


def get_related_pins(id):
    related_pins = []
    # get all boards
    boards = Board.objects.prefetch_related('pins').all() 
    # get all boards that contains the current pin
    related_board = [
        board for board in boards if board.pins.filter(id=id).first()
    ] 
    # get all pins in related boards,
    # The output may be a nested list of queryset objects
    related_pins_lists = [board.pins.all() for board in related_board]
    # make ONE list of all pins
    for i in range(len(related_pins_lists)):
        for p in related_pins_lists[i]:
            related_pins.append(p)
    # remove current pin from related pins
    get_cuurent_pin = [
        related_pins.remove(pin) for pin in related_pins if pin.id == id
    ]
    return set(related_pins)


def pin_detail(request, slug):
    template_name = "pin_detail.html"
    pin = get_object_or_404(Pin, slug=slug)
    related_pins=Pin.objects.filter(
            Q(title__icontains=pin.board.title)|
            Q(description__icontains=pin.title)|
            Q(board__title=pin.board.title)
            
        )
    comment_form = CommentForm()
    comments=Comment.objects.select_related('user__profile').filter(pin=pin)
    return render(
        request,
        template_name,
        {
            "pin": pin,
            "comments": comments,
            
            "comment_form": comment_form,
            'related_pins':related_pins,
        },
    )


def created_pins(request, username):
    user = get_object_or_404(User, username=username)
    created_pins = user.pin_user.all()
    is_following = request.user.followers.filter(following=user).first() if request.user.is_authenticated else None
    context = {
        'created_pins': created_pins,
        'user': user,
        'is_following': is_following
    }
    return render(request, 'profile.html', context)