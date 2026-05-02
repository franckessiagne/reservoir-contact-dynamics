#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reusable generator for the DCMR–RCEI graphical abstract.

Outputs:
  - dcmr_rcei_graphical_abstract_190mm.svg
  - dcmr_rcei_graphical_abstract_190mm.html
  - dcmr_rcei_graphical_abstract_190mm_1200dpi.png
  - dcmr_rcei_graphical_abstract_190mm_1200dpi.tiff
  - dcmr_rcei_graphical_abstract_190mm.pdf

Requirements:
  pip install cairosvg pillow

Recommended for best readable text rendering:
  Install Inkscape and make sure the command "inkscape" is available in PATH.

Journal settings:
  Width: 190 mm
  DPI:   1200
  Background: fully opaque white
"""

from pathlib import Path
import shutil
import subprocess
from PIL import Image

try:
    import cairosvg
except Exception:
    cairosvg = None


# ============================================================
# Configuration
# ============================================================

OUTDIR = Path(".")
BASENAME = "dcmr_rcei_graphical_abstract_190mm"

WIDTH_MM = 190.0
HEIGHT_MM = 89.65
DPI = 1200

WIDTH_PX = round(WIDTH_MM / 25.4 * DPI)
HEIGHT_PX = round(HEIGHT_MM / 25.4 * DPI)


# ============================================================
# SVG source
# ============================================================

SVG = '<svg width="190.00mm" height="89.65mm" viewBox="0 0 1848 872" xmlns="http://www.w3.org/2000/svg" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; background-color:#ffffff;">\n<defs>\n  <linearGradient id="headBlue" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#092b66"/><stop offset="1" stop-color="#0b347a"/></linearGradient>\n  <linearGradient id="headRed" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#7b0000"/><stop offset="1" stop-color="#a01818"/></linearGradient>\n  <linearGradient id="gas" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#9bcdf4"/><stop offset="1" stop-color="#5aa3d7"/></linearGradient>\n  <linearGradient id="oil" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#7aa944"/><stop offset="1" stop-color="#51852f"/></linearGradient>\n  <linearGradient id="water" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#0a66b2"/><stop offset="1" stop-color="#06447c"/></linearGradient>\n  <linearGradient id="sand" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#e9c486"/><stop offset="1" stop-color="#d2a45f"/></linearGradient>\n  <linearGradient id="cubeFace" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#035ca8"/><stop offset=".5" stop-color="#217f35"/><stop offset="1" stop-color="#002f78"/></linearGradient>\n  <linearGradient id="cubeSide" x1="0" x2="1"><stop offset="0" stop-color="#00407f"/><stop offset="1" stop-color="#00305e"/></linearGradient>\n  <linearGradient id="stable" x1="0" x2="1"><stop offset="0" stop-color="#dcefd2"/><stop offset="1" stop-color="#f6f1d2"/></linearGradient>\n  <linearGradient id="trans" x1="0" x2="1"><stop offset="0" stop-color="#fff0af"/><stop offset="1" stop-color="#fde3a0"/></linearGradient>\n  <linearGradient id="unstable" x1="0" x2="1"><stop offset="0" stop-color="#ffd2c6"/><stop offset="1" stop-color="#f9b3a9"/></linearGradient>\n  <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="1" dy="1" stdDeviation="2" flood-color="#999" flood-opacity=".35"/></filter>\n  <marker id="arrowBlue" markerWidth="12" markerHeight="10" refX="10" refY="5" orient="auto"><polygon points="0,0 12,5 0,10" fill="#0d3c9d"/></marker>\n  <marker id="arrowBlack" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><polygon points="0,0 10,4 0,8" fill="#111"/></marker>\n  <marker id="arrowRed" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto"><polygon points="0,0 9,3.5 0,7" fill="#c01818"/></marker>\n  <marker id="arrowGreen" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto"><polygon points="0,0 9,3.5 0,7" fill="#198c24"/></marker>\n</defs>\n\n<rect x="0" y="0" width="1848" height="872" fill="#ffffff"/>\n\n<!-- PANEL 1 -->\n<g transform="translate(14,14)">\n  <rect width="376" height="696" rx="16" fill="#ffffff" stroke="#777" stroke-width="1.2"/>\n  <path d="M0,16 Q0,0 16,0 H360 Q376,0 376,16 V48 H0Z" fill="#ffffff" stroke="#777" stroke-width="1.2"/>\n  <text x="188" y="33" text-anchor="middle" class="titleDark">1. STATIC ASSUMPTION</text>\n  <text x="188" y="83" text-anchor="middle" font-size="17" class="ital dark">Contacts assumed flat,</text>\n  <text x="188" y="114" text-anchor="middle" font-size="17" class="ital dark">static and reversible</text>\n  <!-- Derrick -->\n  <g transform="translate(190,168) scale(.9)" stroke="#111" stroke-width="3" fill="none">\n    <line x1="0" y1="0" x2="-20" y2="76"/><line x1="0" y1="0" x2="20" y2="76"/><line x1="-24" y1="76" x2="24" y2="76"/>\n    <line x1="-12" y1="25" x2="12" y2="25"/><line x1="-18" y1="50" x2="18" y2="50"/>\n    <line x1="-12" y1="25" x2="18" y2="50"/><line x1="12" y1="25" x2="-18" y2="50"/>\n    <circle cx="0" cy="-10" r="4" fill="#111"/>\n  </g>\n  <!-- Reservoir -->\n  <g transform="translate(30,230)">\n    <polygon points="0,18 30,0 308,0 336,18" fill="url(#sand)" stroke="#111"/>\n    <rect x="0" y="18" width="336" height="90" fill="url(#gas)" stroke="#111"/>\n    <rect x="0" y="108" width="336" height="114" fill="url(#oil)" stroke="#111"/>\n    <rect x="0" y="222" width="336" height="114" fill="url(#water)" stroke="#111"/>\n    <line x1="0" y1="108" x2="336" y2="108" stroke="#fff" stroke-width="4" stroke-dasharray="10 10"/>\n    <line x1="0" y1="222" x2="336" y2="222" stroke="#fff" stroke-width="4" stroke-dasharray="10 10"/>\n    <text x="22" y="73" class="lab">GAS</text><text x="22" y="171" class="lab">OIL</text><text x="22" y="286" class="lab" fill="#ffffff">WATER</text>\n    <rect x="260" y="88" width="58" height="36" rx="6" fill="#f7f7f7" stroke="#111"/><text x="289" y="112" text-anchor="middle" font-weight="700" font-size="18">GOC</text>\n    <rect x="260" y="204" width="58" height="36" rx="6" fill="#f7f7f7" stroke="#111"/><text x="289" y="228" text-anchor="middle" font-weight="700" font-size="18">OWC</text>\n  </g>\n  <text x="188" y="624" text-anchor="middle" font-size="17" class="ital dark">Hydrostatic equilibrium</text>\n</g>\n\n<!-- PANEL 2 -->\n<g transform="translate(405,14)">\n  <rect width="816" height="696" rx="16" fill="#ffffff" stroke="#3d5d9d" stroke-width="1.5"/>\n  <path d="M0,16 Q0,0 16,0 H800 Q816,0 816,16 V48 H0Z" fill="#ffffff" stroke="#3d5d9d" stroke-width="1.2"/>\n  <text x="408" y="33" text-anchor="middle" class="titleDark">2. DYNAMIC CONTACT EVOLUTION (THIS STUDY)</text>\n  <text x="408" y="86" text-anchor="middle" font-size="18" class="ital blue">Dynamic, nonlinear and irreversible under transient production</text>\n  <text x="86" y="166" text-anchor="middle" font-size="13" font-weight="700" class="blue">Controlling</text>\n  <text x="86" y="188" text-anchor="middle" font-size="13" font-weight="700" class="blue">mechanisms</text>\n  <!-- icons left -->\n  <g transform="translate(46,225)">\n    <circle cx="0" cy="0" r="28" fill="#f8fbff" stroke="#444"/><path d="M0,-17 C-13,3 -7,15 0,16 C10,15 14,3 0,-17Z" fill="#76bde8" stroke="#165a91"/><line x1="-18" y1="13" x2="18" y2="13" stroke="#111"/>\n    <text x="38" y="6" class="med">Capillarity</text>\n  </g>\n  <g transform="translate(46,312)">\n    <circle cx="0" cy="0" r="28" fill="#f8fbff" stroke="#444"/>\n    <g fill="#111"><circle cx="-12" cy="-12" r="4"/><circle cx="6" cy="-16" r="4"/><circle cx="17" cy="-2" r="4"/><circle cx="-1" cy="1" r="4"/><circle cx="-15" cy="8" r="4"/><circle cx="10" cy="14" r="4"/><circle cx="-7" cy="19" r="3"/></g>\n    <text x="38" y="6" class="med">Heterogeneity</text>\n  </g>\n  <g transform="translate(46,400)">\n    <circle cx="0" cy="0" r="28" fill="#f8fbff" stroke="#444"/>\n    <g stroke="#111" stroke-width="2" marker-end="url(#arrowBlack)"><line x1="0" y1="-19" x2="0" y2="-5"/><line x1="0" y1="19" x2="0" y2="5"/><line x1="-19" y1="0" x2="-5" y2="0"/><line x1="19" y1="0" x2="5" y2="0"/></g>\n    <text x="38" y="-2" class="med">Stress</text><text x="38" y="17" class="med">sensitivity</text>\n  </g>\n  <!-- 3D reservoir cube -->\n  <g transform="translate(188,205)">\n    <polygon points="0,0 305,-45 426,0 125,48" fill="#c9932e" stroke="#111" stroke-width="2"/>\n    <polygon points="0,0 125,48 125,320 0,250" fill="url(#cubeFace)" stroke="#111" stroke-width="2"/>\n    <polygon points="125,48 426,0 426,250 125,320" fill="url(#cubeSide)" stroke="#111" stroke-width="2"/>\n    <!-- top grid -->\n    <g stroke="#422" stroke-width="1" opacity=".8">\n      <path d="M36,-5 L160,42 M75,-12 L199,36 M114,-18 L239,29 M154,-24 L278,22 M195,-30 L319,15 M236,-36 L360,8 M277,-42 L401,2"/>\n      <path d="M37,6 L337,-41 M68,18 L368,-28 M99,30 L399,-15 M132,43 L426,-2"/>\n    </g>\n    <!-- textured verticals -->\n    <g opacity=".35" stroke="#7ed1ff" stroke-width="1"><path d="M22,10 V255 M55,20 V270 M88,33 V286 M155,45 V313 M200,38 V300 M245,31 V290 M290,24 V280 M335,16 V270 M381,8 V260"/></g>\n    <!-- nonlinear contacts -->\n    <polyline points="0,95 35,76 65,112 95,93 125,121 160,101 190,137 225,126 260,151 300,141 335,167 375,154 426,169" fill="none" stroke="#ffd22b" stroke-width="9" opacity=".9"/>\n    <polyline points="0,95 35,76 65,112 95,93 125,121 160,101 190,137 225,126 260,151 300,141 335,167 375,154 426,169" fill="none" stroke="#df0000" stroke-width="2.5"/>\n    <polyline points="0,160 35,150 65,180 95,168 125,190 160,178 190,212 225,205 260,227 300,219 335,243 375,235 426,249" fill="none" stroke="#ffd22b" stroke-width="9" opacity=".9"/>\n    <polyline points="0,160 35,150 65,180 95,168 125,190 160,178 190,212 225,205 260,227 300,219 335,243 375,235 426,249" fill="none" stroke="#df0000" stroke-width="2.5"/>\n    <rect x="353" y="88" width="68" height="34" rx="6" fill="#f7f7f7" stroke="#111"/><text x="387" y="111" text-anchor="middle" font-weight="700" font-size="16">GOC(t)</text>\n    <rect x="353" y="204" width="68" height="34" rx="6" fill="#f7f7f7" stroke="#111"/><text x="387" y="227" text-anchor="middle" font-weight="700" font-size="16">OWC(t)</text>\n    <text x="115" y="317" font-size="20" font-weight="700">X</text><text x="384" y="317" font-size="20" font-weight="700">Y</text>\n    <line x1="-12" y1="120" x2="-12" y2="235" stroke="#111" stroke-width="2" marker-end="url(#arrowBlack)"/><text x="-26" y="180" transform="rotate(-90 -26,180)" font-size="14">Depth</text>\n    <!-- wells -->\n    <g stroke="#111" stroke-width="2" fill="none"><path d="M65,-58 l-14,85 h28z M51,27 h28 M58,-25 h14 M53,4 h24"/><circle cx="65" cy="-68" r="3" fill="#111"/><path d="M178,-60 l-14,87 h28z M164,27 h28 M171,-25 h14 M166,4 h24"/><circle cx="178" cy="-70" r="3" fill="#111"/></g>\n    <g transform="translate(330,-48)" stroke="#111" stroke-width="3" fill="none"><line x1="20" y1="0" x2="6" y2="80"/><line x1="20" y1="0" x2="45" y2="80"/><line x1="8" y1="80" x2="48" y2="80"/><line x1="16" y1="35" x2="36" y2="35"/><circle cx="52" cy="-18" r="18"/><line x1="38" y1="-12" x2="70" y2="-24"/><line x1="70" y1="-24" x2="75" y2="25"/><circle cx="75" cy="25" r="3" fill="#a00"/></g>\n  </g>\n  <!-- behavior boxes -->\n  <text x="718" y="139" text-anchor="middle" font-size="15" font-weight="700" class="blue">Key dynamic</text><text x="718" y="161" text-anchor="middle" font-size="15" font-weight="700" class="blue">behaviors</text>\n  <g transform="translate(626,176)">\n    <rect width="180" height="160" rx="10" fill="#ffffff" stroke="#888"/>\n    <text x="90" y="22" text-anchor="middle" font-size="12" font-weight="700" class="blue">Delayed response</text><text x="90" y="40" text-anchor="middle" font-size="12" font-weight="700" class="blue">&amp; abrupt jumps</text>\n    <line x1="30" y1="122" x2="160" y2="122" stroke="#111" marker-end="url(#arrowBlack)"/><line x1="30" y1="122" x2="30" y2="55" stroke="#111" marker-end="url(#arrowBlack)"/>\n    <polyline points="40,92 105,86 118,40 128,18 160,15" fill="none" stroke="#d7191c" stroke-width="3"/><polyline points="40,92 105,86" fill="none" stroke="green" stroke-width="3"/>\n    <text x="92" y="151" font-size="10">Time</text><text x="8" y="86" transform="rotate(-90 8,86)" font-size="10">Contact depth</text>\n  </g>\n  <g transform="translate(626,342)">\n    <rect width="180" height="145" rx="10" fill="#ffffff" stroke="#888"/>\n    <text x="90" y="20" text-anchor="middle" font-size="12" font-weight="700" class="blue">Hysteresis &amp;</text><text x="90" y="38" text-anchor="middle" font-size="12" font-weight="700" class="blue">irreversibility</text>\n    <line x1="30" y1="110" x2="160" y2="110" stroke="#111" marker-end="url(#arrowBlack)"/><line x1="30" y1="110" x2="30" y2="58" stroke="#111" marker-end="url(#arrowBlack)"/>\n    <path d="M80,65 C120,55 160,80 150,103 C138,130 88,122 63,101 C40,82 52,68 80,65" fill="none" stroke="#0d3c9d" stroke-width="2" marker-end="url(#arrowBlue)"/>\n    <path d="M150,103 C120,125 70,116 58,88" fill="none" stroke="#d7191c" stroke-width="2" marker-end="url(#arrowRed)"/>\n    <text x="118" y="133" font-size="10">Pressure</text><text x="7" y="90" transform="rotate(-90 7,90)" font-size="10">Contact depth</text>\n  </g>\n  <g transform="translate(626,492)">\n    <rect width="180" height="140" rx="10" fill="#ffffff" stroke="#888"/>\n    <text x="90" y="20" text-anchor="middle" font-size="12" font-weight="700" class="blue">Frequency-dependent</text><text x="90" y="38" text-anchor="middle" font-size="12" font-weight="700" class="blue">attenuation &amp; phase lag</text>\n    <line x1="30" y1="110" x2="160" y2="110" stroke="#111" marker-end="url(#arrowBlack)"/><line x1="30" y1="110" x2="30" y2="55" stroke="#111" marker-end="url(#arrowBlack)"/>\n    <path d="M35,45 C70,42 80,72 88,100" fill="none" stroke="#111" stroke-width="2" stroke-dasharray="7 5"/><path d="M60,45 C96,48 105,84 125,103" fill="none" stroke="#d7191c" stroke-width="2"/>\n    <line x1="103" y1="48" x2="116" y2="48" stroke="#111"/><text x="122" y="52" font-size="10">Input</text><line x1="103" y1="70" x2="116" y2="70" stroke="#d7191c"/><text x="122" y="74" font-size="10">Response</text>\n    <text x="85" y="130" font-size="10">Frequency (f)</text><text x="9" y="88" transform="rotate(-90 9,88)" font-size="10">Amplitude</text>\n  </g>\n  <!-- DCMR RCEI box -->\n  <g transform="translate(36,570)">\n    <rect width="560" height="105" rx="10" fill="#ffffff" stroke="#999"/>\n    <g transform="translate(60,52)" stroke="#123c91" stroke-width="5" fill="none"><path d="M-34,25 A40,40 0 1,1 34,25"/><line x1="0" y1="0" x2="23" y2="-22"/><circle cx="0" cy="0" r="5" fill="#123c91"/><path d="M-28,25 h56"/></g>\n    <text x="145" y="36" font-size="23" font-weight="700" class="blue">DCMR</text><text x="145" y="59" text-anchor="middle" font-size="13" font-weight="700">Dynamic Contact</text><text x="145" y="77" text-anchor="middle" font-size="13" font-weight="700">Migration Rate</text><text x="145" y="95" text-anchor="middle" font-size="13">(Mobility)</text>\n    <line x1="278" y1="18" x2="278" y2="88" stroke="#aaa"/>\n    <g transform="translate(360,52)" stroke="#123c91" stroke-width="5" fill="none"><circle cx="0" cy="0" r="33"/><circle cx="0" cy="0" r="18"/><line x1="0" y1="0" x2="27" y2="-27"/><path d="M27,-27 l2,-18 l14,11"/></g>\n    <text x="465" y="36" font-size="23" font-weight="700" class="blue">RCEI</text><text x="465" y="59" text-anchor="middle" font-size="13" font-weight="700">Reservoir Contact</text><text x="465" y="77" text-anchor="middle" font-size="13" font-weight="700">Evolution Index</text><text x="465" y="95" text-anchor="middle" font-size="13">(Sensitivity)</text>\n  </g>\n  <text x="408" y="690" text-anchor="middle" font-size="16" class="ital blue">Quantifying mobility and sensitivity of contact evolution</text>\n</g>\n\n<!-- PANEL 3 -->\n<g transform="translate(1234,14)">\n  <rect width="480" height="696" rx="16" fill="#ffffff" stroke="#a33" stroke-width="1.5"/>\n  <path d="M0,16 Q0,0 16,0 H464 Q480,0 480,16 V48 H0Z" fill="#ffffff" stroke="#a33" stroke-width="1.2"/>\n  <text x="240" y="33" text-anchor="middle" class="titleDark">3. REGIME CLASSIFICATION &amp; CONTROL</text>\n  <text x="240" y="84" text-anchor="middle" font-size="17" class="ital red">DCMR–RCEI framework for prediction</text>\n  <text x="240" y="113" text-anchor="middle" font-size="17" class="ital red">and operational decision</text>\n  <!-- Chart -->\n  <g transform="translate(82,170)">\n    <rect x="0" y="0" width="386" height="344" fill="#ffffff" stroke="#444"/>\n    <rect x="0" y="0" width="120" height="344" fill="url(#stable)"/><rect x="120" y="0" width="150" height="344" fill="url(#trans)"/><rect x="270" y="0" width="116" height="344" fill="url(#unstable)"/>\n    <g stroke="#999" stroke-width=".6" opacity=".6"><path d="M0,344 H386 M0,275 H386 M0,206 H386 M0,137 H386 M0,68 H386"/><path d="M0,0 V344 M77,0 V344 M154,0 V344 M231,0 V344 M309,0 V344 M386,0 V344"/></g>\n    <path d="M70,344 C100,265 120,170 110,0" fill="none" stroke="#333" stroke-width="2" stroke-dasharray="8 8"/><path d="M210,344 C248,247 270,140 260,0" fill="none" stroke="#333" stroke-width="2" stroke-dasharray="8 8"/>\n    <text x="60" y="38" text-anchor="middle" font-size="15" font-weight="700">Stable</text><text x="60" y="58" text-anchor="middle" font-size="14" font-weight="700">(Resilient)</text>\n    <text x="190" y="38" text-anchor="middle" font-size="15" font-weight="700">Transitional</text><text x="190" y="58" text-anchor="middle" font-size="14" font-weight="700" fill="#8b0000">(Responsive)</text>\n    <text x="330" y="38" text-anchor="middle" font-size="15" font-weight="700" fill="#8b0000">Unstable</text><text x="330" y="58" text-anchor="middle" font-size="14" font-weight="700">(High risk)</text>\n    <g fill="#228b22" stroke="#0b5b0b"><circle cx="42" cy="93" r="4"/><circle cx="76" cy="104" r="4"/><circle cx="57" cy="130" r="4"/><circle cx="90" cy="152" r="4"/><circle cx="30" cy="166" r="4"/><circle cx="68" cy="188" r="4"/><circle cx="52" cy="214" r="4"/><circle cx="84" cy="214" r="4"/><circle cx="42" cy="270" r="4"/><circle cx="22" cy="300" r="4"/><circle cx="55" cy="312" r="4"/></g>\n    <g fill="#ffa51e" stroke="#bf6b00"><circle cx="173" cy="99" r="4"/><circle cx="147" cy="119" r="4"/><circle cx="180" cy="126" r="4"/><circle cx="215" cy="113" r="4"/><circle cx="142" cy="170" r="4"/><circle cx="197" cy="143" r="4"/><circle cx="170" cy="215" r="4"/><circle cx="155" cy="268" r="4"/></g>\n    <g fill="#ef2222" stroke="#a00000"><circle cx="302" cy="90" r="4"/><circle cx="332" cy="84" r="4"/><circle cx="350" cy="132" r="4"/><circle cx="282" cy="114" r="4"/><circle cx="322" cy="116" r="4"/><circle cx="295" cy="158" r="4"/><circle cx="335" cy="171" r="4"/><circle cx="275" cy="250" r="4"/><circle cx="320" cy="277" r="4"/><circle cx="305" cy="298" r="4"/></g>\n    <polyline points="86,318 132,286 168,225 204,193 246,156 286,130 326,106 360,94" fill="none" stroke="#111" stroke-width="2"/>\n    <g fill="#f7bd21" stroke="#111" stroke-width="2"><circle cx="86" cy="318" r="7"/><circle cx="132" cy="286" r="7"/><circle cx="168" cy="225" r="7"/><circle cx="204" cy="193" r="7"/><circle cx="246" cy="156" r="7"/><circle cx="286" cy="130" r="7"/></g><g fill="#f72b2b" stroke="#111" stroke-width="2"><circle cx="326" cy="106" r="7"/></g><g fill="#111"><circle cx="360" cy="94" r="7"/></g>\n    <text x="-48" y="178" transform="rotate(-90 -48,178)" font-size="15" font-weight="700">DCMR (Mobility, m/day/bar)</text>\n    <text x="193" y="386" text-anchor="middle" font-size="15" font-weight="700">RCEI (Sensitivity to pressure change)</text>\n    <text x="-8" y="6" text-anchor="end" font-size="13" font-weight="700">10<tspan dy="-5" font-size="9">1</tspan></text><text x="-8" y="75" text-anchor="end" font-size="13" font-weight="700">10<tspan dy="-5" font-size="9">0</tspan></text><text x="-8" y="144" text-anchor="end" font-size="13" font-weight="700">10<tspan dy="-5" font-size="9">-1</tspan></text><text x="-8" y="213" text-anchor="end" font-size="13" font-weight="700">10<tspan dy="-5" font-size="9">-2</tspan></text><text x="-8" y="282" text-anchor="end" font-size="13" font-weight="700">10<tspan dy="-5" font-size="9">-3</tspan></text><text x="-8" y="350" text-anchor="end" font-size="13" font-weight="700">10<tspan dy="-5" font-size="9">-4</tspan></text>\n    <text x="0" y="369" text-anchor="middle" font-size="13" font-weight="700">10<tspan dy="-5" font-size="9">-2</tspan></text><text x="96" y="369" text-anchor="middle" font-size="13" font-weight="700">10<tspan dy="-5" font-size="9">-1</tspan></text><text x="192" y="369" text-anchor="middle" font-size="13" font-weight="700">10<tspan dy="-5" font-size="9">0</tspan></text><text x="288" y="369" text-anchor="middle" font-size="13" font-weight="700">10<tspan dy="-5" font-size="9">1</tspan></text><text x="386" y="369" text-anchor="middle" font-size="13" font-weight="700">10<tspan dy="-5" font-size="9">2</tspan></text>\n  </g>\n  <!-- Control boxes -->\n  <g transform="translate(14,564)">\n    <rect width="218" height="132" rx="8" fill="#ffffff" stroke="#999"/>\n    <text x="109" y="22" text-anchor="middle" font-size="13" font-weight="700">Operational impact</text>\n    <circle cx="32" cy="50" r="9" fill="#e00000" stroke="#111"/><line x1="45" y1="50" x2="84" y2="50" stroke="#b00000" stroke-width="3" marker-end="url(#arrowRed)"/><text x="94" y="48" font-size="13" font-weight="700">Rate control</text><text x="94" y="66" font-size="12" fill="#b00000" font-weight="700">(Higher risk)</text><text x="190" y="65" fill="#d7191c" font-size="36" font-weight="700">↑</text>\n    <circle cx="32" cy="96" r="9" fill="#21a321" stroke="#111"/><line x1="45" y1="96" x2="84" y2="96" stroke="#16821c" stroke-width="3" marker-end="url(#arrowGreen)"/><text x="94" y="94" font-size="13" font-weight="700">BHP control</text><text x="94" y="112" font-size="12" fill="#16821c" font-weight="700">(Lower risk)</text><text x="190" y="112" fill="#16821c" font-size="36" font-weight="700">↓</text>\n  </g>\n  <g transform="translate(238,564)">\n    <rect width="228" height="132" rx="8" fill="#ffffff" stroke="#999"/>\n    <text x="114" y="22" text-anchor="middle" font-size="13" font-weight="700">Outcomes</text>\n    <g transform="translate(27,48)" stroke="#111" stroke-width="2" fill="none"><circle r="12"/><circle r="5"/><line x1="0" y1="0" x2="11" y2="-11" marker-end="url(#arrowBlack)"/></g><text x="52" y="53" font-size="13" font-weight="700">Predict contact behavior</text>\n    <g transform="translate(27,80)" stroke="#111" stroke-width="2" fill="none"><circle r="12"/><text x="-5" y="5" font-size="14" font-weight="700">*</text></g><text x="52" y="85" font-size="13" font-weight="700">Classify flow regime</text>\n    <g transform="translate(27,111)" stroke="#111" stroke-width="2" fill="none"><path d="M0,-13 L13,-7 L10,8 L0,16 L-10,8 L-13,-7Z"/><path d="M-5,0 l4,5 l8,-10"/></g><text x="52" y="116" font-size="13" font-weight="700">Optimize strategy</text>\n  </g>\n</g>\n\n<!-- BOTTOM FLOW -->\n<g transform="translate(55,724)">\n  <rect width="1738" height="124" rx="12" fill="#ffffff" stroke="#999"/>\n  <g transform="translate(82,62)">\n    <circle r="48" fill="#ffffff" stroke="#999"/><rect x="-35" y="18" width="70" height="12" fill="url(#sand)"/><g stroke="#111" stroke-width="2" fill="none"><line x1="0" y1="-35" x2="-17" y2="18"/><line x1="0" y1="-35" x2="17" y2="18"/><line x1="-18" y1="18" x2="18" y2="18"/><line x1="-11" y1="-10" x2="11" y2="-10"/><line x1="-15" y1="5" x2="15" y2="5"/></g><circle cx="0" cy="-40" r="3" fill="#111"/>\n  </g><text x="188" y="53" text-anchor="middle" font-size="19" font-weight="700">Static</text><text x="188" y="81" text-anchor="middle" font-size="19" font-weight="700">assumption</text>\n  <path d="M298,39 h43 v-18 l42,40 -42,40 v-18 h-43z" fill="#0d3c9d"/>\n  <g transform="translate(427,62)"><circle r="48" fill="#ffffff" stroke="#999"/><path d="M-32,18 C-18,-34 -8,34 4,-12 C17,-45 22,18 33,2" fill="none" stroke="#111" stroke-width="3"/></g><text x="547" y="43" font-size="18" font-weight="700">Transient</text><text x="547" y="68" font-size="18" font-weight="700">production</text><text x="547" y="93" font-size="18" font-weight="700">forcing</text>\n  <path d="M667,39 h43 v-18 l42,40 -42,40 v-18 h-43z" fill="#0d3c9d"/>\n  <g transform="translate(775,62)"><circle r="48" fill="#ffffff" stroke="#999"/><clipPath id="flowClip"><circle r="43"/></clipPath><g clip-path="url(#flowClip)"><rect x="-45" y="-5" width="90" height="60" fill="url(#water)"/><path d="M-45,-10 C-28,0 -16,-20 0,-10 C15,0 26,-20 45,-10 V15 H-45Z" fill="#d0a95b"/><path d="M-45,0 C-25,12 -14,-8 3,0 C17,9 28,-8 45,0" fill="none" stroke="#183d9b" stroke-width="3"/></g></g><text x="923" y="53" text-anchor="middle" font-size="17" font-weight="700">Dynamic &amp; nonlinear</text><text x="923" y="81" text-anchor="middle" font-size="17" font-weight="700">contact migration</text>\n  <path d="M1012,39 h43 v-18 l42,40 -42,40 v-18 h-43z" fill="#0d3c9d"/>\n  <g transform="translate(1146,62)"><circle r="48" fill="#ffffff" stroke="#999"/><line x1="-33" y1="33" x2="33" y2="33" stroke="#111"/><line x1="-33" y1="33" x2="-33" y2="-33" stroke="#111" marker-end="url(#arrowBlack)"/><g fill="#111"><circle cx="-15" cy="-18" r="3"/><circle cx="4" cy="-24" r="3"/><circle cx="17" cy="-8" r="3"/><circle cx="-5" cy="5" r="3"/></g><g fill="#208d22"><circle cx="-20" cy="18" r="5"/><circle cx="-3" cy="9" r="4"/></g><g fill="#df1515"><circle cx="12" cy="5" r="4"/><circle cx="25" cy="-10" r="5"/><circle cx="22" cy="20" r="3"/></g><line x1="-22" y1="22" x2="28" y2="-28" stroke="#df1515" stroke-width="2"/></g><text x="1276" y="43" font-size="18" font-weight="700">Regime</text><text x="1276" y="68" font-size="18" font-weight="700">classification</text><text x="1276" y="93" font-size="18" font-weight="700">(DCMR–RCEI)</text>\n  <path d="M1415,39 h43 v-18 l42,40 -42,40 v-18 h-43z" fill="#0d3c9d"/>\n  <g transform="translate(1564,62)"><circle r="48" fill="#ffffff" stroke="#999"/><g transform="translate(-2,0)" stroke="#111" stroke-width="3" fill="none"><line x1="-20" y1="-8" x2="-34" y2="25"/><line x1="-20" y1="-8" x2="20" y2="25"/><line x1="-35" y1="25" x2="33" y2="25"/><line x1="-17" y1="8" x2="12" y2="8"/><circle cx="25" cy="-18" r="16"/><line x1="12" y1="-14" x2="40" y2="-24"/><line x1="40" y1="-24" x2="44" y2="12"/><circle cx="44" cy="12" r="3" fill="#a00"/></g></g><text x="1710" y="43" text-anchor="middle" font-size="18" font-weight="700">Operational</text><text x="1710" y="68" text-anchor="middle" font-size="18" font-weight="700">control &amp; risk</text><text x="1710" y="93" text-anchor="middle" font-size="18" font-weight="700">mitigation</text>\n</g>\n\n</svg>'


# ============================================================
# Export functions
# ============================================================

def write_svg_and_html(outdir: Path) -> tuple[Path, Path]:
    """Write SVG and HTML wrapper."""
    outdir.mkdir(parents=True, exist_ok=True)

    svg_path = outdir / f"{BASENAME}.svg"
    html_path = outdir / f"{BASENAME}.html"

    svg_path.write_text(SVG, encoding="utf-8")

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>DCMR–RCEI Graphical Abstract</title>
<style>
html, body {
  margin: 0;
  background: #ffffff !important;
  font-family: Arial, Helvetica, sans-serif;
}
svg {
  display: block;
  background: #ffffff !important;
  background-color: #ffffff !important;
}
</style>
</head>
<body>
{SVG}
</body>
</html>
"""
    html_path.write_text(html, encoding="utf-8")

    return svg_path, html_path


def export_png_pdf_with_inkscape(svg_path: Path, png_path: Path, pdf_path: Path) -> bool:
    """
    Export using Inkscape when available.
    This is recommended because it usually preserves SVG font metrics better than CairoSVG.
    """
    inkscape = shutil.which("inkscape")
    if inkscape is None:
        return False

    subprocess.run(
        [
            inkscape,
            str(svg_path),
            "--export-type=png",
            f"--export-filename={png_path}",
            f"--export-width={WIDTH_PX}",
            f"--export-height={HEIGHT_PX}",
            "--export-background=#ffffff",
            "--export-background-opacity=1",
        ],
        check=True,
    )

    subprocess.run(
        [
            inkscape,
            str(svg_path),
            "--export-type=pdf",
            f"--export-filename={pdf_path}",
            "--export-background=#ffffff",
            "--export-background-opacity=1",
        ],
        check=True,
    )

    return True


def export_png_pdf_with_cairosvg(svg_path: Path, png_path: Path, pdf_path: Path) -> None:
    """Fallback export using CairoSVG."""
    if cairosvg is None:
        raise RuntimeError(
            "CairoSVG is not installed. Install it with: pip install cairosvg"
        )

    cairosvg.svg2png(
        url=str(svg_path),
        write_to=str(png_path),
        output_width=WIDTH_PX,
        output_height=HEIGHT_PX,
        background_color="white",
    )

    cairosvg.svg2pdf(
        url=str(svg_path),
        write_to=str(pdf_path),
        background_color="white",
    )


def png_to_tiff(png_path: Path, tiff_path: Path) -> None:
    """Convert PNG to 1200 dpi LZW-compressed TIFF."""
    image = Image.open(png_path).convert("RGB")
    image.save(tiff_path, dpi=(DPI, DPI), compression="tiff_lzw")

    # Re-save PNG with DPI metadata.
    image.save(png_path, dpi=(DPI, DPI))


def main() -> None:
    svg_path, html_path = write_svg_and_html(OUTDIR)

    png_path = OUTDIR / f"{BASENAME}_1200dpi.png"
    tiff_path = OUTDIR / f"{BASENAME}_1200dpi.tiff"
    pdf_path = OUTDIR / f"{BASENAME}.pdf"

    used_inkscape = export_png_pdf_with_inkscape(svg_path, png_path, pdf_path)

    if used_inkscape:
        print("Rendered PNG/PDF with Inkscape.")
    else:
        print("Inkscape not found. Rendering PNG/PDF with CairoSVG fallback.")
        export_png_pdf_with_cairosvg(svg_path, png_path, pdf_path)

    png_to_tiff(png_path, tiff_path)

    print("\nDone.")
    print(f"Physical size: {WIDTH_MM:.2f} mm × {HEIGHT_MM:.2f} mm")
    print(f"Raster size:   {WIDTH_PX} × {HEIGHT_PX} px at {DPI} dpi")
    print(f"SVG:  {svg_path.resolve()}")
    print(f"HTML: {html_path.resolve()}")
    print(f"PNG:  {png_path.resolve()}")
    print(f"TIFF: {tiff_path.resolve()}")
    print(f"PDF:  {pdf_path.resolve()}")


if __name__ == "__main__":
    main()
