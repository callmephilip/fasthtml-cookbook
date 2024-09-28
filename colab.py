import os, time, re
from urllib.parse import urlparse
from typing import Optional
from fasthtml.jupyter import *

class ColabFriendlyJupyUvi(JupyUvi):
  def start(self, url="http://localhost:8000",max_attempts=5,initial_delay=1,out="tunnel.log") -> Optional[str]:
    super(ColabFriendlyJupyUvi, self).start()
    try:
      import google.colab

      # setup cloudflare tunnel: https://pkg.cloudflare.com/index.html
      installation_script = """
      sudo mkdir -p --mode=0755 /usr/share/keyrings
      curl -fsSL https://pkg.cloudflare.com/cloudflare-main.gpg | sudo tee /usr/share/keyrings/cloudflare-main.gpg >/dev/null
      echo 'deb [signed-by=/usr/share/keyrings/cloudflare-main.gpg] https://pkg.cloudflare.com/cloudflared focal main' | sudo tee /etc/apt/sources.list.d/cloudflared.list
      sudo apt-get update && sudo apt-get install cloudflared
      """
      if os.system("cloudflared --version") != 0: os.system(installation_script)
      os.system(f"nohup cloudflared tunnel --url {url} > {out} 2>&1 &")
      time.sleep(5)
      attempt = 0
      delay = initial_delay

      while attempt < max_attempts:
          try:
              with open(out) as f:
                for l in f.read().split("\n"):
                  print(l)
                  log_entry = l
                  url_pattern = r"https?://[^\s]*trycloudflare\.com[^\s]*"
                  url_match = re.search(url_pattern, log_entry)
                  if url_match: return urlparse(url_match.group(0)).hostname
                raise ValueError("URL not found")
          except:
              attempt += 1
              if attempt < max_attempts:
                  time.sleep(delay)
                  delay *= 2  # Exponential backoff
              else: return None
    except: return None
