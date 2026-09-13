/* ==========================================================================
   0 Margin Japan Travel — Interactive AI Route Planner
   Rich Multi-City Candidate Spots Database (★4.5+ Verified Places)
   Geographically Accurate Images + Native Lazy Loading + SVG Fallback
   ========================================================================== */

const SVG_FALLBACK_IMAGE = `data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="600" height="340" viewBox="0 0 600 340"><rect width="600" height="340" fill="%23FAF7F2"/><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="22" fill="%2378350F">🌺 沖縄 観光スポット</text></svg>`;

let candidateSpotsDatabase = {};


function getCategoryIcon(cat) {
  if (!cat) return '📍';
  const c = String(cat).toLowerCase();
  if (c.includes('hotel') || c.includes('stay')) return '🏨';
  if (c.includes('café') || c.includes('cafe') || c.includes('bakery')) return '☕';
  if (c.includes('bistro') || c.includes('restaurant') || c.includes('dining')) return '🍷';
  if (c.includes('park') || c.includes('garden')) return '🌳';
  if (c.includes('museum') || c.includes('gallery')) return '🎨';
  if (c.includes('palace') || c.includes('castle') || c.includes('church') || c.includes('cathedral') || c.includes('landmark')) return '🏛️';
  return '📍';
}

const AITravelEngine = {
  selectedMustVisitIds: new Set(),

  trackEvent(eventName, parameters) {
    if (typeof window.gtag !== 'function') return;
    try {
      window.gtag('event', eventName, parameters);
    } catch (error) {
      console.warn(`Analytics event failed: ${eventName}`, error);
    }
  },

  async init() {
    try {
      this.restoreStateFromUrl();
    } catch (error) {
      console.error("Failed to initialize AITravelEngine:", error);
    }
  },

  async loadCityData(cityId) {
    if (candidateSpotsDatabase[cityId]) return;
    try {
      const grid = document.getElementById('candidateSpotsGrid');
      if (grid) {
        grid.innerHTML = `<div style="text-align:center; padding:3rem; grid-column:1/-1;">
          <div style="display:inline-block; animation:spin 1s linear infinite; font-size:2rem;">⚡️</div>
          <div style="margin-top:1rem; color:var(--text-secondary); font-weight:bold;" data-i18n="loading.database">沖縄の厳選スポットを読み込み中...</div>
        </div>`;
      }
      
      const cleanCityName = cityId.split(',')[0].trim().toLowerCase().replace(/\s+/g, '_');
      const fileName = cleanCityName + '.json';
      const basePath = window.API_BASE_PATH || '';
      const response = await fetch(basePath + 'data/cities/' + fileName);
      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
      const spots = await response.json();
      
      // *** Normalization Layer: Convert free-text strings and scattered booleans to strict tags ***
      spots.forEach(spot => {
        const c = String(spot.category || '').toLowerCase();
        spot.tags = {
          isLandmark: c.includes('landmark') || c.includes('史跡') || c.includes('名所') || c.includes('城') || c.includes('寺') || c.includes('神社'),
          isMuseum: c.includes('museum') || c.includes('art') || c.includes('ギャラリー') || c.includes('美術館') || c.includes('博物館') || c.includes('水族館') || c.includes('テーマパーク') || c.includes('theme park') || c.includes('zoo') || c.includes('culture'),
          isCafe: c.includes('café') || c.includes('cafe') || c.includes('bistro') || c.includes('restaurant') || c.includes('dining') || c.includes('bakery') || c.includes('カフェ') || c.includes('レストラン') || c.includes('グルメ') || c.includes('沖縄そば'),
          isScenery: c.includes('scenery') || c.includes('walk') || c.includes('park') || c.includes('プロムナード') || c.includes('散策') || c.includes('ビーチ') || c.includes('岬') || c.includes('海') || c.includes('自然') || c.includes('景観'),
          isKids: spot.kids === true,
          // Strict Shopping Policy: spot.shopping must be true, or primary category explicitly represents Market/Shopping (excluding broad street/scenery)
          isShopping: spot.shopping === true || (c.includes('shopping') && !c.includes('scenery')) || c.includes('market') || c.includes('市場') || c.includes('商店街') || c.includes('アウトレット')
        };
        // Sync boolean flags for consistent UI rendering elsewhere
        spot.kids = spot.tags.isKids;
        spot.shopping = spot.tags.isShopping;
      });
      
      candidateSpotsDatabase[cityId] = spots;
    } catch (error) {
      console.error(`Failed to load city database for ${cityId}:`, error);
      candidateSpotsDatabase[cityId] = [];
    }
  },

  async restoreStateFromUrl() {
    const params = new URLSearchParams(window.location.search);
    const urlCountry = params.get('country');
    const urlCity = params.get('city');
    const urlSpots = params.get('spots');
    
    let targetCity = 'Okinawa, Japan';

    if (urlCountry) {
      const countryElem = document.getElementById('aiPlanCountry');
      if (countryElem) {
        for (let i = 0; i < countryElem.options.length; i++) {
          if (countryElem.options[i].value === urlCountry || countryElem.options[i].text.includes(urlCountry)) {
            countryElem.selectedIndex = i;
            break;
          }
        }
      }
      // Populate city dropdown manually based on country
      const cities = this.countryCityMap[urlCountry] || this.countryCityMap['沖縄'];
      const destElem = document.getElementById('aiPlanDestination');
      if (destElem) {
         destElem.innerHTML = cities.map(c => `<option value="${c.value}">${this.getLocalizedCityLabel(c)}</option>`).join('');
      }
    }
    
    if (urlCity) {
      const decodedCity = decodeURIComponent(urlCity);
      targetCity = decodedCity;
      const destElem = document.getElementById('aiPlanDestination');
      if (destElem) {
        let found = false;
        for (let i = 0; i < destElem.options.length; i++) {
          if (destElem.options[i].value === decodedCity) {
            destElem.selectedIndex = i;
            found = true;
            break;
          }
        }
        if (!found) destElem.value = decodedCity;
      }
    } else {
      const destElem = document.getElementById('aiPlanDestination');
      if (destElem) targetCity = destElem.value || 'Okinawa, Japan';
    }

    if (urlCity && urlSpots) {
      const spotIds = urlSpots.split(',');
      this.selectedMustVisitIds.clear();
      spotIds.forEach(id => this.selectedMustVisitIds.add(id));
    }
    
    this.lastCity = targetCity;
    await this.loadCityData(targetCity);
    
    if (urlCity && urlSpots) {
      setTimeout(() => {
        this.renderCandidateSpots();
        this.renderDualRouteManager(this.lastCity);
        const routeContainer = document.getElementById('routeContainer');
        if (routeContainer) {
          routeContainer.scrollIntoView({ behavior: 'smooth' });
        }
      }, 100);
    } else {
      setTimeout(() => {
        this.renderCandidateSpots();
      }, 100);
    }
  },

  shareGeneral(platform) {
    const t = (k) => window.I18nEngine ? window.I18nEngine.getText(k) : k;
    const text = encodeURIComponent(t('share.generalText') || 'A free app that automatically plans optimal Europe travel routes. Very helpful! ✈️ #0MarginTravel');
    const url = encodeURIComponent('https://zeromargin-travel.github.io/');
    this.openShareLink(platform, text, url);
  },

  shareRoute(platform) {
    if (!this.lastCity || this.selectedMustVisitIds.size === 0) return;
    const t = (k) => window.I18nEngine ? window.I18nEngine.getText(k) : k;
    let baseText = t('share.routeText') || 'I made a 1-day travel plan for [City]! Check out the route 🗺️';
    baseText = baseText.replace('[City]', this.lastCity.split(',')[0]);
    
    const text = encodeURIComponent(baseText);
    const spotIds = Array.from(this.selectedMustVisitIds).join(',');
    const routeUrl = `https://zeromargin-travel.github.io/?city=${encodeURIComponent(this.lastCity)}&spots=${spotIds}`;
    this.openShareLink(platform, text, encodeURIComponent(routeUrl));
  },

  showToast(msg) {
    const toast = document.getElementById('toastNotification');
    if (!toast) return;
    toast.innerHTML = msg;
    toast.classList.add('show');
    if (this._toastTimer) clearTimeout(this._toastTimer);
    this._toastTimer = setTimeout(() => {
      toast.classList.remove('show');
    }, 2500);
  },

  openShareLink(platform, text, url) {
    let shareUrl = '';
    const decodedText = decodeURIComponent(text);
    const decodedUrl = decodeURIComponent(url);

    if (platform === 'x') shareUrl = `https://twitter.com/intent/tweet?text=${text}&url=${url}`;
    if (platform === 'line') shareUrl = `https://line.me/R/msg/text/?${text}%20${url}`;
    if (platform === 'wa') shareUrl = `https://api.whatsapp.com/send?text=${text}%20${url}`;
    if (platform === 'fb') shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${url}`;
    if (platform === 'li') shareUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${url}`;

    if (platform === 'native') {
      if (navigator.share) {
        navigator.share({
          title: '0Margin Travel',
          text: decodedText,
          url: decodedUrl
        }).catch(() => {});
        return;
      } else {
        platform = 'copy';
      }
    }

    if (platform === 'copy') {
      navigator.clipboard.writeText(decodedUrl).then(() => {
        const t = (k) => window.I18nEngine ? window.I18nEngine.getText(k) : k;
        this.showToast(t('share.toastCopied') || 'Link copied to clipboard! ✨');
      }).catch(() => {
        alert('Copy failed. URL: ' + decodedUrl);
      });
      return;
    }

    if (shareUrl) window.open(shareUrl, '_blank', 'noopener,noreferrer');
  },

  // Helper to create single venue Google Maps live search link button
  createMapsLink(placeName, city, compact = false) {
    const cleanPlace = placeName.replace(/[()]/g, '').trim();
    const cleanCity = city.split(',')[0].trim();
    const query = encodeURIComponent(`${cleanPlace} ${cleanCity}`);
    const mapsUrl = `https://www.google.com/maps/search/?api=1&query=${query}`;
    if (compact) {
      return `<a href="${mapsUrl}" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation();" style="display:inline-flex; align-items:center; justify-content:center; background:#EFF6FF; color:#1D4ED8; border:1px solid #93C5FD; padding:0.2rem 0.45rem; border-radius:6px; font-weight:800; text-decoration:none; font-size:0.75rem; white-space:nowrap; flex-shrink:0;" title="Open Google Maps">📍↗</a>`;
    }
    return `<a href="${mapsUrl}" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation();" style="display:inline-flex; align-items:center; justify-content:center; gap:0.2rem; background:#EFF6FF; color:#1D4ED8; border:1.5px solid #93C5FD; padding:0.25rem 0.55rem; border-radius:6px; font-weight:700; text-decoration:none; font-size:0.8rem; white-space:nowrap; max-width:100%;" title="View Live Google Maps Hours, Reviews & Photos">📍 Maps ↗</a>`;
  },

  // MASTER DUAL ROUTE GENERATOR: Route A (Must-Visit Selected Spots) & Route B (Full 1-Day AI Recommended Course)
  generateMultiStopMapsLink(mustVisitVenues, fullDayVenues, city, transportMode) {
    const cleanCity = city.split(',')[0].trim();

    // 1. ROUTE A: Must-Visit Selected Spots Only
    const cleanMust = (mustVisitVenues || []).map(v => v.replace(/[()]/g, '').trim()).filter(Boolean);
    const masterUrlA = this.buildMasterGoogleMapsPath(cleanMust, cleanCity);

    // 2. ROUTE B: Full 1-Day AI Recommended Course (All Destinations)
    const cleanFull = (fullDayVenues || []).map(v => v.replace(/[()]/g, '').trim()).filter(Boolean);
    const masterUrlB = this.buildMasterGoogleMapsPath(cleanFull, cleanCity);

    // Badges for Route A
    const badgesA = cleanMust.map((v, idx) => `
      <span style="display:inline-flex; align-items:center; gap:0.2rem; background:#ECFDF5; color:#047857; border:1px solid #A7F3D0; padding:0.25rem 0.6rem; border-radius:6px; font-weight:700; font-size:0.82rem; margin:0.15rem;">
        <span style="background:#047857; color:#FFF; border-radius:999px; width:18px; height:18px; display:inline-flex; justify-content:center; align-items:center; font-size:0.7rem;">${idx + 1}</span>
        ${escapeHtml(v)}
      </span>
    `).join(' ➔ ');

    // Badges for Route B
    const badgesB = cleanFull.map((v, idx) => `
      <span style="display:inline-flex; align-items:center; gap:0.2rem; background:#FFFBEB; color:#B45309; border:1px solid #FDE68A; padding:0.25rem 0.6rem; border-radius:6px; font-weight:700; font-size:0.82rem; margin:0.15rem;">
        <span style="background:#B45309; color:#FFF; border-radius:999px; width:18px; height:18px; display:inline-flex; justify-content:center; align-items:center; font-size:0.7rem;">${idx + 1}</span>
        ${escapeHtml(v)}
      </span>
    `).join(' ➔ ');

    // Leg-by-Leg links for Route A (Forced to driving mode)
    let legItemsAHtml = '';
    for (let i = 0; i < cleanMust.length - 1; i++) {
      const legUrl = `https://www.google.com/maps/dir/?api=1&origin=${encodeURIComponent(cleanMust[i] + ', ' + cleanCity)}&destination=${encodeURIComponent(cleanMust[i + 1] + ', ' + cleanCity)}&travelmode=driving&dirflg=d`;
      legItemsAHtml += `
        <div style="background:#FFF; border:1px solid #CBD5E1; border-radius:8px; padding:0.4rem 0.75rem; font-size:0.82rem; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-top:0.4rem;">
          <span style="font-weight:700; color:var(--text-primary);">Leg ${i + 1}: ${escapeHtml(cleanMust[i])} ➔ ${escapeHtml(cleanMust[i + 1])}</span>
          <a href="${legUrl}" target="_blank" rel="noopener noreferrer" style="color:#0284C7; font-weight:700; text-decoration:none; background:#F0F9FF; padding:0.15rem 0.55rem; border-radius:4px; border:1px solid #BAE6FD;">
            🚗 Drive Leg ↗
          </a>
        </div>
      `;
    }

    // Leg-by-Leg links for Route B (Forced to driving mode)
    let legItemsBHtml = '';
    for (let i = 0; i < cleanFull.length - 1; i++) {
      const legUrl = `https://www.google.com/maps/dir/?api=1&origin=${encodeURIComponent(cleanFull[i] + ', ' + cleanCity)}&destination=${encodeURIComponent(cleanFull[i + 1] + ', ' + cleanCity)}&travelmode=driving&dirflg=d`;
      legItemsBHtml += `
        <div style="background:#FFF; border:1px solid #CBD5E1; border-radius:8px; padding:0.4rem 0.75rem; font-size:0.82rem; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-top:0.4rem;">
          <span style="font-weight:700; color:var(--text-primary);">Leg ${i + 1}: ${escapeHtml(cleanFull[i])} ➔ ${escapeHtml(cleanFull[i + 1])}</span>
          <a href="${legUrl}" target="_blank" rel="noopener noreferrer" style="color:#0284C7; font-weight:700; text-decoration:none; background:#F0F9FF; padding:0.15rem 0.55rem; border-radius:4px; border:1px solid #BAE6FD;">
            🚗 Drive Leg ↗
          </a>
        </div>
      `;
    }

    return `
      <div style="background:rgba(15, 23, 42, 0.92); border:1px solid rgba(255, 255, 255, 0.2); border-radius:20px; padding:1.75rem; margin-bottom:1.75rem; box-shadow:0 10px 30px rgba(0,0,0,0.6);">
        
        <div style="text-align:center; margin-bottom:1.5rem;">
          <div style="font-size:1.45rem; color:#FCD34D; font-family:var(--font-serif); font-weight:800; text-shadow:0 0 10px rgba(252,211,77,0.3);" class="font-serif">
            🗺️ Dual Multi-Stop Google Maps Navigation Routes
          </div>
          <p style="font-size:0.9rem; color:#CBD5E1; max-width:650px; margin:0.35rem auto 0;">
            Select either <strong style="color:#FFF;">Route A (Must-Visit Spots Only)</strong> or <strong style="color:#FFF;">Route B (Full 1-Day AI Course)</strong> below to open all stops in sequential order in Google Maps!
          </p>
        </div>

        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:1.5rem; margin-bottom:1rem;">
          
          <!-- ROUTE A CARD: MUST-VISIT SPOTS ONLY -->
          <div style="background:rgba(15, 23, 42, 0.95); border:2px solid #10B981; border-radius:16px; padding:1.5rem; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 0 20px rgba(16,185,129,0.3);">
            <div>
              <div style="display:inline-block; background:#059669; color:#FFF; font-weight:800; font-size:0.75rem; padding:0.2rem 0.65rem; border-radius:999px; margin-bottom:0.5rem;">
                ROUTE A — MUST-VISIT SPOTS ONLY
              </div>
              <h4 style="font-size:1.15rem; color:#34D399; font-family:var(--font-serif); margin-bottom:0.35rem;" class="font-serif">
                🎯 Selected Spots Only (${cleanMust.length} Stops)
              </h4>
              <p style="font-size:0.88rem; color:#F9FAFB; line-height:1.5; margin-bottom:0.85rem;">
                Contains strictly your checked <strong>must-visit landmarks</strong> in optimal sequential order.
              </p>
              
              <div style="margin-bottom:1.25rem; line-height:1.8;">
                ${badgesA}
              </div>
            </div>

            <div>
              <a href="${masterUrlA}" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="padding:0.85rem 1.25rem; font-size:1rem; text-decoration:none; text-align:center; width:100%; justify-content:center; background:#059669; border-color:#10B981; color:#FFF; font-weight:800;">
                📍 Open Route A in Google Maps (${cleanMust.length} Spots) ↗
              </a>

              ${cleanMust.length > 1 ? `
                <details style="margin-top:0.75rem; text-align:left; background:rgba(30, 41, 59, 0.9); border-radius:8px; padding:0.4rem 0.65rem; border:1px solid rgba(16,185,129,0.4);">
                  <summary style="font-weight:700; color:#34D399; cursor:pointer; font-size:0.82rem;">
                    🚆 Route A Segment Details (${cleanMust.length - 1} Segments)
                  </summary>
                  <div style="margin-top:0.4rem;">
                    ${legItemsAHtml}
                  </div>
                </details>
              ` : ''}
            </div>
          </div>

          <!-- ROUTE B CARD: FULL 1-DAY AI RECOMMENDED COURSE -->
          <div style="background:rgba(15, 23, 42, 0.95); border:2px solid #F59E0B; border-radius:16px; padding:1.5rem; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 0 20px rgba(245,158,11,0.3);">
            <div>
              <div style="display:inline-block; background:#D97706; color:#FFF; font-weight:800; font-size:0.75rem; padding:0.2rem 0.65rem; border-radius:999px; margin-bottom:0.5rem;">
                ROUTE B — FULL 1-DAY AI RECOMMENDED COURSE
              </div>
              <h4 style="font-size:1.15rem; color:#FCD34D; font-family:var(--font-serif); margin-bottom:0.35rem;" class="font-serif">
                ✨ Full 1-Day AI Course (${cleanFull.length} Stops)
              </h4>
              <p style="font-size:0.88rem; color:#F9FAFB; line-height:1.5; margin-bottom:0.85rem;">
                Combines your selected spots with <strong>AI-curated bistros & attractions to form a full route</strong>.
              </p>

              <div style="margin-bottom:1.25rem; line-height:1.8;">
                ${badgesB}
              </div>
            </div>

            <div>
              <a href="${masterUrlB}" target="_blank" rel="noopener noreferrer" class="btn btn-emerald" style="padding:0.85rem 1.25rem; font-size:1rem; text-decoration:none; text-align:center; width:100%; justify-content:center; background:#D97706; border-color:#F59E0B; color:#FFF; font-weight:800;">
                ✨ Open Route B in Google Maps (${cleanFull.length} Full Stops) ↗
              </a>

              ${cleanFull.length > 1 ? `
                <details style="margin-top:0.75rem; text-align:left; background:rgba(30, 41, 59, 0.9); border-radius:8px; padding:0.4rem 0.65rem; border:1px solid rgba(245,158,11,0.4);">
                  <summary style="font-weight:700; color:#FCD34D; cursor:pointer; font-size:0.82rem;">
                    🚆 Route B Segment Details (${cleanFull.length - 1} Segments)
                  </summary>
                  <div style="margin-top:0.4rem;">
                    ${legItemsBHtml}
                  </div>
                </details>
              ` : ''}
            </div>
          </div>

        </div>

      </div>
    `;
  },

  lastCity: '',
  selectedMustVisitIds: new Set(),
  viewMode: 'grid',
  activePreset: 'ALL',
  activeGenre: 'ALL',
  activeConditions: new Set(),
  categoryFilter: 'ALL',

  setViewMode(mode) {
    this.viewMode = mode;
    this.renderCandidateSpots();
  },

  setPresetFilter(preset) {
    this.activePreset = preset;
    this.renderCandidateSpots();
  },

  toggleGenreFilter(genre) {
    if (this.activeGenre === genre) {
      this.activeGenre = 'ALL';
    } else {
      this.activeGenre = genre;
    }
    this.renderCandidateSpots();
  },

  toggleConditionFilter(condition) {
    if (!this.activeConditions) this.activeConditions = new Set();
    if (this.activeConditions.has(condition)) {
      this.activeConditions.delete(condition);
    } else {
      this.activeConditions.add(condition);
    }
    this.renderCandidateSpots();
  },

  isSpotMatchingFilter(spot, preset, category, conditions) {
    if (!spot) return false;
    
    // Layer 1: Scope Check (ALL, Top7, HiddenGem, Night)
    if (preset === 'Top7' && spot.top7 !== true) return false;
    if (preset === 'HiddenGem' && spot.hiddenGem !== true) return false;
    if (preset === 'Night' && !(spot.is_night_spot === true || spot.night === true || (Array.isArray(spot.categories) && spot.categories.includes('Night')))) return false;

    // Layer 2: Category Check (Pure Venue Genres using Normalization Layer tags)
    if (category && category !== 'ALL') {
      if (category === 'Landmark' && (!spot.tags || !spot.tags.isLandmark)) return false;
      if (category === 'Museum' && (!spot.tags || !spot.tags.isMuseum)) return false;
      if (category === 'Café' && (!spot.tags || !spot.tags.isCafe)) return false;
      if (category === 'Scenery' && (!spot.tags || !spot.tags.isScenery)) return false;
      if (category === 'Kids' && (!spot.tags || !spot.tags.isKids)) return false;
      if (category === 'Shopping' && (!spot.tags || !spot.tags.isShopping)) return false;
    }

    // Layer 3: Conditions Check (AND Logic)
    if (conditions && conditions.size > 0) {
      for (const cond of conditions) {
        if (cond === 'Rain' && spot.rain !== true) return false;
        if (cond === 'Free' && spot.free !== true) return false;
      }
    }

    return true;
  },

  countryCityMap: {
    "沖縄": [
      {
        "value": "Okinawa, Japan",
        "label": "🏝️ 沖縄本島（全域）"
      }
    ]
  },

  getLocalizedCityLabel(c) {
    const lang = window.I18nEngine ? window.I18nEngine.currentLang : 'ja';
    const cityMap = {
      "Okinawa, Japan": { ja: "🏝️ 沖縄本島（全域）", en: "🏝️ Okinawa Main Island", zh: "🏝️ 冲绳本岛 (全域)" }
    };
    if (cityMap[c.value] && cityMap[c.value][lang]) {
      return cityMap[c.value][lang];
    }
    return c.label;
  },

  async onCountryChange() {
    const countryElem = document.getElementById('aiPlanCountry');
    const destElem = document.getElementById('aiPlanDestination');
    if (!countryElem || !destElem) return;

    const country = countryElem.value || '沖縄';
    const cities = this.countryCityMap[country] || this.countryCityMap['沖縄'];
    const currentVal = destElem.value;
    const hasCurrent = cities.some(c => c.value === currentVal);
    const targetVal = hasCurrent ? currentVal : (cities[0] ? cities[0].value : '');

    destElem.innerHTML = cities.map(c => `<option value="${c.value}" ${c.value === targetVal ? 'selected' : ''}>${this.getLocalizedCityLabel(c)}</option>`).join('');
    destElem.value = targetVal;
    
    await this.loadCityData(targetVal);
    this.renderCandidateSpots();
  },

  async onDestinationChange() {
    const destElem = document.getElementById('aiPlanDestination');
    if (!destElem) return;
    const targetVal = destElem.value;
    await this.loadCityData(targetVal);
    this.renderCandidateSpots();
  },

  isCategoryMatch(spot, filterGroup) {
    if (!spot || !filterGroup || filterGroup === 'ALL') return true;
    if (filterGroup === 'Top7') return spot.top7 === true;
    if (filterGroup === 'HiddenGem') return spot.hiddenGem === true;
    if (filterGroup === 'Kids') return spot.kids === true;
    if (filterGroup === 'Rain') return spot.rain === true;
    if (filterGroup === 'Shopping') return spot.shopping === true;
    if (filterGroup === 'Free') return spot.free === true;
    const c = String(spot.category || '').toLowerCase();
    if (filterGroup === 'Landmark') return c.includes('landmark');
    if (filterGroup === 'Museum') return c.includes('museum') || c.includes('art');
    if (filterGroup === 'Café') return c.includes('café') || c.includes('cafe') || c.includes('bakery') || c.includes('restaurant') || c.includes('bistro') || c.includes('dining');
    if (filterGroup === 'Scenery') return c.includes('scenery') || c.includes('park') || c.includes('market') || c.includes('shopping');
    return true;
  },

  getLocalizedSpotName(spot) {
    if (!spot) return '';
    const lang = window.I18nEngine ? window.I18nEngine.currentLang : 'ja';
    if (lang === 'ja') {
      return spot.name_ja || spot.name || spot.name_local || '';
    }
    const val = spot['name_' + lang] || spot.name_en || spot.name_local || spot.name || '';
    return String(val).replace(/（[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\s\-_]+）/g, '')
                      .replace(/\([\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\s\-_]+\)/g, '')
                      .trim();
  },
  getLocalizedDesc(spot) {
    if (!spot) return '';
    const lang = window.I18nEngine ? window.I18nEngine.currentLang : 'ja';
    return spot['desc_' + lang] || spot.desc_ja || spot.desc || spot.desc_en || '';
  },
  getLocalizedTip(spot) {
    if (!spot) return '';
    const lang = window.I18nEngine ? window.I18nEngine.currentLang : 'ja';
    return spot['tip_' + lang] || spot['insiderTip_' + lang] || spot.tip_ja || spot.tip || spot.insiderTip_en || spot.tip_en || '';
  },
  getLocalizedPrice(spot) {
    if (!spot) return '';
    const lang = window.I18nEngine ? window.I18nEngine.currentLang : 'ja';
    return spot['price_' + lang] || spot.price_ja || spot.price || spot.price_en || '';
  },
  getLocalizedCategory(spot) {
    const lang = window.I18nEngine ? window.I18nEngine.currentLang : 'ja';
    
    // Fallback if spot or tags missing
    if (!spot || !spot.tags) {
       const c = String(spot ? spot.category || '' : '').toLowerCase();
       if (c.includes('landmark')) return lang === 'ja' ? '🏛️ 名所' : lang === 'es' ? '🏛️ Monumento' : lang === 'zh' ? '🏛️ 地标' : lang === 'fr' ? '🏛️ Monument' : lang === 'de' ? '🏛️ Highlight' : '🏛️ Landmark';
       return lang === 'ja' ? '📍 名所' : lang === 'es' ? '📍 Lugar' : lang === 'zh' ? '📍 景点' : lang === 'fr' ? '📍 Lieu' : lang === 'de' ? '📍 Ort' : '📍 Spot';
    }
    
    let tags = [];
    if (spot.tags.isLandmark) tags.push(lang === 'ja' ? '🏛️ 史跡・名所' : '🏛️ Landmark');
    if (spot.tags.isMuseum) tags.push(lang === 'ja' ? '🎨 文化・体験' : '🎨 Culture');
    if (spot.tags.isCafe) tags.push(lang === 'ja' ? '☕ カフェ・グルメ' : '☕ Dining');
    if (spot.tags.isScenery) tags.push(lang === 'ja' ? '🌊 絶景・ビーチ' : '🌊 Scenery');
    if (spot.tags.isKids) tags.push(lang === 'ja' ? '🧸 子ども向け' : '🧸 Kids');
    if (spot.tags.isShopping) tags.push(lang === 'ja' ? '🛍️ 買物・市場' : '🛍️ Shopping');
    
    if (tags.length === 0) return lang === 'ja' ? '📍 名所' : '📍 Spot';

    // Prioritize the active genre if the user is filtering
    const activeGenre = this.activeGenre;
    if (activeGenre && activeGenre !== 'ALL') {
      const activeTagIndex = tags.findIndex(t => {
        if (activeGenre === 'Landmark') return t.includes('🏛️');
        if (activeGenre === 'Museum') return t.includes('🎨');
        if (activeGenre === 'Café') return t.includes('☕');
        if (activeGenre === 'Scenery') return t.includes('🌊');
        if (activeGenre === 'Kids') return t.includes('🧸');
        if (activeGenre === 'Shopping') return t.includes('🛍️');
        return false;
      });
      if (activeTagIndex > 0) {
        const activeTag = tags.splice(activeTagIndex, 1)[0];
        tags.unshift(activeTag);
      }
    }
    return tags.join(' ');
  },
  getLocalizedZone(zone) {
    const lang = window.I18nEngine ? window.I18nEngine.currentLang : 'ja';
    if (zone === 'suburban') {
      return lang === 'ja' ? '🏞️ 中部・北部' : '🏞️ Central/North';
    }
    return lang === 'ja' ? '🏙️ 那覇・南部' : '🏙️ Naha/South';
  },

  handleImageError(imgElem, category, rating, cardCatText) {
    if (!imgElem || !imgElem.parentElement) return;
    const parent = imgElem.parentElement;
    const catIcon = (typeof getCategoryIcon === 'function') ? getCategoryIcon(category) : '📍';
    const cleanCat = cardCatText || category || 'Venue';
    const cleanRating = rating || '★4.5';
    
    parent.className = 'spot-header-fallback';
    parent.style.cssText = 'width:100%; height:76px; border-radius:12px; margin-bottom:0.75rem; background:linear-gradient(135deg, #FEF3C7, #E0E7FF); border:1.5px solid var(--border-ink); display:flex; align-items:center; justify-content:space-between; padding:0.75rem 1rem; position:relative; box-sizing:border-box;';
    parent.innerHTML = `
      <div style="display:flex; align-items:center; gap:0.5rem;">
        <span style="font-size:1.5rem;">${catIcon}</span>
        <div>
          <div style="font-weight:800; font-size:0.85rem; color:var(--primary-wood);">${escapeHtml(cleanCat)}</div>
          <div style="font-size:0.72rem; color:var(--text-secondary);">Verified Google Maps Venue</div>
        </div>
      </div>
      <span style="font-size:0.75rem; font-weight:800; background:#FFF; color:#047857; padding:0.2rem 0.55rem; border-radius:6px; border:1px solid #047857;">${escapeHtml(cleanRating)}</span>
    `;
  },

  openSpotModal(spotId) {
    let spot = null;
    if (this.lastCity && candidateSpotsDatabase[this.lastCity]) {
      spot = candidateSpotsDatabase[this.lastCity].find(s => s.id === spotId);
    }
    if (!spot) {
      for (const cityKey in candidateSpotsDatabase) {
        const found = candidateSpotsDatabase[cityKey].find(s => s.id === spotId);
        if (found) {
          spot = found;
          break;
        }
      }
    }
    if (!spot) return;

    let modal = document.getElementById('spotDetailModal');
    if (!modal) {
      modal = document.createElement('div');
      modal.id = 'spotDetailModal';
      modal.className = 'modal-overlay';
      modal.onclick = (e) => this.closeSpotModal(e);
      document.body.appendChild(modal);
    }

    const activeName = this.getLocalizedSpotName(spot);
    const activeDesc = this.getLocalizedDesc(spot);
    const activeTip = this.getLocalizedTip(spot);
    const activePrice = this.getLocalizedPrice(spot);
    const activeCat = this.getLocalizedCategory(spot);
    const activeZone = this.getLocalizedZone(spot.locationZone);

    const hasPhoto = Boolean(spot.image);
    const cleanRating = String(spot.rating || '').startsWith('★') ? spot.rating : `★${spot.rating}`;
    const cityClean = (this.lastCity || '').split(',')[0].trim();

    modal.innerHTML = `
      <div class="modal-content" onclick="event.stopPropagation();" style="max-width:460px; padding:1.25rem; border-radius:20px; animation:fadeIn 0.2s ease;">
        <button type="button" class="modal-close" onclick="AITravelEngine.closeSpotModal()" aria-label="Close modal" title="Close">✕</button>
        
        <div>
          ${hasPhoto ? `
            <div style="width:100%; height:190px; overflow:hidden; border-radius:14px; margin-bottom:0.85rem; background:#FAF7F2; position:relative;">
              <img src="${spot.image}" alt="${escapeHtml(activeName)}" onerror="this.onerror=null; AITravelEngine.handleImageError(this, '${escapeHtml(spot.category)}', '${escapeHtml(cleanRating)}', '${escapeHtml(activeCat)}');" style="width:100%; height:100%; object-fit:cover; display:block;">
              <span style="position:absolute; top:8px; left:8px; font-size:0.68rem; font-weight:800; background:rgba(255,255,255,0.92); color:#0369A1; padding:0.15rem 0.45rem; border-radius:4px; border:1px solid #0284C7;">🌐 Wikipedia</span>
              <span style="position:absolute; top:8px; right:8px; font-size:0.8rem; font-weight:800; background:rgba(255,255,255,0.92); color:#047857; padding:0.2rem 0.55rem; border-radius:6px; border:1px solid #047857;">${cleanRating}</span>
            </div>
          ` : `
            <div style="width:100%; height:90px; border-radius:14px; margin-bottom:0.85rem; background:linear-gradient(135deg, #FEF3C7, #E0E7FF); border:1.5px solid var(--border-ink); display:flex; align-items:center; justify-content:space-between; padding:0.85rem 1.1rem;">
              <div style="display:flex; align-items:center; gap:0.5rem;">
                <span style="font-size:1.6rem;">${getCategoryIcon(spot.category)}</span>
                <div>
                  <div style="font-weight:800; font-size:0.9rem; color:var(--primary-wood);">${escapeHtml(activeCat)}</div>
                  <div style="font-size:0.72rem; color:var(--text-secondary);">Verified Google Maps Venue</div>
                </div>
              </div>
              <span style="font-size:0.8rem; font-weight:800; background:#FFF; color:#047857; padding:0.2rem 0.55rem; border-radius:6px; border:1px solid #047857;">${cleanRating}</span>
            </div>
          `}

          <div style="display:flex; align-items:center; gap:0.35rem; flex-wrap:wrap; margin-bottom:0.5rem;">
            <span style="font-size:0.75rem; font-weight:700; background:rgba(56,189,248,0.2); color:#38BDF8; padding:0.15rem 0.55rem; border-radius:6px; border:1px solid rgba(56,189,248,0.4);">${activeCat}</span>
            <span style="font-size:0.72rem; font-weight:700; background:rgba(245,158,11,0.2); color:#FCD34D; padding:0.15rem 0.45rem; border-radius:6px; border:1px solid rgba(245,158,11,0.4);">
              ${activeZone}
            </span>
            ${spot.kids ? `<span style="font-size:0.72rem; font-weight:800; background:rgba(244,114,182,0.2); color:#F472B6; padding:0.15rem 0.45rem; border-radius:6px; border:1px solid rgba(244,114,182,0.4);">🧸 Kids</span>` : ''}
            ${spot.rain ? `<span style="font-size:0.72rem; font-weight:800; background:rgba(56,189,248,0.2); color:#38BDF8; padding:0.15rem 0.45rem; border-radius:6px; border:1px solid rgba(56,189,248,0.4);">☔ Rain</span>` : ''}
            ${spot.shopping ? `<span style="font-size:0.72rem; font-weight:800; background:rgba(251,191,36,0.2); color:#FBBF24; padding:0.15rem 0.45rem; border-radius:6px; border:1px solid rgba(251,191,36,0.4);">🛍️ Shop</span>` : ''}
            ${spot.free ? `<span style="font-size:0.72rem; font-weight:800; background:rgba(16,185,129,0.2); color:#34D399; padding:0.15rem 0.45rem; border-radius:6px; border:1px solid rgba(16,185,129,0.4);">🆓 Free</span>` : ''}
          </div>

          <h3 style="font-size:1.2rem; margin-bottom:0.4rem; font-family:var(--font-sans); color:var(--text-primary); word-break:break-word;">
            ${escapeHtml(activeName)}
          </h3>

          <p style="font-size:0.9rem; color:var(--text-secondary); line-height:1.55; margin-bottom:0.85rem; word-break:break-word;">
            ${escapeHtml(activeDesc)}
          </p>

          ${activeTip ? `
            <div style="background:#FFFBEB; border:1.5px solid #FCD34D; padding:0.65rem 0.85rem; border-radius:10px; font-size:0.82rem; color:#92400E; margin-bottom:1rem; line-height:1.45;">
              <strong style="display:block; margin-bottom:0.2rem; color:#78350F;">${window.I18nEngine ? window.I18nEngine.getText('modal.insiderTip') : '💡 Insider Tip:'}</strong>
              ${escapeHtml(activeTip)}
            </div>
          ` : ''}

          <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.85rem; border-top:1px dashed #EADEC9; padding-top:0.75rem; margin-top:0.5rem; flex-wrap:wrap; gap:0.5rem;">
            <span style="font-weight:700; color:var(--primary-wood);">${escapeHtml(activePrice)}</span>
            ${this.createMapsLink(spot.name.split(' (')[0], cityClean, false)}
          </div>
        </div>
      </div>
    `;

    modal.classList.add('active');
    // Hide floating CTA bar while modal is open to avoid z-index overlap
    const floatingBar = document.getElementById('floatingCtaBar');
    if (floatingBar) floatingBar.style.display = 'none';
  },

  closeSpotModal(event) {
    if (event && event.target && !event.target.classList.contains('modal-overlay') && !event.target.classList.contains('modal-close')) {
      return;
    }
    const modal = document.getElementById('spotDetailModal');
    if (modal) {
      modal.classList.remove('active');
    }
    // Restore floating CTA bar visibility
    const floatingBar = document.getElementById('floatingCtaBar');
    if (floatingBar) floatingBar.style.display = '';
  },

  formatCompactPrice(priceStr) {
    if (!priceStr) return '';
    const lang = window.I18nEngine ? window.I18nEngine.currentLang : 'en';
    const p = String(priceStr).trim();
    if (p.toLowerCase().includes('free') || p.includes('無料') || p.includes('gratuit') || p.includes('gratis') || p.includes('免费')) {
      return lang === 'ja' ? '無料' : lang === 'es' ? 'Gratis' : lang === 'zh' ? '免费' : lang === 'fr' ? 'Gratuit' : lang === 'de' ? 'Kostenlos' : 'Free';
    }
    const match = p.match(/€\s*\d+([.,]\d+)?/);
    if (match) return match[0].replace(/\s+/, '');
    return p.length > 10 ? p.substring(0, 10) : p;
  },

  setCategoryFilter(category) {
    if (category === 'ALL' || category === 'Top7' || category === 'HiddenGem') {
      this.activePreset = category;
    } else if (['Landmark', 'Museum', 'Café', 'Scenery'].includes(category)) {
      this.activeGenre = (this.activeGenre === category) ? 'ALL' : category;
    } else if (['Kids', 'Rain', 'Free'].includes(category)) {
      this.toggleConditionFilter(category);
      return;
    }
    this.renderCandidateSpots();
  },

  // Step 2: Render Interactive Candidate Spots (Max Cap: 8)
  renderCandidateSpots() {
    console.log('🚀 [0MT ENGINE v130] Rendering 3-Row Filter System...');
    try {
      const selectElem = document.getElementById('aiPlanDestination');
      const city = selectElem ? selectElem.value : 'Okinawa, Japan';
      const areaElem = document.getElementById('aiPlanAreaZone');
      const targetArea = areaElem ? areaElem.value : 'ALL';

      if (this.lastCity && this.lastCity !== city) {
        this.selectedMustVisitIds.clear();
      }
      this.lastCity = city;

      const maxCap = 8;

      let spots = candidateSpotsDatabase[city];
      if (!spots || spots.length === 0) {
        const cleanCityName = city.split(',')[0].trim().toLowerCase();
        for (const k in candidateSpotsDatabase) {
          if (k.toLowerCase().includes(cleanCityName)) {
            spots = candidateSpotsDatabase[k];
            break;
          }
        }
      }
      const container = document.getElementById('candidateSpotsGrid');
      const counterBadge = document.getElementById('spotsCounterBadge');

      if (!spots || spots.length === 0) {
        if (container) {
          container.innerHTML = `<div style="grid-column:1/-1; padding:2rem; text-align:center; color:#F87171; font-weight:700;">⚠️ No spot data found for "${escapeHtml(city)}". Please select a different city.</div>`;
        }
        return;
      }

      if (!container) return;

      // 1. Filter by Area Zone (Step 1 dropdown: ALL / city / suburban)
      let areaSpots = spots;
      if (targetArea && targetArea !== 'ALL') {
        areaSpots = spots.filter(s => (s.locationZone || 'city') === targetArea);
      }

      // 2. Multilingual 3-Layer Filter System & Real-Time Dynamic Counts
      const preset = this.activePreset || 'ALL';
      const category = this.activeGenre || 'ALL';
      const conds = this.activeConditions || new Set();

      let filteredSpots = areaSpots.filter(s => this.isSpotMatchingFilter(s, preset, category, conds));

      if (!filteredSpots) {
        filteredSpots = areaSpots;
      }

      const t = (k) => window.I18nEngine ? window.I18nEngine.getText(k) : k;

      if (counterBadge) {
        const selectedCount = this.selectedMustVisitIds.size;
        counterBadge.innerHTML = `${t('badge.selected')} <strong>${selectedCount} / 8</strong> ${t('badge.maxNotice')}`;
        counterBadge.style.color = selectedCount >= 8 ? '#C2410C' : '#047857';
      }

      // Real-time Dynamic Count Calculations across 3 layers
      const getPresetCount = (p) => areaSpots.filter(s => this.isSpotMatchingFilter(s, p, category, conds)).length;
      const getCategoryCount = (c) => areaSpots.filter(s => this.isSpotMatchingFilter(s, preset, c, conds)).length;
      const getCondCount = (condName) => {
        const testConds = new Set(conds);
        if (!testConds.has(condName)) testConds.add(condName);
        return areaSpots.filter(s => this.isSpotMatchingFilter(s, preset, category, testConds)).length;
      };

      const categoryFilterBarHtml = `
        <div class="category-filter-box" style="grid-column:1 / -1; width:100%; display:flex; flex-direction:column; gap:0.6rem; margin-bottom:1.1rem; background:#FAF7F2; border:2px solid var(--border-ink, #292524); padding:0.85rem 1rem; border-radius:16px; box-shadow:3px 3px 0px var(--border-ink, #292524);">
          
          <!-- Layer 1: Scope (Exclusive Radio: ALL, Top 7, Hidden Gems, Night Spots) -->
          <div class="filter-row" style="display:flex; align-items:center; gap:0.5rem; flex-wrap:wrap;">
            <span class="filter-group-label" style="font-size:0.8rem; font-weight:800; color:var(--primary-forest, #047857); min-width:145px; font-family:var(--font-sans);">
              ${t('filter.layer1')}
            </span>
            <div style="display:flex; gap:0.4rem; flex-wrap:wrap; flex:1;">
              <button type="button" class="filter-chip ${preset === 'ALL' ? 'active' : ''}" onclick="AITravelEngine.setPresetFilter('ALL')">
                ${t('filter.allPreset')} (${getPresetCount('ALL')})
              </button>
              <button type="button" class="filter-chip ${preset === 'Top7' ? 'active' : ''}" onclick="AITravelEngine.setPresetFilter('Top7')" style="background:${preset === 'Top7' ? '#047857' : '#ECFDF5'}; color:${preset === 'Top7' ? '#FFF' : '#047857'}; border-color:#A7F3D0; font-weight:800;">
                ${t('filter.top7')} (${getPresetCount('Top7')})
              </button>
              <button type="button" class="filter-chip ${preset === 'HiddenGem' ? 'active' : ''}" onclick="AITravelEngine.setPresetFilter('HiddenGem')" style="background:${preset === 'HiddenGem' ? '#7E22CE' : '#F3E8FF'}; color:${preset === 'HiddenGem' ? '#FFF' : '#7E22CE'}; border-color:#D8B4FE; font-weight:800;">
                ${t('filter.hiddenGems')} (${getPresetCount('HiddenGem')})
              </button>
              <button type="button" class="filter-chip ${preset === 'Night' ? 'active' : ''}" onclick="AITravelEngine.setPresetFilter('Night')" style="background:${preset === 'Night' ? '#1E1B4B' : '#EEF2FF'}; color:${preset === 'Night' ? '#FFF' : '#312E81'}; border-color:#C7D2FE; font-weight:800;">
                ${t('filter.nightPreset')} (${getPresetCount('Night')})
              </button>
            </div>
          </div>

          <!-- Layer 2: Categories (Single Select Pill matching Pure Venue Genres) -->
          <div class="filter-row" style="display:flex; align-items:center; gap:0.5rem; flex-wrap:wrap; border-top:1px dashed #CBD5E1; padding-top:0.5rem;">
            <span class="filter-group-label" style="font-size:0.8rem; font-weight:800; color:var(--primary-forest, #047857); min-width:145px; font-family:var(--font-sans);">
              ${t('filter.layer2')}
            </span>
            <div style="display:flex; gap:0.4rem; flex-wrap:wrap; flex:1;">
              <button type="button" class="filter-chip ${category === 'ALL' ? 'active' : ''}" onclick="AITravelEngine.toggleGenreFilter('ALL')">
                ${t('filter.catAll')} (${getCategoryCount('ALL')})
              </button>
              <button type="button" class="filter-chip ${category === 'Landmark' ? 'active' : ''}" onclick="AITravelEngine.toggleGenreFilter('Landmark')">
                ${t('filter.landmark')} (${getCategoryCount('Landmark')})
              </button>
              <button type="button" class="filter-chip ${category === 'Museum' ? 'active' : ''}" onclick="AITravelEngine.toggleGenreFilter('Museum')">
                ${t('filter.museum')} (${getCategoryCount('Museum')})
              </button>
              <button type="button" class="filter-chip ${category === 'Café' ? 'active' : ''}" onclick="AITravelEngine.toggleGenreFilter('Café')">
                ${t('filter.cafe')} (${getCategoryCount('Café')})
              </button>
              <button type="button" class="filter-chip ${category === 'Scenery' ? 'active' : ''}" onclick="AITravelEngine.toggleGenreFilter('Scenery')">
                ${t('filter.scenery')} (${getCategoryCount('Scenery')})
              </button>
              <button type="button" class="filter-chip ${category === 'Kids' ? 'active' : ''}" onclick="AITravelEngine.toggleGenreFilter('Kids')">
                ${t('filter.kids')} (${getCategoryCount('Kids')})
              </button>
              <button type="button" class="filter-chip ${category === 'Shopping' ? 'active' : ''}" onclick="AITravelEngine.toggleGenreFilter('Shopping')">
                ${t('filter.shopping')} (${getCategoryCount('Shopping')})
              </button>
            </div>
          </div>

          <!-- Layer 3: Conditions (Horizontal Slide Toggle Switches) -->
          <div class="filter-row" style="display:flex; align-items:center; gap:0.5rem; flex-wrap:wrap; border-top:1px dashed #CBD5E1; padding-top:0.5rem;">
            <span class="filter-group-label" style="font-size:0.8rem; font-weight:800; color:var(--primary-forest, #047857); min-width:145px; font-family:var(--font-sans);">
              ${t('filter.layer3')}
            </span>
            <div style="display:flex; gap:0.6rem; flex-wrap:wrap; flex:1;">
              
              <!-- Rainy Day Toggle Switch -->
              <label class="switch-toggle ${conds.has('Rain') ? 'active' : ''}">
                <input type="checkbox" ${conds.has('Rain') ? 'checked' : ''} onchange="AITravelEngine.toggleConditionFilter('Rain')">
                <span class="switch-track">
                  <span class="switch-thumb"></span>
                </span>
                <span>${t('filter.rain')} (${getCondCount('Rain')})</span>
              </label>

              <!-- Free Entry Toggle Switch -->
              <label class="switch-toggle ${conds.has('Free') ? 'active' : ''}">
                <input type="checkbox" ${conds.has('Free') ? 'checked' : ''} onchange="AITravelEngine.toggleConditionFilter('Free')">
                <span class="switch-track">
                  <span class="switch-thumb"></span>
                </span>
                <span>${t('filter.free')} (${getCondCount('Free')})</span>
              </label>

            </div>
          </div>

        </div>
      `;
const viewModeBarHtml = categoryFilterBarHtml + `
        <div class="view-mode-bar" style="grid-column:1 / -1; width:100%; margin-bottom:0.5rem; background:rgba(15,23,42,0.95); padding:0.75rem 1rem; border-radius:14px; border:2px solid rgba(255,255,255,0.2);">
          <div style="display:flex; align-items:center; gap:0.4rem;">
            <span style="font-size:0.88rem; font-weight:800; color:#FFFFFF;">${t('view.label')}</span>
            <span style="font-size:0.8rem; color:#FCD34D;">(${filteredSpots.length} ${t('view.matching')})</span>
          </div>
          <div style="display:flex; gap:0.4rem; flex-wrap:wrap;">
            <button type="button" class="view-mode-btn ${this.viewMode === 'grid' ? 'active' : ''}" onclick="AITravelEngine.setViewMode('grid')">
              ${t('view.grid')}
            </button>
            <button type="button" class="view-mode-btn ${this.viewMode === 'compact' ? 'active' : ''}" onclick="AITravelEngine.setViewMode('compact')">
              ${t('view.compact')}
            </button>
          </div>
        </div>
      `;

      const activeLang = window.I18nEngine ? window.I18nEngine.currentLang : 'en';

      if (this.viewMode === 'compact') {
        container.style.display = 'flex';
        container.style.flexDirection = 'column';
        container.style.gap = '0.45rem';
        container.style.width = '100%';

        container.innerHTML = viewModeBarHtml + filteredSpots.map(s => {
          const isChecked = this.selectedMustVisitIds.has(s.id);
          const rawRating = String(s.rating || '');
          const cleanRating = rawRating.startsWith('★') ? rawRating : `★${rawRating}`;
          const cardName = this.getLocalizedSpotName(s);
          const cardDesc = this.getLocalizedDesc(s);
          const cardPrice = this.getLocalizedPrice(s);
          const cleanPrice = this.formatCompactPrice(cardPrice);

          return `
            <div class="card spot-candidate-card" style="border:1.5px solid ${isChecked ? '#F59E0B' : 'rgba(255, 255, 255, 0.18)'}; background:${isChecked ? 'rgba(30, 41, 59, 0.95)' : 'rgba(15, 23, 42, 0.88)'}; cursor:pointer; padding:0.45rem 0.55rem; display:flex; align-items:center; justify-content:space-between; gap:0.4rem; border-radius:10px; transition:all 0.15s ease; box-shadow:${isChecked ? '0 0 20px rgba(245, 158, 11, 0.4)' : 'none'}; width:100%; box-sizing:border-box;" onclick="AITravelEngine.toggleSpotSelection('${s.id}', 8)">
              <div style="display:flex; align-items:flex-start; gap:0.45rem; flex:1; min-width:0;">
                <input type="checkbox" id="chk_${s.id}" ${isChecked ? 'checked' : ''} onclick="event.stopPropagation(); AITravelEngine.toggleSpotSelection('${s.id}', 8)" style="width:20px; height:20px; cursor:pointer; accent-color:#F59E0B; flex-shrink:0; margin-top:2px;">
                
                <div style="display:flex; flex-direction:column; justify-content:center; min-width:0; flex:1;">
                  <!-- Line 1: Spot Name (Up to 2 lines wrap) -->
                  <div style="font-weight:800; font-size:0.92rem; color:#FFFFFF; line-height:1.25; word-break:break-word;">
                    ${escapeHtml(cardName)}
                  </div>

                  <!-- Line 2: Description (Up to 3 lines clamped) -->
                  <p style="font-size:0.77rem; color:#CBD5E1; line-height:1.35; margin-top:2px; margin-bottom:0; display:-webkit-box; -webkit-line-clamp:3; -webkit-box-orient:vertical; overflow:hidden; text-overflow:ellipsis;">
                    ${escapeHtml(cardDesc)}
                  </p>
                </div>
              </div>

              <!-- Right Column: Stacked Rating & Budget (Top), Maps Link (Middle), More Button (Bottom) -->
              <div style="flex-shrink:0; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:0.2rem; margin-left:0.25rem; min-width:44px;">
                <div style="display:flex; align-items:center; gap:0.18rem; flex-wrap:nowrap;">
                  ${s.top7 ? '<span style="font-size:0.62rem; font-weight:800; color:#047857; background:#ECFDF5; border:1px solid #A7F3D0; padding:0.05rem 0.3rem; border-radius:4px; white-space:nowrap;">👑 Top 7</span>' : ''}
                  ${s.hiddenGem ? '<span style="font-size:0.62rem; font-weight:800; color:#7E22CE; background:#F3E8FF; border:1px solid #D8B4FE; padding:0.05rem 0.3rem; border-radius:4px; white-space:nowrap;">💎 Hidden</span>' : ''}
                  <span style="font-size:0.62rem; font-weight:800; color:#047857; background:#D1FAE5; padding:0.05rem 0.3rem; border-radius:4px; white-space:nowrap;">
                    ${cleanRating}
                  </span>
                  ${cleanPrice ? `
                    <span style="font-size:0.62rem; font-weight:800; color:#78350F; background:#FEF3C7; padding:0.05rem 0.3rem; border-radius:4px; border:1px solid #FDE68A; white-space:nowrap;">
                      ${cleanPrice}
                    </span>
                  ` : ''}
                </div>

                ${this.createMapsLink(s.name.split(' (')[0], city.split(',')[0], true)}

                <button type="button" onclick="event.stopPropagation(); AITravelEngine.openSpotModal('${s.id}')" onpointerdown="event.stopPropagation(); AITravelEngine.openSpotModal('${s.id}')" style="display:inline-flex; align-items:center; justify-content:center; background:#EFF6FF; color:#0369A1; border:1px solid #BAE6FD; padding:0.12rem 0.35rem; border-radius:4px; font-weight:800; font-size:0.62rem; cursor:pointer; white-space:nowrap; -webkit-tap-highlight-color:transparent;" title="View photo & details">
                  ${t('btn.viewDetails')}
                </button>
              </div>
            </div>
          `;
        }).join('');
      } else {
        container.style.display = 'grid';
        container.style.flexDirection = 'initial';
        container.style.gap = '1.25rem';
        container.style.width = '100%';

        container.innerHTML = viewModeBarHtml + filteredSpots.map(s => {
          const isChecked = this.selectedMustVisitIds.has(s.id);
          const hasPhoto = Boolean(s.image);
          const cardName = this.getLocalizedSpotName(s);
          const cardDesc = this.getLocalizedDesc(s);
          const cardPrice = this.getLocalizedPrice(s);
          const cardCat = this.getLocalizedCategory(s);
          const cardZone = this.getLocalizedZone(s.locationZone);

          return `
            <div class="card spot-candidate-card" style="border:1.5px solid ${isChecked ? '#F59E0B' : 'rgba(255, 255, 255, 0.18)'}; background:${isChecked ? 'rgba(30, 41, 59, 0.95)' : 'rgba(15, 23, 42, 0.88)'}; cursor:pointer; transition:all 0.2s ease; display:flex; flex-direction:column; justify-content:space-between; position:relative; box-shadow:${isChecked ? '0 0 20px rgba(245, 158, 11, 0.45)' : 'none'}; width:100%; box-sizing:border-box;" onclick="AITravelEngine.toggleSpotSelection('${s.id}', 8)">
              ${isChecked ? `
                <div style="position:absolute; top:-10px; left:-10px; background:#F59E0B; color:#0F172A; font-weight:800; font-size:0.75rem; padding:0.25rem 0.65rem; border-radius:999px; border:2px solid #FFF; box-shadow:0 0 10px rgba(245,158,11,0.5); z-index:10;">
                  ✓ ${t('badge.mustVisit')}
                </div>
              ` : ''}

              <div>
                ${hasPhoto ? `
                  <div style="width:100%; height:140px; overflow:hidden; border-radius:12px; margin-bottom:0.75rem; background:#0F172A; position:relative;">
                    <img src="${s.image}" alt="${escapeHtml(cardName)}" loading="lazy" decoding="async" onerror="this.onerror=null; AITravelEngine.handleImageError(this, '${escapeHtml(s.category)}', '${escapeHtml(s.rating)}', '${escapeHtml(cardCat)}');" style="width:100%; height:100%; object-fit:cover; display:block;">
                    <span style="position:absolute; top:8px; left:8px; font-size:0.68rem; font-weight:800; background:rgba(15,23,42,0.85); color:#38BDF8; padding:0.15rem 0.45rem; border-radius:4px; border:1px solid rgba(56,189,248,0.4); box-shadow:0 2px 4px rgba(0,0,0,0.3);">🌐 Wikipedia</span>
                    <span style="position:absolute; top:8px; right:8px; font-size:0.75rem; font-weight:800; background:rgba(15,23,42,0.85); color:#34D399; padding:0.2rem 0.55rem; border-radius:6px; border:1px solid rgba(16,185,129,0.4); box-shadow:0 2px 4px rgba(0,0,0,0.3);">${s.rating}</span>
                  </div>
                ` : `
                  <div style="width:100%; height:76px; border-radius:12px; margin-bottom:0.75rem; background:linear-gradient(135deg, rgba(245,158,11,0.2), rgba(99,102,241,0.2)); border:1px solid rgba(255,255,255,0.18); display:flex; align-items:center; justify-content:space-between; padding:0.75rem 1rem; position:relative;">
                    <div style="display:flex; align-items:center; gap:0.5rem;">
                      <span style="font-size:1.5rem;">${getCategoryIcon(s.category)}</span>
                      <div>
                        <div style="font-weight:800; font-size:0.85rem; color:#FCD34D;">${escapeHtml(cardCat)}</div>
                        <div style="font-size:0.72rem; color:#94A3B8;">Verified Google Maps Venue</div>
                      </div>
                    </div>
                    <span style="font-size:0.75rem; font-weight:800; background:rgba(15,23,42,0.85); color:#34D399; padding:0.2rem 0.55rem; border-radius:6px; border:1px solid rgba(16,185,129,0.4);">${s.rating}</span>
                  </div>
                `}

                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.4rem; flex-wrap:wrap; gap:0.3rem;">
                  <div style="display:flex; align-items:center; gap:0.3rem; flex-wrap:wrap;">
                    <span style="font-size:0.75rem; font-weight:700; background:rgba(56,189,248,0.2); color:#38BDF8; padding:0.15rem 0.55rem; border-radius:6px; border:1px solid rgba(56,189,248,0.4);">${cardCat}</span>
                    <span style="font-size:0.72rem; font-weight:700; background:rgba(245,158,11,0.2); color:#FCD34D; padding:0.15rem 0.45rem; border-radius:6px; border:1px solid rgba(245,158,11,0.4);">
                      ${cardZone}
                    </span>
                    ${s.kids ? `<span style="font-size:0.72rem; font-weight:800; background:rgba(244,114,182,0.2); color:#F472B6; padding:0.15rem 0.45rem; border-radius:6px; border:1px solid rgba(244,114,182,0.4);">🧸 Kids</span>` : ''}
                    ${s.rain ? `<span style="font-size:0.72rem; font-weight:800; background:rgba(56,189,248,0.2); color:#38BDF8; padding:0.15rem 0.45rem; border-radius:6px; border:1px solid rgba(56,189,248,0.4);">☔ Rain</span>` : ''}
                    ${s.shopping ? `<span style="font-size:0.72rem; font-weight:800; background:rgba(251,191,36,0.2); color:#FBBF24; padding:0.15rem 0.45rem; border-radius:6px; border:1px solid rgba(251,191,36,0.4);">🛍️ Shop</span>` : ''}
                    ${s.free ? `<span style="font-size:0.72rem; font-weight:800; background:rgba(16,185,129,0.2); color:#34D399; padding:0.15rem 0.45rem; border-radius:6px; border:1px solid rgba(16,185,129,0.4);">🆓 Free</span>` : ''}
                  </div>
                </div>

                <h4 style="font-size:1.05rem; margin-bottom:0.35rem; font-family:var(--font-sans); color:var(--text-primary); display:flex; align-items:center; gap:0.5rem; word-break:break-word;">
                  <input type="checkbox" id="chk_${s.id}" ${isChecked ? 'checked' : ''} onclick="event.stopPropagation(); AITravelEngine.toggleSpotSelection('${s.id}', 8)" style="width:20px; height:20px; cursor:pointer; accent-color:#047857; flex-shrink:0;">
                  <span>${escapeHtml(cardName)}</span>
                </h4>

                <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5; margin-bottom:0.75rem; word-break:break-word;">${escapeHtml(cardDesc)}</p>
              </div>

              <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.8rem; border-top:1px dashed #EADEC9; padding-top:0.5rem; margin-top:auto; gap:0.4rem; flex-wrap:wrap;">
                <span style="font-weight:700; color:var(--primary-wood);">${escapeHtml(cardPrice)}</span>
                <div style="display:flex; align-items:center; gap:0.4rem;">
                  <button type="button" onclick="event.stopPropagation(); AITravelEngine.openSpotModal('${s.id}')" onpointerdown="event.stopPropagation(); AITravelEngine.openSpotModal('${s.id}')" style="display:inline-flex; align-items:center; justify-content:center; gap:0.25rem; background:#FFFBEB; color:#92400E; border:1.5px solid #FCD34D; padding:0.25rem 0.55rem; border-radius:6px; font-weight:700; font-size:0.8rem; cursor:pointer; white-space:nowrap; -webkit-tap-highlight-color:transparent;" title="View Insider Tip & Details">
                    💡 Insider Tip
                  </button>
                  ${this.createMapsLink(s.name.split(' (')[0], city.split(',')[0])}
                </div>
              </div>
            </div>
          `;
        }).join('');
      }
    } catch (err) {
      console.error('Error in renderCandidateSpots:', err);
    }
  },

  toggleSpotSelection(spotId, maxCap = 8) {
    if (this.selectedMustVisitIds.has(spotId)) {
      this.selectedMustVisitIds.delete(spotId);
    } else {
      if (this.selectedMustVisitIds.size >= maxCap) {
        alert(`Selection Limit Reached! You can select up to ${maxCap} Must-Visit spots.`);
        return;
      }
      this.selectedMustVisitIds.add(spotId);
    }
    this.renderCandidateSpots();
    this.updateFloatingCtaBar();
  },

  updateFloatingCtaBar() {
    const bar = document.getElementById('floatingCtaBar');
    const text = document.getElementById('floatingCtaText');
    const fixedText = document.getElementById('fixedCtaText');
    const fixedContainer = document.getElementById('step3FixedContainer');

    if (!this.ctaObserverSetup && fixedContainer) {
      this.ctaObserverSetup = true;
      const observer = new IntersectionObserver((entries) => {
        const entry = entries[0];
        // Hide if the fixed CTA is in view OR if we have scrolled past it (top < 0)
        this.isFixedCtaVisible = entry.isIntersecting || entry.boundingClientRect.top < 0;
        this.updateFloatingCtaBar();
      }, { threshold: 0.1 });
      observer.observe(fixedContainer);
    }

    if (!bar || !text) return;
    const count = this.selectedMustVisitIds.size;
    if (count > 0) {
      const lang = window.I18nEngine ? window.I18nEngine.currentLang : 'en';
      const ctaMsgMap = {
        'ja': `そのまま使えるGoogle MapsルートA＆Bを自動生成 (${count}/8件) ↗`,
        'nl': `Genereer Direct Te Gebruiken Google Maps Routen (${count}/8) ↗`,
        'fr': `Générer les Itinéraires Google Maps Prêts à l'Emploi (${count}/8) ↗`,
        'de': `Einsatzbereite Google Maps Routen Generieren (${count}/8) ↗`,
        'es': `Generar Rutas Listas para Usar en Google Maps (${count}/8) ↗`,
        'zh': `自动生成包含路线A与B的Google Maps导航 (${count}/8) ↗`,
        'en': `Generate Ready-to-Use Dual Maps Routes (${count}/8 Selected) ↗`
      };
      const ctaMsg = ctaMsgMap[lang] || ctaMsgMap['en'];
      text.innerText = ctaMsg;
      if (fixedText) {
        fixedText.innerText = ctaMsg;
      }
      
      if (this.isFixedCtaVisible) {
        bar.classList.remove('active');
      } else {
        bar.classList.add('active');
      }
    } else {
      bar.classList.remove('active');
    }
  },

  // Calculate Haversine distance in km between two lat/lng coordinates
  calculateDistance(lat1, lng1, lat2, lng2) {
    if (!lat1 || !lng1 || !lat2 || !lng2) return 0;
    const R = 6371; // Earth radius in km
    const dLat = (lat2 - lat1) * Math.PI / 180;
    const dLng = (lng2 - lng1) * Math.PI / 180;
    const a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
              Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
              Math.sin(dLng / 2) * Math.sin(dLng / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    return R * c;
  },

  // Assign time-of-day category slots (1: Morning/Museum, 2: Afternoon Tea, 3: Evening Dinner, 4: Night Walk)
  getCategoryTimeSlot(spot) {
    const cat = String(spot.category || '').toLowerCase();
    const name = String(spot.name || '').toLowerCase();

    // Slot 4: Nightfall & Open Air Walk (River cruises, bridges, illuminated plazas, 24/7 night scenery)
    if (cat.includes('scenery') || cat.includes('walk') || name.includes('cruise') || name.includes('seine') || name.includes('river') || name.includes('bridge') || name.includes('night') || name.includes('plaza')) {
      return 4;
    }

    // Slot 3: Evening Dining (Restaurants, Bistros, Bars, Dinner)
    if (cat.includes('bistro') || cat.includes('restaurant') || cat.includes('dining')) {
      return 3;
    }

    // Slot 2: Afternoon Break & Tea Time (Cafés, Bakeries, Tea Rooms, Parks, Gardens)
    if (cat.includes('café') || cat.includes('cafe') || cat.includes('bakery') || cat.includes('park') || cat.includes('garden')) {
      return 2;
    }

    // Slot 1: Morning & Early Afternoon (Museums, Palaces, Cathedrals, Indoor Landmarks - close around 17:00-18:00)
    return 1;
  },

  // Optimize spot sequence combining Daily Travel Rhythm, Time-of-Day Slots & Geographical Proximity
  optimizeRouteOrder(spots) {
    if (!spots || spots.length <= 1) return spots;

    const list = spots.map(s => ({
      ...s,
      timeSlot: this.getCategoryTimeSlot(s)
    }));

    // Group spots into time-of-day buckets (1: Morning/Afternoon Sightseeing, 2: Cafe/Lunch, 3: Dinner, 4: Night Walk)
    const slot1 = list.filter(s => s.timeSlot === 1);
    const slot2 = list.filter(s => s.timeSlot === 2);
    const slot3 = list.filter(s => s.timeSlot === 3);
    const slot4 = list.filter(s => s.timeSlot === 4);

    // Sub-sort each time bucket by nearest-neighbor geographical distance
    const sortBucketByProximity = (bucket, lastSpot = null) => {
      if (!bucket || bucket.length === 0) return [];
      if (bucket.length === 1) return [...bucket];
      
      const unvisited = [...bucket];
      const sorted = [];

      let current = lastSpot;
      if (!current) {
        // Find westernmost spot in bucket as initial anchor
        let minLng = Infinity;
        let startIdx = 0;
        unvisited.forEach((s, idx) => {
          const lng = Number(s.lng || 0);
          if (lng && lng < minLng) {
            minLng = lng;
            startIdx = idx;
          }
        });
        current = unvisited[startIdx];
        sorted.push(current);
        unvisited.splice(startIdx, 1);
      }

      while (unvisited.length > 0) {
        let nearestIdx = 0;
        let minDistance = Infinity;

        unvisited.forEach((spot, idx) => {
          const dist = this.calculateDistance(current.lat, current.lng, spot.lat, spot.lng);
          if (dist < minDistance) {
            minDistance = dist;
            nearestIdx = idx;
          }
        });

        current = unvisited[nearestIdx];
        sorted.push(current);
        unvisited.splice(nearestIdx, 1);
      }

      return sorted;
    };

    // To prevent consecutive Cafe -> Dinner, split Sightseeing (slot1) into Morning and Afternoon groups!
    let slot1_morning = [];
    let slot1_afternoon = [];

    if (slot1.length > 2 && slot2.length > 0) {
      // Interleave Cafe in the middle of sightseeing (e.g. 2-3 morning sights, Cafe/Lunch, then 2-3 afternoon sights)
      const midPoint = Math.ceil(slot1.length / 2);
      slot1_morning = slot1.slice(0, midPoint);
      slot1_afternoon = slot1.slice(midPoint);
    } else {
      slot1_morning = slot1;
    }

    // 1. Morning Sightseeing (10:00–13:30)
    const sorted1_m = sortBucketByProximity(slot1_morning);
    const last1_m = sorted1_m.length > 0 ? sorted1_m[sorted1_m.length - 1] : null;

    // 2. Mid-Day Cafe & Lunch Break (13:30–15:30)
    const sorted2 = sortBucketByProximity(slot2, last1_m);
    const last2 = sorted2.length > 0 ? sorted2[sorted2.length - 1] : (last1_m || null);

    // 3. Late-Afternoon Sightseeing (15:30–18:00)
    const sorted1_a = sortBucketByProximity(slot1_afternoon, last2);
    const last1_a = sorted1_a.length > 0 ? sorted1_a[sorted1_a.length - 1] : (last2 || null);

    // 4. Evening Dinner (18:30–20:30)
    const sorted3 = sortBucketByProximity(slot3, last1_a);
    const last3 = sorted3.length > 0 ? sorted3[sorted3.length - 1] : (last1_a || null);

    // 5. Night Scenery / Evening Walk (20:00 onwards)
    const sorted4 = sortBucketByProximity(slot4, last3);

    return [...sorted1_m, ...sorted2, ...sorted1_a, ...sorted3, ...sorted4];
  },

  // Step 3: Generate Custom Dual Routes with Geographical & Time-of-Day Flow Optimization
  generateItinerary(event) {
    if (event) event.preventDefault();

    const destElem = document.getElementById('aiPlanDestination');
    const destination = destElem ? destElem.value.trim() : 'Okinawa, Japan';
    const areaElem = document.getElementById('aiPlanAreaZone');
    const areaZone = areaElem ? areaElem.value : 'ALL';
    const transportMode = 'transit';

    const resultContainer = document.getElementById('aiPlanResult');
    if (!resultContainer) return;

    // Look up spots for selected destination — never fall back silently
    let allSpots = candidateSpotsDatabase[destination];
    if (!allSpots || allSpots.length === 0) {
      // Try fuzzy match
      const cleanDest = destination.split(',')[0].trim().toLowerCase();
      for (const k in candidateSpotsDatabase) {
        if (k.toLowerCase().includes(cleanDest)) {
          allSpots = candidateSpotsDatabase[k];
          break;
        }
      }
    }
    if (!allSpots || allSpots.length === 0) {
      if (resultContainer) {
        const t = (key) => window.I18nEngine ? window.I18nEngine.getText(key) : key;
        resultContainer.innerHTML = `<div style="padding:2rem; text-align:center; color:#F87171; font-weight:700; background:rgba(15,23,42,0.9); border:1.5px solid #F87171; border-radius:16px; margin-top:1rem;">⚠️ No spot data found for "${escapeHtml(destination)}". Please select a city from the dropdown above.</div>`;
      }
      return;
    }
    const selectedIds = new Set(this.selectedMustVisitIds);
    
    // Extract checked must-visit spots
    let checkedSpots = allSpots.filter(s => selectedIds.has(s.id));
    const selectedCount = checkedSpots.length;
    if (checkedSpots.length === 0) {
      checkedSpots = allSpots.slice(0, 3);
    }

    // 1. ROUTE A: Geographically & Time-of-Day optimized order for selected spots
    const optimizedSpotsA = this.optimizeRouteOrder(checkedSpots);
    this.routeA_spots = optimizedSpotsA.map(s => ({
      ...s,
      isMustVisit: true
    }));

    // 2. ROUTE B: Smart Interleaved 10-Spot AI Course (Guaranteeing Cafés, Bistros & Sights)
    const unselectedSpots = allSpots.filter(s => !selectedIds.has(s.id) && s.category !== 'Hotel & Stay');
    const chosenExtras = [];

    // Helper to check if a category slot is already present in a spots list
    const hasTimeSlot = (spotsList, slotNum) => spotsList.some(s => this.getCategoryTimeSlot(s) === slotNum);

    // AI Recommendation Guarantee 1: Afternoon Café / Bakery (Slot 2: 14:30〜16:30)
    if (!hasTimeSlot(checkedSpots, 2)) {
      const bestCafe = unselectedSpots.find(s => this.getCategoryTimeSlot(s) === 2);
      if (bestCafe) {
        chosenExtras.push(bestCafe);
      }
    }

    // AI Recommendation Guarantee 2: Evening Bistro / Dinner (Slot 3: 17:30〜20:30)
    if (!hasTimeSlot(checkedSpots, 3)) {
      const chosenIds = new Set(chosenExtras.map(s => s.id));
      const bestDinner = unselectedSpots.find(s => this.getCategoryTimeSlot(s) === 3 && !chosenIds.has(s.id));
      if (bestDinner) {
        chosenExtras.push(bestDinner);
      }
    }

    // AI Recommendation Guarantee 3: Night Scenery / Walk (Slot 4: 20:00以降)
    if (!hasTimeSlot(checkedSpots, 4)) {
      const chosenIds = new Set(chosenExtras.map(s => s.id));
      const bestNight = unselectedSpots.find(s => this.getCategoryTimeSlot(s) === 4 && !chosenIds.has(s.id));
      if (bestNight) {
        chosenExtras.push(bestNight);
      }
    }

    // Fill remaining extra slots up to target (9 sightseeing/dining spots)
    const targetBCount = 9;
    const currentCount = checkedSpots.length + chosenExtras.length;
    const neededRemaining = Math.max(0, targetBCount - currentCount);

    if (neededRemaining > 0) {
      const chosenIds = new Set(chosenExtras.map(s => s.id));
      const remainingCandidates = unselectedSpots.filter(s => !chosenIds.has(s.id));
      chosenExtras.push(...remainingCandidates.slice(0, neededRemaining));
    }

    // Combine checked spots + AI recommended spots
    const combinedSpotsB = [...checkedSpots, ...chosenExtras];

    // Geographically & Time-of-Day optimize ALL spots together into a single continuous, seamless travel flow (導線)
    const optimizedSpotsB = this.optimizeRouteOrder(combinedSpotsB);
    this.routeB_spots = optimizedSpotsB.map(s => ({
      ...s,
      isMustVisit: selectedIds.has(s.id)
    }));

    // 3. Hotel Return Destination: Append ONLY if custom hotel input is provided by the user (Applicable to BOTH Route A and Route B)
    const hotelInputElem = document.getElementById('aiPlanHotelInput');
    const customHotelName = hotelInputElem ? hotelInputElem.value.trim() : '';

    if (customHotelName) {
      const returnHotelObj = {
        id: 'user_hotel_custom',
        name: customHotelName.endsWith('(Hotel)') ? customHotelName : `${customHotelName} (Hotel)`,
        category: 'Hotel & Stay',
        rating: '★Stay',
        price: 'Return Hotel',
        lat: allSpots[0] ? allSpots[0].lat : 48.8566,
        lng: allSpots[0] ? allSpots[0].lng : 2.3522,
        isHotel: true,
        isMustVisit: false
      };

      // Append custom Return Hotel as final destination for BOTH Route A and Route B
      this.routeA_spots.push(returnHotelObj);
      this.routeB_spots.push(returnHotelObj);
    }

    this.renderDualRouteManager(destination, {
      trackGeneration: true,
      selectedCount
    });
  },

  renderDualRouteManager(destination, analytics = {}) {
    const resultContainer = document.getElementById('aiPlanResult');
    if (!resultContainer) return;

    resultContainer.style.display = 'block';

    const cityClean = destination.split(',')[0].trim();
    const t = (k) => window.I18nEngine ? window.I18nEngine.getText(k) : k;

    // Generate Route A Google Maps URL
    const namesA = this.routeA_spots.map(s => s.name);
    const mapsUrlA = this.buildMasterGoogleMapsPath(namesA, destination);

    // Generate Route B Google Maps URL
    const namesB = this.routeB_spots.map(s => s.name);
    const mapsUrlB = this.buildMasterGoogleMapsPath(namesB, destination);

    resultContainer.innerHTML = `
      <div style="background:var(--bg-card-warm); border:2.5px solid var(--border-ink); border-radius:22px; padding:2rem; margin-top:1.5rem; box-shadow:var(--shadow-sketch); animation:fadeIn 0.3s ease;">
        
        <div style="text-align:center; max-width:700px; margin:0 auto 1.5rem;">
          <span class="paper-tape">${t('route.tape')}</span>
          <h3 style="font-size:1.8rem; margin-top:0.4rem; font-family:var(--font-serif);">
            ${escapeHtml(destination)} — ${t('route.title')}
          </h3>
          <p style="font-size:0.9rem; color:var(--text-secondary);">
            ${t('route.sub')}
          </p>
        </div>

        <!-- Bookmark Pre-Map Reminder -->
        <div style="background: linear-gradient(135deg, #4F46E5, #2563EB); color:#FFFFFF; padding:1.25rem; border-radius:16px; margin-bottom:1.5rem; display:flex; align-items:center; gap:1rem; text-align:left; box-shadow: 0 4px 15px rgba(37,99,235,0.4); border:2px solid #93C5FD;">
          <div style="font-size:2.2rem; line-height:1; filter:drop-shadow(0 2px 4px rgba(0,0,0,0.3));">💡</div>
          <div>
            <h4 style="margin:0 0 0.4rem 0; font-size:1.15rem; font-weight:800; text-shadow: 0 1px 2px rgba(0,0,0,0.3); color:#EFF6FF;">${t('bookmark.modalTitle')}</h4>
            <p style="margin:0; font-size:0.95rem; font-weight:600; opacity:0.95; color:#DBEAFE;">${t('bookmark.modalText')}</p>
          </div>
        </div>

        <div class="grid-2" style="gap:1.5rem;">
          
          <!-- ROUTE A CARD: Selected Spots Only -->
          <div style="background:#FFF; border:2px solid #047857; border-radius:18px; padding:1.5rem; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 4px 12px rgba(4,120,87,0.1);">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
                <span style="font-size:0.8rem; font-weight:800; background:#D1FAE5; color:#047857; padding:0.25rem 0.65rem; border-radius:999px; border:1px solid #059669;">
                  ${t('routeA.badge')} (${this.routeA_spots.length})
                </span>
              </div>

              <h4 style="font-size:1.15rem; color:#065F46; margin-bottom:0.35rem;" class="font-serif">
                ${t('routeA.title')}
              </h4>
              <p class="route-card-desc" style="margin-bottom:1rem; color:#047857; font-weight:700;">
                ${t('routeA.sub')}
              </p>

              <!-- Reorderable & Deletable Spot Item List A -->
              <div id="routeA_itemList" style="display:flex; flex-direction:column; gap:0.5rem; margin-bottom:1.25rem;">
                ${this.renderSpotItemsHtml(this.routeA_spots, 'A', cityClean)}
              </div>
            </div>

            <div>
              <a href="${mapsUrlA}" target="_blank" rel="noopener noreferrer" id="btn_maps_RouteA" class="btn btn-emerald" style="width:100%; text-align:center; padding:0.85rem; font-size:0.95rem; border-radius:12px; display:inline-block; text-decoration:none;">
                ${t('routeA.btn')} (${this.routeA_spots.length}) ↗
              </a>
            </div>
          </div>

          <!-- ROUTE B CARD: Full 10-Spot Course -->
          <div style="background:#FFF; border:2px solid #B45309; border-radius:18px; padding:1.5rem; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 4px 12px rgba(180,83,9,0.1);">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
                <span style="font-size:0.8rem; font-weight:800; background:#FEF3C7; color:#B45309; padding:0.25rem 0.65rem; border-radius:999px; border:1px solid #D97706;">
                  ${t('routeB.badge')} (${this.routeB_spots.length})
                </span>
              </div>

              <h4 style="font-size:1.15rem; color:#92400E; margin-bottom:0.35rem;" class="font-serif">
                ${t('routeB.title')}
              </h4>
              <p class="route-card-desc" style="margin-bottom:1rem; color:#B45309; font-weight:700;">
                ${t('routeB.sub')}
              </p>

              <!-- Reorderable & Deletable Spot Item List B -->
              <div id="routeB_itemList" style="display:flex; flex-direction:column; gap:0.5rem; margin-bottom:1.25rem;">
                ${this.renderSpotItemsHtml(this.routeB_spots, 'B', cityClean)}
              </div>
            </div>

            <div>
              <a href="${mapsUrlB}" target="_blank" rel="noopener noreferrer" id="btn_maps_RouteB" class="btn btn-primary" style="width:100%; text-align:center; padding:0.85rem; font-size:0.95rem; border-radius:12px; display:inline-block; text-decoration:none;">
                ${t('routeB.btn')} (${this.routeB_spots.length}) ↗
              </a>
            </div>
          </div>

        </div>

      </div>
      
      <!-- Bottom Share UI -->
      <div style="margin-top:2.5rem; padding:1.75rem 1.25rem; background:rgba(15, 23, 42, 0.95); border:1.5px solid #F59E0B; border-radius:20px; text-align:center; box-shadow:0 0 25px rgba(245, 158, 11, 0.25);">
        <h4 style="font-size:1.15rem; color:#FFFFFF; font-weight:800; margin-bottom:0.4rem;" class="font-serif" data-i18n="share.routeTitle">Share this itinerary</h4>
        <p style="font-size:0.88rem; color:#CBD5E1; margin-bottom:1.1rem;">Send this custom route directly to your travel partners</p>
        
        <div style="display:flex; gap:0.6rem; justify-content:center; align-items:center; flex-wrap:wrap;">
          <!-- WhatsApp -->
          <button class="share-icon-btn" onclick="AITravelEngine.shareRoute('wa')" style="width:42px; height:42px; background:#25D366; color:#FFF;" title="WhatsApp">
            <svg viewBox="0 0 24 24"><path d="M12.031 2c-5.456 0-9.88 4.424-9.88 9.88 0 1.74.452 3.435 1.311 4.935l-1.393 5.088 5.215-1.368c1.448.79 3.085 1.225 4.747 1.225 5.457 0 9.88-4.424 9.88-9.88s-4.423-9.88-9.88-9.88zm5.836 14.168c-.244.688-1.427 1.316-1.97 1.368-.501.047-1.144.072-3.32-.828-2.617-1.082-4.29-3.754-4.42-3.928-.13-.174-1.06-1.41-1.06-2.69 0-1.28.67-1.908.91-2.164.24-.256.526-.32.702-.32.176 0 .352.004.502.01.162.008.38-.061.594.453.22.527.75 1.83.816 1.96.066.13.11.283.022.455-.088.172-.132.28-.262.433-.13.153-.274.341-.392.458-.13.13-.266.27-.115.53.15.26.666 1.1 1.43 1.78.983.876 1.813 1.148 2.074 1.278.26.13.413.108.566-.065.153-.173.655-.764.83-1.025.174-.26.35-.217.587-.13.238.087 1.51.712 1.77.842.26.13.434.195.498.304.065.109.065.631-.179 1.319z"/></svg>
          </button>
          <!-- Facebook -->
          <button class="share-icon-btn" onclick="AITravelEngine.shareRoute('fb')" style="width:42px; height:42px; background:#1877F2; color:#FFF;" title="Facebook">
            <svg viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
          </button>
          <!-- X (Twitter) -->
          <button class="share-icon-btn" onclick="AITravelEngine.shareRoute('x')" style="width:42px; height:42px; background:#000; color:#FFF;" title="X (Twitter)">
            <svg viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
          </button>
          <!-- LinkedIn -->
          <button class="share-icon-btn" onclick="AITravelEngine.shareRoute('li')" style="width:42px; height:42px; background:#0A66C2; color:#FFF;" title="LinkedIn">
            <svg viewBox="0 0 24 24"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/></svg>
          </button>
          <!-- LINE -->
          <button class="share-icon-btn" onclick="AITravelEngine.shareRoute('line')" style="width:42px; height:42px; background:#06C755; color:#FFF;" title="LINE">
            <svg viewBox="0 0 24 24"><path d="M19.34 10.04c0-3.83-3.92-6.95-8.74-6.95-4.82 0-8.74 3.12-8.74 6.95 0 3.43 3.1 6.3 7.3 6.84.28.06.67.19.77.43.09.22.06.56.03.78l-.13.79c-.04.24-.19.94.82.51 1.01-.43 5.46-3.22 7.45-5.51 1.05-1.17 1.24-2.34 1.24-3.84z"/></svg>
          </button>
          <!-- Native Mobile Share Pill -->
          <button class="share-pill-btn" style="background:rgba(30,41,59,0.95) !important; color:#FFFFFF !important; border:1.5px solid #F59E0B !important;" onclick="AITravelEngine.shareRoute('native')">
            <span>📱</span> <span data-i18n="share.nativeShare">More Apps...</span>
          </button>
          <!-- Copy Link -->
          <button class="share-icon-btn" onclick="AITravelEngine.shareRoute('copy')" style="width:42px; height:42px; background:#FDE68A; color:#92400E;" title="Copy Link">
            <svg viewBox="0 0 24 24"><path d="M10.59 13.41c.41.39.41 1.03 0 1.42-.39.39-1.03.39-1.42 0a5.003 5.003 0 0 1 0-7.07l3.54-3.54a5.003 5.003 0 0 1 7.07 0 5.003 5.003 0 0 1 0 7.07l-1.49 1.49c.01-.82-.12-1.64-.4-2.42l.47-.47a3.001 3.001 0 0 0 0-4.24 3.001 3.001 0 0 0-4.24 0l-3.53 3.53a3.001 3.001 0 0 0 0 4.24zm2.82-2.82c-.41-.39-.41-1.03 0-1.42.39-.39 1.03-.39 1.42 0a5.003 5.003 0 0 1 0 7.07l-3.54 3.54a5.003 5.003 0 0 1-7.07 0 5.003 5.003 0 0 1 0-7.07l1.49-1.49c-.01.82.12 1.64.4 2.42l-.47.47a3.001 3.001 0 0 0 0 4.24 3.001 3.001 0 0 0 4.24 0l3.53-3.53a3.001 3.001 0 0 0 0-4.24z"/></svg>
          </button>
        </div>
      </div>

    `;

    
    if (window.I18nEngine) {
      window.I18nEngine.applyLanguage(window.I18nEngine.currentLang);
    }

    if (analytics.trackGeneration) {
      this.trackEvent('route_generated', {
        city: cityClean,
        selected_count: analytics.selectedCount,
        route_a_stop_count: this.routeA_spots.length,
        route_b_stop_count: this.routeB_spots.length,
        has_hotel: this.routeA_spots.some(spot => spot.isHotel === true)
      });
    }

    ['A', 'B'].forEach(routeType => {
      const mapsButton = document.getElementById(`btn_maps_Route${routeType}`);
      if (!mapsButton) return;
      mapsButton.addEventListener('click', () => {
        const routeSpots = routeType === 'A' ? this.routeA_spots : this.routeB_spots;
        const currentDestination = document.getElementById('aiPlanDestination')?.value || destination;
        this.trackEvent('maps_opened', {
          city: currentDestination.split(',')[0].trim(),
          route_type: routeType,
          stop_count: routeSpots.length
        });
      });
    });

    setTimeout(() => {
      resultContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 50);
  },

  renderSpotItemsHtml(spotsArray, routeType, cityClean) {
    if (!spotsArray || spotsArray.length === 0) {
      return '<div style="font-size:0.85rem; color:#9CA3AF; padding:0.75rem; text-align:center; border:1px dashed #E5E7EB; border-radius:8px;">No spots in this route. Add spots or re-select.</div>';
    }

    const t = (key) => window.I18nEngine ? window.I18nEngine.getText(key) : key;

    return spotsArray.map((spot, idx) => {
      const spotDisplayName = this.getLocalizedSpotName(spot);
      const spotDesc = this.getLocalizedDesc(spot);
      const query = `${spot.name || spotDisplayName} ${cityClean}`;
      const mapsUrl = `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(query)}`;

      return `
        <div class="route-spot-card" style="background:#F8FAFC; border:1.5px solid #E2E8F0; padding:0.65rem 0.75rem; border-radius:12px; font-size:0.88rem; display:flex; flex-direction:column; gap:0.45rem; width:100%; box-sizing:border-box; margin-bottom:0.4rem;">
          
          <!-- Row 1: Top Bar (Index + Spot Name + Badges + Remove ✕ Button) -->
          <div style="display:flex; align-items:flex-start; justify-content:space-between; gap:0.5rem; width:100%;">
            
            <div style="display:flex; align-items:flex-start; gap:0.45rem; flex:1; min-width:0;">
              <!-- Index Badge -->
              <span style="font-weight:800; background:#E2E8F0; color:#334155; width:24px; height:24px; display:inline-flex; align-items:center; justify-content:center; border-radius:50%; font-size:0.75rem; flex-shrink:0; margin-top:1px;">${idx + 1}</span>
              
              <!-- Spot Title & Badges -->
              <div style="display:flex; flex-direction:column; min-width:0; flex:1;">
                <div style="font-weight:800; color:#0F172A; font-size:0.92rem; line-height:1.3; word-break:break-word; cursor:pointer;" ${spot.id ? `onclick="AITravelEngine.openSpotModal('${spot.id}')"` : ''} title="${escapeHtml(spotDisplayName)} — View Details">
                  ${escapeHtml(spotDisplayName)}
                </div>
                <div style="display:flex; align-items:center; gap:0.25rem; flex-wrap:wrap; margin-top:0.2rem;">
                  ${spot.isHotel || spot.category === 'Hotel & Stay' ? `
                    <span style="font-size:0.62rem; font-weight:800; background:#F3E8FF; color:#7E22CE; padding:0.06rem 0.3rem; border-radius:4px; border:1px solid #D8B4FE; white-space:nowrap;">${t('badge.returnHotel')}</span>
                  ` : spot.isMustVisit ? `
                    <span style="font-size:0.62rem; font-weight:800; background:#D1FAE5; color:#047857; padding:0.06rem 0.3rem; border-radius:4px; border:1px solid #A7F3D0; white-space:nowrap;">${t('badge.selectedBadge')}</span>
                  ` : `
                    <span style="font-size:0.62rem; font-weight:800; background:#FEF3C7; color:#B45309; padding:0.06rem 0.3rem; border-radius:4px; border:1px solid #FDE68A; white-space:nowrap;">${t('badge.aiPick')}</span>
                  `}
                  ${spot.timeSlot === 1 ? `<span style="font-size:0.62rem; font-weight:800; background:#E0F2FE; color:#0369A1; padding:0.06rem 0.3rem; border-radius:4px; border:1px solid #BAE6FD; white-space:nowrap;">${t('slot.sightseeing')}</span>` : ''}
                  ${spot.timeSlot === 2 ? `<span style="font-size:0.62rem; font-weight:800; background:#FEF3C7; color:#92400E; padding:0.06rem 0.3rem; border-radius:4px; border:1px solid #FDE68A; white-space:nowrap;">${t('slot.cafe')}</span>` : ''}
                  ${spot.timeSlot === 3 ? `<span style="font-size:0.62rem; font-weight:800; background:#FCE7F3; color:#BE185D; padding:0.06rem 0.3rem; border-radius:4px; border:1px solid #FBCFE8; white-space:nowrap;">${t('slot.dinner')}</span>` : ''}
                  ${spot.timeSlot === 4 ? `<span style="font-size:0.62rem; font-weight:800; background:#F1F5F9; color:#334155; padding:0.06rem 0.3rem; border-radius:4px; border:1px solid #CBD5E1; white-space:nowrap;">${t('slot.night')}</span>` : ''}
                </div>
              </div>
            </div>

            <!-- Remove Button (✕) -->
            <button type="button" class="icon-touch-btn danger" onclick="AITravelEngine.removeSpot('${routeType}', ${idx})" title="Remove spot from route" aria-label="Remove spot" style="flex-shrink:0; padding:0.25rem 0.45rem; font-weight:800;">✕</button>
          </div>

          <!-- Row 2: Spot Description (Full Width) -->
          ${spotDesc ? `
            <p style="font-size:0.78rem; color:#475569; line-height:1.4; margin:0; padding-left:1.85rem; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; text-overflow:ellipsis;">
              ${escapeHtml(spotDesc)}
            </p>
          ` : ''}

          <!-- Row 3: Bottom Action Bar (Reorder Up/Down Left | View Details & Maps Right) -->
          <div style="display:flex; align-items:center; justify-content:space-between; gap:0.4rem; padding-top:0.35rem; border-top:1px dashed #E2E8F0; margin-top:0.1rem; flex-wrap:wrap;">
            
            <!-- Reorder Controls -->
            <div style="display:flex; align-items:center; gap:0.25rem; flex-shrink:0;">
              <button type="button" class="icon-touch-btn" onclick="AITravelEngine.moveSpot('${routeType}', ${idx}, -1)" ${idx === 0 ? 'disabled style="opacity:0.3; cursor:not-allowed;"' : ''} aria-label="Move Up" style="padding:0.2rem 0.55rem; font-size:0.75rem; border-radius:6px; font-weight:800;">▲</button>
              <button type="button" class="icon-touch-btn" onclick="AITravelEngine.moveSpot('${routeType}', ${idx}, 1)" ${idx === spotsArray.length - 1 ? 'disabled style="opacity:0.3; cursor:not-allowed;"' : ''} aria-label="Move Down" style="padding:0.2rem 0.55rem; font-size:0.75rem; border-radius:6px; font-weight:800;">▼</button>
            </div>

            <!-- View Details & Google Maps Buttons -->
            <div style="display:flex; align-items:center; gap:0.35rem; flex-shrink:0;">
              ${spot.id ? `
                <button type="button" onclick="AITravelEngine.openSpotModal('${spot.id}')" style="display:inline-flex; align-items:center; justify-content:center; gap:0.2rem; background:#EFF6FF; color:#0369A1; border:1px solid #BAE6FD; padding:0.25rem 0.55rem; border-radius:6px; font-weight:800; font-size:0.75rem; cursor:pointer; white-space:nowrap; -webkit-tap-highlight-color:transparent;" title="${t('btn.viewDetails')}">
                  ${t('btn.viewDetails')}
                </button>
              ` : ''}
              <a href="${mapsUrl}" target="_blank" rel="noopener noreferrer" style="color:#2563EB; font-weight:700; text-decoration:none; font-size:0.75rem; background:#EFF6FF; border:1px solid #BFDBFE; padding:0.25rem 0.55rem; display:inline-flex; align-items:center; border-radius:6px; white-space:nowrap;">📍 Maps ↗</a>
            </div>

          </div>

        </div>
      `;
    }).join('');
  },


  moveSpot(routeType, index, direction) {
    const list = routeType === 'A' ? this.routeA_spots : this.routeB_spots;
    const newIndex = index + direction;
    if (newIndex < 0 || newIndex >= list.length) return;

    const temp = list[index];
    list[index] = list[newIndex];
    list[newIndex] = temp;

    this.refreshRouteCard(routeType);
  },

  removeSpot(routeType, index) {
    const list = routeType === 'A' ? this.routeA_spots : this.routeB_spots;
    list.splice(index, 1);
    this.refreshRouteCard(routeType);
  },

  refreshRouteCard(routeType) {
    const destination = document.getElementById('aiPlanDestination')?.value || this.lastCity || '';
    const cityClean = destination.split(',')[0].trim();

    const listContainer = document.getElementById(routeType === 'A' ? 'routeA_itemList' : 'routeB_itemList');
    const mapsBtn = document.getElementById(routeType === 'A' ? 'btn_maps_RouteA' : 'btn_maps_RouteB');
    const spotsList = routeType === 'A' ? this.routeA_spots : this.routeB_spots;

    if (listContainer) {
      listContainer.innerHTML = this.renderSpotItemsHtml(spotsList, routeType, cityClean);
    }

    if (mapsBtn) {
      const names = spotsList.map(s => s.name);
      const mapsUrl = this.buildMasterGoogleMapsPath(names, destination);
      mapsBtn.href = mapsUrl;
      mapsBtn.innerText = `🗺️ Open Route ${routeType} in Google Maps (${spotsList.length} Destinations) ↗`;
    }
  },

  buildMasterGoogleMapsPath(venueNames, destination) {
    if (!venueNames || venueNames.length === 0) {
      const cityClean = destination.split(',')[0].trim();
      return `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(cityClean)}`;
    }

    const cityClean = destination.split(',')[0].trim();
    const cleanStops = venueNames.map(name => {
      const cleanName = name.replace(/[\（\(].*?[\）\)]/g, '').trim();
      return `${cleanName}, ${cityClean}`;
    });

    if (cleanStops.length === 1) {
      return `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(cleanStops[0])}`;
    }

    const origin = encodeURIComponent(cleanStops[0]);
    const dest = encodeURIComponent(cleanStops[cleanStops.length - 1]);

    if (cleanStops.length === 2) {
      return `https://www.google.com/maps/dir/?api=1&origin=${origin}&destination=${dest}&travelmode=driving&dirflg=d`;
    }

    const intermediateStops = cleanStops.slice(1, -1);
    const waypoints = intermediateStops.map(s => encodeURIComponent(s)).join('|');

    return `https://www.google.com/maps/dir/?api=1&origin=${origin}&destination=${dest}&waypoints=${waypoints}&travelmode=driving&dirflg=d`;
  }
};

function escapeHtml(str) {
  if (str === null || str === undefined) return '';
  return String(str).replace(/[&<>"']/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' }[m]));
}


window.AITravelEngine = AITravelEngine;

function initAITravelEngine() {
  if (window.AITravelEngine && typeof window.AITravelEngine.renderCandidateSpots === 'function') {
    window.AITravelEngine.renderCandidateSpots();
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initAITravelEngine);
} else {
  initAITravelEngine();
}
