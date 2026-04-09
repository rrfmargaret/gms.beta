import sys

file_path = '/home/rrfmargaret/Documents/Projects/Gate Monitoring System/post1-exit.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update duration calculation
calc_duration_old = """function calcDuration(fullTimeInStr) {
  const inTime = parseFullTimestamp(fullTimeInStr);
  if (!inTime) return '—';
  const now = new Date();
  const diffMs = now - inTime;
  const h = Math.floor(diffMs / 3600000);
  const m = Math.floor((diffMs % 3600000) / 60000);
  const s = Math.floor((diffMs % 60000) / 1000);
  return `${String(h).padStart(2,'0')}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
}"""
calc_duration_new = """function calcDuration(fullTimeInStr) {
  const inTime = parseFullTimestamp(fullTimeInStr);
  if (!inTime) return '—';
  const now = new Date();
  const diffMs = Math.max(0, now - inTime);
  return (diffMs / 3600000).toFixed(1) + ' Jam';
}"""
content = content.replace(calc_duration_old, calc_duration_new)

# 2. Update Live Duration Clock Ticking
tick_old = """    const diffMs = Date.now() - inTime.getTime();
    const h = Math.floor(diffMs / 3600000);
    const m = Math.floor((diffMs % 3600000) / 60000);
    const s = Math.floor((diffMs % 60000) / 1000);
    document.getElementById('duration-value').textContent =
      `${String(h).padStart(2,'0')}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`"""

tick_new = """    const diffMs = Math.max(0, Date.now() - inTime.getTime());
    document.getElementById('duration-value').textContent = (diffMs / 3600000).toFixed(1) + ' Jam'"""
content = content.replace(tick_old, tick_new)


# 3. Update Bulk Row HTML to 24h Text Inputs
bulk_old_html = """<input type="time" class="bulk-time-new time-val" onchange="countReady()">"""
bulk_new_html = """<input type="text" class="bulk-time-new time-val" placeholder="HH:MM" maxlength="5" oninput="formatTimeInput(this); countReady();">"""
content = content.replace(bulk_old_html, bulk_new_html)

# Add formatTimeInput JS logic
format_time_js = """function formatTimeInput(input) {
  let v = input.value.replace(/\\D/g, '');
  if (v.length > 4) v = v.slice(0,4);
  if (v.length >= 3) {
    input.value = v.slice(0,2) + ':' + v.slice(2,4);
  } else {
    input.value = v;
  }
}
"""
content = content.replace("function setMode(mode) {", format_time_js + "\nfunction setMode(mode) {")

# 4. Update submitBulkExit to fix cross-date and duration
submit_bulk_old = """      if (outTime < inTime) {
        showToastError(`Plat ${plateInput} - Waktu keluar lebih awal dari waktu masuk.`);
        return; 
      }

      const diffMs = outTime - inTime;
      const hMs = Math.floor(diffMs / 3600000);
      const mMs = Math.floor((diffMs % 3600000) / 60000);
      const sMs = Math.floor((diffMs % 60000) / 1000);
      const customDuration = `${String(hMs).padStart(2,'0')}:${String(mMs).padStart(2,'0')}:${String(sMs).padStart(2,'0')}`;"""

submit_bulk_new = """      // Auto-forward outTime by 1 day if apparently earlier (cross-midnight fix)
      if (outTime < inTime) {
        outTime.setDate(outTime.getDate() + 1);
      }
      
      // Secondary safety check
      if (outTime < inTime) {
        showToastError(`Plat ${plateInput} - Waktu keluar (${outTime.toISOString()}) lebih awal dari masuk (${inTime.toISOString()})`);
        return; 
      }

      const diffMs = Math.max(0, outTime - inTime);
      const customDuration = (diffMs / 3600000).toFixed(1) + ' Jam';"""
content = content.replace(submit_bulk_old, submit_bulk_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Dates successfully")
