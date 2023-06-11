from django.views.generic import CreateView, ListView, DeleteView, DetailView
from django.http import HttpRequest, HttpResponse
from typing import Any
from .models import Blog, Post, Comment
from django.urls import reverse_lazy


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'create_blog.html'
    fields = (
        "author",
        "title",
    )
    success_url = reverse_lazy('create_post')

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.get_form()
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class PostCreateView(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = (
        "blog",
        "author",
        "title",
        "body",
    )
    success_url = reverse_lazy('post_list')

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.get_form()
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class PostListView (ListView):
    model = Post
    template_name = "post_list.html"


class PostInsideView(DetailView):
    model = Post
    template_name = "inside_post.html"


class PostDeleteView (DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("post_list")


class CommentCreateView(CreateView):
    model = Comment
    template_name = "create_comment.html"
    success_url = reverse_lazy("post_list")

    fields = (
        "post",
        "author",
        "body",
    )

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class CommentListView(ListView):
    model = Comment
    template_name = "comment_list.html"









