import sys

file_path = '/home/rrfmargaret/Documents/Projects/Gate Monitoring System/post1-exit.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. ADD CSS FOR NEW ELEMENTS
css_addition = """
  /* Toggle Mode */
  .mode-toggle {
    display: flex;
    justify-content: center;
    gap: 8px;
    margin-bottom: 24px;
  }
  .toggle-btn {
    background: var(--surface);
    border: 1px solid var(--border);
    color: var(--muted);
    font-family: inherit;
    font-weight: 700;
    font-size: 11px;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 10px 24px;
    border-radius: 6px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: all 0.2s;
  }
  .toggle-btn.active {
    background: rgba(29, 185, 106, 0.1);
    border-color: var(--accent);
    color: var(--accent);
  }
  
  /* New Search Section (Auto) */
  .search-section-new {
    background: var(--surface);
    border: 1px solid var(--border);
    border-top: 3px solid var(--accent);
    border-radius: var(--radius);
    padding: 24px;
    margin-bottom: 24px;
  }
  .search-input-container {
    display: flex;
    align-items: stretch;
    border: 1px solid #d0d4e0;
    border-radius: 6px;
    padding: 6px;
    background: var(--input-bg);
  }
  body.light .search-input-container { border-color: var(--accent); }
  
  .plate-input-new {
    flex: 1;
    background: transparent;
    border: none;
    color: var(--text);
    font-family: 'Share Tech Mono', monospace;
    font-size: 32px;
    letter-spacing: 6px;
    text-align: center;
    text-transform: uppercase;
    outline: none;
    min-width: 0;
  }
  body.light .plate-input-new { color: var(--accent); }
  .plate-input-new::placeholder { color: var(--muted); letter-spacing: 4px; opacity: 0.5; font-size: 24px; }
  .btn-scan-small {
    background: var(--surface2);
    border: none;
    color: var(--text);
    padding: 0 16px;
    border-radius: 4px;
    cursor: pointer;
    margin-right: 6px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .btn-search-new {
    background: var(--accent);
    color: #fff;
    border: none;
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 800;
    font-size: 15px;
    letter-spacing: 1px;
    padding: 0 28px;
    border-radius: 4px;
    cursor: pointer;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  /* Manual Bulk New */
  .bulk-section-new {
    background: var(--surface);
    border: 1px solid var(--border);
    border-top: 3px solid #3b82f6; /* Blue indicator for manual */
    border-radius: var(--radius);
    padding: 24px;
    display: none;
  }
  .bulk-section-new.show { display: block; animation: slideIn 0.2s ease-out; }
  
  .bulk-header-new {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border);
  }
  .bulk-title-new {
    font-size: 11px;
    font-weight: 700;
    color: #3b82f6;
    letter-spacing: 1px;
    text-transform: uppercase;
  }
  .btn-fill-now {
    background: var(--surface2);
    border: 1px solid var(--border);
    color: var(--text);
    font-size: 10px;
    font-weight: 700;
    padding: 6px 12px;
    border-radius: 4px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .btn-fill-now:hover { background: #3b82f6; color: #fff; border-color: #3b82f6; }
  
  .bulk-row-new {
    display: flex;
    gap: 12px;
    align-items: center;
    margin-bottom: 12px;
  }
  .bulk-row-index {
    color: #3b82f6;
    font-family: 'Share Tech Mono', monospace;
    font-size: 14px;
    width: 20px;
    text-align: right;
  }
  .bulk-input-new {
    flex: 1;
    background: var(--input-bg);
    border: 1px solid var(--border);
    color: var(--text);
    padding: 12px 16px;
    border-radius: 4px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 16px;
    letter-spacing: 2px;
    text-transform: uppercase;
    outline: none;
  }
  .bulk-input-new:focus { border-color: #3b82f6; }
  .bulk-time-new {
    width: 140px;
    background: var(--input-bg);
    border: 1px solid var(--border);
    color: var(--text);
    padding: 12px;
    border-radius: 4px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 16px;
    text-align: center;
    outline: none;
  }
  .bulk-time-new:focus { border-color: #3b82f6; }
  
  .btn-dash {
    background: var(--surface2);
    border: 1px solid var(--border);
    color: var(--text);
    width: 44px;
    height: 44px;
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
  }
  .btn-delete-row {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--muted);
    width: 44px;
    height: 44px;
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
  }
  .btn-delete-row:hover { background: rgba(229,62,62,0.1); color: var(--red); border-color: var(--red); }
  
  .btn-add-row-new {
    width: 100%;
    background: transparent;
    border: 1.5px dashed var(--border);
    color: #3b82f6;
    padding: 14px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    cursor: pointer;
    margin-top: 8px;
    margin-bottom: 24px;
    text-transform: uppercase;
  }
  .btn-add-row-new:hover { background: rgba(59,130,246,0.05); border-color: #3b82f6; }
  
  .bulk-summary {
    display: flex;
    gap: 16px;
    font-size: 11px;
    color: var(--muted);
    margin-bottom: 16px;
    font-weight: 600;
  }
  .bulk-summary span { color: var(--text); font-weight: 700; }
  
  .btn-submit-bulk-new {
    width: 100%;
    background: #3b82f6;
    color: #fff;
    border: none;
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 900;
    font-size: 16px;
    letter-spacing: 1px;
    padding: 18px;
    border-radius: 6px;
    cursor: pointer;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    transition: opacity 0.2s;
  }
  .btn-submit-bulk-new:hover { opacity: 0.9; }
"""

content = content.replace("  /* Search section */", css_addition + "\n  /* Search section */")

old_html_start = "  <!-- Search by plate -->"
old_html_end = "  <!-- Not found -->"
html_block = content[content.find(old_html_start):content.find(old_html_end)]

new_html = """  <!-- Mode Toggle -->
  <div class="mode-toggle">
    <button class="toggle-btn active" id="btn-auto-nav" onclick="setMode('auto')">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
      AUTO
    </button>
    <button class="toggle-btn" id="btn-bulk-nav" onclick="setMode('bulk')">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
      MANUAL BULK
    </button>
  </div>

  <!-- Search by plate (Auto Mode) -->
  <div class="search-section-new" id="auto-section">
    <div class="section-label" style="text-align: center; margin-bottom: 12px; color: var(--accent);">SEARCH VEHICLE BY LICENSE PLATE</div>
    <div class="search-input-container">
      <input type="text" class="plate-input-new" id="search-plate" placeholder="B 1234 XX"
        maxlength="12" autocomplete="off" spellcheck="false"
        oninput="this.value=this.value.toUpperCase().replace(/\\s+/g, ''); clearResult();"
        onkeydown="if(event.key==='Enter') searchVehicle()">
      <button class="btn-scan-small">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2"/><rect x="7" y="7" width="10" height="10" rx="2"/>
        </svg>
        <span style="font-size:9px; display:block; font-weight:700; margin-top:2px; color:var(--muted)">SCAN</span>
      </button>
      <button class="btn-search-new" onclick="searchVehicle()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
        SEARCH
      </button>
    </div>
  </div>

  <!-- Bulk Update Section (Manual Mode) -->
  <div class="bulk-section-new" id="bulk-section">
    <div class="bulk-header-new">
       <span class="bulk-title-new">DAFTAR KENDARAAN KELUAR - TIAP BARIS BISA BEDA JAM</span>
       <button class="btn-fill-now" onclick="fillAllTimesNow()">
         <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
         ISI SEMUA JAM SEKARANG
       </button>
    </div>
    
    <div id="bulk-rows">
    </div>

    <button class="btn-add-row-new" onclick="addBulkRow()">+ TAMBAH KENDARAAN</button>

    <div class="bulk-summary">
      <div>Total baris: <span id="bulk-total">0</span></div>
      <div>|</div>
      <div>Siap diproses: <span id="bulk-ready" style="color:var(--accent);">0</span></div>
      <div>|</div>
      <div>Tidak ditemukan: <span id="bulk-error" style="color:var(--red);">0</span></div>
    </div>

    <button class="btn-submit-bulk-new" onclick="submitBulkExit()">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 4v16M5 13l7 7 7-7"/></svg>
      LOG EXIT SEMUA
    </button>
  </div>

"""
content = content.replace(html_block, new_html)

js_additions = """
// ---- NEW UI LOGIC ----
function setMode(mode) {
  document.getElementById('btn-auto-nav').classList.toggle('active', mode === 'auto');
  document.getElementById('btn-bulk-nav').classList.toggle('active', mode === 'bulk');
  
  if(mode === 'auto') {
    document.getElementById('auto-section').style.display = 'block';
    document.getElementById('bulk-section').classList.remove('show');
    document.getElementById('search-plate').focus();
    setTimeout(() => { document.getElementById('search-plate').focus(); }, 50);
  } else {
    document.getElementById('auto-section').style.display = 'none';
    document.getElementById('bulk-section').classList.add('show');
    if (document.querySelectorAll('.bulk-row-new').length === 0) {
      addBulkRow();
    }
  }
}

let bulkRowCount = 0;
function addBulkRow() {
  bulkRowCount++;
  const div = document.createElement('div');
  div.className = 'bulk-row-new';
  div.id = 'bulk-row-' + bulkRowCount;
  div.innerHTML = `
    <div class="bulk-row-index">${bulkRowCount}</div>
    <input type="text" class="bulk-input-new plate-val" placeholder="B 1234 XX" oninput="this.value=this.value.toUpperCase().replace(/\\\\s+/g, ''); countReady();">
    <input type="time" class="bulk-time-new time-val" onchange="countReady()">
    <button class="btn-dash"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/></svg></button>
    <button class="btn-delete-row" onclick="removeBulkRow('${div.id}')"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg></button>
  `;
  document.getElementById('bulk-rows').appendChild(div);
  updateBulkCount();
}

function removeBulkRow(id) {
  document.getElementById(id).remove();
  let counter = 1;
  document.querySelectorAll('.bulk-row-index').forEach(el => { el.textContent = counter++; });
  bulkRowCount = counter - 1;
  updateBulkCount();
  countReady();
}

function updateBulkCount() {
  const rows = document.querySelectorAll('.bulk-row-new').length;
  document.getElementById('bulk-total').textContent = rows;
}

function countReady() {
  let ready = 0;
  document.querySelectorAll('.bulk-row-new').forEach(row => {
    let p = row.querySelector('.plate-val').value.trim();
    let t = row.querySelector('.time-val').value;
    if (p && t) ready++;
  });
  document.getElementById('bulk-ready').textContent = ready;
}

function fillAllTimesNow() {
  const now = new Date();
  const h = String(now.getHours()).padStart(2, '0');
  const m = String(now.getMinutes()).padStart(2, '0');
  const timeStr = `${h}:${m}`;
  document.querySelectorAll('.time-val').forEach(input => {
    input.value = timeStr;
  });
  countReady();
}

setTimeout(() => {
  setMode('auto');
}, 50);

// function toggleBulkMode (overwritten)
"""
content = content.replace("function toggleBulkMode() {", js_additions + "\nfunction toggleBulkMode_DISABLED() {")

# Patch submitBulkExit logic
content = content.replace("document.querySelectorAll('.bulk-row')", "document.querySelectorAll('.bulk-row-new')")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated HTML logic successfully")
