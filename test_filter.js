const spot = { category: "Landmark" };
const category = "Café";
const c = String(spot.category || '').toLowerCase();
console.log("c is", c);
console.log("category is", category);

let result = true;
if (category === 'Landmark' && !(c.includes('landmark') || c.includes('史跡') || c.includes('名所'))) result = false;
if (category === 'Museum' && !(c.includes('museum') || c.includes('art') || c.includes('ギャラリー') || c.includes('美術館') || c.includes('博物館'))) result = false;
if (category === 'Café' && !(c.includes('café') || c.includes('bistro') || c.includes('restaurant') || c.includes('dining') || c.includes('bakery') || c.includes('カフェ') || c.includes('レストラン'))) result = false;

console.log("Result:", result);
