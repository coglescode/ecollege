import sys
import urllib.request

try:
    r = urllib.request.urlopen("http://127.0.0.1:8000/health/", timeout=5)
    print("OK", r.status)
    sys.exit(0)
except Exception as e:
    print("FAILED:", repr(e))
    sys.exit(1)