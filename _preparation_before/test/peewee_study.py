# *.* coding = utf-8 *.*


#Mdel Definition
from peewee import *
db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()           #str
    birthday = DateField()       #日期
    is_relative = BooleanField() #判断，是否是relative的

    class Meta:
        database = db #这里用的是people.db database

class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db #this model uses the 'people.db' database

#Storing data
# db.create_tables([Person, Pet])#直接创建，不需要繁琐的过程

#you can use .save() to store
from datetime import date
uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
uncle_bob.save() # bob is now stored in the database
#直接用.create()来insert
grandma = Person.create(name = 'Grandma',
                        birthday = date(1935, 3, 1),
                        is_relative = True)
herb = Person.create(name = 'Herb',
                     birthday = date(1950,5,5),
                     is_relative = True)
#直接引用属性然后.save()保存改变属性
grandma.name = 'Grandama L.'
grandma.save()



























































