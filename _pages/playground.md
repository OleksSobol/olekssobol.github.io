---
layout: single
title: "Playground"
permalink: /lab/playground/
sitemap: false
excerpt: "Interactive developer tools. API tester, JSON formatter, Base64 encoder, subnet calculator, UUID generator."
classes: wide
---

<style>
.tool-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}
.tool-card {
  background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
  border: 1px solid #3a3a3a;
  border-radius: 8px;
  padding: 1.5rem;
  transition: all 0.2s;
}
.tool-card:hover {
  border-color: #52adc8;
  transform: translateY(-2px);
}
.tool-card h3 {
  color: #52adc8;
  margin-top: 0;
  font-size: 1.3rem;
}
.tool-section {
  background: #1a1a1a;
  border: 1px solid #3a3a3a;
  border-radius: 8px;
  padding: 2rem;
  margin: 2rem 0;
}
.input-group {
  margin: 1rem 0;
}
.input-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #b0b0b0;
  font-weight: 600;
}
.input-group input, .input-group select, .input-group textarea {
  width: 100%;
  padding: 0.8rem;
  background: #0a0a0a;
  border: 1px solid #3a3a3a;
  border-radius: 4px;
  color: #e0e0e0;
  font-family: 'Monaco', 'Courier New', monospace;
  font-size: 0.9rem;
}
.input-group textarea {
  min-height: 120px;
  resize: vertical;
}
.btn-playground {
  background: #52adc8;
  color: #fff;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  margin: 0.5rem 0.5rem 0.5rem 0;
}
.btn-playground:hover {
  background: #3d8ca3;
  transform: translateY(-2px);
}
.btn-secondary {
  background: #3a3a3a;
}
.btn-secondary:hover {
  background: #4a4a4a;
}
.output-box {
  background: #0a0a0a;
  border: 1px solid #3a3a3a;
  border-radius: 4px;
  padding: 1rem;
  margin-top: 1rem;
  min-height: 100px;
  font-family: 'Monaco', 'Courier New', monospace;
  font-size: 0.9rem;
  white-space: pre-wrap;
  word-wrap: break-word;
  color: #e0e0e0;
}
.success {
  border-left: 4px solid #4caf50;
  background: #1a2f1a;
}
.error {
  border-left: 4px solid #f44336;
  background: #2f1a1a;
}
.method-badge {
  display: inline-block;
  padding: 0.3rem 0.6rem;
  border-radius: 3px;
  font-size: 0.75rem;
  font-weight: 700;
  margin-right: 0.5rem;
}
.method-get { background: #4caf50; color: #fff; }
.method-post { background: #2196f3; color: #fff; }
.method-put { background: #ff9800; color: #fff; }
.method-delete { background: #f44336; color: #fff; }
.tab-container {
  margin: 1.5rem 0;
}
.tab-buttons {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}
.tab-button {
  background: #2d2d2d;
  border: 1px solid #3a3a3a;
  color: #e0e0e0;
  padding: 0.6rem 1.2rem;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 500;
}
.tab-button:hover {
  background: #3a3a3a;
}
.tab-button.active {
  background: #52adc8;
  border-color: #52adc8;
  color: #fff;
}
.tab-content {
  display: none;
}
.tab-content.active {
  display: block;
}
.status-indicator {
  display: inline-block;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  margin-right: 0.5rem;
}
.status-success { background: #4caf50; }
.status-error { background: #f44336; }
.status-pending { background: #ff9800; }
</style>

<p style="text-align: center; font-size: 1.1rem; color: #b0b0b0; margin: 1rem 0 2rem;">
  A collection of interactive developer tools I've built for testing and experimentation
</p>

---

<!-- ## Quick Tools Overview

<div class="tool-grid">
  <div class="tool-card">
    <h3>🌐 API Tester</h3>
    <p>Test REST APIs with GET, POST, PUT, DELETE methods. View formatted responses with headers and status codes.</p>
  </div>
  <div class="tool-card">
    <h3>✨ JSON Formatter</h3>
    <p>Format, validate, and beautify JSON data. Syntax highlighting and error detection included.</p>
  </div>
  <div class="tool-card">
    <h3>🔐 Base64 Encoder/Decoder</h3>
    <p>Encode and decode Base64 strings. Useful for API authentication and data transmission.</p>
  </div>
  <div class="tool-card">
    <h3>🧮 Subnet Calculator</h3>
    <p>Calculate network information, subnet masks, and IP ranges for network configuration.</p>
  </div>
  <div class="tool-card">
    <h3>🔑 UUID Generator</h3>
    <p>Generate v4 UUIDs for database records, API keys, and unique identifiers.</p>
  </div>
</div>

--- -->

<div class="tab-container">
  <div class="tab-buttons">
    <button class="tab-button active" onclick="switchTab('api-tester')">API Tester</button>
    <button class="tab-button" onclick="switchTab('json-formatter')">JSON Formatter</button>
    <button class="tab-button" onclick="switchTab('base64')">Base64 Tool</button>
    <button class="tab-button" onclick="switchTab('subnet-calc')">Subnet Calculator</button>
    <button class="tab-button" onclick="switchTab('uuid-gen')">UUID Generator</button>
  </div>

  <!-- API Tester -->
  <div id="api-tester" class="tab-content active">
    <div class="tool-section">
      <h2>🌐 API Tester</h2>
      <p>Test REST API endpoints with different HTTP methods and view formatted responses.</p>

      <div class="input-group">
        <label>HTTP Method</label>
        <select id="apiMethod">
          <option value="GET">GET</option>
          <option value="POST">POST</option>
          <option value="PUT">PUT</option>
          <option value="DELETE">DELETE</option>
        </select>
      </div>

      <div class="input-group">
        <label>API Endpoint URL</label>
        <input type="text" id="apiUrl" placeholder="https://jsonplaceholder.typicode.com/todos/1" value="https://jsonplaceholder.typicode.com/todos/1">
      </div>

      <div class="input-group">
        <label>Headers (JSON format, optional)</label>
        <textarea id="apiHeaders" placeholder='{"Content-Type": "application/json"}'></textarea>
      </div>

      <div class="input-group" id="apiBodyGroup" style="display: none;">
        <label>Request Body (JSON)</label>
        <textarea id="apiBody" placeholder='{"title": "Test", "completed": false}'></textarea>
      </div>

      <button class="btn-playground" onclick="testAPI()">Send Request</button>
      <button class="btn-playground btn-secondary" onclick="clearAPITester()">Clear</button>

      <div id="apiOutput" class="output-box" style="display: none;"></div>
    </div>
  </div>

  <!-- JSON Formatter -->
  <div id="json-formatter" class="tab-content">
    <div class="tool-section">
      <h2>✨ JSON Formatter & Validator</h2>
      <p>Format, validate, and beautify JSON data with syntax highlighting.</p>

      <div class="input-group">
        <label>JSON Input</label>
        <textarea id="jsonInput" placeholder='{"name":"John","age":30,"city":"New York"}'></textarea>
      </div>

      <button class="btn-playground" onclick="formatJSON()">Format & Validate</button>
      <button class="btn-playground" onclick="minifyJSON()">Minify</button>
      <button class="btn-playground btn-secondary" onclick="clearJSON()">Clear</button>

      <div id="jsonOutput" class="output-box" style="display: none;"></div>
    </div>
  </div>

  <!-- Base64 Tool -->
  <div id="base64" class="tab-content">
    <div class="tool-section">
      <h2>🔐 Base64 Encoder/Decoder</h2>
      <p>Encode and decode Base64 strings for API authentication and data transmission.</p>

      <div class="input-group">
        <label>Input Text</label>
        <textarea id="base64Input" placeholder="Enter text to encode or Base64 string to decode"></textarea>
      </div>

      <button class="btn-playground" onclick="encodeBase64()">Encode to Base64</button>
      <button class="btn-playground" onclick="decodeBase64()">Decode from Base64</button>
      <button class="btn-playground btn-secondary" onclick="clearBase64()">Clear</button>

      <div id="base64Output" class="output-box" style="display: none;"></div>
    </div>
  </div>

  <!-- Subnet Calculator -->
  <div id="subnet-calc" class="tab-content">
    <div class="tool-section">
      <h2>🧮 Subnet Calculator</h2>
      <p>Calculate network information, subnet masks, and IP ranges.</p>

      <div class="input-group">
        <label>IP Address</label>
        <input type="text" id="subnetIP" placeholder="192.168.1.0" value="192.168.1.0">
      </div>

      <div class="input-group">
        <label>Subnet Mask (CIDR)</label>
        <input type="number" id="subnetMask" placeholder="24" value="24" min="1" max="32">
      </div>

      <button class="btn-playground" onclick="calculateSubnet()">Calculate</button>
      <button class="btn-playground btn-secondary" onclick="clearSubnet()">Clear</button>

      <div id="subnetOutput" class="output-box" style="display: none;"></div>
    </div>
  </div>

  <!-- UUID Generator -->
  <div id="uuid-gen" class="tab-content">
    <div class="tool-section">
      <h2>🔑 UUID Generator</h2>
      <p>Generate v4 UUIDs for database records, API keys, and unique identifiers.</p>

      <div class="input-group">
        <label>Number of UUIDs</label>
        <input type="number" id="uuidCount" value="1" min="1" max="100">
      </div>

      <button class="btn-playground" onclick="generateUUIDs()">Generate UUIDs</button>
      <button class="btn-playground btn-secondary" onclick="clearUUID()">Clear</button>

      <div id="uuidOutput" class="output-box" style="display: none;"></div>
    </div>
  </div>
</div>

<script>
// Tab switching
function switchTab(tabId) {
  document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
  document.querySelectorAll('.tab-button').forEach(btn => btn.classList.remove('active'));
  document.getElementById(tabId).classList.add('active');
  event.target.classList.add('active');
}

// Show/hide body field based on method
document.getElementById('apiMethod').addEventListener('change', function() {
  const bodyGroup = document.getElementById('apiBodyGroup');
  bodyGroup.style.display = (this.value === 'POST' || this.value === 'PUT') ? 'block' : 'none';
});

// API Tester
async function testAPI() {
  const method = document.getElementById('apiMethod').value;
  const url = document.getElementById('apiUrl').value;
  const headersText = document.getElementById('apiHeaders').value;
  const body = document.getElementById('apiBody').value;
  const output = document.getElementById('apiOutput');

  if (!url) {
    output.style.display = 'block';
    output.className = 'output-box error';
    output.textContent = 'Error: Please enter a URL';
    return;
  }

  output.style.display = 'block';
  output.className = 'output-box';
  output.textContent = 'Sending request...';

  try {
    const options = { method };

    if (headersText) {
      try {
        options.headers = JSON.parse(headersText);
      } catch (e) {
        output.className = 'output-box error';
        output.textContent = 'Error: Invalid headers JSON format';
        return;
      }
    }

    if ((method === 'POST' || method === 'PUT') && body) {
      options.body = body;
    }

    const response = await fetch(url, options);
    const data = await response.text();

    let formattedData;
    try {
      formattedData = JSON.stringify(JSON.parse(data), null, 2);
    } catch {
      formattedData = data;
    }

    const result = `Status: ${response.status} ${response.statusText}\n\nResponse:\n${formattedData}`;

    output.className = response.ok ? 'output-box success' : 'output-box error';
    output.textContent = result;
  } catch (error) {
    output.className = 'output-box error';
    output.textContent = `Error: ${error.message}`;
  }
}

function clearAPITester() {
  document.getElementById('apiUrl').value = '';
  document.getElementById('apiHeaders').value = '';
  document.getElementById('apiBody').value = '';
  document.getElementById('apiOutput').style.display = 'none';
}

// JSON Formatter
function formatJSON() {
  const input = document.getElementById('jsonInput').value;
  const output = document.getElementById('jsonOutput');
  output.style.display = 'block';

  try {
    const parsed = JSON.parse(input);
    const formatted = JSON.stringify(parsed, null, 2);
    output.className = 'output-box success';
    output.textContent = formatted;
  } catch (error) {
    output.className = 'output-box error';
    output.textContent = `Invalid JSON: ${error.message}`;
  }
}

function minifyJSON() {
  const input = document.getElementById('jsonInput').value;
  const output = document.getElementById('jsonOutput');
  output.style.display = 'block';

  try {
    const parsed = JSON.parse(input);
    const minified = JSON.stringify(parsed);
    output.className = 'output-box success';
    output.textContent = minified;
  } catch (error) {
    output.className = 'output-box error';
    output.textContent = `Invalid JSON: ${error.message}`;
  }
}

function clearJSON() {
  document.getElementById('jsonInput').value = '';
  document.getElementById('jsonOutput').style.display = 'none';
}

// Base64 Tool
function encodeBase64() {
  const input = document.getElementById('base64Input').value;
  const output = document.getElementById('base64Output');
  output.style.display = 'block';

  if (!input) {
    output.className = 'output-box error';
    output.textContent = 'Error: Please enter text to encode';
    return;
  }

  try {
    const encoded = btoa(input);
    output.className = 'output-box success';
    output.textContent = encoded;
  } catch (error) {
    output.className = 'output-box error';
    output.textContent = `Error: ${error.message}`;
  }
}

function decodeBase64() {
  const input = document.getElementById('base64Input').value;
  const output = document.getElementById('base64Output');
  output.style.display = 'block';

  if (!input) {
    output.className = 'output-box error';
    output.textContent = 'Error: Please enter Base64 string to decode';
    return;
  }

  try {
    const decoded = atob(input);
    output.className = 'output-box success';
    output.textContent = decoded;
  } catch (error) {
    output.className = 'output-box error';
    output.textContent = `Error: Invalid Base64 string`;
  }
}

function clearBase64() {
  document.getElementById('base64Input').value = '';
  document.getElementById('base64Output').style.display = 'none';
}


// Subnet Calculator
function calculateSubnet() {
  const ip = document.getElementById('subnetIP').value;
  const cidr = parseInt(document.getElementById('subnetMask').value);
  const output = document.getElementById('subnetOutput');
  output.style.display = 'block';

  if (!ip || !cidr) {
    output.className = 'output-box error';
    output.textContent = 'Error: Please enter IP address and CIDR';
    return;
  }

  try {
    const ipParts = ip.split('.').map(Number);
    if (ipParts.length !== 4 || ipParts.some(p => p < 0 || p > 255)) {
      throw new Error('Invalid IP address');
    }

    const mask = -1 << (32 - cidr);
    const maskParts = [
      (mask >>> 24) & 255,
      (mask >>> 16) & 255,
      (mask >>> 8) & 255,
      mask & 255
    ];

    const networkParts = ipParts.map((p, i) => p & maskParts[i]);
    const broadcastParts = networkParts.map((p, i) => p | (~maskParts[i] & 255));

    const totalHosts = Math.pow(2, 32 - cidr);
    const usableHosts = totalHosts - 2;

    const firstUsable = [...networkParts];
    firstUsable[3] += 1;
    const lastUsable = [...broadcastParts];
    lastUsable[3] -= 1;

    const result = `Network Address: ${networkParts.join('.')}
Subnet Mask: ${maskParts.join('.')}
CIDR Notation: /${cidr}
Broadcast Address: ${broadcastParts.join('.')}
First Usable IP: ${firstUsable.join('.')}
Last Usable IP: ${lastUsable.join('.')}
Total Hosts: ${totalHosts}
Usable Hosts: ${usableHosts}`;

    output.className = 'output-box success';
    output.textContent = result;
  } catch (error) {
    output.className = 'output-box error';
    output.textContent = `Error: ${error.message}`;
  }
}

function clearSubnet() {
  document.getElementById('subnetIP').value = '';
  document.getElementById('subnetMask').value = '';
  document.getElementById('subnetOutput').style.display = 'none';
}

// UUID Generator
function generateUUIDs() {
  const count = parseInt(document.getElementById('uuidCount').value);
  const output = document.getElementById('uuidOutput');
  output.style.display = 'block';

  if (!count || count < 1 || count > 100) {
    output.className = 'output-box error';
    output.textContent = 'Error: Please enter a number between 1 and 100';
    return;
  }

  const uuids = [];
  for (let i = 0; i < count; i++) {
    uuids.push(generateUUID());
  }

  output.className = 'output-box success';
  output.textContent = uuids.join('\n');
}

function generateUUID() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    const r = Math.random() * 16 | 0;
    const v = c === 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
}

function clearUUID() {
  document.getElementById('uuidCount').value = '1';
  document.getElementById('uuidOutput').style.display = 'none';
}
</script>

---

## About This Playground

This collection of tools demonstrates practical JavaScript development and API interaction patterns. All tools run client-side in your browser — no data is sent to external servers (except for the API Tester when you specify an endpoint).

**Technologies Used:**
- Vanilla JavaScript (ES6+)
- Fetch API for HTTP requests
- Client-side data processing
- Responsive CSS Grid layout

**Planned Additions:**
- JWT Decoder & Validator
- Hash Generator (MD5, SHA-256)
- Regex Tester
- Network Port Scanner (client-side)
- Color Code Converter

---

[Back to Home](/) | [View Projects](/projects/) | [Contact Me](/contact/)
