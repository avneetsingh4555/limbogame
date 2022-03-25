# from _typeshed import ReadableBuffer
from django.db.models.fields import NullBooleanField
from django.shortcuts import render
import random
from .models import Player 
from django.http import HttpResponse, request


import  json

from django.db import connections
def index(request):
    return render(request, 'game/index.html')

def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    Total_cards=['AH','2H','3H','4H','5H', '6H','7H','8H','9H','10H','JH','QH','KH','AD','2D','3D','4D','5D', '6D','7D','8D','9D','10D','JD','QD','KD','AC','2C','3C','4C','5C', '6C','7C','8C','9C','10C','JC','QC','KC', 'AS','2S','3S','4S','5S', '6S','7S','8S','9S','10S','JS','QS','KS']
    if(Player.objects.filter(roomid=room_name).exists()):
        w1 = Player.objects.filter(roomid=room_name)
        player1_cards=w1[0].player1_cards
        player2_cards=[]
        while True:
            if len(player2_cards)==5:
                break
            index=random.randint(0,len(Total_cards)-1)
            no=Total_cards[index]
            if no not in player2_cards and no not in player1_cards:
                player2_cards.append(no)

        remaining_cards= []
        for i in Total_cards:
            if i not in player1_cards and i not in player2_cards:
                remaining_cards.append(i)
                
        print(remaining_cards)
        w1 = Player.objects.filter(roomid=room_name).update(
        username2=username,player2_cards=player2_cards,remaining_cards=remaining_cards)
        current_turn=2
        return render(request, 'game/room.html',{'room_name':room_name,'username':username,'player2_cards':player2_cards,'w1':current_turn})

        


    else:
        current_turn=1
        player1_cards= []
        while True:
            if len(player1_cards)==5:
                break
            index=random.randint(0,len(Total_cards)-1)
            no=Total_cards[index]
            if no not in player1_cards:
                player1_cards.append(no)

        remaining_cards=list(set(Total_cards)-set(player1_cards))
        used_cards=''
        g = Player(username1=username,roomid=room_name,used_cards=used_cards,player1_cards=player1_cards,current_turn=current_turn,remaining_cards=remaining_cards)
        g.save()
        w1 = Player.objects.filter(roomid=room_name)
        w1=w1[0].current_turn

        return render(request, 'game/room.html',{'room_name':room_name,'username':username,'player1_cards':player1_cards,'w1':w1})

    
    return render(request, 'game/room.html',)

def upload(request):
    
    if request.method == 'GET':
        rdata=request.POST['rdata']
        pt=Player.objects.filter(roomid=rdata)
        a=[pt[0].used_cards]
        
        return HttpResponse(json.dumps(a), content_type="application/json")    