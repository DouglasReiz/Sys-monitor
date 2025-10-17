from flask import Flask, render_template, jsonify
import psutil, time, threading, webbrowser

app = Flask(__name__)
last_net = psutil.net_io_counters()
last_time = time.time()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/metrics')
def metrics():
    global last_net, last_time
    cpu = psutil.cpu_percent(interval=None)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    now_net = psutil.net_io_counters()
    now_time = time.time()
    elapsed = now_time - last_time if now_time > last_time else 1
    upload = (now_net.bytes_sent - last_net.bytes_sent) / elapsed / 1024
    download = (now_net.bytes_recv - last_net.bytes_recv) / elapsed / 1024
    last_net, last_time = now_net, now_time
    return jsonify({'cpu': cpu, 'memory': mem, 'disk': disk, 'upload': upload, 'download': download})

def open_browser():
    webbrowser.open("http://localhost:5000")

if __name__ == '__main__':
    threading.Timer(1.5, open_browser).start()
    app.run(host='0.0.0.0', port=5000)
