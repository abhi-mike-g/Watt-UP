from flask import Flask, render_template_string
import pathlib
app = Flask(__name__)
AUDIT = pathlib.Path('/opt/ondevice-agent/src/logs/audit.log')  # when installed to /opt

HTML = '''
<!doctype html>
<title>On-Device Agent UI</title>
<h2>On-Device Battery Agent - UI</h2>
<div>Refresh the page to see recent audit entries.</div>
<h3>Recent Audit</h3>
<pre id="audit">Loading...</pre>
<script>
async function load(){ let r=await fetch('/audit'); let j=await r.text(); document.getElementById('audit').innerText=j; }
load(); setInterval(load,5000);
</script>
'''

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/audit')
def audit():
    if not AUDIT.exists(): return 'No logs yet'
    lines = AUDIT.read_text().strip().split('\n')[-100:]
    return '\n'.join(lines)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
