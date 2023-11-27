from django.db import models


# Create your models here.
class characters(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    main_power = models.TextField()
    creator = models.TextField()
    property = models.TextField()


def add_character(name, age, powers, creator, property):
    character = characters(
        name=name, age=age, main_power=powers, creator=creator, property=property
    )
    character.save()
    return character


def view_All():
    character = characters.objects.all()
    return character


def view_by_creator(creator):
    character = characters.objects.filter(creator=creator)
    return character


def view_by_character_name(character_name):
    try:
        character = characters.objects.get(name=character_name)
        return character
    except:
        return None


def update_creator(character_name, new_creator):
    character = characters.objects.get(name=character_name)
    character.creator = new_creator
    character.save()
    return character


def delete_character(character_name):
    character = characters.objects.get(name=character_name)
    character.delete()
    return character
