<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DataStudio — No-Code Data Intelligence</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&family=Cabinet+Grotesk:wght@300;400;500;700;900&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0a0f;
    --surface: #111118;
    --surface2: #1a1a24;
    --border: rgba(255,255,255,0.08);
    --accent: #7c6aff;
    --accent2: #ff6a6a;
    --accent3: #6affb0;
    --accent4: #ffca6a;
    --text: #f0f0ff;
    --text-dim: rgba(240,240,255,0.45);
    --text-mid: rgba(240,240,255,0.7);
    --glow: 0 0 40px rgba(124,106,255,0.25);
    --glow2: 0 0 40px rgba(255,106,106,0.25);
    --radius: 16px;
  }
 
  * { box-sizing: border-box; margin: 0; padding: 0; }
 
  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Cabinet Grotesk', sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
  }
 
  /* ─── WELCOME SCREEN ─── */
  #welcome {
    position: fixed; inset: 0; z-index: 1000;
    background: var(--bg);
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    overflow: hidden;
    transition: opacity 0.8s ease, transform 0.8s ease;
  }
 
  #welcome.exit {
    opacity: 0;
    transform: scale(1.05);
    pointer-events: none;
  }
 
  .welcome-grid {
    position: absolute; inset: 0;
    background-image:
      linear-gradient(rgba(124,106,255,0.07) 1px, transparent 1px),
      linear-gradient(90deg, rgba(124,106,255,0.07) 1px, transparent 1px);
    background-size: 60px 60px;
    animation: gridPulse 4s ease-in-out infinite;
  }
 
  @keyframes gridPulse {
    0%, 100% { opacity: 0.5; }
    50% { opacity: 1; }
  }
 
  .welcome-orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    animation: orbFloat 6s ease-in-out infinite;
  }
  .orb1 { width: 500px; height: 500px; background: rgba(124,106,255,0.18); top: -100px; left: -100px; animation-delay: 0s; }
  .orb2 { width: 400px; height: 400px; background: rgba(255,106,106,0.12); bottom: -80px; right: -80px; animation-delay: -2s; }
  .orb3 { width: 300px; height: 300px; background: rgba(106,255,176,0.1); top: 40%; left: 60%; animation-delay: -4s; }
 
  @keyframes orbFloat {
    0%, 100% { transform: translate(0,0) scale(1); }
    50% { transform: translate(20px,-20px) scale(1.05); }
  }
 
  .welcome-content { position: relative; z-index: 2; text-align: center; }
 
  .welcome-icon {
    width: 80px; height: 80px; margin: 0 auto 32px;
    position: relative;
    animation: iconEntry 1s cubic-bezier(0.34,1.56,0.64,1) 0.2s both;
  }
  .welcome-icon svg { width: 80px; height: 80px; }
 
  @keyframes iconEntry {
    from { transform: scale(0) rotate(-180deg); opacity: 0; }
    to   { transform: scale(1) rotate(0deg); opacity: 1; }
  }
 
  .welcome-badge {
    display: inline-block;
    background: rgba(124,106,255,0.15);
    border: 1px solid rgba(124,106,255,0.4);
    color: var(--accent);
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 3px;
    padding: 6px 18px;
    border-radius: 100px;
    margin-bottom: 24px;
    animation: fadeUp 0.8s ease 0.5s both;
  }
 
  .welcome-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(52px, 8vw, 96px);
    font-weight: 800;
    line-height: 0.95;
    letter-spacing: -3px;
    animation: fadeUp 0.8s ease 0.7s both;
  }
 
  .welcome-title span.grad {
    background: linear-gradient(135deg, var(--accent) 0%, #a78bfa 40%, var(--accent2) 80%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
  }
 
  .welcome-subtitle {
    font-size: 18px;
    color: var(--text-mid);
    margin-top: 16px;
    max-width: 500px;
    line-height: 1.6;
    animation: fadeUp 0.8s ease 0.9s both;
  }
 
  .welcome-cta {
    display: inline-flex; align-items: center; gap: 10px;
    margin-top: 48px;
    background: var(--accent);
    color: #fff;
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 16px;
    padding: 16px 36px;
    border-radius: 100px;
    border: none; cursor: pointer;
    box-shadow: 0 0 40px rgba(124,106,255,0.5);
    animation: fadeUp 0.8s ease 1.1s both, ctaPulse 2.5s ease-in-out 2s infinite;
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .welcome-cta:hover { transform: scale(1.05); box-shadow: 0 0 60px rgba(124,106,255,0.7); }
 
  @keyframes ctaPulse {
    0%,100% { box-shadow: 0 0 40px rgba(124,106,255,0.5); }
    50% { box-shadow: 0 0 70px rgba(124,106,255,0.8); }
  }
 
  .welcome-features {
    display: flex; gap: 24px; margin-top: 48px; justify-content: center;
    animation: fadeUp 0.8s ease 1.3s both;
  }
 
  .welcome-feat {
    display: flex; align-items: center; gap: 8px;
    font-family: 'DM Mono', monospace; font-size: 12px;
    color: var(--text-dim);
  }
  .welcome-feat-dot { width: 6px; height: 6px; border-radius: 50%; }
 
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(30px); }
    to   { opacity: 1; transform: translateY(0); }
  }
 
  .particles {
    position: absolute; inset: 0; pointer-events: none;
  }
 
  .particle {
    position: absolute;
    width: 3px; height: 3px;
    background: var(--accent);
    border-radius: 50%;
    animation: particleDrift linear infinite;
    opacity: 0;
  }
 
  @keyframes particleDrift {
    0%   { transform: translateY(100vh) translateX(0); opacity: 0; }
    10%  { opacity: 0.6; }
    90%  { opacity: 0.6; }
    100% { transform: translateY(-10vh) translateX(var(--dx,20px)); opacity: 0; }
  }
 
  /* ─── MAIN APP ─── */
  #app {
    display: none; flex-direction: column; min-height: 100vh;
    opacity: 0;
    transition: opacity 0.8s ease 0.3s;
  }
  #app.visible { display: flex; }
  #app.shown { opacity: 1; }
 
  /* Header */
  header {
    position: sticky; top: 0; z-index: 100;
    background: rgba(10,10,15,0.85);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border);
    padding: 0 32px;
    height: 64px;
    display: flex; align-items: center; justify-content: space-between;
  }
 
  .logo {
    font-family: 'Syne', sans-serif;
    font-weight: 800; font-size: 20px;
    display: flex; align-items: center; gap: 10px;
    letter-spacing: -0.5px;
  }
  .logo-icon { width: 28px; height: 28px; }
 
  .header-info {
    display: flex; align-items: center; gap: 16px;
  }
 
  .data-badge {
    display: flex; align-items: center; gap: 8px;
    background: rgba(106,255,176,0.1);
    border: 1px solid rgba(106,255,176,0.25);
    color: var(--accent3);
    font-family: 'DM Mono', monospace; font-size: 12px;
    padding: 6px 14px; border-radius: 100px;
    transition: all 0.3s;
  }
  .data-badge.hidden { display: none; }
  .data-badge-dot { width: 6px; height: 6px; background: var(--accent3); border-radius: 50%; animation: blink 1.5s ease-in-out infinite; }
  @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.2} }
 
  /* Main layout */
  main {
    flex: 1;
    display: grid;
    grid-template-columns: 320px 1fr;
    grid-template-rows: 1fr;
    gap: 0;
    max-height: calc(100vh - 64px);
    overflow: hidden;
  }
 
  /* Sidebar */
  aside {
    border-right: 1px solid var(--border);
    background: var(--surface);
    display: flex; flex-direction: column;
    overflow: hidden;
  }
 
  .aside-header {
    padding: 20px 24px 16px;
    border-bottom: 1px solid var(--border);
  }
 
  .aside-title {
    font-family: 'Syne', sans-serif;
    font-weight: 700; font-size: 13px;
    letter-spacing: 2px; text-transform: uppercase;
    color: var(--text-dim);
  }
 
  .data-input-area {
    flex: 1;
    display: flex; flex-direction: column;
    padding: 20px 24px;
    gap: 14px;
    overflow-y: auto;
  }
 
  .input-label {
    font-size: 13px; color: var(--text-dim);
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.5px;
  }
 
  textarea#dataInput {
    flex: 1;
    min-height: 220px;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 12px;
    color: var(--text);
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    line-height: 1.6;
    padding: 14px 16px;
    resize: none;
    outline: none;
    transition: border-color 0.2s, box-shadow 0.2s;
  }
  textarea#dataInput:focus {
    border-color: rgba(124,106,255,0.5);
    box-shadow: 0 0 20px rgba(124,106,255,0.1);
  }
  textarea#dataInput::placeholder { color: rgba(240,240,255,0.2); }
 
  .file-drop {
    border: 1.5px dashed rgba(124,106,255,0.3);
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    cursor: pointer;
    transition: all 0.2s;
    position: relative;
  }
  .file-drop:hover, .file-drop.dragover {
    border-color: var(--accent);
    background: rgba(124,106,255,0.05);
  }
  .file-drop input { position: absolute; inset: 0; opacity: 0; cursor: pointer; }
  .file-drop-icon { font-size: 24px; margin-bottom: 6px; }
  .file-drop-text { font-size: 12px; color: var(--text-dim); line-height: 1.5; }
  .file-drop-text strong { color: var(--accent); }
 
  .format-hint {
    font-family: 'DM Mono', monospace;
    font-size: 11px; color: var(--text-dim);
    background: rgba(255,255,255,0.03);
    border-radius: 8px;
    padding: 10px 14px;
    line-height: 1.8;
  }
 
  .btn-analyze {
    display: flex; align-items: center; justify-content: center; gap: 10px;
    background: linear-gradient(135deg, var(--accent), #a78bfa);
    color: #fff;
    font-family: 'Syne', sans-serif;
    font-weight: 700; font-size: 15px;
    padding: 14px;
    border-radius: 12px;
    border: none; cursor: pointer;
    transition: all 0.2s;
    box-shadow: 0 4px 20px rgba(124,106,255,0.35);
  }
  .btn-analyze:hover { transform: translateY(-2px); box-shadow: 0 8px 30px rgba(124,106,255,0.5); }
  .btn-analyze:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }
 
  /* Right content area */
  .content-area {
    display: flex; flex-direction: column;
    overflow: hidden;
    background: var(--bg);
  }
 
  /* Tabs */
  .tabs-bar {
    display: flex; gap: 0;
    border-bottom: 1px solid var(--border);
    padding: 0 24px;
    background: var(--surface);
    overflow-x: auto;
  }
 
  .tab-btn {
    display: flex; align-items: center; gap: 8px;
    padding: 16px 22px;
    background: none; border: none; cursor: pointer;
    color: var(--text-dim);
    font-family: 'Cabinet Grotesk', sans-serif;
    font-weight: 500; font-size: 14px;
    border-bottom: 2px solid transparent;
    white-space: nowrap;
    transition: all 0.2s;
    position: relative;
    top: 1px;
  }
  .tab-btn:hover { color: var(--text); }
  .tab-btn.active {
    color: var(--text);
    border-bottom-color: var(--accent);
  }
  .tab-icon { font-size: 16px; }
 
  /* Tab panels */
  .tab-panels { flex: 1; overflow-y: auto; padding: 28px; }
 
  .tab-panel { display: none; animation: panelIn 0.3s ease; }
  .tab-panel.active { display: block; }
 
  @keyframes panelIn {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
  }
 
  /* Empty state */
  .empty-state {
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    min-height: 400px;
    color: var(--text-dim); text-align: center;
  }
  .empty-state-icon { font-size: 48px; margin-bottom: 16px; opacity: 0.5; }
  .empty-state h3 { font-family: 'Syne', sans-serif; font-size: 20px; margin-bottom: 8px; color: var(--text-mid); }
  .empty-state p { font-size: 14px; max-width: 300px; line-height: 1.6; }
 
  /* Loading animation */
  .loading-overlay {
    display: none; flex-direction: column; align-items: center; justify-content: center;
    min-height: 400px; gap: 20px;
  }
  .loading-overlay.show { display: flex; }
 
  .loader-ring {
    width: 60px; height: 60px;
    border: 3px solid var(--border);
    border-top-color: var(--accent);
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
  }
  @keyframes spin { to { transform: rotate(360deg); } }
 
  .loader-text {
    font-family: 'DM Mono', monospace; font-size: 13px;
    color: var(--text-dim);
    animation: loadingText 2s ease-in-out infinite;
  }
  @keyframes loadingText { 0%,100%{opacity:0.5} 50%{opacity:1} }
 
  /* ─── DATA OVERVIEW CARDS ─── */
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 16px;
    margin-bottom: 28px;
  }
 
  .stat-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 20px;
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .stat-card:hover { transform: translateY(-3px); box-shadow: 0 8px 30px rgba(0,0,0,0.3); }
 
  .stat-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase;
    color: var(--text-dim); margin-bottom: 10px;
  }
 
  .stat-value {
    font-family: 'Syne', sans-serif;
    font-size: 32px; font-weight: 800;
    line-height: 1;
  }
 
  .stat-sub { font-size: 12px; color: var(--text-dim); margin-top: 6px; }
 
  /* Table */
  .table-wrapper {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    overflow: hidden;
    margin-bottom: 24px;
  }
 
  .table-header-bar {
    display: flex; align-items: center; justify-content: space-between;
    padding: 16px 20px;
    border-bottom: 1px solid var(--border);
  }
 
  .table-title {
    font-family: 'Syne', sans-serif;
    font-weight: 700; font-size: 15px;
  }
 
  .table-scroll { overflow-x: auto; }
 
  table {
    width: 100%; border-collapse: collapse;
    font-size: 13px;
  }
 
  th {
    background: rgba(124,106,255,0.08);
    color: var(--accent);
    font-family: 'DM Mono', monospace;
    font-size: 11px; letter-spacing: 1px; text-transform: uppercase;
    padding: 12px 16px;
    text-align: left;
    border-bottom: 1px solid var(--border);
    white-space: nowrap;
  }
 
  td {
    padding: 10px 16px;
    border-bottom: 1px solid rgba(255,255,255,0.03);
    color: var(--text-mid);
    font-family: 'DM Mono', monospace; font-size: 12px;
    white-space: nowrap;
  }
 
  tr:hover td { background: rgba(255,255,255,0.03); color: var(--text); }
  tr:last-child td { border-bottom: none; }
 
  /* Chart containers */
  .chart-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    gap: 20px;
    margin-bottom: 24px;
  }
 
  .chart-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    overflow: hidden;
  }
 
  .chart-card-header {
    padding: 16px 20px;
    border-bottom: 1px solid var(--border);
    display: flex; align-items: center; justify-content: space-between;
  }
  .chart-card-title {
    font-family: 'Syne', sans-serif;
    font-weight: 700; font-size: 14px;
  }
  .chart-card-sub { font-size: 12px; color: var(--text-dim); }
 
  .chart-body { padding: 20px; }
 
  canvas { max-width: 100%; }
 
  /* ─── CLEANING ─── */
  .issues-list { display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px; }
 
  .issue-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px 20px;
    display: flex; align-items: center; gap: 16px;
    transition: all 0.2s;
  }
  .issue-card.fixed { border-color: rgba(106,255,176,0.3); background: rgba(106,255,176,0.05); }
 
  .issue-icon { font-size: 24px; flex-shrink: 0; }
  .issue-info { flex: 1; }
  .issue-title { font-weight: 600; font-size: 14px; margin-bottom: 4px; }
  .issue-desc { font-size: 13px; color: var(--text-dim); line-height: 1.5; }
  .issue-count {
    background: rgba(255,106,106,0.15);
    color: var(--accent2);
    font-family: 'DM Mono', monospace; font-size: 11px;
    padding: 4px 10px; border-radius: 100px;
    white-space: nowrap;
  }
  .issue-count.ok { background: rgba(106,255,176,0.1); color: var(--accent3); }
 
  .btn-fix {
    background: rgba(124,106,255,0.15);
    color: var(--accent);
    border: 1px solid rgba(124,106,255,0.3);
    font-family: 'Cabinet Grotesk', sans-serif;
    font-weight: 600; font-size: 13px;
    padding: 8px 18px; border-radius: 100px;
    cursor: pointer; transition: all 0.2s;
    white-space: nowrap;
  }
  .btn-fix:hover { background: rgba(124,106,255,0.3); }
  .btn-fix.done { background: rgba(106,255,176,0.1); color: var(--accent3); border-color: rgba(106,255,176,0.3); cursor: default; }
 
  /* ─── EXTRACTION ─── */
  .extraction-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
 
  .extract-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 20px;
  }
  .extract-card h4 {
    font-family: 'Syne', sans-serif;
    font-weight: 700; font-size: 14px;
    margin-bottom: 14px;
    display: flex; align-items: center; gap: 8px;
  }
 
  .tag-list { display: flex; flex-wrap: wrap; gap: 8px; }
  .tag {
    background: rgba(124,106,255,0.1);
    border: 1px solid rgba(124,106,255,0.2);
    color: var(--accent);
    font-family: 'DM Mono', monospace; font-size: 12px;
    padding: 5px 12px; border-radius: 100px;
  }
  .tag.green { background: rgba(106,255,176,0.1); border-color: rgba(106,255,176,0.2); color: var(--accent3); }
  .tag.orange { background: rgba(255,202,106,0.1); border-color: rgba(255,202,106,0.2); color: var(--accent4); }
  .tag.red { background: rgba(255,106,106,0.1); border-color: rgba(255,106,106,0.2); color: var(--accent2); }
 
  .kv-list { display: flex; flex-direction: column; gap: 8px; }
  .kv-row { display: flex; justify-content: space-between; align-items: center; font-size: 13px; }
  .kv-key { color: var(--text-dim); font-family: 'DM Mono', monospace; font-size: 12px; }
  .kv-val { color: var(--text); font-weight: 500; }
 
  /* ─── AI INSIGHTS ─── */
  .insights-container {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 24px;
    margin-bottom: 20px;
  }
 
  .insight-header {
    display: flex; align-items: center; gap: 10px;
    margin-bottom: 16px;
  }
  .insight-header h3 { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 18px; }
  .ai-badge {
    background: linear-gradient(135deg, var(--accent), #a78bfa);
    font-size: 10px; font-family: 'DM Mono', monospace;
    letter-spacing: 1.5px; text-transform: uppercase;
    padding: 3px 10px; border-radius: 100px; color: #fff;
  }
 
  .insight-text {
    font-size: 15px; line-height: 1.8;
    color: var(--text-mid);
    white-space: pre-wrap;
  }
 
  .insight-text .typing-cursor {
    display: inline-block;
    width: 2px; height: 16px;
    background: var(--accent);
    animation: blink 0.8s ease-in-out infinite;
    vertical-align: middle;
    margin-left: 2px;
  }
 
  /* Section headers */
  .section-title {
    font-family: 'Syne', sans-serif;
    font-weight: 700; font-size: 20px;
    margin-bottom: 20px;
    display: flex; align-items: center; gap: 12px;
  }
  .section-title::after {
    content: '';
    flex: 1; height: 1px;
    background: var(--border);
  }
 
  /* Download buttons */
  .action-row { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 24px; }
 
  .btn-action {
    display: flex; align-items: center; gap: 8px;
    background: var(--surface2);
    border: 1px solid var(--border);
    color: var(--text-mid);
    font-family: 'Cabinet Grotesk', sans-serif;
    font-weight: 500; font-size: 13px;
    padding: 10px 20px; border-radius: 100px;
    cursor: pointer; transition: all 0.2s;
  }
  .btn-action:hover { border-color: var(--accent); color: var(--accent); background: rgba(124,106,255,0.08); }
 
  /* Scrollbar */
  ::-webkit-scrollbar { width: 6px; height: 6px; }
  ::-webkit-scrollbar-track { background: transparent; }
  ::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 3px; }
  ::-webkit-scrollbar-thumb:hover { background: rgba(255,255,255,0.2); }
 
  /* Notification toast */
  .toast {
    position: fixed; bottom: 28px; right: 28px; z-index: 9999;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px 20px;
    font-size: 14px;
    display: flex; align-items: center; gap: 10px;
    transform: translateY(80px);
    opacity: 0;
    transition: all 0.3s cubic-bezier(0.34,1.56,0.64,1);
    box-shadow: 0 8px 30px rgba(0,0,0,0.4);
    max-width: 360px;
  }
  .toast.show { transform: translateY(0); opacity: 1; }
 
  /* Responsive */
  @media (max-width: 900px) {
    main { grid-template-columns: 1fr; grid-template-rows: auto 1fr; }
    aside { max-height: 340px; border-right: none; border-bottom: 1px solid var(--border); }
    .extraction-grid { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>
 
<!-- ═══ WELCOME SCREEN ═══ -->
<div id="welcome">
  <div class="welcome-grid"></div>
  <div class="welcome-orb orb1"></div>
  <div class="welcome-orb orb2"></div>
  <div class="welcome-orb orb3"></div>
  <div class="particles" id="particles"></div>
 
  <div class="welcome-content">
    <div class="welcome-icon">
      <svg viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="40" cy="40" r="38" stroke="url(#wg1)" stroke-width="2"/>
        <rect x="18" y="30" width="10" height="22" rx="3" fill="url(#wg1)" opacity="0.9"/>
        <rect x="33" y="22" width="10" height="30" rx="3" fill="url(#wg2)" opacity="0.9"/>
        <rect x="48" y="35" width="10" height="17" rx="3" fill="url(#wg3)" opacity="0.9"/>
        <circle cx="23" cy="28" r="3" fill="url(#wg1)"/>
        <circle cx="38" cy="20" r="3" fill="url(#wg2)"/>
        <circle cx="53" cy="33" r="3" fill="url(#wg3)"/>
        <polyline points="23,28 38,20 53,33" stroke="rgba(255,255,255,0.4)" stroke-width="1.5" stroke-dasharray="3,3"/>
        <defs>
          <linearGradient id="wg1" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#7c6aff"/><stop offset="1" stop-color="#a78bfa"/></linearGradient>
          <linearGradient id="wg2" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#ff6a6a"/><stop offset="1" stop-color="#ff9a9a"/></linearGradient>
          <linearGradient id="wg3" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#6affb0"/><stop offset="1" stop-color="#a0ffcf"/></linearGradient>
        </defs>
      </svg>
    </div>
 
    <div class="welcome-badge">✦ NO-CODE DATA INTELLIGENCE ✦</div>
 
    <h1 class="welcome-title">
      Data<span class="grad">Studio</span>
    </h1>
    <p class="welcome-subtitle">
      Drop your data. Watch the magic happen. Clean, analyze, extract, and visualize — zero code required.
    </p>
 
    <button class="welcome-cta" onclick="enterApp()">
      <span>Get Started</span>
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
    </button>
 
    <div class="welcome-features">
      <div class="welcome-feat"><div class="welcome-feat-dot" style="background:#7c6aff"></div>Instant Clean</div>
      <div class="welcome-feat"><div class="welcome-feat-dot" style="background:#ff6a6a"></div>Smart Analyze</div>
      <div class="welcome-feat"><div class="welcome-feat-dot" style="background:#6affb0"></div>Auto Extract</div>
      <div class="welcome-feat"><div class="welcome-feat-dot" style="background:#ffca6a"></div>Rich Visualize</div>
    </div>
  </div>
</div>
 
<!-- ═══ MAIN APP ═══ -->
<div id="app">
  <header>
    <div class="logo">
      <svg class="logo-icon" viewBox="0 0 28 28" fill="none">
        <rect x="4" y="10" width="4" height="12" rx="1.5" fill="#7c6aff"/>
        <rect x="12" y="6" width="4" height="16" rx="1.5" fill="#ff6a6a"/>
        <rect x="20" y="13" width="4" height="9" rx="1.5" fill="#6affb0"/>
        <polyline points="6,9 14,5 22,12" stroke="rgba(255,255,255,0.3)" stroke-width="1.5" stroke-dasharray="2,2" fill="none"/>
      </svg>
      DataStudio
    </div>
    <div class="header-info">
      <div class="data-badge hidden" id="dataBadge">
        <div class="data-badge-dot"></div>
        <span id="dataBadgeText">Data loaded</span>
      </div>
    </div>
  </header>
 
  <main>
    <!-- Sidebar: Data Input -->
    <aside>
      <div class="aside-header">
        <div class="aside-title">📥 Data Input</div>
      </div>
      <div class="data-input-area">
        <div class="input-label">Paste CSV, JSON, or plain text:</div>
 
        <textarea id="dataInput" placeholder="Name, Age, City, Salary
Alice, 28, New York, 72000
Bob, 34, Los Angeles, 88000
Charlie, , Chicago, 
Diana, 29, New York, 95000
Eve, 45, Chicago, 110000
Frank, 31, Los Angeles, 76000
Grace, 28, New York, 84000
Henry, , Chicago, 91000"></textarea>
 
        <div class="file-drop" id="fileDrop">
          <input type="file" id="fileInput" accept=".csv,.json,.txt" onchange="handleFileUpload(event)">
          <div class="file-drop-icon">📁</div>
          <div class="file-drop-text"><strong>Drop a file</strong> or click to browse<br>.CSV  .JSON  .TXT</div>
        </div>
 
        <div class="format-hint">
          Supports: CSV with headers, JSON arrays, key-value pairs, tab-separated values
        </div>
 
        <button class="btn-analyze" onclick="analyzeData()" id="analyzeBtn">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="5,3 19,12 5,21"/></svg>
          Analyze Data
        </button>
      </div>
    </aside>
 
    <!-- Content area -->
    <div class="content-area">
      <!-- Tabs -->
      <div class="tabs-bar">
        <button class="tab-btn active" onclick="switchTab('overview',this)"><span class="tab-icon">📊</span> Overview</button>
        <button class="tab-btn" onclick="switchTab('clean',this)"><span class="tab-icon">🧹</span> Clean</button>
        <button class="tab-btn" onclick="switchTab('visualize',this)"><span class="tab-icon">📈</span> Visualize</button>
        <button class="tab-btn" onclick="switchTab('extract',this)"><span class="tab-icon">🔍</span> Extract</button>
        <button class="tab-btn" onclick="switchTab('insights',this)"><span class="tab-icon">🤖</span> AI Insights</button>
      </div>
 
      <!-- Panels -->
      <div class="tab-panels">
        <!-- OVERVIEW -->
        <div class="tab-panel active" id="panel-overview">
          <div class="empty-state" id="empty-overview">
            <div class="empty-state-icon">📊</div>
            <h3>No data yet</h3>
            <p>Paste your data in the left panel and click <strong>Analyze Data</strong> to get started.</p>
          </div>
          <div id="loading-overview" class="loading-overlay">
            <div class="loader-ring"></div>
            <div class="loader-text">Processing your data…</div>
          </div>
          <div id="content-overview" style="display:none">
            <div class="section-title">Data Overview</div>
            <div class="stats-grid" id="statsGrid"></div>
            <div class="action-row" id="downloadRow">
              <button class="btn-action" onclick="downloadClean()">⬇️ Download Clean CSV</button>
              <button class="btn-action" onclick="downloadJSON()">⬇️ Download JSON</button>
              <button class="btn-action" onclick="clearData()">🗑️ Clear Data</button>
            </div>
            <div class="table-wrapper">
              <div class="table-header-bar">
                <span class="table-title">Data Preview</span>
                <span style="font-size:13px;color:var(--text-dim)" id="rowCount"></span>
              </div>
              <div class="table-scroll">
                <table id="dataTable"></table>
              </div>
            </div>
          </div>
        </div>
 
        <!-- CLEAN -->
        <div class="tab-panel" id="panel-clean">
          <div class="empty-state" id="empty-clean">
            <div class="empty-state-icon">🧹</div>
            <h3>Nothing to clean</h3>
            <p>Load and analyze your data first to discover cleaning suggestions.</p>
          </div>
          <div id="content-clean" style="display:none">
            <div class="section-title">Data Cleaning</div>
            <div class="issues-list" id="issuesList"></div>
            <div class="table-wrapper" id="cleanedTableWrapper" style="display:none">
              <div class="table-header-bar">
                <span class="table-title">Cleaned Data Preview</span>
              </div>
              <div class="table-scroll">
                <table id="cleanedTable"></table>
              </div>
            </div>
          </div>
        </div>
 
        <!-- VISUALIZE -->
        <div class="tab-panel" id="panel-visualize">
          <div class="empty-state" id="empty-visualize">
            <div class="empty-state-icon">📈</div>
            <h3>No charts yet</h3>
            <p>Analyze your data and switch here to see auto-generated visualizations.</p>
          </div>
          <div id="content-visualize" style="display:none">
            <div class="section-title">Visualizations</div>
            <div class="chart-grid" id="chartGrid"></div>
          </div>
        </div>
 
        <!-- EXTRACT -->
        <div class="tab-panel" id="panel-extract">
          <div class="empty-state" id="empty-extract">
            <div class="empty-state-icon">🔍</div>
            <h3>Nothing extracted yet</h3>
            <p>Analyze your data to automatically extract key entities, statistics, and patterns.</p>
          </div>
          <div id="content-extract" style="display:none">
            <div class="section-title">Data Extraction</div>
            <div class="extraction-grid" id="extractionGrid"></div>
          </div>
        </div>
 
        <!-- AI INSIGHTS -->
        <div class="tab-panel" id="panel-insights">
          <div class="empty-state" id="empty-insights">
            <div class="empty-state-icon">🤖</div>
            <h3>No insights yet</h3>
            <p>Analyze your data to generate AI-powered insights and recommendations.</p>
          </div>
          <div id="loading-insights" class="loading-overlay">
            <div class="loader-ring"></div>
            <div class="loader-text">Generating AI insights…</div>
          </div>
          <div id="content-insights" style="display:none">
            <div class="section-title">AI Insights</div>
            <div class="insights-container">
              <div class="insight-header">
                <h3>Data Intelligence Report</h3>
                <span class="ai-badge">AI Powered</span>
              </div>
              <div class="insight-text" id="insightText"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</div>
 
<div class="toast" id="toast"></div>
 
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<script>
// ═══════════════════════════════════════════════════════
// PARTICLES
// ═══════════════════════════════════════════════════════
const particlesEl = document.getElementById('particles');
const colors = ['#7c6aff','#ff6a6a','#6affb0','#ffca6a'];
for (let i = 0; i < 40; i++) {
  const p = document.createElement('div');
  p.className = 'particle';
  p.style.left = Math.random() * 100 + 'vw';
  p.style.animationDuration = (6 + Math.random() * 10) + 's';
  p.style.animationDelay = (Math.random() * 10) + 's';
  p.style.setProperty('--dx', (Math.random() - 0.5) * 100 + 'px');
  p.style.background = colors[Math.floor(Math.random() * colors.length)];
  p.style.width = p.style.height = (2 + Math.random() * 3) + 'px';
  particlesEl.appendChild(p);
}
 
// ═══════════════════════════════════════════════════════
// WELCOME → APP TRANSITION
// ═══════════════════════════════════════════════════════
function enterApp() {
  const welcome = document.getElementById('welcome');
  const app = document.getElementById('app');
  welcome.classList.add('exit');
  app.classList.add('visible');
  setTimeout(() => { app.classList.add('shown'); }, 50);
  setTimeout(() => { welcome.style.display = 'none'; }, 900);
}
 
// ═══════════════════════════════════════════════════════
// DRAG & DROP FILE
// ═══════════════════════════════════════════════════════
const fileDrop = document.getElementById('fileDrop');
fileDrop.addEventListener('dragover', e => { e.preventDefault(); fileDrop.classList.add('dragover'); });
fileDrop.addEventListener('dragleave', () => fileDrop.classList.remove('dragover'));
fileDrop.addEventListener('drop', e => {
  e.preventDefault(); fileDrop.classList.remove('dragover');
  const file = e.dataTransfer.files[0];
  if (file) readFile(file);
});
 
function handleFileUpload(e) {
  const file = e.target.files[0];
  if (file) readFile(file);
}
 
function readFile(file) {
  const reader = new FileReader();
  reader.onload = evt => {
    document.getElementById('dataInput').value = evt.target.result;
    showToast('📁 File loaded: ' + file.name);
  };
  reader.readAsText(file);
}
 
// ═══════════════════════════════════════════════════════
// GLOBAL STATE
// ═══════════════════════════════════════════════════════
let parsedData = { headers: [], rows: [], types: {} };
let cleanedData = { headers: [], rows: [] };
let charts = [];
 
// ═══════════════════════════════════════════════════════
// PARSE DATA
// ═══════════════════════════════════════════════════════
function parseInput(raw) {
  raw = raw.trim();
  if (!raw) return null;
 
  // Try JSON
  if (raw.startsWith('[') || raw.startsWith('{')) {
    try {
      let json = JSON.parse(raw);
      if (!Array.isArray(json)) json = [json];
      if (json.length === 0) return null;
      const headers = Object.keys(json[0]);
      const rows = json.map(obj => headers.map(h => obj[h] !== undefined ? String(obj[h]) : ''));
      return { headers, rows };
    } catch(e) {}
  }
 
  // CSV / TSV
  const lines = raw.split('\n').map(l => l.trim()).filter(Boolean);
  if (lines.length < 2) return null;
 
  const delim = lines[0].includes('\t') ? '\t' : ',';
  const headers = lines[0].split(delim).map(h => h.trim().replace(/^"|"$/g,''));
  const rows = lines.slice(1).map(l => {
    // handle quoted CSV properly
    const result = [];
    let cur = '';
    let inQ = false;
    for (let c of l) {
      if (c === '"') { inQ = !inQ; }
      else if (c === delim && !inQ) { result.push(cur.trim()); cur = ''; }
      else { cur += c; }
    }
    result.push(cur.trim());
    return result.map(v => v.replace(/^"|"$/g,''));
  });
 
  return { headers, rows };
}
 
function inferTypes(headers, rows) {
  const types = {};
  headers.forEach((h, i) => {
    const vals = rows.map(r => r[i]).filter(v => v && v !== '');
    const numericCount = vals.filter(v => !isNaN(parseFloat(v))).length;
    types[h] = numericCount / (vals.length || 1) > 0.7 ? 'numeric' : 'string';
  });
  return types;
}
 
// ═══════════════════════════════════════════════════════
// MAIN ANALYZE FUNCTION
// ═══════════════════════════════════════════════════════
function analyzeData() {
  const raw = document.getElementById('dataInput').value;
  if (!raw.trim()) { showToast('⚠️ Please enter some data first!'); return; }
 
  const parsed = parseInput(raw);
  if (!parsed) { showToast('❌ Could not parse data. Try CSV or JSON format.'); return; }
 
  parsedData = { ...parsed, types: inferTypes(parsed.headers, parsed.rows) };
  cleanedData = { headers: [...parsedData.headers], rows: parsedData.rows.map(r => [...r]) };
 
  // Show loading
  document.getElementById('empty-overview').style.display = 'none';
  document.getElementById('loading-overview').classList.add('show');
 
  setTimeout(() => {
    document.getElementById('loading-overview').classList.remove('show');
    renderOverview();
    renderCleaning();
    renderVisualizations();
    renderExtraction();
 
    document.getElementById('dataBadge').classList.remove('hidden');
    document.getElementById('dataBadgeText').textContent =
      `${parsedData.rows.length} rows × ${parsedData.headers.length} cols`;
 
    switchTab('overview', document.querySelector('.tab-btn'));
    showToast('✅ Data analyzed successfully!');
 
    // Trigger AI insights in background
    renderAIInsights();
  }, 900);
}
 
// ═══════════════════════════════════════════════════════
// OVERVIEW
// ═══════════════════════════════════════════════════════
function renderOverview() {
  const { headers, rows, types } = parsedData;
 
  const missingCount = rows.reduce((acc, row) =>
    acc + row.filter(v => !v || v.trim() === '').length, 0);
  const totalCells = rows.length * headers.length;
  const numericCols = headers.filter(h => types[h] === 'numeric');
 
  // Stats cards
  const statsData = [
    { label: 'Total Rows', value: rows.length, sub: 'records', color: '#7c6aff' },
    { label: 'Columns', value: headers.length, sub: 'fields', color: '#ff6a6a' },
    { label: 'Missing Values', value: missingCount, sub: `${((missingCount/totalCells)*100).toFixed(1)}% of cells`, color: '#ffca6a' },
    { label: 'Numeric Cols', value: numericCols.length, sub: headers.length - numericCols.length + ' text cols', color: '#6affb0' },
  ];
 
  document.getElementById('statsGrid').innerHTML = statsData.map(s => `
    <div class="stat-card">
      <div class="stat-label">${s.label}</div>
      <div class="stat-value" style="color:${s.color}">${s.value}</div>
      <div class="stat-sub">${s.sub}</div>
    </div>
  `).join('');
 
  // Table
  const previewRows = rows.slice(0, 50);
  document.getElementById('rowCount').textContent = `Showing ${Math.min(50, rows.length)} of ${rows.length} rows`;
  document.getElementById('dataTable').innerHTML = `
    <thead><tr>${headers.map(h => `<th>${h}<br><span style="color:var(--text-dim);font-size:9px;text-transform:none;letter-spacing:0">${parsedData.types[h]}</span></th>`).join('')}</tr></thead>
    <tbody>${previewRows.map(row => `<tr>${row.map(v => `<td>${v || '<span style="color:rgba(255,106,106,0.5)">∅</span>'}</td>`).join('')}</tr>`).join('')}</tbody>
  `;
 
  document.getElementById('content-overview').style.display = 'block';
}
 
// ═══════════════════════════════════════════════════════
// CLEANING
// ═══════════════════════════════════════════════════════
function renderCleaning() {
  const { headers, rows, types } = parsedData;
  const issues = [];
 
  // Missing values per column
  headers.forEach((h, i) => {
    const missing = rows.filter(r => !r[i] || r[i].trim() === '').length;
    if (missing > 0) {
      issues.push({
        icon: '🕳️',
        title: `Missing values in "${h}"`,
        desc: `${missing} out of ${rows.length} values are empty.`,
        count: missing + ' missing',
        action: 'fill',
        colIndex: i,
        colName: h,
        colType: types[h],
        fixed: false
      });
    }
  });
 
  // Duplicates
  const seen = new Set();
  let dupCount = 0;
  rows.forEach(r => {
    const key = r.join('|');
    if (seen.has(key)) dupCount++;
    else seen.add(key);
  });
  if (dupCount > 0) {
    issues.push({ icon: '👥', title: 'Duplicate rows detected', desc: `${dupCount} rows appear to be duplicates and can be removed.`, count: dupCount + ' duplicates', action: 'dedup', fixed: false });
  }
 
  // Inconsistent casing (string cols)
  headers.forEach((h, i) => {
    if (types[h] === 'string') {
      const vals = rows.map(r => r[i]).filter(Boolean);
      const mixed = vals.some(v => /[A-Z]/.test(v) && /[a-z]/.test(v));
      if (mixed && vals.length > 3) {
        issues.push({ icon: '🔡', title: `Inconsistent casing in "${h}"`, desc: `Values have mixed upper/lower case. Normalizing improves consistency.`, count: 'mixed case', action: 'normalize', colIndex: i, fixed: false });
      }
    }
  });
 
  // Numeric outliers
  headers.forEach((h, i) => {
    if (types[h] === 'numeric') {
      const vals = rows.map(r => parseFloat(r[i])).filter(v => !isNaN(v));
      if (vals.length > 3) {
        const mean = vals.reduce((a,b)=>a+b,0)/vals.length;
        const std = Math.sqrt(vals.map(v=>(v-mean)**2).reduce((a,b)=>a+b,0)/vals.length);
        const outliers = vals.filter(v => Math.abs(v-mean) > 3*std).length;
        if (outliers > 0) {
          issues.push({ icon: '📊', title: `Outliers in "${h}"`, desc: `${outliers} values are more than 3 standard deviations from the mean.`, count: outliers + ' outliers', action: 'outlier', colIndex: i, colName: h, fixed: false });
        }
      }
    }
  });
 
  if (issues.length === 0) {
    issues.push({ icon: '✅', title: 'Data looks clean!', desc: 'No obvious issues were detected. Your data is ready for analysis.', count: 'all good', action: null, fixed: true });
  }
 
  const issuesList = document.getElementById('issuesList');
  issuesList.innerHTML = issues.map((issue, idx) => `
    <div class="issue-card ${issue.fixed ? 'fixed' : ''}" id="issue-${idx}">
      <span class="issue-icon">${issue.icon}</span>
      <div class="issue-info">
        <div class="issue-title">${issue.title}</div>
        <div class="issue-desc">${issue.desc}</div>
      </div>
      <span class="issue-count ${issue.fixed ? 'ok' : ''}">${issue.count}</span>
      ${issue.action ? `<button class="btn-fix" onclick="applyFix(${idx}, ${JSON.stringify(issue).replace(/"/g,'&quot;')})">Fix</button>` : ''}
    </div>
  `).join('');
 
  document.getElementById('empty-clean').style.display = 'none';
  document.getElementById('content-clean').style.display = 'block';
}
 
function applyFix(idx, issue) {
  if (issue.action === 'fill') {
    const vals = cleanedData.rows.map(r => r[issue.colIndex]).filter(v => v && !isNaN(parseFloat(v)));
    const fill = issue.colType === 'numeric'
      ? (vals.reduce((a,b)=>a+parseFloat(b),0)/vals.length).toFixed(2)
      : 'N/A';
    cleanedData.rows.forEach(r => { if (!r[issue.colIndex] || r[issue.colIndex].trim() === '') r[issue.colIndex] = fill; });
    showToast(`✅ Filled missing values in "${issue.colName}" with ${fill}`);
  } else if (issue.action === 'dedup') {
    const seen = new Set();
    cleanedData.rows = cleanedData.rows.filter(r => {
      const key = r.join('|');
      if (seen.has(key)) return false;
      seen.add(key); return true;
    });
    showToast('✅ Removed duplicate rows');
  } else if (issue.action === 'normalize') {
    cleanedData.rows.forEach(r => {
      if (r[issue.colIndex]) r[issue.colIndex] = r[issue.colIndex].trim().toLowerCase()
        .replace(/\b\w/g, c => c.toUpperCase());
    });
    showToast(`✅ Normalized casing in column`);
  } else if (issue.action === 'outlier') {
    const vals = cleanedData.rows.map(r => parseFloat(r[issue.colIndex])).filter(v => !isNaN(v));
    const mean = vals.reduce((a,b)=>a+b,0)/vals.length;
    const std = Math.sqrt(vals.map(v=>(v-mean)**2).reduce((a,b)=>a+b,0)/vals.length);
    cleanedData.rows = cleanedData.rows.filter(r => {
      const v = parseFloat(r[issue.colIndex]);
      return isNaN(v) || Math.abs(v - mean) <= 3 * std;
    });
    showToast(`✅ Removed outliers from "${issue.colName}"`);
  }
 
  // Mark as fixed
  const card = document.getElementById(`issue-${idx}`);
  if (card) {
    card.classList.add('fixed');
    const btn = card.querySelector('.btn-fix');
    if (btn) { btn.textContent = '✓ Fixed'; btn.classList.add('done'); btn.disabled = true; }
    const count = card.querySelector('.issue-count');
    if (count) count.classList.add('ok');
  }
 
  // Show cleaned preview
  renderCleanedTable();
}
 
function renderCleanedTable() {
  const { headers, rows } = cleanedData;
  document.getElementById('cleanedTable').innerHTML = `
    <thead><tr>${headers.map(h=>`<th>${h}</th>`).join('')}</tr></thead>
    <tbody>${rows.slice(0,20).map(row=>`<tr>${row.map(v=>`<td>${v||'∅'}</td>`).join('')}</tr>`).join('')}</tbody>
  `;
  document.getElementById('cleanedTableWrapper').style.display = 'block';
}
 
// ═══════════════════════════════════════════════════════
// VISUALIZATIONS
// ═══════════════════════════════════════════════════════
function renderVisualizations() {
  // Destroy old charts
  charts.forEach(c => c.destroy());
  charts = [];
 
  const { headers, rows, types } = parsedData;
  const numericCols = headers.filter(h => types[h] === 'numeric');
  const stringCols = headers.filter(h => types[h] === 'string');
 
  const grid = document.getElementById('chartGrid');
  grid.innerHTML = '';
 
  if (numericCols.length === 0 && stringCols.length === 0) {
    document.getElementById('empty-visualize').style.display = 'flex';
    return;
  }
 
  const palette = ['#7c6aff','#ff6a6a','#6affb0','#ffca6a','#6abaff','#ff6adb'];
 
  // Chart 1: Bar chart for first numeric column
  if (numericCols.length > 0 && stringCols.length > 0) {
    const yCol = numericCols[0];
    const xCol = stringCols[0];
    const yIdx = headers.indexOf(yCol);
    const xIdx = headers.indexOf(xCol);
    const labels = rows.map(r => r[xIdx] || 'N/A').slice(0, 12);
    const data = rows.map(r => parseFloat(r[yIdx]) || 0).slice(0, 12);
 
    const card = createChartCard(`${yCol} by ${xCol}`, 'Bar Chart');
    grid.appendChild(card);
    const ctx = card.querySelector('canvas').getContext('2d');
    charts.push(new Chart(ctx, {
      type: 'bar',
      data: {
        labels,
        datasets: [{ label: yCol, data, backgroundColor: labels.map((_,i) => palette[i%palette.length] + '99'), borderColor: labels.map((_,i) => palette[i%palette.length]), borderWidth: 2, borderRadius: 6 }]
      },
      options: chartOpts(`${yCol} by ${xCol}`)
    }));
  }
 
  // Chart 2: Line chart for numeric columns
  if (numericCols.length >= 1) {
    const col = numericCols[0];
    const idx = headers.indexOf(col);
    const data = rows.map(r => parseFloat(r[idx]) || 0).slice(0, 20);
    const labels = data.map((_,i) => `Row ${i+1}`);
 
    const card = createChartCard(`${col} Trend`, 'Line Chart');
    grid.appendChild(card);
    const ctx = card.querySelector('canvas').getContext('2d');
    charts.push(new Chart(ctx, {
      type: 'line',
      data: {
        labels,
        datasets: [{ label: col, data, borderColor: '#7c6aff', backgroundColor: 'rgba(124,106,255,0.1)', borderWidth: 2.5, pointRadius: 4, pointBackgroundColor: '#7c6aff', tension: 0.4, fill: true }]
      },
      options: chartOpts(`${col} over records`)
    }));
  }
 
  // Chart 3: Doughnut for string column distribution
  if (stringCols.length > 0) {
    const col = stringCols[0];
    const idx = headers.indexOf(col);
    const freq = {};
    rows.forEach(r => { const v = r[idx] || 'N/A'; freq[v] = (freq[v]||0)+1; });
    const sorted = Object.entries(freq).sort((a,b)=>b[1]-a[1]).slice(0, 8);
    const labels = sorted.map(e=>e[0]);
    const data = sorted.map(e=>e[1]);
 
    const card = createChartCard(`${col} Distribution`, 'Doughnut Chart');
    grid.appendChild(card);
    const ctx = card.querySelector('canvas').getContext('2d');
    charts.push(new Chart(ctx, {
      type: 'doughnut',
      data: { labels, datasets: [{ data, backgroundColor: palette.slice(0,data.length).map(c=>c+'cc'), borderColor: palette.slice(0,data.length), borderWidth: 2 }] },
      options: {
        ...chartOpts(`${col} breakdown`),
        plugins: {
          legend: { display: true, position: 'bottom', labels: { color: 'rgba(240,240,255,0.6)', font: { family: 'DM Mono', size: 11 }, padding: 12 } },
          tooltip: { callbacks: { label: ctx => `${ctx.label}: ${ctx.raw} (${((ctx.raw/rows.length)*100).toFixed(1)}%)` } }
        }
      }
    }));
  }
 
  // Chart 4: Multi-numeric scatter or grouped bar
  if (numericCols.length >= 2) {
    const col1 = numericCols[0], col2 = numericCols[1];
    const idx1 = headers.indexOf(col1), idx2 = headers.indexOf(col2);
    const scatterData = rows.slice(0,50).map(r => ({
      x: parseFloat(r[idx1]) || 0,
      y: parseFloat(r[idx2]) || 0
    }));
 
    const card = createChartCard(`${col1} vs ${col2}`, 'Scatter Plot');
    grid.appendChild(card);
    const ctx = card.querySelector('canvas').getContext('2d');
    charts.push(new Chart(ctx, {
      type: 'scatter',
      data: { datasets: [{ label: 'Data Points', data: scatterData, backgroundColor: '#7c6aff99', borderColor: '#7c6aff', borderWidth: 1.5, pointRadius: 6 }] },
      options: { ...chartOpts(`${col1} vs ${col2}`), scales: {
        x: { title: { display: true, text: col1, color: 'rgba(240,240,255,0.5)', font: { family: 'DM Mono', size: 11 } }, ...scaleOpts() },
        y: { title: { display: true, text: col2, color: 'rgba(240,240,255,0.5)', font: { family: 'DM Mono', size: 11 } }, ...scaleOpts() }
      }}
    }));
  }
 
  // Chart 5: Stats overview (horizontal bar)
  if (numericCols.length > 0) {
    const statsRows = numericCols.slice(0, 5).map(col => {
      const idx = headers.indexOf(col);
      const vals = rows.map(r => parseFloat(r[idx])).filter(v => !isNaN(v));
      if (!vals.length) return null;
      return { col, avg: vals.reduce((a,b)=>a+b,0)/vals.length };
    }).filter(Boolean);
 
    if (statsRows.length > 1) {
      const card = createChartCard('Column Averages', 'Horizontal Bar');
      grid.appendChild(card);
      const ctx = card.querySelector('canvas').getContext('2d');
      charts.push(new Chart(ctx, {
        type: 'bar',
        data: {
          labels: statsRows.map(s=>s.col),
          datasets: [{ label: 'Average', data: statsRows.map(s=>s.avg.toFixed(2)), backgroundColor: palette.slice(0,statsRows.length).map(c=>c+'99'), borderColor: palette.slice(0,statsRows.length), borderWidth: 2, borderRadius: 6 }]
        },
        options: { ...chartOpts('Averages'), indexAxis: 'y' }
      }));
    }
  }
 
  document.getElementById('empty-visualize').style.display = 'none';
  document.getElementById('content-visualize').style.display = 'block';
}
 
function createChartCard(title, subtitle) {
  const card = document.createElement('div');
  card.className = 'chart-card';
  card.innerHTML = `
    <div class="chart-card-header">
      <span class="chart-card-title">${title}</span>
      <span class="chart-card-sub">${subtitle}</span>
    </div>
    <div class="chart-body">
      <canvas height="220"></canvas>
    </div>`;
  return card;
}
 
function scaleOpts() {
  return {
    grid: { color: 'rgba(255,255,255,0.05)' },
    ticks: { color: 'rgba(240,240,255,0.5)', font: { family: 'DM Mono', size: 11 } }
  };
}
 
function chartOpts(title) {
  return {
    responsive: true,
    animation: { duration: 800, easing: 'easeOutQuart' },
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: '#1a1a24', borderColor: 'rgba(124,106,255,0.3)', borderWidth: 1,
        titleFont: { family: 'Syne', size: 13 }, bodyFont: { family: 'DM Mono', size: 12 },
        titleColor: '#f0f0ff', bodyColor: 'rgba(240,240,255,0.7)', padding: 12
      }
    },
    scales: {
      x: scaleOpts(),
      y: scaleOpts()
    }
  };
}
 
// ═══════════════════════════════════════════════════════
// EXTRACTION
// ═══════════════════════════════════════════════════════
function renderExtraction() {
  const { headers, rows, types } = parsedData;
  const numericCols = headers.filter(h => types[h] === 'numeric');
  const stringCols = headers.filter(h => types[h] === 'string');
 
  const grid = document.getElementById('extractionGrid');
  grid.innerHTML = '';
 
  // Column summary
  const colCard = document.createElement('div');
  colCard.className = 'extract-card';
  colCard.innerHTML = `
    <h4>📋 Column Types</h4>
    <div class="kv-list">
      ${headers.map(h => `
        <div class="kv-row">
          <span class="kv-key">${h}</span>
          <span class="tag ${types[h]==='numeric'?'green':'orange'}">${types[h]}</span>
        </div>
      `).join('')}
    </div>`;
  grid.appendChild(colCard);
 
  // Unique values
  if (stringCols.length > 0) {
    const col = stringCols[0];
    const idx = headers.indexOf(col);
    const uniq = [...new Set(rows.map(r => r[idx]).filter(Boolean))].slice(0,12);
    const uniqCard = document.createElement('div');
    uniqCard.className = 'extract-card';
    uniqCard.innerHTML = `
      <h4>🏷️ Unique Values — "${col}"</h4>
      <div class="tag-list">
        ${uniq.map(v=>`<span class="tag">${v}</span>`).join('')}
        ${uniq.length === 12 ? '<span class="tag" style="opacity:0.5">+ more…</span>' : ''}
      </div>`;
    grid.appendChild(uniqCard);
  }
 
  // Numeric stats
  if (numericCols.length > 0) {
    const col = numericCols[0];
    const idx = headers.indexOf(col);
    const vals = rows.map(r => parseFloat(r[idx])).filter(v => !isNaN(v)).sort((a,b)=>a-b);
    if (vals.length > 0) {
      const sum = vals.reduce((a,b)=>a+b,0);
      const mean = sum/vals.length;
      const median = vals[Math.floor(vals.length/2)];
      const std = Math.sqrt(vals.map(v=>(v-mean)**2).reduce((a,b)=>a+b,0)/vals.length);
 
      const statsCard = document.createElement('div');
      statsCard.className = 'extract-card';
      statsCard.innerHTML = `
        <h4>📐 Statistics — "${col}"</h4>
        <div class="kv-list">
          <div class="kv-row"><span class="kv-key">Min</span><span class="kv-val">${vals[0].toFixed(2)}</span></div>
          <div class="kv-row"><span class="kv-key">Max</span><span class="kv-val">${vals[vals.length-1].toFixed(2)}</span></div>
          <div class="kv-row"><span class="kv-key">Mean</span><span class="kv-val">${mean.toFixed(2)}</span></div>
          <div class="kv-row"><span class="kv-key">Median</span><span class="kv-val">${median.toFixed(2)}</span></div>
          <div class="kv-row"><span class="kv-key">Std Dev</span><span class="kv-val">${std.toFixed(2)}</span></div>
          <div class="kv-row"><span class="kv-key">Sum</span><span class="kv-val">${sum.toFixed(2)}</span></div>
          <div class="kv-row"><span class="kv-key">Count</span><span class="kv-val">${vals.length}</span></div>
        </div>`;
      grid.appendChild(statsCard);
    }
  }
 
  // All numeric stats summary
  if (numericCols.length > 0) {
    const allStatsCard = document.createElement('div');
    allStatsCard.className = 'extract-card';
    allStatsCard.style.gridColumn = '1 / -1';
    const rows2 = parsedData.rows;
 
    allStatsCard.innerHTML = `
      <h4>📊 All Numeric Column Summary</h4>
      <div class="table-scroll">
        <table>
          <thead><tr><th>Column</th><th>Min</th><th>Max</th><th>Mean</th><th>Non-null</th><th>Missing</th></tr></thead>
          <tbody>
            ${numericCols.map(col => {
              const idx = headers.indexOf(col);
              const vals = rows2.map(r => parseFloat(r[idx])).filter(v => !isNaN(v));
              const missing = rows2.filter(r => !r[idx] || r[idx].trim()==='').length;
              if (!vals.length) return `<tr><td>${col}</td><td colspan="4" style="color:var(--text-dim)">no numeric data</td><td>${missing}</td></tr>`;
              const mean = vals.reduce((a,b)=>a+b,0)/vals.length;
              return `<tr>
                <td style="color:var(--accent)">${col}</td>
                <td>${Math.min(...vals).toFixed(2)}</td>
                <td>${Math.max(...vals).toFixed(2)}</td>
                <td>${mean.toFixed(2)}</td>
                <td>${vals.length}</td>
                <td>${missing > 0 ? `<span style="color:var(--accent2)">${missing}</span>` : `<span style="color:var(--accent3)">0</span>`}</td>
              </tr>`;
            }).join('')}
          </tbody>
        </table>
      </div>`;
    grid.appendChild(allStatsCard);
  }
 
  // Pattern detection
  const patterns = [];
  headers.forEach((h, i) => {
    const vals = rows.map(r => r[i]).filter(Boolean);
    const emailPat = vals.filter(v => /\S+@\S+\.\S+/.test(v)).length;
    const datePat = vals.filter(v => /\d{4}-\d{2}-\d{2}|\d{2}\/\d{2}\/\d{4}/.test(v)).length;
    const phonePat = vals.filter(v => /[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}/.test(v)).length;
    if (emailPat > 0) patterns.push({ col: h, pattern: 'Email addresses', count: emailPat });
    if (datePat > 0) patterns.push({ col: h, pattern: 'Date values', count: datePat });
    if (phonePat > 0) patterns.push({ col: h, pattern: 'Phone numbers', count: phonePat });
  });
 
  if (patterns.length > 0) {
    const patCard = document.createElement('div');
    patCard.className = 'extract-card';
    patCard.innerHTML = `
      <h4>🎯 Detected Patterns</h4>
      <div class="kv-list">
        ${patterns.map(p=>`<div class="kv-row"><span class="kv-key">${p.col}</span><span class="tag green">${p.pattern} (${p.count})</span></div>`).join('')}
      </div>`;
    grid.appendChild(patCard);
  }
 
  document.getElementById('empty-extract').style.display = 'none';
  document.getElementById('content-extract').style.display = 'block';
}
 
// ═══════════════════════════════════════════════════════
// AI INSIGHTS (calls Anthropic API)
// ═══════════════════════════════════════════════════════
async function renderAIInsights() {
  document.getElementById('empty-insights').style.display = 'none';
  document.getElementById('loading-insights').classList.add('show');
 
  const { headers, rows, types } = parsedData;
  const numericCols = headers.filter(h => types[h] === 'numeric');
  const stringCols = headers.filter(h => types[h] === 'string');
 
  // Compute basic stats for prompt
  const statsForPrompt = numericCols.map(col => {
    const idx = headers.indexOf(col);
    const vals = rows.map(r => parseFloat(r[idx])).filter(v => !isNaN(v));
    if (!vals.length) return null;
    const mean = vals.reduce((a,b)=>a+b,0)/vals.length;
    return `${col}: min=${Math.min(...vals).toFixed(1)}, max=${Math.max(...vals).toFixed(1)}, mean=${mean.toFixed(1)}`;
  }).filter(Boolean).join('; ');
 
  const missingTotal = rows.reduce((acc, row) => acc + row.filter(v=>!v||v.trim()==='').length, 0);
  const sampleRows = rows.slice(0,5).map(r => r.join(', ')).join('\n');
 
  const prompt = `You are a data analyst. Analyze this dataset and provide a concise, insightful report.
 
Dataset: ${rows.length} rows, columns: ${headers.join(', ')}
Column types: ${headers.map(h=>`${h}(${types[h]})`).join(', ')}
Missing values: ${missingTotal} total
Numeric stats: ${statsForPrompt || 'N/A'}
Sample rows:
${sampleRows}
 
Write a 3-4 paragraph data intelligence report covering:
1. What this dataset appears to represent
2. Key patterns and interesting findings in the numeric data
3. Data quality observations and recommendations
4. Actionable insights or questions worth exploring further
 
Be specific, use actual numbers from the stats, and be concise. Do not use markdown headers or bullet points — write in flowing paragraphs.`;
 
  try {
    const response = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        model: "claude-sonnet-4-20250514",
        max_tokens: 1000,
        messages: [{ role: "user", content: prompt }]
      })
    });
 
    const data = await response.json();
    const text = data.content.map(i => i.text || '').join('');
 
    document.getElementById('loading-insights').classList.remove('show');
    document.getElementById('content-insights').style.display = 'block';
 
    // Typewriter effect
    const el = document.getElementById('insightText');
    el.innerHTML = '<span class="typing-cursor"></span>';
    let i = 0;
    const interval = setInterval(() => {
      if (i < text.length) {
        el.innerHTML = text.slice(0, i+1) + '<span class="typing-cursor"></span>';
        i += 3;
      } else {
        el.innerHTML = text;
        clearInterval(interval);
      }
    }, 18);
 
  } catch (err) {
    document.getElementById('loading-insights').classList.remove('show');
    document.getElementById('content-insights').style.display = 'block';
    document.getElementById('insightText').textContent =
      `Based on your dataset (${rows.length} rows, ${headers.length} columns), here is what stands out:\n\n` +
      `The data contains ${numericCols.length} numeric column(s) (${numericCols.join(', ')}) and ${stringCols.length} categorical column(s) (${stringCols.join(', ')}). ` +
      `There are ${missingTotal} missing values across the dataset which may require attention before drawing conclusions.\n\n` +
      `For the numeric columns, the distribution and range of values should be examined for any skewness or outliers. ` +
      `Consider checking correlations between numeric variables to uncover relationships in the data.\n\n` +
      `Recommendation: Clean missing values using the Clean tab, then explore the Visualize tab to identify trends and patterns visually.`;
  }
}
 
// ═══════════════════════════════════════════════════════
// TAB SWITCHING
// ═══════════════════════════════════════════════════════
function switchTab(name, btn) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  if (btn) btn.classList.add('active');
  else document.querySelectorAll('.tab-btn').forEach(b => {
    if (b.textContent.toLowerCase().includes(name)) b.classList.add('active');
  });
  const panel = document.getElementById('panel-' + name);
  if (panel) panel.classList.add('active');
}
 
// ═══════════════════════════════════════════════════════
// DOWNLOAD
// ═══════════════════════════════════════════════════════
function downloadClean() {
  const { headers, rows } = cleanedData.rows.length ? cleanedData : parsedData;
  const csv = [headers.join(','), ...rows.map(r => r.map(v => `"${v}"`).join(','))].join('\n');
  download(csv, 'cleaned_data.csv', 'text/csv');
}
 
function downloadJSON() {
  const { headers, rows } = parsedData;
  const json = JSON.stringify(rows.map(r => Object.fromEntries(headers.map((h,i)=>[h,r[i]]))), null, 2);
  download(json, 'data.json', 'application/json');
}
 
function download(content, filename, type) {
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([content], { type }));
  a.download = filename;
  a.click();
  showToast('⬇️ Download started: ' + filename);
}
 
function clearData() {
  parsedData = { headers:[], rows:[], types:{} };
  cleanedData = { headers:[], rows:[] };
  charts.forEach(c=>c.destroy()); charts = [];
  document.getElementById('dataBadge').classList.add('hidden');
  ['overview','clean','visualize','extract','insights'].forEach(tab => {
    document.getElementById('empty-'+tab).style.display = 'flex';
    document.getElementById('content-'+tab) && (document.getElementById('content-'+tab).style.display='none');
    document.getElementById('loading-'+tab) && document.getElementById('loading-'+tab).classList.remove('show');
  });
  document.getElementById('dataInput').value = '';
  showToast('🗑️ Data cleared');
}
 
// ═══════════════════════════════════════════════════════
// TOAST
// ═══════════════════════════════════════════════════════
let toastTimer;
function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove('show'), 3000);
}
 
// Handle empty states for panels with no loading overlay
['clean','visualize','extract','insights'].forEach(tab => {
  if (!document.getElementById('empty-' + tab)) return;
  const el = document.getElementById('empty-' + tab);
  el.style.display = 'flex';
});
</script>
</body>
</html>