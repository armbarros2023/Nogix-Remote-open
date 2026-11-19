"""Prévia do NogixDesk com o visual do NOGIX v0.3 (theme.css/styles.css de
nogixremotesupport.com) e as funções do RustDesk 1.5.3 por trás.
Valores de cor, raio, espaçamento e textos copiados do CSS/HTML do NOGIX."""
import pathlib, sys
HERE = pathlib.Path(__file__).parent
OS = {k: (HERE / f"{k}.svg").read_text().replace('width="441" height="512"', 'viewBox="0 0 441 512"') for k in ("win", "linux", "mac")}
from playwright.sync_api import sync_playwright

MARK = ('<svg viewBox="0 0 36 36" fill="none"><path d="M8 26V10L28 26V10" stroke="currentColor" stroke-width="3.4" '
        'stroke-linecap="round" stroke-linejoin="round"/><circle cx="8" cy="10" r="3" fill="currentColor"/>'
        '<circle cx="28" cy="26" r="3" fill="currentColor"/></svg>')
NAV_CONN = ('<svg viewBox="0 0 24 24" fill="none"><rect x="3" y="4" width="8" height="7" rx="1.4" stroke="currentColor" stroke-width="1.7"/>'
            '<rect x="13" y="13" width="8" height="7" rx="1.4" stroke="currentColor" stroke-width="1.7"/><path d="M11 7.5h2a2 2 0 0 1 2 2V13M13 16.5h-2a2 2 0 0 1-2-2V11" '
            'stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>')
NAV_SET = ('<svg viewBox="0 0 24 24" fill="none"><path d="M4 6h5m4 0h7M4 12h9m4 0h3M4 18h2m4 0h10" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/>'
           '<circle cx="11" cy="6" r="2" fill="currentColor"/><circle cx="15" cy="12" r="2" fill="currentColor"/><circle cx="8" cy="18" r="2" fill="currentColor"/></svg>')
THEME = ('<svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="8" stroke="currentColor" stroke-width="1.7"/>'
         '<path d="M12 4a8 8 0 0 1 0 16V4Z" fill="currentColor"/></svg>')
COPY = ('<svg viewBox="0 0 20 20" fill="none"><rect x="7" y="6" width="9" height="11" rx="1.5" stroke="currentColor" stroke-width="1.5"/>'
        '<path d="M13 6V4.5A1.5 1.5 0 0 0 11.5 3h-7A1.5 1.5 0 0 0 3 4.5v9A1.5 1.5 0 0 0 4.5 15H7" stroke="currentColor" stroke-width="1.5"/></svg>')
REFRESH = '<svg viewBox="0 0 24 24"><path fill="currentColor" d="M17.65 6.35A7.958 7.958 0 0 0 12 4c-4.42 0-7.99 3.58-7.99 8s3.57 8 7.99 8c3.73 0 6.84-2.55 7.73-6h-2.08A5.99 5.99 0 0 1 12 18c-3.31 0-6-2.69-6-6s2.69-6 6-6c1.66 0 3.14.69 4.22 1.78L13 11h7V4l-2.35 2.35z"/></svg>'
EXIT = ('<svg viewBox="0 0 24 24" fill="none"><path d="M10 4H5v16h5m4-12 4 4-4 4m-5-4h9" stroke="currentColor" stroke-width="1.7" '
        'stroke-linecap="round" stroke-linejoin="round"/></svg>')
MONITOR = ('<svg viewBox="0 0 24 24" fill="none"><rect x="3.5" y="4.5" width="17" height="13" rx="2" stroke="currentColor" stroke-width="1.6"/>'
           '<path d="M8 21h8M12 17.5V21" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>')
STAR = '<svg viewBox="0 0 24 24" fill="none"><path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9 6.8 19.6l1-5.8L3.5 9.7l5.9-.9z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>'
EDIT = '<svg viewBox="0 0 24 24"><path fill="currentColor" d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a.996.996 0 0 0 0-1.41l-2.34-2.34a.996.996 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>'
HELP = '<svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.6"/><path d="M9.6 9.5a2.5 2.5 0 1 1 3.4 2.3c-.6.3-1 .8-1 1.5v.5M12 17h.01" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>'
I = {  # Material Icons (Apache 2.0), os mesmos do RustDesk
 "history": "M13 3a9 9 0 0 0-9 9H1l3.89 3.89.07.14L9 12H6c0-3.87 3.13-7 7-7s7 3.13 7 7-3.13 7-7 7c-1.93 0-3.68-.79-4.94-2.06l-1.42 1.42A8.954 8.954 0 0 0 13 21a9 9 0 0 0 0-18zm-1 5v5l4.28 2.54.72-1.21-3.5-2.08V8H12z",
 "star": "M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z",
 "explore": "M12 10.9c-.61 0-1.1.49-1.1 1.1s.49 1.1 1.1 1.1c.61 0 1.1-.49 1.1-1.1s-.49-1.1-1.1-1.1zM12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm2.19 12.19L6 18l3.81-8.19L18 6l-3.81 8.19z",
 "book": "M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 4h5v8l-2.5-1.5L6 12V4z",
 "group": "M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z",
 "search": "M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z",
 "refresh": "M17.65 6.35A7.958 7.958 0 0 0 12 4c-4.42 0-7.99 3.58-7.99 8s3.57 8 7.99 8c3.73 0 6.84-2.55 7.73-6h-2.08A5.99 5.99 0 0 1 12 18c-3.31 0-6-2.69-6-6s2.69-6 6-6c1.66 0 3.14.69 4.22 1.78L13 11h7V4l-2.35 2.35z",
 "grid": "M3 3v8h8V3H3zm6 6H5V5h4v4zm-6 4v8h8v-8H3zm6 6H5v-4h4v4zm4-16v8h8V3h-8zm6 6h-4V5h4v4zm-6 4v8h8v-8h-8zm6 6h-4v-4h4v4z",
 "sort": "M3 18h6v-2H3v2zM3 6v2h18V6H3zm0 7h12v-2H3v2z",
}
ic = lambda n: f'<svg viewBox="0 0 24 24"><path fill="currentColor" d="{I[n]}"/></svg>'
DOTS = '<svg viewBox="0 0 24 24"><circle cx="12" cy="6" r="1.7" fill="currentColor"/><circle cx="12" cy="12" r="1.7" fill="currentColor"/><circle cx="12" cy="18" r="1.7" fill="currentColor"/></svg>'

PEERS = [  # exemplos fictícios
    ("loja@CAIXA-01", "123 456 789", "blue", True, False, "win"),
    ("admin@SERVIDOR-ERP", "234 567 891", "teal", True, True, "linux"),
    ("armando@MacBook-Air", "345 678 912", "violet", False, False, "mac"),
    ("estoque@ESTOQUE-02", "456 789 123", "blue", True, False, "win"),
]

CSS = """
*{box-sizing:border-box}
:root{--canvas:#edf2f8;--paper:#fff;--ink:#16243a;--muted:#64758d;--line:#dce5ef;--green:#1769ed;--green-deep:#1054c2;
 font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Inter,sans-serif}
:root[data-theme=dark]{--canvas:#07111f;--paper:#0d1b2d;--ink:#e8f1fc;--muted:#9aadc3;--line:#253a54}
body{margin:0;width:1280px;height:820px;overflow:hidden;background:var(--canvas);color:var(--ink);display:flex;flex-direction:column}
.topbar{display:flex;align-items:center;justify-content:space-between;gap:24px;min-height:68px;padding:10px 28px;border-bottom:1px solid #1b314a;background:#081323}
:root[data-theme=dark] .topbar{background:#060f1d}
.brand{display:flex;align-items:center;gap:10px;color:#f4f8ff}
.brand-mark{display:grid;place-items:center;width:37px;height:37px;color:#fff;border-radius:11px 11px 11px 3px;background:linear-gradient(135deg,#2686ff,#0647bc);box-shadow:0 8px 24px rgba(20,100,230,.25)}
.brand-mark svg{width:27px;height:27px}
.brand-copy{display:flex;flex-direction:column;line-height:1}
.wordmark{font:800 21px/1 -apple-system,BlinkMacSystemFont,'Segoe UI',Inter,sans-serif;letter-spacing:.45px}
.brand-copy small{margin-top:4px;color:#7fa8d5;font-size:11px;font-weight:700;letter-spacing:2px}
.nav{display:flex;gap:8px}
.nav a{display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 15px;border-radius:8px;color:#b6c9df;font-size:13px;font-weight:600}
.nav a.on{color:#fff;background:#17416f}
.nav svg{width:18px;height:18px}
.page{flex:1;display:flex;flex-direction:column;padding:22px 28px 12px;min-height:0}
.heading h2{margin:2px 0 6px;font-size:26px;letter-spacing:-.02em}
.heading p{margin:0 0 18px;color:#526a85;font-size:14px}
:root[data-theme=dark] .heading p{color:#a8bed8}
.work{display:grid;grid-template-columns:1fr 1fr;gap:14px;max-width:1040px;width:100%;margin:0 auto}
.card{position:relative;padding:17px 18px;border-radius:13px}
.card::before{position:absolute;top:0;right:20px;left:20px;height:3px;content:'';border-radius:0 0 5px 5px}
.invite{border:1.5px solid #83b8ed;background:linear-gradient(145deg,#dcecff 0%,#eaf4ff 62%,#f2f8ff 100%);box-shadow:0 16px 38px rgba(28,103,197,.14)}
.invite::before{background:linear-gradient(90deg,#277df0,#77c5ff)}
.connect{border:1.5px solid #79c2c7;background:linear-gradient(145deg,#dcf2f1 0%,#eaf8f7 62%,#f2fbfa 100%);box-shadow:0 16px 38px rgba(20,117,128,.13)}
.connect::before{background:linear-gradient(90deg,#1597ac,#78d8d7)}
:root[data-theme=dark] .invite{border-color:#2868a6;background:linear-gradient(145deg,#102a48 0%,#10223a 62%,#101e32 100%)}
:root[data-theme=dark] .connect{border-color:#237984;background:linear-gradient(145deg,#10333d 0%,#102a36 62%,#10212f 100%)}
.card h3{margin:0 0 14px;font-size:16px;line-height:1.35;color:#18304d}
.connect h3{color:#174752}
:root[data-theme=dark] .card h3{color:#e8f2ff} :root[data-theme=dark] .connect h3{color:#d9f3f3}
.modes{display:flex;gap:8px;margin:0 0 10px}
.modes legend{display:block;width:100%;margin-bottom:8px;color:#53605a;font-size:12px;font-weight:650}
:root[data-theme=dark] .modes legend{color:#a8bed8}
.mode{display:flex;align-items:center;gap:7px;flex:1;padding:11px 12px;border:1px solid #dbe3dd;border-radius:8px;font-size:14px;font-weight:650;background:rgba(255,255,255,.55)}
.mode.on{color:#176b45;background:#ecf7ef;border-color:#66aa7b}
:root[data-theme=dark] .mode{border-color:#2a425d;background:rgba(4,14,27,.4);color:#c9d9ea}
:root[data-theme=dark] .mode.on{color:#9be0c0;background:#12352e;border-color:#27664f}
.radio{width:14px;height:14px;border-radius:50%;border:2px solid currentColor;display:grid;place-items:center}
.mode.on .radio::after{content:'';width:6px;height:6px;border-radius:50%;background:#1f8050}
.help{min-height:20px;color:#5c6860;font-size:12px;line-height:1.5;margin:0 0 12px}
:root[data-theme=dark] .help{color:#a1b4ca}
.lblrow{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.lbl{color:#6d85a1;font-size:11px;font-weight:700;letter-spacing:1.25px}
.invite .lbl{color:#286daf} .connect .lbl{color:#187986}
:root[data-theme=dark] .invite .lbl{color:#91c5ff} :root[data-theme=dark] .connect .lbl{color:#84d5d7}
.state{display:flex;align-items:center;gap:5px;color:#738aaa;font-size:11px}
.dot{width:6px;height:6px;border-radius:50%;background:#2dba94}
.codebox{display:flex;align-items:center;justify-content:space-between;min-height:44px;padding:0 6px 0 15px;border:1px dashed #9ec6f1;border-radius:8px;background:rgba(255,255,255,.82)}
:root[data-theme=dark] .codebox{border-color:#315e8e;background:rgba(4,14,27,.58)}
.codebox output{color:#183c72;font:700 17px/1 -apple-system,'Segoe UI',Inter,sans-serif;letter-spacing:1.7px}
:root[data-theme=dark] .codebox output{color:#c8e4ff}
.iconbtn{display:grid;place-items:center;width:40px;height:40px;border-radius:6px;color:#3674b6}
.iconbtn svg{width:18px;height:18px}
.titlerow{display:flex;align-items:center;justify-content:space-between}
.titlerow h3{margin-bottom:14px}
.helpic{width:20px;height:20px;color:#3c8f98;margin-top:-12px}
:root[data-theme=dark] .helpic{color:#84d5d7}
.split{display:inline-flex;align-items:center;justify-content:center;width:42px;height:42px;border-radius:8px;border:1px solid #79c2c7;color:#106c7b;font-size:12px}
:root[data-theme=dark] .split{border-color:#237984;color:#84d5d7}
:root[data-theme=dark] .iconbtn{color:#91c5f6}
.gap{height:10px}
.actions{display:flex;gap:8px;margin-top:12px;align-items:center}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:42px;padding:0 14px;border-radius:8px;font-size:11px;font-weight:700;border:1px solid transparent}
.primary{width:190px;color:#fff;background:linear-gradient(135deg,#1769ed,#3287f1);box-shadow:0 6px 16px rgba(23,105,237,.2)}
.quiet{color:#5d7899} :root[data-theme=dark] .quiet{color:#a2bad4}
.inputwrap{display:flex;align-items:center;min-height:44px;padding:0 6px 0 11px;border:1px solid #b2dcdf;border-radius:8px;background:rgba(255,255,255,.86)}
:root[data-theme=dark] .inputwrap{border-color:#2a6670;background:#0a202b}
.inputwrap span{flex:1;color:#a4b5c9;font-size:12px} :root[data-theme=dark] .inputwrap span{color:#7890a9}
.paste{padding:6px 8px;color:#1769ad;font-size:11px;font-weight:700} :root[data-theme=dark] .paste{color:#91c5f6}
.connectbtn{width:190px;color:#fff;background:#106c7b;box-shadow:0 6px 16px rgba(16,108,123,.17);justify-content:space-between}
.connectbtn span{font-size:16px;font-weight:400}
.tools{display:flex;gap:6px;margin-top:12px;flex-wrap:wrap}
.chip{padding:7px 10px;border:1px solid #b2dcdf;border-radius:999px;color:#174752;font-size:11px;font-weight:650;background:rgba(255,255,255,.6)}
:root[data-theme=dark] .chip{border-color:#2a6670;color:#a9dfe0;background:rgba(4,14,27,.35)}
.recent{margin-top:16px;padding:15px 16px;border:1px solid #1d3551;border-radius:14px;color:#edf5ff;background:linear-gradient(145deg,#0b1728,#10233a);box-shadow:0 16px 38px rgba(10,29,54,.16);max-width:1040px;width:100%;margin-left:auto;margin-right:auto}
.recent h2{margin:0 0 13px;color:#f2f7ff;font-size:17px}
.rgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.rhead{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:12px}
.rhead h2{margin:0}
.tabs{display:flex;gap:4px}
.tab{display:inline-flex;align-items:center;gap:6px;min-height:34px;padding:0 10px;border-radius:7px;color:#9aadc4;font-size:12px;font-weight:650}
.tab svg{width:17px;height:17px}
.tab.on{color:#fff;background:#17416f}
.racts{display:flex;gap:4px;margin-left:auto}
.racts span{display:grid;place-items:center;width:32px;height:32px;border-radius:7px;color:#9aadc4}
.racts svg{width:18px;height:18px}
.racts .search{display:flex;align-items:center;gap:6px;width:auto;padding:0 10px;border:1px solid #28415f;color:#7f95ae;font-size:12px;background:rgba(255,255,255,.03)}
.os{position:absolute;right:56px;top:12px;width:36px;height:36px;opacity:.85}
.os svg{width:36px;height:36px}
.rcard{position:relative;display:flex;flex-direction:column;justify-content:space-between;min-height:112px;padding:10px 12px;border:1px solid #28415f;border-radius:10px;background:#101f33;overflow:hidden}
.rcard::after{position:absolute;right:0;bottom:0;left:0;height:3px;content:'';background:#428de7}
.rcard.teal{background:#10232f} .rcard.teal::after{background:#18899b}
.rcard.violet{background:#171d36} .rcard.violet::after{background:#7764d0}
.rtop{display:flex;justify-content:space-between;align-items:center}
.rdot{width:8px;height:8px;border:1px solid rgba(255,255,255,.65);border-radius:50%;background:#9aafc8}
.rdot.on{background:#37d765}
.rctl{display:grid;place-items:center;width:30px;height:30px;border-radius:7px;background:rgba(7,16,29,.55);color:#fff}
.rctl svg{width:17px;height:17px} .rctl.fav{color:#f0c66d} .rctl.fav svg path{fill:currentColor}
.rid{display:flex;align-items:center;gap:7px}
.rid svg{width:18px;height:18px;flex:0 0 18px}
.rname{font-size:13px;font-weight:750;line-height:1.4;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:190px}
.rcode{font:500 10px/1.35 ui-monospace,Menlo,Consolas,monospace;color:#e3edfa}
.rmenu{position:absolute;right:7px;bottom:10px;color:#c9d8ea;width:18px;height:18px}
footer{display:flex;align-items:center;gap:20px;margin-top:auto;padding-top:16px;color:#526a85;font-size:12px}
:root[data-theme=dark] footer{color:#a8bed8}
.fbrand{display:flex;flex:1;align-items:center;gap:12px}
.fword{font-weight:800;font-size:15px;letter-spacing:.45px;color:var(--ink)}
.fstate{display:flex;align-items:center;gap:6px}
.fstate i{width:7px;height:7px;border-radius:50%;background:#2dba94}
.powered{font-size:10px;opacity:.7}
.fright{display:flex;align-items:center;gap:16px}
.version{padding:3px 6px;border-radius:5px;color:#61470d;background:#f7e8b4;font-size:11px;font-weight:850;letter-spacing:.3px}
.exit{display:inline-flex;align-items:center;gap:7px;min-height:42px;padding:0 14px;border:1px solid #c6d5e6;border-radius:8px;color:#973d35;font-size:13px;font-weight:650}
:root[data-theme=dark] .exit{border-color:#3e526a;color:#ffb2a9}
.exit svg{width:18px;height:18px}
.arb{width:42px;height:42px;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle at 35% 30%,#f7df8a,#c99a1c);color:#3d2a00;font:800 10px/1 Inter,sans-serif;letter-spacing:.3px}
"""


def page(theme):
    cards = "".join(f"""
    <div class="rcard {tone}"><div class="rtop"><span class="rdot{' on' if on else ''}"></span>
      <span class="rctl{' fav' if fav else ''}">{STAR}</span></div>
      <span class="os">{OS[osn]}</span>
      <div class="rid"><div><div class="rname">{name}</div><div class="rcode">{code}</div></div></div>
      <span class="rmenu">{DOTS}</span></div>""" for name, code, tone, on, fav, osn in PEERS)
    tabs = "".join(f'<span class="tab{" on" if i == 0 else ""}">{ic(n)}{t}</span>' for i, (n, t) in enumerate(
        [("history", "Recentes"), ("star", "Favoritos"), ("explore", "Na rede"), ("book", "Catálogo"), ("group", "Grupos")]))
    return f"""<!doctype html><html data-theme="{theme}"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<header class="topbar">
  <div class="brand"><span class="brand-mark">{MARK}</span><span class="brand-copy"><span class="wordmark">NOGIX</span><small>REMOTE</small></span></div>
  <nav class="nav"><a class="on">{NAV_CONN}Conexão</a><a>{NAV_SET}Configurações</a><a>{THEME}Claro / escuro</a></nav>
</header>
<main class="page">
  <div class="heading"><h2>Conexão</h2><p>Compartilhe o código deste computador ou acesse outro pelo código dele.</p></div>
  <section class="work">
    <article class="card invite">
      <h3>Este computador</h3>
      <div class="modes"><div class="mode on"><span class="radio"></span>Com aceite</div><div class="mode"><span class="radio"></span>Sem aceite</div></div>
      <p class="help">Você aprova cada conexão neste computador.</p>
      <div class="lblrow"><span class="lbl">CÓDIGO DESTE COMPUTADOR</span><span class="state"><span class="dot"></span>Pronto para receber pedidos</span></div>
      <div class="codebox"><output>1 482 907 316</output><span style="display:flex"><span class="iconbtn">{COPY}</span><span class="iconbtn">{DOTS}</span></span></div>
      <div class="gap"></div>
      <div class="lblrow"><span class="lbl">SENHA DE USO ÚNICO</span></div>
      <div class="codebox"><output>k7m2qx</output><span style="display:flex"><span class="iconbtn">{REFRESH}</span><span class="iconbtn">{EDIT}</span><span class="iconbtn">{COPY}</span></span></div>
    </article>
    <article class="card connect">
      <div class="titlerow"><h3>Acessar outro computador</h3><span class="helpic">{HELP}</span></div>
      <div class="modes"><div class="mode on"><span class="radio"></span>Com aceite</div><div class="mode"><span class="radio"></span>Sem aceite</div></div>
      <p class="help">A pessoa no outro computador aprova a conexão.</p>
      <div class="lblrow"><span class="lbl">CÓDIGO DO OUTRO COMPUTADOR</span></div>
      <div class="inputwrap"><span>Digite ou cole o código</span><b class="paste">Colar</b></div>
      <div class="actions"><span class="btn connectbtn">Conectar <span>→</span></span><span class="split">▼</span></div>
      <div class="tools"><span class="chip">Transferir arquivos</span><span class="chip">Terminal</span><span class="chip">Túnel TCP / RDP</span><span class="chip">Ver câmera</span></div>
    </article>
  </section>
  <section class="recent"><div class="rhead"><h2>Computadores recentes</h2><div class="tabs">{tabs}</div>
    <div class="racts"><span class="search">{ic("search")}Pesquisar ID</span><span>{ic("refresh")}</span><span>{ic("grid")}</span><span>{ic("sort")}</span></div></div>
    <div class="rgrid">{cards}</div></section>
  <footer>
    <span class="fbrand"><span class="fword">NOGIX</span><span class="fstate"><i></i>Pronto</span><span class="powered">· Desenvolvido por RustDesk</span></span>
    <span class="fright"><span class="arb">ARB</span><span>Versão <strong class="version">1.5.3-nogix.0</strong></span><span class="exit">{EXIT}Sair</span></span>
  </footer>
</main></body></html>"""


def main(out):
    out = pathlib.Path(out)
    out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        pg = b.new_page(viewport={"width": 1280, "height": 820}, device_scale_factor=1.5)
        for th, name in (("light", "nogixdesk-visual-nogix-claro"), ("dark", "nogixdesk-visual-nogix-escuro")):
            pg.set_content(page(th))
            pg.screenshot(path=str(out / f"{name}.png"))
            print(name)
        b.close()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "out")
