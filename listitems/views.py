from ILBe.settings import MEDIA_ROOT
from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, ListView
from listitems.models import Item, Owner
from listitems.forms import RegisterForm, RequestForm
import requests
import os
import datetime


class IndexView(ListView):
    def get(self, request, *args, **kwargs):
        if request.GET.get('left') == "1":
            items = Item.objects.filter(left_or_unknown="1")
            return render(request, 'listitems/index.html', {
            'items': items
        })
        elif request.GET.get('unknown') == "2":
            items = Item.objects.filter(left_or_unknown="2")
            return render(request, 'listitems/index.html', {
            'items': items
        })
        elif request.GET.get('past') == "3":
            items = Item.objects.all()
            past_items = []
            for item in items:
                past = item.deadline - datetime.date.today()
                if past.days < 0:
                    past_items.append(item)
            return render(request, 'listitems/index.html', {
            'items': past_items
        })
        else:
            items = Item.objects.all()
            return render(request, 'listitems/index.html', {
                'items': items
            })

class ItemDetail(DetailView):
    template_name = 'listitems/detail.html'
    model = Item

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm(request.POST or None)
        return render(request, 'listitems/register.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            owner = Owner()
            owner.save()
            # 物品の新規登録
            item = Item()
            item.founder = form.cleaned_data['founder']
            item.name = form.cleaned_data['name']
            item.photo = form.cleaned_data['photo']
            item.left_or_unknown = form.cleaned_data['left_or_unknown']
            item.comment = form.cleaned_data['comment']

#             owner = Owner()
#             owner.save()

            item.owner = owner
            item.save()
            #LINE Notify
            if form.cleaned_data['left_or_unknown'] == 1:
                self.notify(item)
            return HttpResponseRedirect('..')
        else:
            form = RegisterForm()
        #フォーム画面に不備があった場合、空のフォーム画面を表示
        return render(request, 'listitems/register.html', {
            'form': form
        })
    
    # LINENotifyでメッセージを送信
    def notify(self, item):
        url = "https://notify-api.line.me/api/notify"
        access_token = '30w9y6bbseumxqyxCOR3x8rrTzkx9La2oPM5OBR0wu2' # 自分
        # access_token = 'jiNDx4y3h0ja9y9nUPqkqfwAQ6ORl4WX6vAahP4WDZb' // たいし達とのチャット
        ilbe_link = 'http://127.0.0.1:8000/detail/'+str(item.id)+'/'
        headers = {'Authorization': 'Bearer ' + access_token}
        message = item.founder+'さんが'+item.name+'を忘れ物登録しました。\n'+ilbe_link
        image = os.path.join(MEDIA_ROOT, item.photo.name) # png or jpg
        payload = {'message': message}
        files = {'imageFile': open(image, 'rb')}
        r = requests.post(url, headers=headers, params=payload, files=files,)

class RequestView(View):
    def get(self, request, *args, **kwargs):
        item = Item.objects.get(id=self.kwargs['pk'])
        form = RequestForm(request.POST or None)
        return render(request, 'listitems/request.html', {
            'form': form,
            'item': item,
        })

    def post(self, request, *args, **kwargs):
        form = RequestForm(request.POST)
        if form.is_valid():
            # 申請者の登録
            owner = Owner()
            owner.name = form.cleaned_data['name']
            owner.number = form.cleaned_data['number']
            owner.comment = form.cleaned_data['comment']
            owner.save()
            # 物品との紐付け
            item = Item.objects.get(id=self.kwargs['pk'])
            item.owner = owner
            item.save()
            return HttpResponseRedirect('../../')
        else:
            form = RequestForm()
        #フォーム画面に不備があった場合、空のフォーム画面を表示
        return render(request, 'listitems/request.html', {
            'form': form
        })