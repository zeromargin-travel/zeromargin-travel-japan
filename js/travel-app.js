/* ==========================================================================
   0Margin Travel — App Controller, Savings Calculator & Member Gamification
   ========================================================================== */

function switchTab(tabId) {
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.tab === tabId);
  });

  document.querySelectorAll('.nav-item').forEach(item => {
    item.classList.toggle('active', item.getAttribute('onclick') && item.getAttribute('onclick').includes(tabId));
  });
  
  document.querySelectorAll('.tab-content').forEach(content => {
    content.classList.toggle('active', content.id === `tab-${tabId}`);
  });
  
  const navElement = document.querySelector('.tab-nav');
  if (navElement) {
    window.scrollTo({ top: navElement.offsetTop - 90, behavior: 'smooth' });
  }
}

// 0 Margin Savings Calculator
function calculateSavings() {
  const input = document.getElementById('calcInput');
  if (!input) return;
  
  const val = parseFloat(input.value) || 0;
  const traditionalFee = Math.round(val * 0.25); // Traditional platform 25% cut
  const savings = traditionalFee;
  const net = val;

  const feeEl = document.getElementById('calcTraditionalFee');
  const savingsEl = document.getElementById('calcSavings');
  const netEl = document.getElementById('calcNet');

  if (feeEl) feeEl.innerText = `$${traditionalFee.toLocaleString()}`;
  if (savingsEl) savingsEl.innerText = `$${savings.toLocaleString()}`;
  if (netEl) netEl.innerText = `$${net.toLocaleString()}`;
}

// Modal Controllers
function openRegisterModal() {
  const modal = document.getElementById('registerModal');
  if (modal) modal.classList.add('active');
}

function closeRegisterModal() {
  const modal = document.getElementById('registerModal');
  if (modal) modal.classList.remove('active');
}

function openVerifyModal() {
  const modal = document.getElementById('verifyModal');
  if (modal) modal.classList.add('active');
}

function closeVerifyModal() {
  const modal = document.getElementById('verifyModal');
  if (modal) modal.classList.remove('active');
}

// Rank & Contribution Calculator
function calculateMemberRank(pts, isVerified) {
  let basePoints = pts || 0;
  if (isVerified) basePoints += 150;
  
  if (basePoints >= 1000) {
    return { title: 'Golden Pioneer Fellow', icon: '🌟', color: '#D97706', level: 5, nextPts: 2000, desc: 'Master Pioneer nurturing global travel & peace' };
  } else if (basePoints >= 500) {
    return { title: 'Fruitful Companion', icon: '🍎', color: '#E11D48', level: 4, nextPts: 1000, desc: 'Providing fruits of support & active local walks' };
  } else if (basePoints >= 250) {
    return { title: 'Growing Tree Member', icon: '🌳', color: '#059669', level: 3, nextPts: 500, desc: 'Established roots in community cultural exchange' };
  } else if (basePoints >= 100) {
    return { title: 'Sprout Fellow', icon: '🌿', color: '#16A34A', level: 2, nextPts: 250, desc: 'Actively connecting with local companions' };
  } else {
    return { title: 'Seed Traveler', icon: '🌱', color: '#C2410C', level: 1, nextPts: 100, desc: 'Starting your 0Margin Travel journey' };
  }
}

function handleRegisterSubmit(event) {
  event.preventDefault();
  
  const name = document.getElementById('regName').value.trim();
  const email = document.getElementById('regEmail').value.trim();
  const wantVerified = document.getElementById('regVerifiedCheck').checked;
  
  if (!name || !email) {
    alert('Please enter your name and email.');
    return;
  }
  
  const memberId = 'ZMT-' + Math.floor(10000 + Math.random() * 90000);
  const memberData = {
    name: name,
    email: email,
    memberId: memberId,
    points: 50,
    history: [
      { action: 'Initial Community Registration', pts: '+50', date: new Date().toLocaleDateString() }
    ],
    isVerified: wantVerified,
    registeredDate: new Date().toLocaleDateString()
  };
  
  localStorage.setItem('zeroMarginTravelMember', JSON.stringify(memberData));
  closeRegisterModal();
  updateMemberState();
  
  if (wantVerified) {
    openVerifyModal();
  } else {
    alert(`Welcome to 0Margin Travel, ${name}!\nMember ID: ${memberId}\nYour rank: 🌱 Seed Traveler (50 pts)`);
  }
}

function handleVerificationSubmit(event) {
  event.preventDefault();
  
  const docType = document.getElementById('verifyDocType').value;
  const realName = document.getElementById('verifyRealName').value.trim();
  
  const saved = localStorage.getItem('zeroMarginTravelMember');
  if (!saved) return;
  
  let memberObj = JSON.parse(saved);
  memberObj.isVerified = true;
  if (realName) memberObj.name = realName;
  memberObj.points = (memberObj.points || 50) + 150;
  memberObj.history.unshift({ action: `Real-Name Verification (${docType})`, pts: '+150', date: new Date().toLocaleDateString() });
  
  localStorage.setItem('zeroMarginTravelMember', JSON.stringify(memberObj));
  closeVerifyModal();
  updateMemberState();
  
  const rank = calculateMemberRank(memberObj.points, memberObj.isVerified);
  alert(`Verification Complete!\n${memberObj.name} is now a "🔵 Verified Trust Member".\nNew Rank: ${rank.icon} ${rank.title} (${memberObj.points} pts)`);
}

function logContributionAction(actionName, ptsValue) {
  const saved = localStorage.getItem('zeroMarginTravelMember');
  if (!saved) {
    openRegisterModal();
    return;
  }
  
  let memberObj = JSON.parse(saved);
  memberObj.points = (memberObj.points || 0) + ptsValue;
  if (!memberObj.history) memberObj.history = [];
  memberObj.history.unshift({ action: actionName, pts: `+${ptsValue}`, date: new Date().toLocaleDateString() });
  
  localStorage.setItem('zeroMarginTravelMember', JSON.stringify(memberObj));
  updateMemberState();
  
  const rank = calculateMemberRank(memberObj.points, memberObj.isVerified);
  alert(`Contribution Logged!\nAction: ${actionName} (+${ptsValue} pts)\nTotal Points: ${memberObj.points} pts\nCurrent Rank: ${rank.icon} ${rank.title}`);
}

function updateMemberState() {
  const saved = localStorage.getItem('zeroMarginTravelMember');
  const navContainer = document.getElementById('navMemberArea');
  const myPageTabBtn = document.getElementById('myPageTabBtn');
  const myPageContent = document.getElementById('myPageContentArea');
  
  if (saved) {
    const member = JSON.parse(saved);
    const rank = calculateMemberRank(member.points, member.isVerified);
    
    if (myPageTabBtn) myPageTabBtn.style.display = 'inline-flex';
    
    if (navContainer) {
      navContainer.innerHTML = `
        <div style="display:flex; align-items:center; gap:0.5rem; background:#FFFDF9; border:1.5px solid var(--border-ink); padding:0.35rem 0.85rem; border-radius:9999px; cursor:pointer;" onclick="switchTab('mypage')">
          <span style="font-size:1.1rem;">${rank.icon}</span>
          <span style="font-weight:700; font-size:0.85rem; color:#1F2937;">${escapeHtml(member.name)}</span>
          ${member.isVerified ? 
            `<span class="verified-badge">🔵 Verified</span>` : 
            `<span style="font-size:0.75rem; color:#78716C;">⚪ ${rank.title}</span>`}
        </div>
      `;
    }
    
    if (myPageContent) {
      const fillPercent = Math.min(100, Math.round((member.points / rank.nextPts) * 100));
      
      myPageContent.innerHTML = `
        <div style="background:var(--bg-card); border:2px solid var(--border-ink); border-radius:22px; padding:2.5rem; margin-bottom:2rem; box-shadow:var(--shadow-sketch);">
          
          <div style="display:flex; align-items:center; gap:1.25rem; margin-bottom:2rem; background:var(--bg-card-warm); border:2px solid var(--border-ink); border-radius:18px; padding:1.75rem;">
            <div style="width:70px; height:70px; border-radius:50%; background:#FFF; border:2px solid var(--border-ink); display:flex; align-items:center; justify-content:center; font-size:2.3rem;">
              ${rank.icon}
            </div>
            <div style="flex:1;">
              <h2 style="font-size:1.6rem; font-family:var(--font-sans); margin:0;">${escapeHtml(member.name)}</h2>
              <p style="font-size:0.85rem; color:#57534E; margin-top:0.2rem;">
                Member ID: <strong>${member.memberId}</strong> | Rank Level ${rank.level}: <strong style="color:${rank.color};">${rank.title}</strong>
              </p>
              
              <div style="margin-top:0.75rem;">
                <div style="display:flex; justify-content:space-between; font-size:0.8rem; font-weight:700; color:#4A5568;">
                  <span>Contribution Points: ${member.points} pts</span>
                  <span>Next Goal: ${rank.nextPts} pts</span>
                </div>
                <div style="width:100%; height:12px; background:#D6C7B2; border:1px solid #292524; border-radius:9999px; overflow:hidden; margin-top:0.3rem;">
                  <div style="height:100%; background:linear-gradient(90deg, #047857, #B45309); width:${fillPercent}%;"></div>
                </div>
              </div>
            </div>
          </div>

          <h3 style="font-size:1.2rem; margin-bottom:1rem; font-family:var(--font-sans);">📜 Travel & Contribution History</h3>
          <div style="background:#FFF; border:1.5px solid var(--border-ink); border-radius:12px; padding:1rem;">
            ${member.history && member.history.length > 0 ? 
              member.history.map(item => `
                <div style="display:flex; justify-content:space-between; align-items:center; padding:0.6rem 0; border-bottom:1px dashed #EADEC9;">
                  <div>
                    <strong style="font-size:0.9rem; color:#1F2937;">${escapeHtml(item.action)}</strong>
                    <span style="font-size:0.75rem; color:#718096; margin-left:0.5rem;">${item.date}</span>
                  </div>
                  <span style="font-weight:700; color:#059669; font-size:0.9rem;">${item.pts} pts</span>
                </div>
              `).join('') : 
              `<p style="font-size:0.85rem; color:#718096;">No activities logged yet.</p>`}
          </div>

          <div style="margin-top:2rem; text-align:right;">
            <button class="btn btn-secondary" style="font-size:0.85rem; color:#E11D48;" onclick="handleLogout()">
              Log Out
            </button>
          </div>
        </div>
      `;
    }
  } else {
    if (myPageTabBtn) myPageTabBtn.style.display = 'none';
    if (navContainer) {
      navContainer.innerHTML = `
        <button class="btn btn-emerald" style="padding:0.45rem 1rem; font-size:0.85rem;" onclick="openRegisterModal()">
          👤 Member Sign Up (Free)
        </button>
      `;
    }
  }
}

function handleLogout() {
  if (confirm('Are you sure you want to log out?')) {
    localStorage.removeItem('zeroMarginTravelMember');
    updateMemberState();
    switchTab('planner');
  }
}

function escapeHtml(str) {
  if (str === null || str === undefined) return '';
  return String(str).replace(/[&<>"']/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' }[m]));
}

window.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => switchTab(btn.dataset.tab));
  });

  const calcInput = document.getElementById('calcInput');
  if (calcInput) {
    calcInput.addEventListener('input', calculateSavings);
    calculateSavings();
  }
  
  updateMemberState();
});
