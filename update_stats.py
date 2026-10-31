import os
import re
import json
import urllib.request
import html

GH_USER = "shantoshdurai"
YT_CHANNEL_ID = "UCokhrwUBEeCxIgQJTmUv-JA"
YT_API_KEY = os.environ.get("YOUTUBE_API_KEY", "AIzaSyDViYz1jaDASHXT0vLf-GgAjAYXekCoU-s")
GH_TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

headers = {
    "User-Agent": "GitHub-Profile-Updater"
}
if GH_TOKEN:
    headers["Authorization"] = f"Bearer {GH_TOKEN}"

# 1. Fetch GitHub User info
public_repos = 26
followers = 6
try:
    req = urllib.request.Request(f"https://api.github.com/users/{GH_USER}", headers=headers)
    with urllib.request.urlopen(req) as resp:
        gh_user = json.loads(resp.read().decode('utf-8'))
    public_repos = gh_user.get("public_repos", 26)
    followers = gh_user.get("followers", 6)
except Exception as e:
    print(f"Notice (user info): {e}")

# 2. Fetch total stars
total_stars = 4
try:
    req = urllib.request.Request(f"https://api.github.com/users/{GH_USER}/repos?per_page=100", headers=headers)
    with urllib.request.urlopen(req) as resp:
        repos = json.loads(resp.read().decode('utf-8'))
    total_stars = sum(r.get("stargazers_count", 0) for r in repos)
except Exception as e:
    print(f"Notice (stars): {e}")

# 3. Fetch commits via GraphQL if token available
total_commits = 876
if GH_TOKEN:
    try:
        query = """
        query {
          user(login: "shantoshdurai") {
            contributionsCollection {
              totalCommitContributions
              restrictedContributionsCount
            }
          }
        }
        """
        req = urllib.request.Request(
            "https://api.github.com/graphql",
            data=json.dumps({"query": query}).encode('utf-8'),
            headers={**headers, "Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            cc = data.get("data", {}).get("user", {}).get("contributionsCollection", {})
            total_commits = cc.get("totalCommitContributions", 708) + cc.get("restrictedContributionsCount", 168)
    except Exception as e:
        print(f"Notice (GraphQL): {e}")

# 4. Fetch live YouTube subscribers
yt_subscribers = 161
try:
    yt_url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={YT_CHANNEL_ID}&key={YT_API_KEY}"
    req = urllib.request.Request(yt_url, headers={"User-Agent": "Profile-Stats"})
    with urllib.request.urlopen(req) as resp:
        yt_data = json.loads(resp.read().decode('utf-8'))
        items = yt_data.get("items", [])
        if items:
            yt_subscribers = int(items[0]["statistics"].get("subscriberCount", 161))
except Exception as e:
    print(f"Notice (YouTube): {e}")

print(f"Current Live Stats -> Repos: {public_repos}, Stars: {total_stars}, Commits: {total_commits}, Subscribers: {yt_subscribers}")

# ASCII text lines (63 lines)
art_path = os.path.join(os.path.dirname(__file__), "ascii_art.txt")
if not os.path.exists(art_path):
    # fallback to scratch file
    art_path = r"C:\Users\Dog\.gemini\antigravity\brain\96973a28-fd83-4b44-9e9c-3158ff408f94\scratch\ascii_art.txt"

with open(art_path, "r", encoding="utf-8") as f:
    ascii_lines = f.read().splitlines()

header_dash = "—" * 42 + "-—-"

rows = [
    (30, f'<tspan x="475" y="30">shantosh@durai</tspan> -{header_dash}'),
    (50, f'<tspan x="475" y="50" class="cc">. </tspan><tspan class="key">OS</tspan>:<tspan class="cc"> ........................ </tspan><tspan class="value">Windows 11, Android, Linux</tspan>'),
    (70, f'<tspan x="475" y="70" class="cc">. </tspan><tspan class="key">Role</tspan>:<tspan class="cc"> ...................... </tspan><tspan class="value">Full-Stack &amp; AI Developer</tspan>'),
    (90, f'<tspan x="475" y="90" class="cc">. </tspan><tspan class="key">Host</tspan>:<tspan class="cc"> ............................. </tspan><tspan class="value">DSU (B.Tech AI &amp; DS)</tspan>'),
    (110, f'<tspan x="475" y="110" class="cc">. </tspan><tspan class="key">Intern</tspan>:<tspan class="cc"> ............................ </tspan><tspan class="value">Maac Technologies</tspan>'),
    (130, f'<tspan x="475" y="130" class="cc">. </tspan><tspan class="key">IDE</tspan>:<tspan class="cc"> ........................ </tspan><tspan class="value">VS Code, Android Studio</tspan>'),
    (150, f'<tspan x="475" y="150" class="cc">. </tspan>'),
    (170, f'<tspan x="475" y="170" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Programming</tspan>:<tspan class="cc"> ..... </tspan><tspan class="value">Python, JavaScript, Dart</tspan>'),
    (190, f'<tspan x="475" y="190" class="cc">. </tspan><tspan class="key">Frameworks</tspan>:<tspan class="cc"> .......... </tspan><tspan class="value">React, Flutter, FastAPI, LangChain</tspan>'),
    (210, f'<tspan x="475" y="210" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Real</tspan>:<tspan class="cc"> ................. </tspan><tspan class="value">English, Tamil, Hindi</tspan>'),
    (230, f'<tspan x="475" y="230" class="cc">. </tspan>'),
    (250, f'<tspan x="475" y="250" class="cc">. </tspan><tspan class="key">Focus</tspan>:<tspan class="cc"> ................... </tspan><tspan class="value">LLM Reasoning, AI Agents</tspan>'),
    (270, f'<tspan x="475" y="270" class="cc">. </tspan><tspan class="key">Creative</tspan>:<tspan class="cc"> ................ </tspan><tspan class="value">Blender, Manim Animation</tspan>'),
    (310, f'<tspan x="475" y="310">- Contact</tspan> -{"—" * 46}-—-'),
    (330, f'<tspan x="475" y="330" class="cc">. </tspan><tspan class="key">Email</tspan>:<tspan class="cc"> ..................... </tspan><tspan class="value">shantoshdurai06@gmail.com</tspan>'),
    (350, f'<tspan x="475" y="350" class="cc">. </tspan><tspan class="key">Portfolio</tspan>:<tspan class="cc"> ............ </tspan><tspan class="value">shantoshdurai.github.io/portfolio</tspan>'),
    (370, f'<tspan x="475" y="370" class="cc">. </tspan><tspan class="key">LinkedIn</tspan>:<tspan class="cc"> ................................... </tspan><tspan class="value">santoshp123</tspan>'),
    (390, f'<tspan x="475" y="390" class="cc">. </tspan><tspan class="key">YouTube</tspan>:<tspan class="cc"> .................... </tspan><tspan class="value">@santastuffs ({yt_subscribers} subs)</tspan>'),
    (410, f'<tspan x="475" y="410" class="cc">. </tspan><tspan class="key">Location</tspan>:<tspan class="cc"> ................................ </tspan><tspan class="value">Trichy, India</tspan>'),
    (450, f'<tspan x="475" y="450">- GitHub Stats</tspan> -{"—" * 41}-—-'),
    (470, f'<tspan x="475" y="470" class="cc">. </tspan><tspan class="key">Repos</tspan>:<tspan class="cc"> .... </tspan><tspan class="value">{public_repos}</tspan> {{<tspan class="key">Public</tspan>: <tspan class="value">{public_repos}</tspan>}} | <tspan class="key">Stars</tspan>:<tspan class="cc"> ............ </tspan><tspan class="value">{total_stars}</tspan>'),
    (490, f'<tspan x="475" y="490" class="cc">. </tspan><tspan class="key">Commits</tspan>:<tspan class="cc"> ................... </tspan><tspan class="value">{total_commits:,}</tspan> | <tspan class="key">Subscribers</tspan>:<tspan class="cc"> ... </tspan><tspan class="value">{yt_subscribers}</tspan>'),
    (510, f'<tspan x="475" y="510" class="cc">. </tspan><tspan class="key">Top Projects</tspan>:<tspan class="cc">. </tspan><tspan class="value">TouchPlay, Letterbook, Phone-Local-Agent</tspan>')
]

info_lines_xml = "\n".join(row[1] for row in rows)
dark_info_block = f'<text x="475" y="30" fill="#c9d1d9">\n{info_lines_xml}\n</text>'
light_info_block = f'<text x="475" y="30" fill="#24292f">\n{info_lines_xml}\n</text>'

start_y = 20.0
line_step = 8.1
font_size = 5.7
x_pos = 15

dark_tspans = []
light_tspans = []
for i, l in enumerate(ascii_lines):
    y = start_y + i * line_step
    esc = html.escape(l)
    dark_tspans.append(f'<tspan x="{x_pos}" y="{y:.1f}">{esc}</tspan>')
    light_tspans.append(f'<tspan x="{x_pos}" y="{y:.1f}">{esc}</tspan>')

dark_ascii = f'<text x="{x_pos}" y="{start_y}" fill="#c9d1d9" class="ascii" font-size="{font_size}px">\n' + "\n".join(dark_tspans) + "\n</text>"
light_ascii = f'<text x="{x_pos}" y="{start_y}" fill="#24292f" class="ascii" font-size="{font_size}px">\n' + "\n".join(light_tspans) + "\n</text>"

svg_w = 1080
svg_h = 545

dark_svg = f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="{svg_w}px" height="{svg_h}px" font-size="16px">
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
-webkit-size-adjust: 109%;
size-adjust: 109%;
}}
.key {{fill: #ffa657;}}
.value {{fill: #a5d6ff;}}
.addColor {{fill: #3fb950;}}
.delColor {{fill: #f85149;}}
.cc {{fill: #616e7f;}}
text, tspan {{white-space: pre;}}
</style>
<rect width="{svg_w}px" height="{svg_h}px" fill="#161b22" rx="15"/>
{dark_ascii}
{dark_info_block}
</svg>"""

light_svg = f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="{svg_w}px" height="{svg_h}px" font-size="16px">
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
-webkit-size-adjust: 109%;
size-adjust: 109%;
}}
.key {{fill: #953800;}}
.value {{fill: #0a3069;}}
.addColor {{fill: #1a7f37;}}
.delColor {{fill: #cf222e;}}
.cc {{fill: #c2cfde;}}
text, tspan {{white-space: pre;}}
</style>
<rect width="{svg_w}px" height="{svg_h}px" fill="#f6f8fa" stroke="#d0d7de" rx="15"/>
{light_ascii}
{light_info_block}
</svg>"""

# Write to target directory (passed as arg or current dir)
import sys
target_dirs = [r"C:\WORk\shantoshdurai_repo", r"C:\WORk\For antigravity\profile-readme"]
if len(sys.argv) > 1:
    target_dirs = [sys.argv[1]]

for d in target_dirs:
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "dark_mode.svg"), "w", encoding="utf-8") as f:
        f.write(dark_svg)
    with open(os.path.join(d, "light_mode.svg"), "w", encoding="utf-8") as f:
        f.write(light_svg)
    print(f"Updated dark_mode.svg and light_mode.svg in {d}")
