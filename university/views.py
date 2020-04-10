from django.http import HttpResponse
from django.template import loader
import mysql.connector


def index(request):

    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))


def database(request):

    mydb = mysql.connector.Connect(
        host = "localhost",
        user = "root",
        passwd = "Clarkson",
        auth_plugin = "mysql_native_password",
        database = "university"
    )
    cursor = mydb.cursor(dictionary=True)

    sql = """
    SELECT * FROM instructor
        WHERE salary > 90000;
"""
    cursor.execute(sql)


    template = loader.get_template("query_forum.html")
    context = {
        "show_id":True,
        "show_name":True,
        "show_dept":True,
        "show_salary":False,
        "data":cursor}
    return HttpResponse(template.render(context, request))