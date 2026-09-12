import re
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
target_path = os.path.join(base_dir, '..', 'js', 'ai-travel-engine.js')

with open(target_path, 'r', encoding='utf-8') as f:
    code = f.read()

m1 = code.find('// 1. Filter by Area Zone (Step 1 dropdown: ALL / city / suburban)')
m2 = code.find('const viewModeBarHtml = categoryFilterBarHtml +', m1)

if m1 == -1 or m2 == -1:
    print("ERROR: Target block not found")
    exit(1)

old_block = code[m1:m2]

new_block = """// 1. Filter by Area Zone (Step 1 dropdown: ALL / city / suburban)
      let areaSpots = spots;
      if (targetArea && targetArea !== 'ALL') {
        areaSpots = spots.filter(s => (s.locationZone || 'city') === targetArea);
      }

      // 2. Multilingual 3-Row Filter System & Real-Time Dynamic Counts
      const preset = this.activePreset || 'ALL';
      const genre = this.activeGenre || 'ALL';
      const conds = this.activeConditions || new Set();

      let filteredSpots = areaSpots.filter(s => this.isSpotMatchingFilter(s, preset, genre, conds));

      if (!filteredSpots) {
        filteredSpots = areaSpots;
      }

      const t = (k) => window.I18nEngine ? window.I18nEngine.getText(k) : k;

      if (counterBadge) {
        const selectedCount = this.selectedMustVisitIds.size;
        counterBadge.innerHTML = `${t('badge.selected')} <strong>${selectedCount} / 8</strong> ${t('badge.maxNotice')}`;
        counterBadge.style.color = selectedCount >= 8 ? '#C2410C' : '#047857';
      }

      // Real-time Dynamic Count Calculations
      const getPresetCount = (p) => areaSpots.filter(s => this.isSpotMatchingFilter(s, p, genre, conds)).length;
      const getGenreCount = (g) => areaSpots.filter(s => this.isSpotMatchingFilter(s, preset, g, conds)).length;
      const getCondCount = (c) => {
        const testConds = new Set(conds);
        if (!testConds.has(c)) testConds.add(c);
        return areaSpots.filter(s => this.isSpotMatchingFilter(s, preset, genre, testConds)).length;
      };

      const categoryFilterBarHtml = `
        <div class="category-filter-box" style="grid-column:1 / -1; width:100%; display:flex; flex-direction:column; gap:0.5rem; margin-bottom:1rem; background:#FAF7F2; border:1.5px solid var(--border-ink, #292524); padding:0.75rem 0.9rem; border-radius:14px; box-shadow:2px 2px 0px var(--border-ink, #292524);">
          
          <!-- Row 1: Presets (Exclusive Radio) -->
          <div class="filter-row" style="display:flex; align-items:center; gap:0.5rem; flex-wrap:wrap;">
            <span class="filter-group-label" style="font-size:0.78rem; font-weight:800; color:var(--primary-forest, #047857); min-width:95px; font-family:var(--font-sans);">
              ${t('filter.presetGroup')}
            </span>
            <div style="display:flex; gap:0.35rem; flex-wrap:wrap; flex:1;">
              <button type="button" class="filter-chip ${preset === 'ALL' ? 'active' : ''}" onclick="AITravelEngine.setPresetFilter('ALL')">
                ${t('filter.all')} (${getPresetCount('ALL')})
              </button>
              <button type="button" class="filter-chip ${preset === 'Top7' ? 'active' : ''}" onclick="AITravelEngine.setPresetFilter('Top7')" style="background:${preset === 'Top7' ? '#047857' : '#ECFDF5'}; color:${preset === 'Top7' ? '#FFF' : '#047857'}; border-color:#A7F3D0; font-weight:800;">
                ${t('filter.top7')} (${getPresetCount('Top7')})
              </button>
              <button type="button" class="filter-chip ${preset === 'HiddenGem' ? 'active' : ''}" onclick="AITravelEngine.setPresetFilter('HiddenGem')" style="background:${preset === 'HiddenGem' ? '#7E22CE' : '#F3E8FF'}; color:${preset === 'HiddenGem' ? '#FFF' : '#7E22CE'}; border-color:#D8B4FE; font-weight:800;">
                ${t('filter.hiddenGems')} (${getPresetCount('HiddenGem')})
              </button>
            </div>
          </div>

          <!-- Row 2: Genres (Single Select Toggle) -->
          <div class="filter-row" style="display:flex; align-items:center; gap:0.5rem; flex-wrap:wrap; border-top:1px dashed #CBD5E1; padding-top:0.45rem;">
            <span class="filter-group-label" style="font-size:0.78rem; font-weight:800; color:var(--primary-forest, #047857); min-width:95px; font-family:var(--font-sans);">
              ${t('filter.genreGroup')}
            </span>
            <div style="display:flex; gap:0.35rem; flex-wrap:wrap; flex:1;">
              <button type="button" class="filter-chip ${genre === 'Landmark' ? 'active' : ''}" onclick="AITravelEngine.toggleGenreFilter('Landmark')">
                ${t('filter.landmark')} (${getGenreCount('Landmark')})
              </button>
              <button type="button" class="filter-chip ${genre === 'Museum' ? 'active' : ''}" onclick="AITravelEngine.toggleGenreFilter('Museum')">
                ${t('filter.museum')} (${getGenreCount('Museum')})
              </button>
              <button type="button" class="filter-chip ${genre === 'Café' ? 'active' : ''}" onclick="AITravelEngine.toggleGenreFilter('Café')">
                ${t('filter.cafe')} (${getGenreCount('Café')})
              </button>
              <button type="button" class="filter-chip ${genre === 'Scenery' ? 'active' : ''}" onclick="AITravelEngine.toggleGenreFilter('Scenery')">
                ${t('filter.scenery')} (${getGenreCount('Scenery')})
              </button>
            </div>
          </div>

          <!-- Row 3: Features & Conditions (Multi-select AND Toggle) -->
          <div class="filter-row" style="display:flex; align-items:center; gap:0.5rem; flex-wrap:wrap; border-top:1px dashed #CBD5E1; padding-top:0.45rem;">
            <span class="filter-group-label" style="font-size:0.78rem; font-weight:800; color:var(--primary-forest, #047857); min-width:95px; font-family:var(--font-sans);">
              ${t('filter.conditionGroup')}
            </span>
            <div style="display:flex; gap:0.35rem; flex-wrap:wrap; flex:1;">
              <button type="button" class="filter-chip ${conds.has('Kids') ? 'active' : ''}" onclick="AITravelEngine.toggleConditionFilter('Kids')" style="border-color:${conds.has('Kids') ? '#2563EB' : '#CBD5E1'}; background:${conds.has('Kids') ? '#DBEAFE' : '#FFF'}; color:${conds.has('Kids') ? '#1E40AF' : 'inherit'}; font-weight:${conds.has('Kids') ? '800' : '500'};">
                ${t('filter.kids')} (${getCondCount('Kids')})
              </button>
              <button type="button" class="filter-chip ${conds.has('Rain') ? 'active' : ''}" onclick="AITravelEngine.toggleConditionFilter('Rain')" style="border-color:${conds.has('Rain') ? '#0284C7' : '#CBD5E1'}; background:${conds.has('Rain') ? '#E0F2FE' : '#FFF'}; color:${conds.has('Rain') ? '#0369A1' : 'inherit'}; font-weight:${conds.has('Rain') ? '800' : '500'};">
                ${t('filter.rain')} (${getCondCount('Rain')})
              </button>
              <button type="button" class="filter-chip ${conds.has('Free') ? 'active' : ''}" onclick="AITravelEngine.toggleConditionFilter('Free')" style="border-color:${conds.has('Free') ? '#16A34A' : '#CBD5E1'}; background:${conds.has('Free') ? '#DCFCE7' : '#FFF'}; color:${conds.has('Free') ? '#15803D' : 'inherit'}; font-weight:${conds.has('Free') ? '800' : '500'};">
                ${t('filter.free')} (${getCondCount('Free')})
              </button>
            </div>
          </div>

        </div>
      `;
"""

code = code[:m1] + new_block + code[m2:]

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully updated filter logic and 3-row layout in ai-travel-engine.js!")
