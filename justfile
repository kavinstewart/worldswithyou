build:
    python3 tools/build.py

check:
    python3 tools/check.py public

serve:
    python3 -m http.server 4173 --bind 127.0.0.1 --directory public
