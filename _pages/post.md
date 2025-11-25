---
layout: single
title: "Post Editor"
permalink: /post/
excerpt: "Create and edit blog posts directly from browser"
---

<style>
.post-editor {
  max-width: 900px;
  margin: 0 auto;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}
.editor-panel {
  border: 1px solid #333;
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 1rem;
}
.panel-header {
  background: #1a1a1a;
  padding: 0.75rem 1rem;
  font-weight: 600;
  border-bottom: 1px solid #333;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.editor-textarea {
  width: 100%;
  height: 600px; /* Increased height for the editor */
  padding: 1rem;
  border: none;
  background: #111;
  color: #e1e1e1;
  font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
  font-size: 14px;
  line-height: 1.5;
  resize: vertical;
}
.preview-area {
  width: 100%;
  height: 400px; /* Set height for the preview */
  padding: 1rem;
  border: 1px solid #333;
  background: #222;
  color: #e1e1e1;
  overflow-y: auto;
  font-family: inherit;
}
.form-group {
  margin: 1rem 0;
}
.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
}
.form-input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #333;
  border-radius: 4px;
  background: #111;
  color: #e1e1e1;
  font-size: 14px;
}
.button-group {
  display: flex;
  gap: 0.5rem;
  margin: 1rem 0;
}
.btn {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 600;
  text-decoration: none;
  display: inline-block;
  text-align: center;
}
.btn-primary {
  background: #0066cc;
  color: white;
}
.btn-secondary {
  background: #333;
  color: #e1e1e1;
}
.btn-success {
  background: #28a745;
  color: white;
}
.toolbar {
  padding: 0.5rem;
  background: #1a1a1a;
  border-bottom: 1px solid #333;
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}
.toolbar-btn {
  background: #333;
  border: none;
  color: #e1e1e1;
  padding: 0.25rem 0.5rem;
  border-radius: 3px;
  cursor: pointer;
  font-size: 12px;
}
.toolbar-btn:hover {
  background: #555;
}
@media (max-width: 768px) {
  .editor-panel {
    margin-bottom: 1rem;
  }
}
</style>

<div class="post-editor">
  <h1>📝 Post Editor</h1>
  
  <div class="form-group">
    <label for="post-title">Post Title</label>
    <input type="text" id="post-title" class="form-input" placeholder="Enter post title...">
  </div>
  
  <div class="form-group">
    <label for="post-excerpt">Excerpt (Optional)</label>
    <input type="text" id="post-excerpt" class="form-input" placeholder="Brief description...">
  </div>
  
  <div class="form-group">
    <label for="post-tags">Tags (comma-separated)</label>
    <input type="text" id="post-tags" class="form-input" placeholder="development, tutorial, personal">
  </div>
  
  <div class="editor-panel">
    <div class="panel-header">
      📝 Markdown Editor
      <div class="toolbar">
        <button class="toolbar-btn" onclick="insertMarkdown('**', '**')" title="Bold">B</button>
        <button class="toolbar-btn" onclick="insertMarkdown('*', '*')" title="Italic">I</button>
        <button class="toolbar-btn" onclick="insertMarkdown('`', '`')" title="Code">&lt;/&gt;</button>
        <button class="toolbar-btn" onclick="insertMarkdown('## ', '')" title="Heading">H2</button>
        <button class="toolbar-btn" onclick="insertMarkdown('- ', '')" title="List">•</button>
        <button class="toolbar-btn" onclick="insertMarkdown('[link text](', ')')" title="Link">🔗</button>
        <button class="toolbar-btn" onclick="insertMarkdown('![alt text](', ')')" title="Image">🖼️</button>
      </div>
    </div>
    <textarea id="post-content" class="editor-textarea" placeholder="Write your post content in Markdown..."></textarea>
  </div>
  
  <div class="editor-panel">
    <div class="panel-header">👁️ Live Preview</div>
    <div id="preview-area" class="preview-area"></div>
  </div>
  
  <div class="button-group">
    <button class="btn btn-primary" onclick="generatePost()">📋 Generate Post File</button>
    <button class="btn btn-secondary" onclick="clearEditor()">🗑️ Clear</button>
    <button class="btn btn-success" onclick="openNetlifyCMS()">🚀 Open Netlify CMS</button>
  </div>
  
  <div id="output-area" style="margin-top: 2rem; display: none;">
    <h3>📄 Generated Post File</h3>
    <p>Copy this content and save as <code id="filename"></code> in your <code>_posts/</code> directory:</p>
    <textarea id="output-content" class="editor-textarea" style="height: 200px;" readonly></textarea>
    <div class="button-group">
      <button class="btn btn-primary" onclick="copyToClipboard()">📋 Copy to Clipboard</button>
      <button class="btn btn-secondary" onclick="downloadFile()">💾 Download File</button>
    </div>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script>
// Live preview
document.getElementById('post-content').addEventListener('input', updatePreview);

function updatePreview() {
  const markdown = document.getElementById('post-content').value;
  const preview = document.getElementById('preview-area');
  preview.innerHTML = marked.parse(markdown);
}

// Markdown insertion helpers
function insertMarkdown(before, after) {
  const textarea = document.getElementById('post-content');
  const start = textarea.selectionStart;
  const end = textarea.selectionEnd;
  const selectedText = textarea.value.substring(start, end);
  const replacement = before + selectedText + after;
  
  textarea.value = textarea.value.substring(0, start) + replacement + textarea.value.substring(end);
  textarea.focus();
  textarea.setSelectionRange(start + before.length, start + before.length + selectedText.length);
  updatePreview();
}

// Generate post file
function generatePost() {
  const title = document.getElementById('post-title').value.trim();
  const excerpt = document.getElementById('post-excerpt').value.trim();
  const tags = document.getElementById('post-tags').value.trim();
  const content = document.getElementById('post-content').value.trim();
  
  if (!title || !content) {
    alert('Please fill in at least the title and content fields.');
    return;
  }
  
  const date = new Date().toISOString().split('T')[0];
  const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  const filename = `${date}-${slug}.md`;
  
  let frontmatter = `---\nlayout: single\ntitle: "${title.replace(/"/g, '\\"')}"\ndate: ${new Date().toISOString()}\npermalink: /blog/${slug}/`;

  if (excerpt) {
    frontmatter += `\nexcerpt: "${excerpt.replace(/"/g, '\\"')}"`;
  }
  
  if (tags) {
    const tagArray = tags.split(',').map(tag => `"${tag.trim()}"`).join(', ');
    frontmatter += `\ntags: [${tagArray}]`;
  }
  
  frontmatter += `\ncategories: ["blog"]\n---\n\n`;

  const fullContent = frontmatter + content;
  
  document.getElementById('filename').textContent = filename;
  document.getElementById('output-content').value = fullContent;
  document.getElementById('output-area').style.display = 'block';
}

// Utility functions
function clearEditor() {
  if (confirm('Are you sure you want to clear all fields?')) {
    document.getElementById('post-title').value = '';
    document.getElementById('post-excerpt').value = '';
    document.getElementById('post-tags').value = '';
    document.getElementById('post-content').value = '';
    document.getElementById('preview-area').innerHTML = '';
    document.getElementById('output-area').style.display = 'none';
  }
}

function copyToClipboard() {
  const content = document.getElementById('output-content');
  content.select();
  document.execCommand('copy');
  alert('Post content copied to clipboard!');
}

function downloadFile() {
  const filename = document.getElementById('filename').textContent;
  const content = document.getElementById('output-content').value;
  const blob = new Blob([content], { type: 'text/markdown' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  a.click();
  URL.revokeObjectURL(url);
}

function openNetlifyCMS() {
  window.open('/admin/', '_blank');
}

// Auto-save to localStorage
function autoSave() {
  const data = {
    title: document.getElementById('post-title').value,
    excerpt: document.getElementById('post-excerpt').value,
    tags: document.getElementById('post-tags').value,
    content: document.getElementById('post-content').value
  };
  localStorage.setItem('post-editor-draft', JSON.stringify(data));
}

function loadDraft() {
  const draft = localStorage.getItem('post-editor-draft');
  if (draft) {
    const data = JSON.parse(draft);
    document.getElementById('post-title').value = data.title || '';
    document.getElementById('post-excerpt').value = data.excerpt || '';
    document.getElementById('post-tags').value = data.tags || '';
    document.getElementById('post-content').value = data.content || '';
    updatePreview();
  }
}

// Auto-save every 30 seconds
setInterval(autoSave, 30000);

// Load draft on page load
window.addEventListener('load', loadDraft);

// Auto-save on input
['post-title', 'post-excerpt', 'post-tags', 'post-content'].forEach(id => {
  document.getElementById(id).addEventListener('input', autoSave);
});
</script>