# Builds the infographic HTML from the rows below. Run: python3 build.py && ./render.sh
import pathlib
ROWS = [  # old, new, old in/out, new in/out, cut label, HLE old, HLE new
    ("claude-4-5-sonnet", "claude-5-5-sonnet", "$3 / $15", "$2 / $10", "−33%", 7.2, 55.0),
    ("claude-4-7-opus", "claude-5-5-opus", "$5 / $25", "$4 / $20", "−20%", 42.3, 61.4),
    ("gpt-5.5", "gpt-6.1-sol", "$5 / $30", "$2 / $10", "−60%+", 45.8, 52.9),
    ("gpt-5.6-terra", "gpt-6.1-terra", "$2 / $12", "$1 / $5", "−50%+", 42.9, 46.2),
    ("gpt-5.2", "gpt-6.1-terra", "$1.75 / $14", "$1 / $5", "−43%+", 37.7, 46.2),
]
SCALE = 65.0  # HLE % that fills the bar track
def row(o, n, po, pn, cut, ho, hn):
    return f'''<div class="r"><div class="names"><span class="o">{o}</span><span class="nw"><i>→</i> {n}</span></div>
<div class="price"><div class="cut">{cut}</div><div class="pp"><s>{po}</s> → <b>{pn}</b></div></div>
<div class="hle"><div class="row"><div class="track"><div class="b old" style="width:{ho/SCALE*100:.1f}%"></div></div><span class="v">{ho}%</span></div>
<div class="row"><div class="track"><div class="b new" style="width:{hn/SCALE*100:.1f}%"></div></div><span class="v n">{hn}%</span></div></div></div>'''
html = pathlib.Path(__file__).with_name("template.html").read_text().replace("{{ROWS}}", "\n".join(row(*r) for r in ROWS))
pathlib.Path(__file__).with_name("infographic.html").write_text(html)
