import os
import sys
import django
import click
import MySQLdb
import datetime
import ToDo.settings

os.environ['DJANGO_SETTINGS_MODULE']='ToDo.settings'
sys.path.append('ToDo')
django.setup()

from todos.models import *

@click.group()
def start():
    pass

@start.command()
def populate():
    for each in range(10):
        todolist=ToDoList(name='this is some name of todolist'+str(each+1),created=datetime.datetime.now())
        todolist.save()
        for a in range(5):
            todoitem=ToDoItem(desc='some random desc'+str(a+1),due_date=datetime.date(2016,8,20),completed=False,todolist=todolist)
            todoitem.save()
        print 'succesfully added one todo list'


@start.command()
@click.argument('dbname')
@click.argument('username')
@click.argument('password')
def drop(dbname, username, password):
    connection=MySQLdb.connect(user=username,passwd=password)
    cursor=connection.cursor()
    cursor.execute('use '+dbname)
    cursor.execute('DELETE FROM todos_todoitem')
    cursor.execute('DELETE FROM todos_todolist')

    connection.commit()
    click.echo('Successfully deleted data')


start()