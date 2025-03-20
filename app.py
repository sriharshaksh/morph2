from django.shortcuts import HttpResponse
import os, datetime, subprocess

def htop(request):
    name = "Your Full Name"
    username = os.getlogin()
    ist_time = datetime.datetime.now(datetime.timezone.utc).astimezone(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    top_output = subprocess.getoutput("top -bn1 | head -20")
    
    response = f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time (IST): {ist_time}</h3>
    <pre>{top_output}</pre>
    """
    return HttpResponse(response)




