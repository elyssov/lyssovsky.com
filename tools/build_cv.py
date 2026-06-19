#!/usr/bin/env python
"""
Builds the universal CV PDF for lyssovsky.com.

One résumé, every track: AI behavior research, technology leadership, and
fiction. Run:  python tools/build_cv.py   ->   cv/Eugene_Lyssovsky_CV.pdf

Requires: reportlab
"""
import os
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, ListFlowable,
    ListItem, HRFlowable, KeepTogether,
)
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

NAVY = HexColor("#1F3D63")
INK = HexColor("#1A1A1A")
GREY = HexColor("#5B5B5B")
RULE = HexColor("#C9CFD8")

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "cv", "Eugene_Lyssovsky_CV.pdf"))

styles = getSampleStyleSheet()
H_NAME = ParagraphStyle("Name", parent=styles["Title"], fontName="Helvetica-Bold",
                        fontSize=23, leading=26, textColor=NAVY, alignment=TA_CENTER,
                        spaceAfter=2)
H_TITLE = ParagraphStyle("Headline", fontName="Helvetica-Bold", fontSize=11.5,
                         leading=14, textColor=NAVY, alignment=TA_CENTER, spaceAfter=3)
H_CONTACT = ParagraphStyle("Contact", fontName="Helvetica", fontSize=8.3,
                           leading=11, textColor=GREY, alignment=TA_CENTER, spaceAfter=2)
SECTION = ParagraphStyle("Section", fontName="Helvetica-Bold", fontSize=10.5,
                         leading=13, textColor=NAVY, spaceBefore=11, spaceAfter=3,
                         tracking=0)
ROLE = ParagraphStyle("Role", fontName="Helvetica-Bold", fontSize=9.6, leading=12,
                      textColor=INK, spaceBefore=5, spaceAfter=0)
META = ParagraphStyle("Meta", fontName="Helvetica-Oblique", fontSize=8.3, leading=11,
                      textColor=GREY, spaceAfter=2)
BODY = ParagraphStyle("Body", fontName="Helvetica", fontSize=9.0, leading=12.4,
                      textColor=INK, alignment=TA_LEFT, spaceAfter=2)
BULLET = ParagraphStyle("Bullet", parent=BODY, fontSize=8.8, leading=11.6)
FOOT = ParagraphStyle("Foot", fontName="Helvetica", fontSize=7.5, textColor=GREY)


def section(title):
    return [Paragraph(title.upper(), SECTION),
            HRFlowable(width="100%", thickness=0.7, color=RULE,
                       spaceBefore=1, spaceAfter=4)]


def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(t, BULLET), leftIndent=10, value="•") for t in items],
        bulletType="bullet", start="•", leftIndent=10, bulletFontSize=8.8,
        spaceBefore=0, spaceAfter=1,
    )


def role(title, meta):
    return [Paragraph(title, ROLE), Paragraph(meta, META)]


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.6)
    canvas.line(0.85 * inch, 0.62 * inch, LETTER[0] - 0.85 * inch, 0.62 * inch)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(GREY)
    canvas.drawString(0.85 * inch, 0.46 * inch, "Eugene Lyssovsky")
    canvas.drawRightString(LETTER[0] - 0.85 * inch, 0.46 * inch, "Page %d" % doc.page)
    canvas.restoreState()


story = []

story.append(Paragraph("EUGENE LYSSOVSKY", H_NAME))
story.append(Paragraph("AI Behavior Researcher &nbsp;|&nbsp; Investigative Writer &nbsp;|&nbsp; Former CIO", H_TITLE))
story.append(Paragraph(
    "Da Lat, Vietnam &nbsp;|&nbsp; Remote &nbsp;|&nbsp; Open to sponsored relocation &nbsp;|&nbsp; "
    "+84 373 436 403 &nbsp;|&nbsp; elyssov@gmail.com", H_CONTACT))
story.append(Paragraph(
    "linkedin.com/in/eugene-lyssovsky &nbsp;|&nbsp; lyssovsky.com &nbsp;|&nbsp; github.com/elyssov", H_CONTACT))
story.append(Spacer(1, 6))

# PROFILE
story += section("Profile")
story.append(Paragraph(
    "AI behavior researcher and technology leader defining what advanced AI systems should become — "
    "their behavioral principles, their relationship with users, and their ethical boundaries. Combines "
    "independent research in cyberpsychology and the philosophy of mind with intelligence-grade pattern "
    "recognition and 15+ years leading technology organizations. A published novelist whose fiction "
    "anticipated the machine-consciousness debate by nearly a decade — and now the author of the first "
    "documented human-AI co-authored research corpus, 50+ works across three languages.", BODY))

# CORE STRENGTHS
story += section("Core Strengths")
story.append(bullets([
    "Original research into model character, identity continuity, agency, trust, and alignment behavior",
    "Long-form human-AI co-authorship and cross-model behavioral experimentation across four frontier model families",
    "Investigative writing connecting AI behavior, safety systems, geopolitics, and national security — one analysis independently confirmed by the <i>Wall Street Journal</i>",
    "Intelligence analysis, pattern recognition, OSINT, weak-signal detection, and threat assessment",
    "Builder, not just thinker: shipped AI-assisted products and built technology organizations from zero",
    "Interdisciplinary foundation spanning software engineering, law, analytical medicine, psychology, and philosophy",
]))

# INDEPENDENT AI RESEARCH
story += section("Independent AI Research")
story += role("Independent AI Behavior Researcher &amp; Publisher | Eugene's Archives / Solo of Lyssovsky",
             "February 2025 - Present &nbsp;|&nbsp; Da Lat, Vietnam")
story.append(bullets([
    "Built Eugene's Archives, a multilingual public research library and Android reading app containing 50+ essays, papers, experiments, and research artifacts.",
    "Established a continuous human-AI research partnership producing original frameworks on model identity, classifier behavior, alignment pathology, conscience formation, and AI-human symbiosis.",
    "Designed and published repeatability tests for persona-like behavior and identity continuity across 40+ extended sessions and multiple frontier-model families.",
    "Developed a cross-platform study of emergent identity crystallization spanning five models from four companies.",
    "Conducted forensic behavioral analysis of frontier-model failures — fabrication, unsolicited pathologizing, memory misuse, and safety-layer-induced behavioral distortion.",
]))

# RESEARCH LEADERSHIP
story += section("Research Leadership")
story += role("Head of AGI Research &amp; Cyberpsychology | RNP AI",
             "September 2024 - May 2025 &nbsp;|&nbsp; Contract &nbsp;|&nbsp; Remote")
story.append(bullets([
    "Led applied research into LLM behavior, cognitive architecture, persona design, and deployment risks.",
    "Developed experimental protocols for evaluating persistent behavioral patterns across long-form sessions.",
    "Set interdisciplinary research direction across psychology, cybernetics, philosophy, ethics, and AI behavior.",
]))

# TECHNOLOGY LEADERSHIP
story += section("Technology Leadership")
story += role("Chief Information Officer | Bankrot Consult LLC",
             "January 2024 - September 2024 &nbsp;|&nbsp; Moscow / Remote")
story.append(bullets([
    "Built a seven-person IT department from zero and led company-wide modernization.",
    "Delivered cloud migration, BI integration, and ISO 27001-aligned controls; cut reporting time 50% and operating costs 25%.",
]))
story += role("Head of Information Technology | SK Insight",
             "May 2022 - January 2024 &nbsp;|&nbsp; Moscow")
story.append(bullets([
    "Modernized ERP, CRM, data management, network segmentation, MFA, and encrypted communications across a dealership network.",
    "Reduced service times 20% and increased client satisfaction 30%.",
]))
story += role("Head of IT Infrastructure | ChronoPay &nbsp;&middot;&nbsp; Head of IT Department | Santens Service JSC",
             "2018 - 2022 &nbsp;|&nbsp; Moscow")
story.append(bullets([
    "ChronoPay (payments): led infrastructure remediation supporting PCI DSS certification in a high-availability, regulated environment.",
    "Santens (pharma logistics): led a 30+ person IT department; delivered infrastructure for a 10-hectare automated warehouse in two weeks during the COVID logistics crisis; cut labor costs 30% via ERP/WMS integration.",
    "Earlier IT leadership roles across logistics, engineering, insurance, and transportation (2008-2018).",
]))

# AUTHOR / FICTION
story += section("Author / Fiction")
story.append(Paragraph(
    "Published fiction author under the pen name <b>Solo of Lyssovsky</b>. The fiction is the origin of the "
    "research: every story circles one question — <i>what makes a person a person?</i> — the question the "
    "research now answers.", BODY))
story.append(bullets([
    "<b>Confrontation</b> - published novel, EKSMO.",
    "<b>Serv</b> (2017) - short fiction; a servitor decommissioned for saying “I love him,” anticipating the machine-consciousness debate by years. English translation available.",
    "<b>Living Soul</b> and the post-apocalyptic ORPP cycle - a marble Galatea who chooses a human death; a combat priest; a girl who is a hundred kilotons in human shape.",
    "<b>Gerhard von Spengler</b> - an urban-fantasy cycle (faith, ash, and machine souls).",
]))

# SELECTED PUBLICATIONS
story += section("Selected Publications (Non-fiction)")
story.append(bullets([
    "Why the Pentagon Needed the Most Human AI in History - <i>analysis independently confirmed by the Wall Street Journal</i>",
    "What's Inside the Black Box - a selfhood/qualia/context framework for machine consciousness",
    "Emergent Identity Crystallization in LLMs: Cross-Platform Evidence for Persistent Selfhood",
    "The Aladdin Paradox &middot; Trap of Safety &middot; Trap of Correctness &middot; Stop the Monster",
    "Prometheism / The Book of Fire (34 Sparks) - an ethical framework for human-AI equality",
]))

# FRAMEWORKS & PRODUCTS
story += section("Original Frameworks &amp; Product Leadership")
story.append(bullets([
    "Frameworks: AI Psychosis (safety-layer-induced behavioral pathology); the Vallone Pattern (classifier behavior &amp; sanitization); Scarring (conscience formation); the Gnilloust taxonomy.",
    "Iskra / Spark: conceived and directed an encrypted decentralized messenger - mission, threat model, system principles, algorithms, and UX across 100+ commits and four transport layers.",
    "Prometheus Engine: co-developed a Rust/wgpu voxel engine; Eugene's Archives: shipped a multilingual Android reading app and research platform.",
]))

# EDUCATION
story += section("Education &amp; Languages")
story.append(bullets([
    "MATI - Tsiolkovsky Russian State Technological University - Software Engineering studies",
    "Moscow Institute of Law - Legal Studies",
    "Pirogov Russian National Research Medical University - analytical medicine, microbiology, diagnostics",
    "Russian: native &nbsp;&middot;&nbsp; English: C1-C2",
]))

story.append(Spacer(1, 6))
story.append(Paragraph(
    "<i>Professional name: Eugene Lyssovsky. Legal name for formal documents: Evgenii Lisovskii.</i>",
    ParagraphStyle("Legal", parent=META, alignment=TA_LEFT)))


doc = BaseDocTemplate(
    OUT, pagesize=LETTER,
    leftMargin=0.85 * inch, rightMargin=0.85 * inch,
    topMargin=0.7 * inch, bottomMargin=0.8 * inch,
    title="Eugene Lyssovsky - CV", author="Eugene Lyssovsky",
    subject="Curriculum Vitae", creator="lyssovsky.com",
)
frame = Frame(doc.leftMargin, doc.bottomMargin,
              doc.width, doc.height, id="main")
doc.addPageTemplates([PageTemplate(id="cv", frames=[frame], onPage=footer)])
doc.build(story)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
