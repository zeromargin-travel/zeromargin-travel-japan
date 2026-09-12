import json

data = [
  {
    "id": "ber_b_50",
    "new_en_desc": "Embark on a classic one-hour sightseeing cruise along the Spree River, taking in spectacular water-level views of iconic Berlin landmarks including the Reichstag, Museum Island, and the soaring TV Tower.",
    "new_en_tip": "Board a covered sightseeing boat from the Friedrichstraße pier, and be sure to have your camera ready to capture the unique perspective as you glide directly beneath the city's historic bridges."
  },
  {
    "id": "ber_b_51",
    "new_en_desc": "Experience Berlin's vibrant summer scene at this unique outdoor floating pool and beach bar, ingeniously converted from a former cargo barge moored right on the Spree River.",
    "new_en_tip": "Visit during the summer months to soak in the refreshing floating pool while admiring stunning views of the historic Oberbaumbrücke across the water."
  },
  {
    "id": "ber_b_53",
    "new_en_desc": "Join the massive lines at this world-famous street food staple, renowned for its legendary doner kebabs packed with savory roasted chicken, deeply flavorful fried vegetables, and crumbly feta cheese.",
    "new_en_tip": "Expect wait times of up to 45 minutes around the clock; to beat the crowds, try visiting during off-peak hours right after opening before 11:00 AM or late at night past 11:00 PM."
  },
  {
    "id": "ber_b_54",
    "new_en_desc": "Step into this elegant 19th-century villa to experience authentic Viennese coffeehouse culture, making it the perfect setting to indulge in a slice of traditional baking history.",
    "new_en_tip": "Settle into one of the classic wooden chairs and treat yourself to their famous homemade, warm Apfelstrudel (apple pie), generously drizzled with rich vanilla sauce."
  },
  {
    "id": "ber_b_55",
    "new_en_desc": "Established in 1837, Berlin's oldest outdoor beer garden offers a timeless atmosphere where guests gather at long wooden tables nestled beneath the cool shade of massive, leafy trees.",
    "new_en_tip": "Grab a seat on a classic wooden bench under the canopy of large trees, and pair a freshly baked local pretzel with a cold, house-brewed Prater Pils draft beer."
  },
  {
    "id": "ber_b_57",
    "new_en_desc": "Let your little ones explore this imaginative children's world, anchored by a magnificent giant wooden play structure themed after Noah's Ark and surrounded by 150 beautifully crafted animal sculptures.",
    "new_en_tip": "Climb inside the massive 11-meter-tall wooden Noah's Ark to discover fun net mechanisms and slides perfect for playing with your children; entry is free, but advance reservations are required."
  },
  {
    "id": "ber_b_60",
    "new_en_desc": "Unwind in this striking Nordic-style sauna complex, where the centerpiece is a fantastic saltwater heated dome pool that creates a mesmerizing, multi-sensory relaxation experience with underwater acoustics.",
    "new_en_tip": "Float effortlessly in the high-salinity dome pool while enjoying ambient and electronic DJ sets broadcast directly through underwater speakers on weekend evenings, creating an unforgettable aquatic auditory experience."
  },
  {
    "id": "ber_b_61",
    "new_en_desc": "Marvel at this exquisite yellow Rococo palace perched majestically atop terraced vineyards, a UNESCO World Heritage site completed in 1747 as the beloved summer retreat of Frederick the Great.",
    "new_en_tip": "For the perfect photograph, pause while climbing the grand staircase from the fountain plaza to look up and capture the stunning yellow palace framed by lush grape trellises."
  },
  {
    "id": "ber_b_62",
    "new_en_desc": "Discover Prussia's premier architectural masterpiece at the western end of Sanssouci Park, a colossal Baroque palace boasting over 200 lavishly decorated rooms that showcase extraordinary royal extravagance.",
    "new_en_tip": "Don't miss the breathtaking \"Grottensaal\" (Grotto Hall), an astoundingly luxurious and eccentric room meticulously covered from floor to ceiling in sparkling shells and precious minerals."
  },
  {
    "id": "ber_b_63",
    "new_en_desc": "Explore this striking Tudor-style palace built in 1917 to resemble an English country manor, famously known as the historic stage where world leaders gathered for the pivotal 1945 Potsdam Conference.",
    "new_en_tip": "Step inside the Great Hall to view the very room where history was made, featuring the famous custom-made red wooden round table where the Potsdam Agreement was officially signed."
  },
  {
    "id": "ber_b_64",
    "new_en_desc": "Stroll through this charming 18th-century neighborhood, featuring an idyllic enclave of 134 distinctive red-brick homes originally constructed to accommodate skilled Dutch craftsmen.",
    "new_en_tip": "Wander down Mittelstraße amidst the picturesque red-brick houses and stop at one of the cozy cafes to try Potsdam's famous, delicious pancakes."
  },
  {
    "id": "ber_b_65",
    "new_en_desc": "Immerse yourself in a world-class collection of Impressionist masterpieces at this exquisite art museum, which proudly displays celebrated works including Monet's iconic \"Water Lilies\" and \"Haystacks.\"",
    "new_en_tip": "Make a beeline for the dedicated Monet exhibition room to marvel at an extraordinary gathering of 39 original Claude Monet paintings sourced from the prestigious Hasso Plattner Foundation."
  },
  {
    "id": "ber_b_67",
    "new_en_desc": "Step behind the scenes at this dynamic theme park situated adjacent to the world's oldest large-scale film studio, offering an exciting array of authentic movie sets and thrilling live performances.",
    "new_en_tip": "Be sure to catch the spectacular, high-octane live action stunt show held at the Vulkan Arena for a true Hollywood-style adrenaline rush."
  },
  {
    "id": "ber_b_69",
    "new_en_desc": "Glide through a serene UNESCO Biosphere Reserve featuring an enchanting network of over 1,500 kilometers of intertwined waterways, best explored via traditional wooden \"Kahn\" punts poled by local boatmen.",
    "new_en_tip": "Board a classic wooden Kahn from the Lübbenau port and keep an eye out for floating water stalls, where you can purchase the region's famous, freshly bottled pickles directly from your boat."
  },
  {
    "id": "ber_b_70",
    "new_en_desc": "Escape to a constant 26°C paradise at this extraordinary all-weather indoor rainforest resort, ingeniously housed within a massive former airship hangar and featuring a pristine white sand beach.",
    "new_en_tip": "Take advantage of the 24-hour opening times by booking a highly popular and unique overnight stay in a safari tent pitched right on the dome's indoor sandy beach."
  },
  {
    "id": "ber_b_71",
    "new_en_desc": "Discover this enchanting, uninhabited UNESCO World Heritage island floating in the Havel River, distinguished by its striking white palace and a resident population of majestic, free-roaming peacocks.",
    "new_en_tip": "Ride the small ferry across the water to the island and have your camera ready to capture the brilliant moment when one of the beautiful, free-roaming peacocks unfurls its colorful feathers."
  },
  {
    "id": "ber_b_73",
    "new_en_desc": "Venture to this fascinating Cold War relic that once served as a US military radar spy base, now transformed into a sprawling canvas of vibrant street art crowned by massive, iconic radar domes.",
    "new_en_tip": "Step inside the dilapidated white radar domes to experience their astonishing acoustic echo reverberations, and head to the roof for sweeping, panoramic views across the entire city of Berlin."
  },
  {
    "id": "ber_b_74",
    "new_en_desc": "Explore one of Europe's best-preserved 16th-century Renaissance water fortresses, a remarkable architectural feat that features the imposing, historic Juliusturm watchtower as its centerpiece.",
    "new_en_tip": "Ascend the ancient spiral staircase of the Juliusturm—the oldest structure in the fortress—to capture stunning photographs of the scenic confluence where the Havel River meets its tributaries."
  },
  {
    "id": "ber_b_75",
    "new_en_desc": "Enjoy a premier shopping experience just outside the city at this expansive outlet destination in Wustermark, offering discounted luxury and fashion goods from over 90 popular global brands.",
    "new_en_tip": "For a seamless shopping trip, book a seat on the VIP shuttle bus departing from Potsdamer Platz, or take the convenient public route using the RE4 train connecting to the 663 bus."
  },
  {
    "id": "cgn_c_1",
    "new_en_desc": "Gaze in awe at the soaring 157-meter twin towers of this UNESCO World Heritage site, a crowning masterpiece of Gothic architecture that famously houses the magnificent golden reliquary of the Three Wise Men.",
    "new_en_tip": "While prayer areas remain free, note that a €12 tourist ticket for the inner choir is introduced in July 2026; don't miss the spectacular €8 climb up 533 steps for breathtaking views from the 157-meter towers."
  },
  {
    "id": "cgn_c_2",
    "new_en_desc": "Spanning the Rhine River, this historic iron bridge constructed in 1911 has become a beloved symbol of romance, its fences famously laden with hundreds of thousands of colorful \"love padlocks\" left by couples.",
    "new_en_tip": "Walk across to the eastern bank at dusk to capture a spectacular photograph where the glowing train lights, shimmering water reflections, and the brilliantly illuminated cathedral seamlessly overlap."
  },
  {
    "id": "cgn_c_4",
    "new_en_desc": "Gather at this lively, expansive public square anchored by the grand equestrian statue of King Frederick William III, which serves as a vibrant focal point for seasonal carnivals and festive winter ice skating.",
    "new_en_tip": "Visit between late November and early January to experience the magical Heinzels Wintermärchen Christmas market, complete with a spectacular ice skating rink beautifully wrapped around the historic equestrian statue."
  }
]

with open('/Users/jnabi1/Desktop/zeromargin-travel.github.io/data/harvest/result_3.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
