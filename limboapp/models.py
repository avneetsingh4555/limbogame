from django.db import models

# class Message(models.Model):
#     username = models.CharField(max_length=255)
#     room = models.CharField(max_length=255)
#     content = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#     myList = models.TextField(null=True)

    # class Meta:
    #     ordering = ('date_added',)


class Player(models.Model):
    username1 = models.CharField(max_length=255)
    username2 = models.CharField(max_length=255)
    current_turn = models.CharField(max_length=255)
    player1_cards= models.TextField(null=True)
    player2_cards= models.TextField(null=True)
    roomid = models.CharField(max_length=255)
    total_cards=models.TextField(null=True)
    used_cards=models.TextField(null=True)
    remaining_cards=models.TextField(null=True)

    # content = models.TextField()
    # date_added = models.DateTimeField(auto_now_add=True)
    # myList = models.TextField(null=True)

    # class Meta:
    #     room_name = ('room_name',)        