---
layout: single
title: "Projects"
permalink: /projects/
excerpt: "Backend automation systems, APIs, and applications I've built"
---

<style>
.project-card {
  background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
  border: 1px solid #3a3a3a;
  border-radius: 8px;
  padding: 2rem;
  margin: 2rem 0;
  transition: all 0.3s;
}
.project-card:hover {
  border-color: #52adc8;
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0,0,0,0.3);
}
.project-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}
.project-icon {
  font-size: 2.5rem;
}
.project-title-section h3 {
  margin: 0;
  color: #52adc8;
  font-size: 1.6rem;
}
.impact-badge {
  display: inline-block;
  background: linear-gradient(135deg, #2d5016 0%, #3d6820 100%);
  border: 1px solid #4a7a28;
  color: #a8ff78;
  padding: 0.4rem 0.8rem;
  border-radius: 4px;
  font-size: 0.85rem;
  font-weight: 700;
  margin-top: 0.5rem;
  letter-spacing: 0.5px;
}
.tech-stack {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 1rem 0;
}
.tech-tag {
  background: #2d2d2d;
  border: 1px solid #52adc8;
  color: #52adc8;
  padding: 0.3rem 0.7rem;
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: 500;
}
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
  padding: 1rem;
  background: #0a0a0a;
  border-radius: 6px;
}
.stat-item {
  text-align: center;
}
.stat-number {
  font-size: 1.8rem;
  font-weight: 700;
  color: #52adc8;
}
.stat-label {
  font-size: 0.75rem;
  color: #b0b0b0;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 0.3rem;
}
.feature-list {
  margin: 1rem 0;
}
.feature-list li {
  margin: 0.5rem 0;
  padding-left: 1.5rem;
  position: relative;
}
.feature-list li:before {
  content: "▸";
  position: absolute;
  left: 0;
  color: #52adc8;
  font-weight: bold;
}
.project-links {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
  flex-wrap: wrap;
}
.project-btn {
  display: inline-block;
  padding: 0.6rem 1.2rem;
  background: #52adc8;
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
  font-weight: 600;
  transition: all 0.2s;
}
.project-btn:hover {
  background: #3d8ca3;
  transform: translateY(-2px);
  color: #fff;
}
.project-btn-secondary {
  background: #3a3a3a;
  border: 1px solid #52adc8;
  color: #52adc8;
}
.project-btn-secondary:hover {
  background: #2d2d2d;
  color: #52adc8;
}
.section-header {
  text-align: center;
  margin: 3rem 0 2rem;
}
.section-subtitle {
  color: #b0b0b0;
  font-size: 1.1rem;
  margin-top: 0.5rem;
}
.status-badge {
  display: inline-block;
  background: #2d2d2d;
  border: 1px solid #ff9800;
  color: #ff9800;
  padding: 0.3rem 0.6rem;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 600;
  margin-left: 0.5rem;
}
</style>

<div class="section-header">
  <p class="section-subtitle">Building practical backend solutions that automate workflows and scale efficiently</p>
</div>

---

## Production Systems

<div class="project-card" id="utopia-account-creation-uac">
  <div class="project-header">
    <div class="project-icon">👥</div>
    <div class="project-title-section">
      <h3>Utopia Account Creation (UAC)</h3>
      <div class="impact-badge">⚡ 95% FASTER ONBOARDING</div>
    </div>
  </div>

  <p>Production-grade automation system that handles seamless customer data integration between Utopia and PowerCode platforms. Serves <strong>4000+ clients</strong> with 99.9% reliability.</p>

  <div class="stats-grid">
    <div class="stat-item">
      <div class="stat-number">20min → 1min</div>
      <div class="stat-label">Onboarding Time</div>
    </div>
    <div class="stat-item">
      <div class="stat-number">90%</div>
      <div class="stat-label">Fewer Errors</div>
    </div>
    <div class="stat-item">
      <div class="stat-number">4000+</div>
      <div class="stat-label">Clients Served</div>
    </div>
    <div class="stat-item">
      <div class="stat-number">99.9%</div>
      <div class="stat-label">Reliability</div>
    </div>
  </div>

  <div class="tech-stack">
    <span class="tech-tag">Python</span>
    <span class="tech-tag">Flask</span>
    <span class="tech-tag">REST APIs</span>
    <span class="tech-tag">OAuth2</span>
    <span class="tech-tag">MySQL</span>
    <span class="tech-tag">Error Handling</span>
  </div>

  <strong>Key Features:</strong>
  <ul class="feature-list">
    <li>Automated customer provisioning and account creation</li>
    <li>Real-time API synchronization between multiple systems</li>
    <li>Comprehensive error handling and logging for production reliability</li>
    <li>Reduced manual data entry errors by 90%</li>
  </ul>

  <strong>Technical Highlights:</strong>
  <ul class="feature-list">
    <li>RESTful API design with Flask framework</li>
    <li>Database schema design and optimization</li>
    <li>OAuth2 authentication implementation</li>
    <li>Retry logic and graceful failure handling</li>
  </ul>

  <div class="project-links">
    <a href="https://github.com/OleksSobol/Utopia-Account-Creation---UAC" class="project-btn">View on GitHub</a>
  </div>
</div>

<div class="project-card" id="dhcp-lease-runner-dlr">
  <div class="project-header">
    <div class="project-icon">🔧</div>
    <div class="project-title-section">
      <h3>DHCP Lease Runner (DLR)</h3>
      <div class="impact-badge">⏱️ 15+ HOURS SAVED WEEKLY</div>
    </div>
  </div>

  <p>Automated equipment management system for ISP operations. Manages DHCP leases, equipment provisioning, and synchronization across network management platforms.</p>

  <div class="stats-grid">
    <div class="stat-item">
      <div class="stat-number">15+hrs</div>
      <div class="stat-label">Time Saved Weekly</div>
    </div>
    <div class="stat-item">
      <div class="stat-number">100+</div>
      <div class="stat-label">Concurrent Devices</div>
    </div>
    <div class="stat-item">
      <div class="stat-number">80%</div>
      <div class="stat-label">Faster Deployment</div>
    </div>
  </div>

  <div class="tech-stack">
    <span class="tech-tag">Python</span>
    <span class="tech-tag">Mikrotik API</span>
    <span class="tech-tag">Powercode API</span>
    <span class="tech-tag">Cron</span>
    <span class="tech-tag">Linux</span>
    <span class="tech-tag">Multi-threading</span>
  </div>

  <strong>Key Features:</strong>
  <ul class="feature-list">
    <li>Automated DHCP lease monitoring and management</li>
    <li>Equipment lifecycle automation (provisioning, updates, decommissioning)</li>
    <li>Integration with Mikrotik routers and Powercode billing system</li>
    <li>Scheduled automation with Cron jobs</li>
  </ul>

  <strong>Technical Highlights:</strong>
  <ul class="feature-list">
    <li>Multi-threaded processing for handling 100+ devices concurrently</li>
    <li>Custom API wrapper for Mikrotik RouterOS</li>
    <li>Database design for equipment tracking and state management</li>
    <li>Logging and alerting system for anomaly detection</li>
  </ul>

  <div class="project-links">
    <a href="https://github.com/OleksSobol/DHCP-LEASE-RUNNER---DLR" class="project-btn">View on GitHub</a>
  </div>
</div>

---

## Mobile & Web Applications

<div class="project-card" id="expense-tracker">
  <div class="project-header">
    <div class="project-icon">📱</div>
    <div class="project-title-section">
      <h3>Expense Tracker</h3>
      <span class="status-badge">In Development</span>
    </div>
  </div>

  <p>Cross-platform mobile application for personal finance management. Features intuitive expense tracking, category-based organization, and visual spending analytics.</p>

  <div class="tech-stack">
    <span class="tech-tag">Flutter</span>
    <span class="tech-tag">Dart</span>
    <span class="tech-tag">Mobile Development</span>
    <span class="tech-tag">iOS</span>
    <span class="tech-tag">Android</span>
  </div>

  <strong>Key Features:</strong>
  <ul class="feature-list">
    <li>Clean, responsive UI for iOS and Android platforms</li>
    <li>Local data persistence for offline functionality</li>
    <li>Expense categorization and smart filtering</li>
    <li>Visual spending reports and trend analysis</li>
  </ul>

  <div class="project-links">
    <a href="https://github.com/OleksSobol/expenses-tracker" class="project-btn">View on GitHub</a>
  </div>
</div>

<div class="project-card">
  <div class="project-header">
    <div class="project-icon">💍</div>
    <div class="project-title-section">
      <h3>Wedding Website</h3>
    </div>
  </div>

  <p>Custom-built event website with password protection, RSVP management, and responsive design. Demonstrates full-stack web development skills and deployment experience.</p>

  <div class="tech-stack">
    <span class="tech-tag">HTML</span>
    <span class="tech-tag">CSS</span>
    <span class="tech-tag">JavaScript</span>
    <span class="tech-tag">Nginx</span>
    <span class="tech-tag">Authentication</span>
  </div>

  <strong>Key Features:</strong>
  <ul class="feature-list">
    <li>Password-protected access control system</li>
    <li>RSVP form with backend processing</li>
    <li>Responsive design for mobile and desktop</li>
    <li>Custom domain and hosting configuration</li>
  </ul>

  <div class="project-links">
    <a href="https://osobol.com/wedding-website/" class="project-btn">View Live Site</a>
    <a href="https://github.com/OleksSobol/wedding-website" class="project-btn project-btn-secondary">View on GitHub</a>
  </div>
</div>

---

## Learning & Exploration Projects

<div class="project-card">
  <div class="project-header">
    <div class="project-icon">🎵</div>
    <div class="project-title-section">
      <h3>Spotify Top 100 Analysis</h3>
    </div>
  </div>

  <p>Data analysis project exploring Spotify's top tracks. Demonstrates API integration, data processing, and analytical thinking with real-world datasets.</p>

  <div class="tech-stack">
    <span class="tech-tag">Python</span>
    <span class="tech-tag">Spotify API</span>
    <span class="tech-tag">Pandas</span>
    <span class="tech-tag">Data Analysis</span>
  </div>

  <div class="project-links">
    <a href="https://github.com/OleksSobol/Spotify-Top-100" class="project-btn">View on GitHub</a>
  </div>
</div>

<div class="project-card">
  <div class="project-header">
    <div class="project-icon">🎹</div>
    <div class="project-title-section">
      <h3>Patatap Clone</h3>
    </div>
  </div>

  <p>Interactive audio-visual web application where each keypress triggers unique sounds and animations. Built to explore creative coding and browser APIs.</p>

  <div class="tech-stack">
    <span class="tech-tag">JavaScript</span>
    <span class="tech-tag">Web Audio API</span>
    <span class="tech-tag">HTML5 Canvas</span>
    <span class="tech-tag">Animation</span>
  </div>

  <div class="project-links">
    <a href="https://github.com/OleksSobol/PatatapClone" class="project-btn">View on GitHub</a>
  </div>
</div>

<div class="project-card">
  <div class="project-header">
    <div class="project-icon">🌐</div>
    <div class="project-title-section">
      <h3>Personal Portfolio Website</h3>
    </div>
  </div>

  <p>This portfolio site itself is built with Jekyll static site generator, featuring a blog, project showcase, interactive playground, and custom layouts. Demonstrates technical writing and modern web development skills.</p>

  <div class="tech-stack">
    <span class="tech-tag">Jekyll</span>
    <span class="tech-tag">Ruby</span>
    <span class="tech-tag">GitHub Pages</span>
    <span class="tech-tag">Markdown</span>
    <span class="tech-tag">GitHub Actions</span>
  </div>

  <div class="project-links">
    <a href="https://osobol.com" class="project-btn">View Live Site</a>
    <a href="https://github.com/OleksSobol/olekssobol.github.io" class="project-btn project-btn-secondary">View Source</a>
  </div>
</div>

---

## Automation Tools & Infrastructure

<div style="background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%); border-left: 4px solid #52adc8; padding: 1.5rem; border-radius: 8px; margin: 2rem 0;">

Throughout my career, I've developed dozens of automation scripts and production tools for:

- **Network Device Management** — Python and Bash scripts for configuration automation
- **Firmware Deployment** — Automated systems reducing deployment time by 80%
- **Monitoring & Alerting** — Custom solutions for system health tracking
- **Data Migration Pipelines** — ETL processes for large-scale data transformation
- **API Testing & Validation** — Custom testing frameworks and tools

Many of these tools are proprietary to previous employers, but the patterns, architectures, and approaches are reflected in my public repositories and personal projects.

</div>

---

## Explore More

<div style="text-align: center; margin: 3rem 0 2rem;">
  <p style="font-size: 1.1rem; color: #b0b0b0; margin-bottom: 1.5rem;">
    Check out my GitHub profile for additional projects, contributions, and code samples
  </p>
  <a href="https://github.com/OleksSobol" class="project-btn" style="margin: 0.5rem;">View GitHub Profile</a>
  <a href="/playground/" class="project-btn" style="margin: 0.5rem; background: #3a3a3a; border: 1px solid #52adc8; color: #52adc8;">Try the Playground</a>
  <a href="/contact/" class="project-btn project-btn-secondary" style="margin: 0.5rem;">Contact Me</a>
</div>