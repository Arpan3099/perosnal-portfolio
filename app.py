import streamlit as st
import base64

st.set_page_config(
    page_title="Arpan Chowdhury",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap');
:root {
  --bg:#080c14;--bg2:#0d1420;--bg3:#111827;
  --glass:rgba(255,255,255,0.04);--glass-b:rgba(255,255,255,0.08);
  --blue:#3b82f6;--blue-glow:rgba(59,130,246,0.25);--blue-dim:rgba(59,130,246,0.12);
  --cyan:#22d3ee;--text:#e2e8f0;--text-dim:#94a3b8;--text-muted:#4b5563;
  --mono:'Space Mono',monospace;--sans:'Syne',sans-serif;
}
.stApp{background:var(--bg)!important;color:var(--text)!important;font-family:var(--sans)!important;}
.stApp>header{display:none!important;}
.block-container{padding-top:0!important;padding-bottom:4rem!important;max-width:1200px!important;}
[data-testid="collapsedControl"]{display:none!important;}
.stTabs [data-baseweb="tab-list"]{background:var(--bg2)!important;border-bottom:1px solid rgba(59,130,246,0.2)!important;gap:0!important;padding:0 2rem!important;}
.stTabs [data-baseweb="tab"]{font-family:var(--mono)!important;font-size:0.75rem!important;color:var(--text-dim)!important;padding:1rem 1.5rem!important;letter-spacing:0.08em!important;background:transparent!important;border:none!important;text-transform:uppercase!important;}
.stTabs [aria-selected="true"]{color:var(--blue)!important;border-bottom:2px solid var(--blue)!important;}
.stTabs [data-baseweb="tab-panel"]{background:transparent!important;padding:2.5rem 2rem!important;}
.hero{background:linear-gradient(135deg,var(--bg) 0%,var(--bg2) 50%,#0a1628 100%);padding:4rem 3rem 3rem;position:relative;overflow:hidden;border-bottom:1px solid rgba(59,130,246,0.15);}
.hero::before{content:'';position:absolute;top:-200px;right:-200px;width:600px;height:600px;background:radial-gradient(circle,rgba(59,130,246,0.07) 0%,transparent 70%);pointer-events:none;}
.hero::after{content:'';position:absolute;bottom:-100px;left:-100px;width:400px;height:400px;background:radial-gradient(circle,rgba(34,211,238,0.04) 0%,transparent 70%);pointer-events:none;}
.hero-grid{display:grid;grid-template-columns:1fr 380px;gap:4rem;align-items:center;max-width:1100px;margin:0 auto;}
.status-pill{display:inline-flex;align-items:center;gap:0.5rem;background:var(--blue-dim);border:1px solid rgba(59,130,246,0.3);border-radius:100px;padding:0.35rem 1rem;font-family:var(--mono);font-size:0.7rem;color:var(--blue);letter-spacing:0.08em;margin-bottom:1.5rem;}
.status-dot{width:7px;height:7px;background:#22c55e;border-radius:50%;box-shadow:0 0 6px #22c55e;animation:pulse 2s infinite;}
@keyframes pulse{0%,100%{opacity:1;}50%{opacity:0.4;}}
.hero-name{font-family:var(--sans)!important;font-size:4.5rem!important;font-weight:800!important;line-height:1.0!important;color:var(--text)!important;margin:0 0 0.75rem!important;letter-spacing:-0.02em!important;}
.hero-name .accent{color:var(--blue);}
.hero-tagline{font-family:var(--mono);font-size:0.8rem;color:var(--cyan);letter-spacing:0.12em;text-transform:uppercase;margin:0 0 1.5rem;}
.hero-bio{font-size:1rem;line-height:1.7;color:var(--text-dim);max-width:520px;margin:0 0 2.5rem;}
.hero-ctas{display:flex;gap:1rem;flex-wrap:wrap;}
.btn-primary{background:var(--blue)!important;color:white!important;padding:0.75rem 1.5rem!important;border-radius:8px!important;font-family:var(--mono)!important;font-size:0.78rem!important;font-weight:700!important;text-decoration:none!important;letter-spacing:0.05em!important;transition:all 0.2s!important;box-shadow:0 0 20px var(--blue-glow)!important;}
.btn-primary:hover{background:#2563eb!important;box-shadow:0 0 30px rgba(59,130,246,0.4)!important;}
.btn-secondary{background:transparent!important;color:var(--blue)!important;padding:0.75rem 1.5rem!important;border-radius:8px!important;border:1px solid var(--blue)!important;font-family:var(--mono)!important;font-size:0.78rem!important;font-weight:700!important;text-decoration:none!important;letter-spacing:0.05em!important;transition:all 0.2s!important;}
.btn-secondary:hover{background:var(--blue-dim)!important;}
.btn-ghost{background:transparent!important;color:var(--text-dim)!important;padding:0.75rem 1.5rem!important;border-radius:8px!important;border:1px solid var(--glass-b)!important;font-family:var(--mono)!important;font-size:0.78rem!important;text-decoration:none!important;letter-spacing:0.05em!important;transition:all 0.2s!important;}
.btn-ghost:hover{border-color:rgba(255,255,255,0.2)!important;color:var(--text)!important;}
.hero-right{display:flex;flex-direction:column;align-items:center;gap:1.5rem;}
.photo-frame{position:relative;width:200px;height:220px;}
.hero-photo{width:200px;height:220px;object-fit:cover;border-radius:16px;border:2px solid rgba(59,130,246,0.4);position:relative;z-index:2;filter:grayscale(10%) contrast(1.05);}
.photo-glow{position:absolute;inset:-8px;border-radius:20px;background:radial-gradient(ellipse,var(--blue-glow) 0%,transparent 70%);z-index:1;}
.stat-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:0.75rem;width:100%;}
.stat-card{background:var(--glass);border:1px solid var(--glass-b);border-radius:10px;padding:0.75rem 0.5rem;text-align:center;backdrop-filter:blur(10px);}
.stat-num{display:block;font-family:var(--mono);font-size:1.4rem;font-weight:700;color:var(--blue);}
.stat-label{display:block;font-size:0.6rem;color:var(--text-muted);letter-spacing:0.05em;text-transform:uppercase;margin-top:0.2rem;}
.section-header{display:flex;align-items:center;gap:1rem;margin-bottom:2.5rem;}
.section-tag{font-family:var(--mono);font-size:0.7rem;color:var(--blue);letter-spacing:0.1em;}
.section-header h2{font-size:1.8rem!important;font-weight:800!important;color:var(--text)!important;margin:0!important;letter-spacing:-0.02em!important;}
.glass-card{background:var(--glass)!important;border:1px solid var(--glass-b)!important;border-radius:14px!important;backdrop-filter:blur(12px)!important;transition:border-color 0.2s,box-shadow 0.2s!important;}
.glass-card:hover{border-color:rgba(59,130,246,0.3)!important;box-shadow:0 4px 24px rgba(59,130,246,0.08)!important;}
.timeline{position:relative;padding-left:2rem;}
.timeline::before{content:'';position:absolute;left:0;top:0;bottom:0;width:1px;background:linear-gradient(to bottom,var(--blue),rgba(59,130,246,0.1));}
.tl-item{position:relative;margin-bottom:2rem;}
.tl-marker{position:absolute;left:-2.4rem;top:1.2rem;width:12px;height:12px;background:var(--blue);border-radius:50%;box-shadow:0 0 10px var(--blue-glow);}
.tl-marker-sm{width:8px;height:8px;left:-2.25rem;top:1.4rem;background:var(--bg3);border:2px solid var(--blue);box-shadow:none;}
.tl-content{padding:1.5rem!important;}
.tl-meta{display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem;flex-wrap:wrap;gap:0.5rem;}
.company-tag{font-family:var(--mono);font-size:0.65rem;color:var(--cyan);letter-spacing:0.1em;text-transform:uppercase;background:rgba(34,211,238,0.08);border:1px solid rgba(34,211,238,0.2);padding:0.2rem 0.6rem;border-radius:4px;}
.date-tag{font-family:var(--mono);font-size:0.65rem;color:var(--text-muted);letter-spacing:0.05em;}
.role-title{font-size:1.1rem!important;font-weight:700!important;color:var(--text)!important;margin:0 0 1rem!important;}
.role-sub{color:var(--text-dim);font-weight:400;font-size:0.9rem;}
.tl-bullets{list-style:none!important;padding:0!important;margin:0!important;}
.tl-bullets li{position:relative;padding-left:1.2rem;color:var(--text-dim);font-size:0.9rem;line-height:1.65;margin-bottom:0.6rem;}
.tl-bullets li::before{content:'→';position:absolute;left:0;color:var(--blue);font-size:0.8rem;}
.highlight{color:var(--blue);font-weight:700;}
.edu-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1.25rem;}
.edu-card{padding:1.5rem!important;position:relative;}
.edu-card.featured{border-color:rgba(59,130,246,0.3)!important;}
.edu-badge{position:absolute;top:1rem;right:1rem;font-family:var(--mono);font-size:0.6rem;padding:0.2rem 0.6rem;border-radius:100px;background:var(--blue-dim);color:var(--blue);border:1px solid rgba(59,130,246,0.3);letter-spacing:0.08em;text-transform:uppercase;}
.edu-badge.top5{background:rgba(34,211,238,0.08);color:var(--cyan);border-color:rgba(34,211,238,0.2);}
.edu-badge.top10{background:rgba(168,85,247,0.08);color:#a855f7;border-color:rgba(168,85,247,0.2);}
.edu-card h3{font-size:1rem!important;font-weight:700!important;color:var(--text)!important;margin:0 0 0.4rem!important;}
.edu-school{color:var(--text-dim);font-size:0.85rem;margin:0 0 0.25rem;}
.edu-location{font-family:var(--mono);font-size:0.65rem;color:var(--text-muted);margin:0 0 0.6rem;letter-spacing:0.05em;}
.edu-note{font-size:0.82rem;color:var(--blue);margin:0;}
.projects-grid{display:grid;grid-template-columns:2fr 1fr;gap:1.25rem;margin-bottom:2.5rem;}
.project-card{padding:1.75rem!important;text-decoration:none!important;display:block;}
.featured-project{border-color:rgba(59,130,246,0.25)!important;}
.proj-tag{font-family:var(--mono);font-size:0.6rem;color:var(--cyan);letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.75rem;}
.project-card h3{font-size:1.05rem!important;font-weight:700!important;color:var(--text)!important;margin:0 0 0.75rem!important;}
.project-card p{font-size:0.875rem;color:var(--text-dim);line-height:1.6;margin:0 0 1rem;}
.proj-link{font-family:var(--mono);font-size:0.72rem;color:var(--blue);letter-spacing:0.08em;}
.skills-section{margin-top:1rem;}
.skills-title{font-size:0.75rem!important;font-family:var(--mono)!important;color:var(--text-muted)!important;letter-spacing:0.1em!important;text-transform:uppercase!important;margin:1.5rem 0 0.75rem!important;}
.skills-grid{display:flex;flex-wrap:wrap;gap:0.6rem;}
.skill-item{background:var(--glass);border:1px solid var(--glass-b);border-radius:6px;padding:0.4rem 0.85rem;font-family:var(--mono);font-size:0.72rem;color:var(--text-dim);letter-spacing:0.04em;}
.skill-item.lang{color:var(--text);}
.contact-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1.25rem;margin-bottom:2rem;}
.contact-card{padding:1.5rem!important;display:flex!important;flex-direction:column!important;gap:0.35rem!important;text-decoration:none!important;}
.contact-icon{font-family:var(--mono);font-size:1.2rem;color:var(--blue);font-weight:700;}
.contact-label{font-family:var(--mono);font-size:0.65rem;color:var(--text-muted);letter-spacing:0.1em;text-transform:uppercase;}
.contact-val{font-size:0.9rem;color:var(--text-dim);}
.contact-card:hover .contact-val{color:var(--blue);}
.footer-text{text-align:center;font-family:var(--mono);font-size:0.7rem;color:var(--text-muted);letter-spacing:0.08em;margin-top:3rem;}
@media(max-width:900px){
  .hero-grid{grid-template-columns:1fr;}
  .hero-right{display:none;}
  .edu-grid{grid-template-columns:1fr;}
  .projects-grid{grid-template-columns:1fr;}
  .contact-grid{grid-template-columns:1fr;}
}
"""

st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

def img_to_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def pdf_to_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

photo_b64 = img_to_b64("photo.png")
cv_b64 = pdf_to_b64("CV_Arpan_Chowdhury_Master.pdf")
cv_href = f"data:application/pdf;base64,{cv_b64}"

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero">
  <div class="hero-grid">
    <div class="hero-left">
      <div class="status-pill"><span class="status-dot"></span>MBA Candidate · EBS Germany</div>
      <h1 class="hero-name">Arpan<br><span class="accent">Chowdhury</span></h1>
      <p class="hero-tagline">Product Manager · B2B SaaS · Automotive Tech</p>
      <p class="hero-bio">4 years building B2B SaaS at HighRadius — from intern to de-facto PM leading a 6-engineer pod. Now doing my MBA at EBS, Germany, with a capstone at Schaeffler AG. I like hard problems, clean systems, and products that actually get used.</p>
      <div class="hero-ctas">
        <a href="https://schaeffler-ai-innovation-assistant.streamlit.app/" target="_blank" class="btn-primary">⚡ View Capstone Project</a>
        <a href="{cv_href}" download="Arpan_Chowdhury_CV.pdf" class="btn-secondary">↓ Download CV</a>
        <a href="https://linkedin.com/in/arpan-c" target="_blank" class="btn-ghost">LinkedIn ↗</a>
      </div>
    </div>
    <div class="hero-right">
      <div class="photo-frame">
        <img src="data:image/jpeg;base64,{photo_b64}" class="hero-photo" />
        <div class="photo-glow"></div>
      </div>
      <div class="stat-cards">
        <div class="stat-card"><span class="stat-num">4+</span><span class="stat-label">Years in Product</span></div>
        <div class="stat-card"><span class="stat-num">40%</span><span class="stat-label">Productivity gain shipped</span></div>
        <div class="stat-card"><span class="stat-num">57%</span><span class="stat-label">Ticket reduction</span></div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── TABS ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs(["Experience", "Education", "Projects & Skills", "Contact"])

with tab1:
    st.markdown("""
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
""", unsafe_allow_html=True)

with tab2:
    st.markdown("""
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
""", unsafe_allow_html=True)

with tab3:
    st.markdown("""
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
    <div class="skill-item lang">🇬🇧 English — C2 Professional</div>
    <div class="skill-item lang">🇩🇪 German — B1 Conversational</div>
  </div>
  <h3 class="skills-title">Certifications</h3>
  <div class="skills-grid">
    <div class="skill-item">Product Management — NextLeap (2023)</div>
    <div class="skill-item">MTA: Python for Beginners — Microsoft (2019)</div>
  </div>
</div>
""", unsafe_allow_html=True)

with tab4:
    st.markdown(f"""
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
""", unsafe_allow_html=True)
