#!/usr/bin/python3
"""
Test suite for console
"""
import sys
import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO


class TestConsole(unittest.TestCase):
    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertEqual('Prints the string representation of an \
instance based on the class name and id.\n', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        self.assertEqual('Creates a new instance of a given \
class, saves it (to the JSON file) and prints the id.\n', f.getvalue())

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        self.assertIsInstance(f.getvalue(), str)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1111")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1111")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        self.assertIsInstance(f.getvalue(), str)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
        self.assertIsInstance(f.getvalue(), str)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1111")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        model_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {model_id}")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {model_id} first")
        self.assertEqual(f.getvalue(), '** value missing **\n')

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        self.assertEqual(f.getvalue(), '')

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        self.assertEqual(f.getvalue(), '\n')

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
        self.assertEqual(f.getvalue(), '')

    def test_basedotall(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
        self.assertNotIn('[City]', f.getvalue())
        self.assertNotIn('[Review]', f.getvalue())
        self.assertNotIn('[Place]', f.getvalue())
        self.assertNotIn('[Amenity]', f.getvalue())
        self.assertNotIn('[State]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all")
        self.assertIn('**', f.getvalue())

    def test_reviewdotall(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
        self.assertNotIn('[BaseModel]', f.getvalue())
        self.assertNotIn('[User]', f.getvalue())
        self.assertNotIn('[State]', f.getvalue())
        self.assertNotIn('[Place]', f.getvalue())
        self.assertNotIn('[City]', f.getvalue())
        self.assertNotIn('[Amenity]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all")
        self.assertIn('**', f.getvalue())

    def test_userdotall(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
        self.assertNotIn('[BaseModel]', f.getvalue())
        self.assertNotIn('[City]', f.getvalue())
        self.assertNotIn('[Review]', f.getvalue())
        self.assertNotIn('[Place]', f.getvalue())
        self.assertNotIn('[Amenity]', f.getvalue())
        self.assertNotIn('[State]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all")
        self.assertIn('**', f.getvalue())

    def test_statedotall(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
        self.assertNotIn('[BaseModel]', f.getvalue())
        self.assertNotIn('[City]', f.getvalue())
        self.assertNotIn('[Review]', f.getvalue())
        self.assertNotIn('[Place]', f.getvalue())
        self.assertNotIn('[Amenity]', f.getvalue())
        self.assertNotIn('[User]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all")
        self.assertIn('***', f.getvalue())

    def test_placedotall(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
        self.assertNotIn('[BaseModel]', f.getvalue())
        self.assertNotIn('[City]', f.getvalue())
        self.assertNotIn('[Review]', f.getvalue())
        self.assertNotIn('[State]', f.getvalue())
        self.assertNotIn('[Amenity]', f.getvalue())
        self.assertNotIn('[User]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all")
        self.assertIn('**', f.getvalue())

    def test_amenitydotall(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
        self.assertNotIn('[BaseModel]', f.getvalue())
        self.assertNotIn('[City]', f.getvalue())
        self.assertNotIn('[Review]', f.getvalue())
        self.assertNotIn('[Place]', f.getvalue())
        self.assertNotIn('[State]', f.getvalue())
        self.assertNotIn('[User]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all")
        self.assertIn('**', f.getvalue())

    def test_citydotall(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
        self.assertNotIn('[BaseModel]', f.getvalue())
        self.assertNotIn('[State]', f.getvalue())
        self.assertNotIn('[Review]', f.getvalue())
        self.assertNotIn('[Place]', f.getvalue())
        self.assertNotIn('[Amenity]', f.getvalue())
        self.assertNotIn('[User]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all")
        self.assertIn('**', f.getvalue())

    def test_basedotcount(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
        self.assertIsInstance(int(f.getvalue().strip()), int)

    def test_userdotcount(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
        self.assertIsInstance(int(f.getvalue().strip()), int)

    def test_statedotcount(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
        self.assertIsInstance(int(f.getvalue().strip()), int)

    def test_placedotcount(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
        self.assertIsInstance(int(f.getvalue().strip()), int)

    def test_citydotcount(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
        self.assertIsInstance(int(f.getvalue().strip()), int)

    def test_amenitydotcount(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
        self.assertIsInstance(int(f.getvalue().strip()), int)

    def test_reviewdotcount(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
        self.assertIsInstance(int(f.getvalue().strip()), int)

    def test_basedotshow(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show({model_id})")
        self.assertIn('[BaseModel]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_userdotshow(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show({model_id})")
        self.assertIn('[User]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_citydotshow(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.show()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.show({model_id})")
        self.assertIn('[City]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.show(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_statedotshow(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.show()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show({model_id})")
        self.assertIn('[State]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_placedotshow(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.show()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show({model_id})")
        self.assertIn('[Place]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_amenitydotshow(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.show()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show({model_id})")
        self.assertIn('[Amenity]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_reviewdotshow(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.show()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show({model_id})")
        self.assertIn('[Review]', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_reviewdotdestroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.destroy()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.destroy({model_id})")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show({model_id})")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.destroy(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_basedotdestroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.destroy({model_id})")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show({model_id})")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.destroy(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_userdotdestroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.destroy({model_id})")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show({model_id})")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.destroy(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_placedotdestroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.destroy()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.destroy({model_id})")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show({model_id})")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.destroy(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_statedotdestroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.destroy()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.destroy({model_id})")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show({model_id})")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.destroy(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_citydotdestroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.destroy()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.destroy({model_id})")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.show({model_id})")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.destroy(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_amenitydotdestroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.destroy()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.destroy({model_id})")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show({model_id})")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.destroy(idf)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_basedotupdate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update(1111)")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update({model_id})")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update({model_id}, first)")
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update({model_id}, first, 3)")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show({model_id})")
        self.assertIn('first', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update({model_id},\
{{'second': 5, 'third': three}})")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show({model_id})")
        self.assertIn('third', f.getvalue())
        self.assertIn('second', f.getvalue())

    def test_userdotupdate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update(1111)")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update({model_id})")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update({model_id}, first)")
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update({model_id}, first, 3)")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show({model_id})")
        self.assertIn('first', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update({model_id},\
{{'second': 5, 'third': three}})")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show({model_id})")
        self.assertIn('third', f.getvalue())
        self.assertIn('second', f.getvalue())

    def test_placedotupdate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.update(1111)")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update({model_id})")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update({model_id}, first)")
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update({model_id}, first, 3)")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show({model_id})")
        self.assertIn('first', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update({model_id},\
{{'second': 5, 'third': three}})")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show({model_id})")
        self.assertIn('third', f.getvalue())
        self.assertIn('second', f.getvalue())

    def test_statedotupdate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.update(1111)")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.update({model_id})")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.update({model_id}, first)")
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.update({model_id}, first, 3)")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show({model_id})")
        self.assertIn('first', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.update({model_id},\
{{'second': 5, 'third': three}})")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show({model_id})")
        self.assertIn('third', f.getvalue())
        self.assertIn('second', f.getvalue())

    def test_citydotupdate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.update(1111)")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.update({model_id})")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.update({model_id}, first)")
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.update({model_id}, first, 3)")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.show({model_id})")
        self.assertIn('first', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.update({model_id},\
{{'second': 5, 'third': three}})")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.show({model_id})")
        self.assertIn('third', f.getvalue())
        self.assertIn('second', f.getvalue())

    def test_amenitydotupdate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.update(1111)")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.update({model_id})")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.update({model_id}, first)")
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.update({model_id}, first, 3)")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show({model_id})")
        self.assertIn('first', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.update({model_id},\
{{'second': 5, 'third': three}})")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show({model_id})")
        self.assertIn('third', f.getvalue())
        self.assertIn('second', f.getvalue())

    def test_reviewdotupdate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.update()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.update(1111)")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.update({model_id})")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.update({model_id}, first)")
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.update({model_id}, first, 3)")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show({model_id})")
        self.assertIn('first', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.update({model_id},\
{{'second': 5, 'third': three}})")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show({model_id})")
        self.assertIn('third', f.getvalue())
        self.assertIn('second', f.getvalue())
