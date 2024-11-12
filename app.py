from flask import app

@app.route('/htop')
def htop():
    import os
    from datetime import datetime
    import subprocess
    name = "Purnajearswami Kesavapatnam"
    username = os.getlogin()
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    top_output = subprocess.getoutput("top -bn1 | head -n 10")
    return f"Name: {name}, Username: {username}, Server Time: {server_time}, Top Output: {top_output}"