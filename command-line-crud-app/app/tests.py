from django.test import TestCase
from app import models


# Create your tests here.
class Testcharacters(TestCase):
    def test_add_character(self):
        character = models.add_character(
            "Monkey D. Luffy",
            19,
            "Gomu Gomu No Mi",
            "Eiichiro Oda",
            "One Piece",
        )

        self.assertEqual(character.id, 1)
        self.assertEqual(character.name, "Monkey D. Luffy")
        self.assertEqual(character.age, 19)
        self.assertEqual(character.main_power, "Gomu Gomu No Mi")
        self.assertEqual(character.creator, "Eiichiro Oda")
        self.assertEqual(character.property, "One Piece")

    def test_view_all(self):
        characters_Data = [
            {
                "name": "Monkey D. Luffy",
                "age": 19,
                "main_power": "Gomu Gomu No Mi",
                "creator": "Eiichiro Oda",
                "property": "One Piece",
            },
            {
                "name": "Roronoa Zoro",
                "age": 21,
                "main_power": "Haki",
                "creator": "Eiichiro Oda",
                "property": "One Piece",
            },
            {
                "name": "Gordon Freeman",
                "age": 47,
                "main_power": "Crowbar",
                "creator": "Valve",
                "property": "Half-Life",
            },
            {
                "name": "Batman",
                "age": 48,
                "main_power": "Being Rich",
                "creator": "DC Comics",
                "property": "Batman",
            },
        ]
        for character_Data in characters_Data:
            models.add_character(
                character_Data["name"],
                character_Data["age"],
                character_Data["main_power"],
                character_Data["creator"],
                character_Data["property"],
            )

        characters = models.view_All()

        self.assertEqual(len(characters), len(characters_Data))

        characters_Data = sorted(characters_Data, key=lambda c: c["name"])
        characters = sorted(characters, key=lambda c: c.name)

        for data, character in zip(characters_Data, characters):
            self.assertEqual(data["name"], character.name)
            self.assertEqual(data["age"], character.age)
            self.assertEqual(data["main_power"], character.main_power)
            self.assertEqual(data["creator"], character.creator)
            self.assertEqual(data["property"], character.property)

    def test_can_search_by_name(self):
        characters_Data = [
            {
                "name": "Monkey D. Luffy",
                "age": 19,
                "main_power": "Gomu Gomu No Mi",
                "creator": "Eiichiro Oda",
                "property": "One Piece",
            },
            {
                "name": "Roronoa Zoro",
                "age": 21,
                "main_power": "Haki",
                "creator": "Eiichiro Oda",
                "property": "One Piece",
            },
            {
                "name": "Gordon Freeman",
                "age": 47,
                "main_power": "Crowbar",
                "creator": "Valve",
                "property": "Half-Life",
            },
            {
                "name": "Batman",
                "age": 48,
                "main_power": "Being Rich",
                "creator": "DC Comics",
                "property": "Batman",
            },
        ]
        for character_Data in characters_Data:
            models.add_character(
                character_Data["name"],
                character_Data["age"],
                character_Data["main_power"],
                character_Data["creator"],
                character_Data["property"],
            )

        self.assertIsNone(models.view_by_character_name("sssss"))

        character = models.view_by_character_name("Monkey D. Luffy")

        self.assertIsNotNone(character)
        self.assertEqual(character.creator, "Eiichiro Oda")

    def test_view_by_dev(self):
        characters_Data = [
            {
                "name": "Monkey D. Luffy",
                "age": 19,
                "main_power": "Gomu Gomu No Mi",
                "creator": "Eiichiro Oda",
                "property": "One Piece",
            },
            {
                "name": "Roronoa Zoro",
                "age": 21,
                "main_power": "Haki",
                "creator": "Eiichiro Oda",
                "property": "One Piece",
            },
            {
                "name": "Gordon Freeman",
                "age": 47,
                "main_power": "Crowbar",
                "creator": "Valve",
                "property": "Half-Life",
            },
            {
                "name": "Batman",
                "age": 48,
                "main_power": "Being Rich",
                "creator": "DC Comics",
                "property": "Batman",
            },
        ]
        for character_Data in characters_Data:
            models.add_character(
                character_Data["name"],
                character_Data["age"],
                character_Data["main_power"],
                character_Data["creator"],
                character_Data["property"],
            )
        self.assertEqual(len(models.view_by_creator("Eiichiro Oda")), 2)

    def test_update_creator(self):
        characters_Data = [
            {
                "name": "Monkey D. Luffy",
                "age": 19,
                "main_power": "Gomu Gomu No Mi",
                "creator": "Eiichiro Oda",
                "property": "One Piece",
            },
            {
                "name": "Roronoa Zoro",
                "age": 21,
                "main_power": "Haki",
                "creator": "Eiichiro Oda",
                "property": "One Piece",
            },
            {
                "name": "Gordon Freeman",
                "age": 47,
                "main_power": "Crowbar",
                "creator": "EA",
                "property": "Half-Life",
            },
            {
                "name": "Batman",
                "age": 48,
                "main_power": "Being Rich",
                "creator": "DC Comics",
                "property": "Batman",
            },
        ]
        for character_Data in characters_Data:
            models.add_character(
                character_Data["name"],
                character_Data["age"],
                character_Data["main_power"],
                character_Data["creator"],
                character_Data["property"],
            )
        models.update_creator("Gordon Freeman", "Valve")

        self.assertEqual(
            models.view_by_character_name("Gordon Freeman").creator, "Valve"
        )

    def test_delete_character(self):
        characters_Data = [
            {
                "name": "Monkey D. Luffy",
                "age": 19,
                "main_power": "Gomu Gomu No Mi",
                "creator": "Eiichiro Oda",
                "property": "One Piece",
            },
            {
                "name": "Roronoa Zoro",
                "age": 21,
                "main_power": "Haki",
                "creator": "Eiichiro Oda",
                "property": "One Piece",
            },
            {
                "name": "Gordon Freeman",
                "age": 47,
                "main_power": "Crowbar",
                "creator": "EA",
                "property": "Half-Life",
            },
            {
                "name": "Batman",
                "age": 48,
                "main_power": "Being Rich",
                "creator": "DC Comics",
                "property": "Batman",
            },
        ]
        for character_Data in characters_Data:
            models.add_character(
                character_Data["name"],
                character_Data["age"],
                character_Data["main_power"],
                character_Data["creator"],
                character_Data["property"],
            )

        models.delete_character("Roronoa Zoro")

        self.assertEqual(len(models.view_All()), 3)
