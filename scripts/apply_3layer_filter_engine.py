import re
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
target_path = os.path.join(base_dir, '..', 'js', 'ai-travel-engine.js')

with open(target_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update isSpotMatchingFilter implementation
old_is_spot_match = re.search(r'isSpotMatchingFilter\(spot,\s*preset,\s*genre,\s*conditions\)\s*\{.*?\n  \},', code, re.DOTALL)

new_is_spot_match = """isSpotMatchingFilter(spot, preset, category, conditions) {
    if (!spot) return false;
    
    // Layer 1: Scope Check
    if (preset === 'Top7' && spot.top7 !== true) return false;
    if (preset === 'HiddenGem' && spot.hiddenGem !== true) return false;

    // Layer 2: Category Check (Array or String Match)
    if (category && category !== 'ALL') {
      if (Array.isArray(spot.categories)) {
        if (!spot.categories.includes(category)) return false;
      } else {
        const c = String(spot.category || '').toLowerCase();
        if (category === 'Landmark' && !(c.includes('landmark') || c.includes('史跡') || c.includes('名所'))) return false;
        if (category === 'Museum' && !(c.includes('museum') || c.includes('art') || c.includes('ギャラリー') || c.includes('美術館') || c.includes('博物館'))) return false;
        if (category === 'Café' && !(c.includes('café') || c.includes('bistro') || c.includes('restaurant') || c.includes('dining') || c.includes('bakery') || c.includes('カフェ') || c.includes('レストラン'))) return false;
        if (category === 'Scenery' && !(c.includes('scenery') || c.includes('walk') || c.includes('park') || c.includes('プロムナード') || c.includes('散策'))) return false;
        if (category === 'Kids' && !(c.includes('kids') || spot.kids === true)) return false;
        if (category === 'Shopping' && !(c.includes('shopping') || spot.shopping === true)) return false;
        if (category === 'Night' && !(c.includes('night') || spot.night === true)) return false;
      }
    }

    // Layer 3: Conditions Check (AND Logic for ON Switches)
    if (conditions && conditions.size > 0) {
      for (const cond of conditions) {
        if (cond === 'Rain' && spot.rain !== true) return false;
        if (cond === 'Free' && spot.free !== true) return false;
      }
    }

    return true;
  },"""

if old_is_spot_match:
    code = code[:old_is_spot_match.start()] + new_is_spot_match + code[old_is_spot_match.end():]

# 2. Update renderCandidateSpots block
m1 = code.find('// 1. Filter by Area Zone (Step 1 dropdown: ALL / city / suburban)')
m2 = code.find('const viewModeBarHtml = categoryFilterBarHtml +', m1)

if m1 != -1 and m2 != -1:
    new_block = """// 1. Filter by Area Zone (Step 1 dropdown: ALL / city / suburban)
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
          
          <!-- Layer 1: Scope (Exclusive Radio) -->
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
            </div>
          </div>

          <!-- Layer 2: Categories (Single Select Pill with Array Match) -->
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
              <button type="button" class="filter-chip ${category === 'Night' ? 'active' : ''}" onclick="AITravelEngine.toggleGenreFilter('Night')">
                ${t('filter.night')} (${getCategoryCount('Night')})
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
"""
    code = code[:m1] + new_block + code[m2:]

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("🎉 Successfully applied 3-Layer Filter Engine (Scope, Categories Array, Slide Toggles) in ai-travel-engine.js!")
