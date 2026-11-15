#!/usr/bin/env python3
"""
Generates the SVG artwork for the GitHub profile README (light + dark).
Edit the content below and run:  python3 scripts/generate_assets.py
Outputs go to assets/. No dependencies.
"""
from pathlib import Path
from textwrap import wrap
from html import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

THEMES = {
    "dark": dict(bg="#0d1117", bg2="#161b22", line="#30363d", fg="#e6edf3", muted="#8b949e",
                 teal="#2dd4bf", amber="#f5b041", violet="#a78bfa", blob1="#0f766e", blob2="#7c3aed",
                 blob3="#b45309", bubble_user="#1f6feb", bubble_ai="#21262d", chip="#21262d", blobop="0.55"),
    "light": dict(bg="#ffffff", bg2="#f6f8fa", line="#d0d7de", fg="#1f2328", muted="#57606a",
                  teal="#0f766e", amber="#b45309", violet="#6d28d9", blob1="#5eead4", blob2="#c4b5fd",
                  blob3="#fcd34d", bubble_user="#0969da", bubble_ai="#eaeef2", chip="#eaeef2", blobop="0.45"),
}

# ── content ────────────────────────────────────────────────────────────────
NAME = "Anmol Bisht"
KICKER = "LEAD FULL STACK ENGINEER · INFIHEAL"
TYPED = [
    "building real-time, AI-powered products",
    "leading the web & app team behind Healo",
    "SSE · Socket.IO · LLM streaming · Next.js",
]
STATS = [
    ("2M+", "people use Healo", "the mental-health AI I help build"),
    ("3,800+", "commits", "top contributor to the platform"),
    ("2", "npm SDKs", "chat, booking & service adapters"),
    ("5", "languages", "Healo ships in, worldwide"),
]
PROJECTS = [
    dict(slug="townplay", kind="FULL STACK · BOOKING", title="Townplay",
         desc="Local sports venue booking with concurrency-safe slot locking, Razorpay webhooks, QR ticketing and split payments.",
         stack=["Next.js", "Node.js", "MongoDB", "Socket.IO"]),
    dict(slug="stock-signals", kind="AUTOMATION · FINTECH", title="Stock Signals",
         desc="Personal swing and positional signal bot for NSE stocks with Telegram alerts, paper trading and an admin panel.",
         stack=["Node.js", "MongoDB", "Next.js", "TanStack Query"]),
    dict(slug="stock-analyser", kind="AI · API", title="Stock Analyser",
         desc="Stock analysis API with LLM-powered insights, background queues, rate limiting and payments.",
         stack=["Express", "TypeScript", "Redis", "BullMQ"]),
    dict(slug="eduerp", kind="SAAS · MULTI-TENANT", title="EduERP",
         desc="Multi-tenant school management and billing engine with an admin web app.",
         stack=["Node.js", "TypeScript", "MongoDB", "Express"]),
    dict(slug="kiddo", kind="CREATIVE TOOLING", title="Unique Kiddo Studio",
         desc="An engine that renders kid-paced learning Shorts for a YouTube channel, from script to finished video.",
         stack=["Python", "FFmpeg", "Automation"]),
    dict(slug="portfolio", kind="PORTFOLIO", title="anmolbisht.com",
         desc="My portfolio: the Healo story, the platform I build, and a live 3D graph of my GitHub activity.",
         stack=["Next.js", "TypeScript", "Three.js"]),
]


def banner(t, theme):
    W, H = 1280, 360
    cyc = 12
    # typing slots
    typed = []
    for i, line in enumerate(TYPED):
        w = len(line) * 13.2 + 10   # ~0.6em per char at 22px mono
        s = i / len(TYPED)
        e = (i + 1) / len(TYPED)
        if i == 0:
            kt = f"0;{s+0.12:.4f};{e-0.05:.4f};{e-0.02:.4f};1"
            vals = f"0;{w:.0f};{w:.0f};0;0"
        else:
            kt = f"0;{s:.4f};{s+0.12:.4f};{e-0.05:.4f};{e-0.02:.4f};1"
            vals = f"0;0;{w:.0f};{w:.0f};0;0"
        xs = ";".join(str(80 + 26 + float(v)) for v in vals.split(";"))
        typed.append(f"""
  <clipPath id="c{i}"><rect x="106" y="236" height="40" width="0">
    <animate attributeName="width" values="{vals}" keyTimes="{kt}" dur="{cyc}s" repeatCount="indefinite"/></rect></clipPath>
  <text x="106" y="263" font-family="{MONO}" font-size="22" fill="{t['fg']}" clip-path="url(#c{i})">{escape(line)}</text>
  <rect x="106" y="242" width="11" height="26" fill="{t['teal']}" opacity="0">
    <animate attributeName="x" values="{xs}" keyTimes="{kt}" dur="{cyc}s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="{'1;1;1;0;0' if i==0 else '0;1;1;1;0;0'}" keyTimes="{kt}" dur="{cyc}s" repeatCount="indefinite" calcMode="discrete"/>
  </rect>""")
    # chat illustration (right side), loops every cyc seconds
    cx = 820
    ai_lines = ["Let's slow down for a moment.", "What's weighing on you most", "right now?"]
    ai_text = "".join(
        f'<tspan x="{cx+34}" dy="{0 if j==0 else 24}">{escape(l)}</tspan>' for j, l in enumerate(ai_lines))
    chat = f"""
  <g font-family="{SANS}">
    <rect x="{cx}" y="58" width="390" height="250" rx="18" fill="{t['bg2']}" stroke="{t['line']}"/>
    <circle cx="{cx+24}" cy="80" r="5" fill="#ff5f57"/><circle cx="{cx+42}" cy="80" r="5" fill="#febc2e"/><circle cx="{cx+60}" cy="80" r="5" fill="#28c840"/>
    <text x="{cx+366}" y="85" text-anchor="end" font-family="{MONO}" font-size="12" fill="{t['muted']}">event-stream · live</text>
    <circle cx="{cx+214}" cy="81" r="4" fill="{t['teal']}"><animate attributeName="opacity" values="1;0.2;1" dur="1.4s" repeatCount="indefinite"/></circle>
    <g opacity="0">
      <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.06;0.92;1" dur="{cyc}s" repeatCount="indefinite"/>
      <rect x="{cx+140}" y="104" width="232" height="40" rx="14" fill="{t['bubble_user']}"/>
      <text x="{cx+156}" y="130" font-size="16" fill="#ffffff">Work has been a lot lately…</text>
    </g>
    <g opacity="0">
      <animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.14;0.18;0.92;1" dur="{cyc}s" repeatCount="indefinite"/>
      <rect x="{cx+20}" y="158" width="300" height="98" rx="14" fill="{t['bubble_ai']}"/>
      <clipPath id="stream"><rect x="{cx+30}" y="164" height="84" width="0">
        <animate attributeName="width" values="0;0;285;285;0" keyTimes="0;0.18;0.5;0.92;1" dur="{cyc}s" repeatCount="indefinite"/></rect></clipPath>
      <text y="190" font-size="16" fill="{t['fg']}" clip-path="url(#stream)">{ai_text}</text>
    </g>
    <g font-family="{MONO}" font-size="12" fill="{t['muted']}" opacity="0">
      <animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.5;0.55;0.92;1" dur="{cyc}s" repeatCount="indefinite"/>
      <text x="{cx+20}" y="284">data: {{"done": true}}</text>
      <text x="{cx+370}" y="284" text-anchor="end" fill="{t['teal']}">streamed in 1.2s</text>
    </g>
  </g>"""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{NAME}, Lead Full Stack Engineer">
  <defs>
    <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="{t['line']}"/></pattern>
    <clipPath id="frame"><rect width="{W}" height="{H}" rx="20"/></clipPath>
  </defs>
  <g clip-path="url(#frame)">
    <rect width="{W}" height="{H}" fill="{t['bg']}"/>
    <rect width="{W}" height="{H}" fill="url(#dots)" opacity="0.6"/>
    <g filter="url(#blur)" opacity="{t['blobop']}">
      <circle r="150" fill="{t['blob1']}"><animate attributeName="cx" values="180;360;180" dur="18s" repeatCount="indefinite"/><animate attributeName="cy" values="80;220;80" dur="22s" repeatCount="indefinite"/></circle>
      <circle r="170" fill="{t['blob2']}"><animate attributeName="cx" values="1080;880;1080" dur="20s" repeatCount="indefinite"/><animate attributeName="cy" values="300;120;300" dur="16s" repeatCount="indefinite"/></circle>
      <circle r="120" fill="{t['blob3']}"><animate attributeName="cx" values="620;760;620" dur="24s" repeatCount="indefinite"/><animate attributeName="cy" values="360;260;360" dur="19s" repeatCount="indefinite"/></circle>
    </g>
    <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="20" fill="none" stroke="{t['line']}"/>
  </g>
  <text x="80" y="104" font-family="{MONO}" font-size="15" letter-spacing="3" fill="{t['teal']}">{escape(KICKER)}</text>
  <text x="76" y="190" font-family="{SANS}" font-size="78" font-weight="800" letter-spacing="-2" fill="{t['fg']}">{escape(NAME)}</text>
  <text x="80" y="263" font-family="{MONO}" font-size="22" fill="{t['amber']}">&gt;</text>{''.join(typed)}
  <text x="80" y="318" font-family="{SANS}" font-size="18" fill="{t['muted']}">Noida, India · real-time systems · AI products · engineering leadership</text>{chat}
</svg>"""


def stats(t):
    W, H = 1280, 170
    tw = (W - 3 * 20) / 4
    tiles = []
    for i, (num, label, note) in enumerate(STATS):
        x = i * (tw + 20)
        col = [t["teal"], t["amber"], t["violet"], t["teal"]][i]
        d = 0.15 + i * 0.18
        tiles.append(f"""
  <g opacity="0" transform="translate(0 14)">
    <animate attributeName="opacity" from="0" to="1" begin="{d:.2f}s" dur="0.6s" fill="freeze"/>
    <animateTransform attributeName="transform" type="translate" from="0 14" to="0 0" begin="{d:.2f}s" dur="0.6s" fill="freeze"/>
    <rect x="{x+0.5:.1f}" y="0.5" width="{tw-1:.1f}" height="{H-1}" rx="16" fill="{t['bg2']}" stroke="{t['line']}"/>
    <text x="{x+28:.1f}" y="78" font-family="{SANS}" font-size="52" font-weight="800" letter-spacing="-1" fill="{col}">{escape(num)}</text>
    <text x="{x+28:.1f}" y="112" font-family="{SANS}" font-size="22" font-weight="700" fill="{t['fg']}">{escape(label)}</text>
    <text x="{x+28:.1f}" y="144" font-family="{SANS}" font-size="16" fill="{t['muted']}">{escape(note)}</text>
  </g>""")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="By the numbers">{''.join(tiles)}
</svg>"""


def card(t, p):
    W, H = 620, 236
    lines = wrap(p["desc"], 52)[:3]
    desc = "".join(f'<tspan x="28" dy="{0 if i==0 else 25}">{escape(l)}</tspan>' for i, l in enumerate(lines))
    chips, x = [], 28
    for s in p["stack"]:
        w = len(s) * 8.4 + 26
        chips.append(f'<rect x="{x:.0f}" y="184" width="{w:.0f}" height="30" rx="15" fill="{t["chip"]}" stroke="{t["line"]}"/>'
                     f'<text x="{x + w/2:.0f}" y="204" text-anchor="middle" font-family="{MONO}" font-size="14" fill="{t["fg"]}">{escape(s)}</text>')
        x += w + 8
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(p['title'])}">
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t['teal']}" stop-opacity="0.16"/><stop offset="0.55" stop-color="{t['bg2']}" stop-opacity="0"/></linearGradient></defs>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="{t['bg2']}" stroke="{t['line']}"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="url(#g)"/>
  <text x="28" y="42" font-family="{MONO}" font-size="13" letter-spacing="2" fill="{t['teal']}">{escape(p['kind'])}</text>
  <text x="{W-28}" y="42" text-anchor="end" font-family="{SANS}" font-size="20" fill="{t['muted']}">↗</text>
  <text x="28" y="84" font-family="{SANS}" font-size="31" font-weight="800" fill="{t['fg']}">{escape(p['title'])}</text>
  <text y="120" font-family="{SANS}" font-size="18" fill="{t['muted']}">{desc}</text>
  {''.join(chips)}
</svg>"""


for name, t in THEMES.items():
    (OUT / f"banner-{name}.svg").write_text(banner(t, name))
    (OUT / f"stats-{name}.svg").write_text(stats(t))
    for p in PROJECTS:
        (OUT / f"card-{p['slug']}-{name}.svg").write_text(card(t, p))
print("wrote", len(list(OUT.glob('*.svg'))), "SVGs to", OUT)
