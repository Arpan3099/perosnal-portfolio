import streamlit as st
import base64

st.set_page_config(
    page_title="Arpan Chowdhury",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "section" not in st.session_state:
    st.session_state.section = "Experience"

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap');
:root {
  --bg:#080c14;--bg2:#0d1420;--bg3:#111827;
  --glass:rgba(255,255,255,0.06);--glass-b:rgba(255,255,255,0.12);
  --blue:#3b82f6;--blue-glow:rgba(59,130,246,0.25);--blue-dim:rgba(59,130,246,0.15);
  --cyan:#22d3ee;--text:#ffffff;--text-dim:#ffffff;--text-muted:#cbd5e1;
  --mono:'Space Mono',monospace;--sans:'Syne',sans-serif;
}
.stApp{background:var(--bg)!important;color:var(--text)!important;font-family:var(--sans)!important;}
.stApp>header{display:none!important;}
[data-testid="collapsedControl"]{display:none!important;}
[data-testid="stToolbar"]{display:none!important;}
[data-testid="stDecoration"]{display:none!important;}
[data-testid="stSidebar"]{display:none!important;}
.block-container{padding:0!important;max-width:100%!important;}
section[data-testid="stMain"] > div{padding:0!important;}

/* ── LAYOUT ── */
.portfolio-wrap{display:flex;min-height:100vh;width:100%;}

/* ── LEFT PANEL ── */
.left-panel{
  width:320px;min-width:320px;
  background:var(--bg2);
  border-right:1px solid rgba(59,130,246,0.15);
  display:flex;flex-direction:column;
  padding:2.5rem 1.75rem;
  position:sticky;top:0;height:100vh;overflow-y:auto;
}
.status-pill{display:inline-flex;align-items:center;gap:0.5rem;background:var(--blue-dim);border:1px solid rgba(59,130,246,0.3);border-radius:100px;padding:0.35rem 0.9rem;font-family:var(--mono);font-size:0.8rem;color:var(--blue);letter-spacing:0.06em;margin-bottom:1.25rem;}
.status-dot{width:7px;height:7px;background:#22c55e;border-radius:50%;box-shadow:0 0 6px #22c55e;animation:pulse 2s infinite;}
@keyframes pulse{0%,100%{opacity:1;}50%{opacity:0.4;}}
.left-name{font-family:var(--sans);font-size:2.5rem;font-weight:800;line-height:1.05;color:#ffffff;margin:0 0 0.5rem;letter-spacing:-0.02em;}
.left-name .accent{color:var(--blue);}
.left-tagline{font-family:var(--mono);font-size:0.75rem;color:var(--cyan);letter-spacing:0.1em;text-transform:uppercase;margin:0 0 1.25rem;}
.left-bio{font-size:0.9rem;line-height:1.65;color:#ffffff;margin:0 0 2rem;}
.photo-wrap{margin-bottom:1.75rem;}
.hero-photo{width:100%;max-width:220px;border-radius:14px;border:2px solid rgba(59,130,246,0.4);display:block;filter:contrast(1.05);}
.stat-row{display:grid;grid-template-columns:repeat(3,1fr);gap:0.5rem;margin-bottom:2rem;}
.stat-card{background:var(--glass);border:1px solid var(--glass-b);border-radius:10px;padding:0.6rem 0.4rem;text-align:center;}
.stat-num{display:block;font-family:var(--mono);font-size:1.25rem;font-weight:700;color:var(--blue);}
.stat-label{display:block;font-size:0.6rem;color:#ffffff;letter-spacing:0.04em;text-transform:uppercase;margin-top:0.15rem;line-height:1.3;}

/* NAV */
.nav-label{font-family:var(--mono);font-size:0.65rem;color:var(--text-muted);letter-spacing:0.12em;text-transform:uppercase;margin:0 0 0.75rem;}
.nav-links{display:flex;flex-direction:column;gap:0.35rem;margin-bottom:2rem;}
.nav-btn{background:transparent;border:1px solid transparent;border-radius:8px;padding:0.65rem 1rem;font-family:var(--mono);font-size:0.8rem;color:#ffffff;letter-spacing:0.06em;text-align:left;cursor:pointer;transition:all 0.15s;width:100%;}
.nav-btn:hover{background:var(--glass);border-color:var(--glass-b);color:#ffffff;}
.nav-btn.active{background:var(--blue-dim);border-color:rgba(59,130,246,0.4);color:var(--blue);}
.left-ctas{display:flex;flex-direction:column;gap:0.6rem;margin-top:auto;padding-top:1.5rem;border-top:1px solid rgba(255,255,255,0.06);}
.btn-primary{background:var(--blue)!important;color:#fff!important;padding:0.75rem 1.25rem!important;border-radius:8px!important;font-family:var(--mono)!important;font-size:0.8rem!important;font-weight:700!important;text-decoration:none!important;letter-spacing:0.05em!important;text-align:center!important;display:block!important;box-shadow:0 0 18px var(--blue-glow)!important;}
.btn-secondary{background:transparent!important;color:var(--blue)!important;padding:0.7rem 1.25rem!important;border-radius:8px!important;border:1px solid var(--blue)!important;font-family:var(--mono)!important;font-size:0.8rem!important;font-weight:700!important;text-decoration:none!important;letter-spacing:0.05em!important;text-align:center!important;display:block!important;}
.btn-ghost{background:transparent!important;color:#ffffff!important;padding:0.7rem 1.25rem!important;border-radius:8px!important;border:1px solid rgba(255,255,255,0.15)!important;font-family:var(--mono)!important;font-size:0.8rem!important;text-decoration:none!important;letter-spacing:0.05em!important;text-align:center!important;display:block!important;}

/* ── RIGHT PANEL ── */
.right-panel{flex:1;padding:3rem 3.5rem;overflow-y:auto;}
.section-header{display:flex;align-items:center;gap:1rem;margin-bottom:2.5rem;}
.section-tag{font-family:var(--mono);font-size:0.875rem;color:var(--blue);letter-spacing:0.1em;}
.section-header h2{font-size:2.5rem!important;font-weight:800!important;color:#ffffff!important;margin:0!important;letter-spacing:-0.02em!important;}

/* Glass card */
.glass-card{background:var(--glass)!important;border:1px solid var(--glass-b)!important;border-radius:14px!important;backdrop-filter:blur(12px)!important;transition:border-color 0.2s,box-shadow 0.2s!important;}
.glass-card:hover{border-color:rgba(59,130,246,0.35)!important;box-shadow:0 4px 28px rgba(59,130,246,0.1)!important;}

/* Timeline */
.timeline{position:relative;padding-left:2.25rem;}
.timeline::before{content:'';position:absolute;left:0;top:0;bottom:0;width:1px;background:linear-gradient(to bottom,var(--blue),rgba(59,130,246,0.08));}
.tl-item{position:relative;margin-bottom:2rem;}
.tl-marker{position:absolute;left:-2.65rem;top:1.3rem;width:13px;height:13px;background:var(--blue);border-radius:50%;box-shadow:0 0 12px var(--blue-glow);}
.tl-marker-sm{width:9px;height:9px;left:-2.5rem;top:1.5rem;background:var(--bg3);border:2px solid var(--blue);box-shadow:none;}
.tl-content{padding:1.75rem!important;}
.tl-meta{display:flex;justify-content:space-between;align-items:center;margin-bottom:0.6rem;flex-wrap:wrap;gap:0.5rem;}
.company-tag{font-family:var(--mono);font-size:0.8rem;color:var(--cyan);letter-spacing:0.1em;text-transform:uppercase;background:rgba(34,211,238,0.08);border:1px solid rgba(34,211,238,0.2);padding:0.25rem 0.7rem;border-radius:4px;}
.date-tag{font-family:var(--mono);font-size:0.8rem;color:#ffffff;letter-spacing:0.05em;}
.role-title{font-size:1.4rem!important;font-weight:700!important;color:#ffffff!important;margin:0 0 1rem!important;}
.role-sub{color:#ffffff;font-weight:400;font-size:1.1rem;}
.tl-bullets{list-style:none!important;padding:0!important;margin:0!important;}
.tl-bullets li{position:relative;padding-left:1.4rem;color:#ffffff;font-size:1.1rem;line-height:1.7;margin-bottom:0.7rem;}
.tl-bullets li::before{content:'→';position:absolute;left:0;color:var(--blue);font-size:0.9rem;}
.highlight{color:var(--blue);font-weight:700;}

/* Education */
.edu-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1.25rem;}
.edu-card{padding:1.75rem!important;position:relative;}
.edu-card.featured{border-color:rgba(59,130,246,0.35)!important;}
.edu-badge{position:absolute;top:1rem;right:1rem;font-family:var(--mono);font-size:0.7rem;padding:0.25rem 0.65rem;border-radius:100px;background:var(--blue-dim);color:var(--blue);border:1px solid rgba(59,130,246,0.3);letter-spacing:0.08em;text-transform:uppercase;}
.edu-badge.top5{background:rgba(34,211,238,0.08);color:var(--cyan);border-color:rgba(34,211,238,0.2);}
.edu-badge.top10{background:rgba(168,85,247,0.08);color:#a855f7;border-color:rgba(168,85,247,0.2);}
.edu-card h3{font-size:1.25rem!important;font-weight:700!important;color:#ffffff!important;margin:0 0 0.45rem!important;}
.edu-school{color:#ffffff;font-size:1.05rem;margin:0 0 0.3rem;}
.edu-location{font-family:var(--mono);font-size:0.8rem;color:#ffffff;margin:0 0 0.65rem;letter-spacing:0.04em;}
.edu-note{font-size:1rem;color:var(--blue);margin:0;}

/* Projects */
.projects-grid{display:grid;grid-template-columns:2fr 1fr;gap:1.25rem;margin-bottom:2.5rem;}
.project-card{padding:1.75rem!important;text-decoration:none!important;display:block;}
.featured-project{border-color:rgba(59,130,246,0.3)!important;}
.proj-tag{font-family:var(--mono);font-size:0.75rem;color:var(--cyan);letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.75rem;}
.project-card h3{font-size:1.3rem!important;font-weight:700!important;color:#ffffff!important;margin:0 0 0.75rem!important;}
.project-card p{font-size:1.05rem;color:#ffffff;line-height:1.65;margin:0 0 1rem;}
.proj-link{font-family:var(--mono);font-size:0.875rem;color:var(--blue);letter-spacing:0.06em;}
.skills-section{margin-top:1.25rem;}
.skills-title{font-size:0.875rem!important;font-family:var(--mono)!important;color:#ffffff!important;letter-spacing:0.1em!important;text-transform:uppercase!important;margin:1.5rem 0 0.75rem!important;}
.skills-grid{display:flex;flex-wrap:wrap;gap:0.6rem;}
.skill-item{background:var(--glass);border:1px solid var(--glass-b);border-radius:6px;padding:0.45rem 1rem;font-family:var(--mono);font-size:0.875rem;color:#ffffff;letter-spacing:0.04em;}

/* Contact */
.contact-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1.25rem;margin-bottom:2rem;}
.contact-card{padding:1.75rem!important;display:flex!important;flex-direction:column!important;gap:0.4rem!important;text-decoration:none!important;}
.contact-icon{font-family:var(--mono);font-size:1.5rem;color:var(--blue);font-weight:700;}
.contact-label{font-family:var(--mono);font-size:0.75rem;color:#ffffff;letter-spacing:0.1em;text-transform:uppercase;}
.contact-val{font-size:1.05rem;color:#ffffff;}
.contact-card:hover .contact-val{color:var(--blue);}
.footer-text{text-align:center;font-family:var(--mono);font-size:0.8rem;color:#ffffff;letter-spacing:0.06em;margin-top:3rem;}

/* Streamlit button overrides */
div[data-testid="stColumns"]{gap:0!important;}
.stButton>button{display:none!important;}
"""

st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

def img_to_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def pdf_to_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

photo_b64   = img_to_b64("photo.png")
cv_b64      = pdf_to_b64("CV_Arpan_Chowdhury_Master.pdf")
cv_href     = f"data:application/pdf;base64,{cv_b64}"

SECTIONS = ["Experience", "Education", "Projects & Skills", "Contact"]

# ── TWO-COLUMN LAYOUT ─────────────────────────────────────────────────────────
left_col, right_col = st.columns([1, 2.8], gap="small")

# ── LEFT PANEL ────────────────────────────────────────────────────────────────
with left_col:
    nav_links_html = "".join([
        f'<button class="nav-btn {"active" if st.session_state.section == s else ""}" '
        f'onclick="window.location.href=\'?section={s.replace(" ", "+")}\'">{s}</button>'
        for s in SECTIONS
    ])

    st.markdown(f"""
<div class="left-panel">
  <div class="status-pill"><span class="status-dot"></span>MBA Candidate · EBS Germany</div>
  <div class="photo-wrap">
    <img src="data:image/jpeg;base64,{photo_b64}" class="hero-photo" />
  </div>
  <h1 class="left-name">Arpan<br><span class="accent">Chowdhury</span></h1>
  <p class="left-tagline">Product Manager · B2B SaaS · Automotive Tech</p>
  <p class="left-bio">4 years building B2B SaaS at HighRadius — from intern to de-facto PM leading a 6-engineer pod. MBA at EBS, Germany with a capstone at Schaeffler AG.</p>
  <div class="stat-row">
    <div class="stat-card"><span class="stat-num">4+</span><span class="stat-label">Yrs in Product</span></div>
    <div class="stat-card"><span class="stat-num">40%</span><span class="stat-label">Productivity gain</span></div>
    <div class="stat-card"><span class="stat-num">57%</span><span class="stat-label">Ticket reduction</span></div>
  </div>
  <p class="nav-label">Navigation</p>
  <div class="nav-links" id="nav">{nav_links_html}</div>
  <div class="left-ctas">
    <a href="https://schaeffler-ai-innovation-assistant.streamlit.app/" target="_blank" class="btn-primary">⚡ View Capstone</a>
    <a href="{cv_href}" download="Arpan_Chowdhury_CV.pdf" class="btn-secondary">↓ Download CV</a>
    <a href="https://linkedin.com/in/arpan-c" target="_blank" class="btn-ghost">LinkedIn ↗</a>
  </div>
</div>
""", unsafe_allow_html=True)

    # Actual nav buttons (hidden visually, used for session state)
    for s in SECTIONS:
        if st.button(s, key=f"nav_{s}"):
            st.session_state.section = s
            st.rerun()

# ── RIGHT PANEL ───────────────────────────────────────────────────────────────
with right_col:
    sec = st.session_state.section

    if sec == "Experience":
        st.markdown("""
<div class="right-panel">
<div class="section-header"><span class="section-tag">// 01</span><h2>Professional Experience</h2></div>
<div class="timeline">
  <div class="tl-item">
    <div class="tl-marker"></div>
    <div class="tl-content glass-card">
      <div class="tl-meta"><span class="company-tag">HighRadius Technologies</span><span class="date-tag">Jan 2023 – Dec 2024</span></div>
      <h3 class="role-title">Senior Product Analyst <span class="role-sub">· Deductions Product</span></h3>
      <ul class="tl-bullets">
        <li>De-facto PM for a 6-engineer POD — full sprint ownership: backlog, stories, planning, retro.</li>
        <li>Primary bridge between enterprise clients, Consulting, and Engineering. Lead contact for top 3 pilot clients on SAP/Oracle ERP automation rollouts.</li>
        <li>Launched in-app analytics and RCA dashboards for real-time deduction tracking — cut client escalation cycles, gave end users self-serve visibility.</li>
        <li>Designed UX flows and mockups for a low-code automation config tool; drove engineering integration through to full go-live.</li>
        <li>Partnered with Sales Engineering in enterprise deal cycles; ran UAT, sprint reviews, and demos with VP/Director-level stakeholders.</li>
      </ul>
    </div>
  </div>
  <div class="tl-item">
    <div class="tl-marker tl-marker-sm"></div>
    <div class="tl-content glass-card">
      <div class="tl-meta"><span class="company-tag">HighRadius Technologies</span><span class="date-tag">Feb 2021 – Dec 2022</span></div>
      <h3 class="role-title">Product Analyst <span class="role-sub">· ML Deductions</span></h3>
      <ul class="tl-bullets">
        <li>Built AI-assisted automations linking backup docs to ERP short-payment deductions — <span class="highlight">40% productivity boost</span>.</li>
        <li>Rolled out automation journeys to 3 early adopter clients — <span class="highlight">30% daily productivity gain</span> confirmed via in-app metrics and QBR feedback.</li>
        <li>Analysed 500+ Zendesk/Jira tickets to surface recurring pain points; insights directly shaped the 2023 product roadmap.</li>
        <li>Co-owned user stories, acceptance criteria, and release docs across 3 major releases — adopted as standard onboarding collateral.</li>
      </ul>
    </div>
  </div>
  <div class="tl-item">
    <div class="tl-marker tl-marker-sm"></div>
    <div class="tl-content glass-card">
      <div class="tl-meta"><span class="company-tag">HighRadius Technologies</span><span class="date-tag">Jul 2020 – Feb 2021</span></div>
      <h3 class="role-title">Intern <span class="role-sub">· Analytics</span></h3>
      <ul class="tl-bullets">
        <li>Built SQL queries for O2C reports and dashboards across all product lines.</li>
        <li>Resolved client issues via Zendesk — <span class="highlight">57% reduction in ticket inflow</span>.</li>
        <li>Coordinated peer intern team on daily Analytics support. Awarded Pre-Placement Offer (PPO) ahead of graduation.</li>
      </ul>
    </div>
  </div>
</div>
</div>
""", unsafe_allow_html=True)

    elif sec == "Education":
        st.markdown("""
<div class="right-panel">
<div class="section-header"><span class="section-tag">// 02</span><h2>Education</h2></div>
<div class="edu-grid">
  <div class="edu-card glass-card featured">
    <div class="edu-badge">Current</div>
    <h3>MBA</h3>
    <p class="edu-school">EBS Universität für Wirtschaft und Recht</p>
    <p class="edu-location">Oestrich-Winkel, Germany · Jan 2026 – Present</p>
    <p class="edu-note">Capstone Project @ Schaeffler AG · AI Innovation Research Assistant</p>
  </div>
  <div class="edu-card glass-card">
    <div class="edu-badge top5">Top 5%</div>
    <h3>Global Management Program</h3>
    <p class="edu-school">S.P. Jain Institute of Industrial Technology</p>
    <p class="edu-location">Mumbai, India · May – Dec 2025</p>
    <p class="edu-note">GPA 3.2 / 4.0 · International Exchange – EBS MBA</p>
  </div>
  <div class="edu-card glass-card">
    <div class="edu-badge top10">CGPA 9.0</div>
    <h3>B.Tech – Computer Science</h3>
    <p class="edu-school">KIIT, Bhubaneswar</p>
    <p class="edu-location">India · Jul 2017 – Mar 2021</p>
    <p class="edu-note">Top 10% · KIITEE Merit Scholarship</p>
  </div>
  <div class="edu-card glass-card">
    <h3>Higher Secondary (Class XII)</h3>
    <p class="edu-school">Dyal Singh Public School</p>
    <p class="edu-location">Karnal, India · 2017</p>
    <p class="edu-note">85.5% · Science stream</p>
  </div>
</div>
</div>
""", unsafe_allow_html=True)

    elif sec == "Projects & Skills":
        st.markdown("""
<div class="right-panel">
<div class="section-header"><span class="section-tag">// 03</span><h2>Projects & Skills</h2></div>
<div class="projects-grid">
  <a href="https://schaeffler-ai-innovation-assistant.streamlit.app/" target="_blank" class="project-card glass-card featured-project">
    <div class="proj-tag">MBA Capstone · Live</div>
    <h3>Schaeffler AI Innovation Assistant</h3>
    <p>AI research assistant built for Schaeffler AG as part of the EBS MBA capstone. Explores AI-driven innovation frameworks in the automotive and industrial space.</p>
    <span class="proj-link">Launch App ↗</span>
  </a>
  <div class="project-card glass-card">
    <div class="proj-tag">NextLeap · 2023</div>
    <h3>YouTube Premium Growth Strategy</h3>
    <p>End-to-end PM project — competitor analysis, user research, persona creation, wireframing, and success metric definition for subscription growth.</p>
  </div>
</div>
<div class="skills-section">
  <h3 class="skills-title">Tools & Stack</h3>
  <div class="skills-grid">
    <div class="skill-item">Jira / Confluence</div><div class="skill-item">Zendesk / ServiceNow</div>
    <div class="skill-item">SQL (Intermediate)</div><div class="skill-item">Python (Beginner)</div>
    <div class="skill-item">SAP / Oracle ERP</div><div class="skill-item">MS Office Suite</div>
  </div>
  <h3 class="skills-title">Languages</h3>
  <div class="skills-grid">
    <div class="skill-item">🇬🇧 English — C2 Professional</div>
    <div class="skill-item">🇩🇪 German — B1 Conversational</div>
  </div>
  <h3 class="skills-title">Certifications</h3>
  <div class="skills-grid">
    <div class="skill-item">Product Management — NextLeap (2023)</div>
    <div class="skill-item">MTA: Python for Beginners — Microsoft (2019)</div>
  </div>
</div>
</div>
""", unsafe_allow_html=True)

    elif sec == "Contact":
        st.markdown(f"""
<div class="right-panel">
<div class="section-header"><span class="section-tag">// 04</span><h2>Get in Touch</h2></div>
<div class="contact-grid">
  <a href="mailto:arpan.chowdhury@students.ebs.de" class="contact-card glass-card">
    <span class="contact-icon">✉</span><span class="contact-label">Email</span>
    <span class="contact-val">arpan.chowdhury@students.ebs.de</span>
  </a>
  <a href="https://linkedin.com/in/arpan-c" target="_blank" class="contact-card glass-card">
    <span class="contact-icon">in</span><span class="contact-label">LinkedIn</span>
    <span class="contact-val">linkedin.com/in/arpan-c</span>
  </a>
  <a href="tel:+4915215100331" class="contact-card glass-card">
    <span class="contact-icon">☎</span><span class="contact-label">Phone</span>
    <span class="contact-val">+49 152 151 00331</span>
  </a>
  <a href="{cv_href}" download="Arpan_Chowdhury_CV.pdf" class="contact-card glass-card">
    <span class="contact-icon">↓</span><span class="contact-label">Resume</span>
    <span class="contact-val">Download full CV (PDF)</span>
  </a>
</div>
<p class="footer-text">Wiesbaden, Germany · Open to Product, Strategy & Consulting roles</p>
</div>
""", unsafe_allow_html=True)
