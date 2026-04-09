import sys

file_path = '/home/rrfmargaret/Documents/Projects/Gate Monitoring System/post1-exit.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Clear Button to HTML
header_old = '<span class="log-count" id="log-count">0 exits</span>'
header_new = '<div style="display:flex; align-items:center; gap:12px;"><span class="log-count" id="log-count">0 exits</span><button onclick="clearExitLogDisplay()" style="background:none; border:none; color:var(--red); font-size:10px; font-weight:700; text-transform:uppercase; cursor:pointer; display:flex; align-items:center; gap:4px;"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 6L6 18M6 6l12 12"/></svg> CLEAR</button></div>'
content = content.replace(header_old, header_new)

# 2. Add JS Function
js_clear = """
function clearExitLogDisplay() {
  if (confirm('Clear only the UI log display? This will not delete any data from Google Sheets or the database.')) {
    const tbody = document.getElementById('log-body');
    const count = document.getElementById('log-count');
    if (tbody) tbody.innerHTML = '<tr><td colspan="9" style="text-align:center;color:var(--muted);padding:20px;font-size:13px">Log cleared for this session</td></tr>';
    if (count) count.textContent = '0 exits';
    showToast('UI log cleared');
  }
}
"""
content = content.replace('function renderExitLog() {', js_clear + '\nfunction renderExitLog() {')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Added clear button logic")
