from flask import (
    Blueprint,
    render_template, 
    g,
    request,
    session,
    redirect,
    url_for,
    flash
)
from app import app

#
import app.config as config
import platform
import os
import psutil

# Create a document blueprint
systembp = Blueprint('systembp', __name__, url_prefix='/system')


@systembp.route('/', methods=['GET'])
def index():
    # auth page
    if not g.user:
        return redirect(url_for('login'))
    
    user = g.user

    print("="*40, "System Information", "="*40)
    uname = platform.uname()

    # Calling psutil.cpu_precent() for 4 seconds
    cpu_usage = psutil.cpu_percent(4)

    print(psutil.virtual_memory())

    return render_template(
        'pages/system/information.html',
        title=config.APP_NAME,
        description="",
        platform={
            "system": uname.system,
            "node": uname.node,
            "release": uname.release,
            "version": uname.version,
            "machine": uname.machine,
            "processor": uname.processor,
            "cpuusage": cpu_usage,
            "ramusagepercentage": psutil.virtual_memory()[2],
            "ramusage": psutil.virtual_memory()[3]/1000000000,
            "ram": psutil.virtual_memory()[0]/1000000000
        })