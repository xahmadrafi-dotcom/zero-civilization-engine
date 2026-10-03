AI learning app **v0.dev**  
  
  
🎯 এক লাইনে অ্যাপটা কী  
**শেখার তারা** — ৩-৯ বছরের শিশুদের জন্য মাতৃভাষা-ভিত্তিক AI learning app, যা বাংলা-ইংরেজি-আরবি-গণিত শেখাকে খেলায়, গল্পে, আর adaptive practice-এ বদলে দেয়।  
  
⸻  
  
🔍 সমস্যা বিশ্লেষণ  
  
* **কার সমস্যা:** ৩-৯ বছরের শিশু, তাদের বাবা-মা, এবং বাংলা-ভিত্তিক early learning খুঁজছেন এমন পরিবার  
* **সমস্যাটা কী:** ভালো learning app আছে, কিন্তু সেগুলো হয় English-first, নয়তো একেবারে static। শিশুর বয়স, ভাষা, আগ্রহ, শেখার গতি—কিছুই ধরতে পারে না।  
* **এখন মানুষ কীভাবে সমাধান করছে:** YouTube, random worksheet, আলাদা আলাদা app—একটা বাংলা, একটা phonics, একটা Quranic Arabic, আরেকটা math  
* **কেন সেটা যথেষ্ট না:** fragmented experience, progress tracking দুর্বল, child-safe design দুর্বল, cultural relevance কম, এবং parent-এর কাছে clear answer নেই: “বাচ্চা আসলে কী শিখল?”  
  
⸻  
  
💡 প্রোডাক্ট ভিশন  
  
* **কী:** একটি mobile-first, child-safe, AI-assisted learning world  
* **কার জন্য:**  
    * ৩-৫: pre-school explorers  
    * ৫-৭: early learners  
    * ৭-৯: builders  
    * secondary user: parents  
* **কেন আলাদা:**  
    * বাংলা + ইংরেজি + Quranic Arabic + Math + Life Skills এক ছাদের নিচে  
    * age-banded UX  
    * adaptive learning path  
    * parent progress dashboard  
    * South Asian cultural context  
* **পিচ লাইন:**  
    **“শেখার তারা — প্রতিটা শিশুর জন্য নিজের ভাষায়, নিজের গতিতে, আনন্দের শেখার জগৎ।”**  
  
⸻  
  
⚡ MVP ফিচার ম্যাপ  
  
**ফেজ ১ (ছাড়া চলবে না):**  
১. **Age-based onboarding + child profile**  
  
* বয়স গ্রুপ বাছাই: ৩-৫ / ৫-৭ / ৭-৯  
* parent-gated setup  
* learning language preference  
  
২. **Core lesson loop (বাংলা + Math)**  
  
* ২টা module দিয়েই শুরু  
* mini lesson → quick activity → reward  
* বাংলা: অক্ষর/শব্দ  
* Math: সংখ্যা/গোনা/shape  
  
৩. **Adaptive practice engine (simple AI, not heavy AI)**  
  
* ভুল হলে same concept-এর easier variation  
* ভালো করলে next difficulty  
* interest tag দিয়ে example বদলাবে (animal, fruits, vehicles)  
  
৪. **Parent dashboard + weekly summary**  
  
* আজ কী শিখল  
* কোথায় শক্তিশালী  
* কোথায় practice দরকার  
* screen-time settings  
  
**ফেজ ২+ (পরে যোগ হবে):**  
  
* English phonics  
* Quranic Arabic letters + audio  
* stories + life skills module  
* streak rewards, wardrobe unlocks  
* voice pronunciation feedback  
* offline mode  
* multi-child household support  
* AI-generated weekly learning plan  
* creative sandbox  
  
⸻  
  
🗺️ ইউজার ফ্লো  
  
**বাচ্চার ফ্লো:**  
ধাপ ১: app খোলে → বড়, warm welcome screen → character দেখে  
→ ধাপ ২: নিজের avatar/animal guide দেখে  
→ ধাপ ৩: “আজকের ১টা শেখা” card পায়  
→ ধাপ ৪: 3-5 মিনিটের lesson খেলে  
→ ধাপ ৫: activity complete করে তারা ⭐ পায়  
→ ধাপ ৬: sticker/unlock পায়  
→ ধাপ ৭: app নরমভাবে বলে “আজকের কাজ শেষ”  
  
**বাবা-মায়ের ফ্লো:**  
ধাপ ১: parent gate দিয়ে sign in / child create  
→ ধাপ ২: বয়স, ভাষা, লক্ষ্য, screen-time set  
→ ধাপ ৩: child lesson শুরু করে  
→ ধাপ ৪: parent dashboard-এ mastery, streak, time spent দেখে  
→ ধাপ ৫: weekly AI summary পায়  
→ ধাপ ৬: কোন module on/off করবে ঠিক করে  
  
**প্রথম ৩ মিনিটের wow moment:**  
  
* বাচ্চার নাম ধরে welcome  
* cute guide character  
* first activity instantly playable  
* ১ মিনিটের মধ্যে first star reward  
  
⸻  
  
🏗️ টেক স্ট্যাক  
  
**ফ্রন্টএন্ড:**  
  
* **Next.js + React**  
* mobile-first responsive UI  
* PWA support যাতে app-like feel আসে  
  
**ব্যাকএন্ড:**  
  
* **Supabase**  
* auth, database, storage, row-level security  
  
**ডেটাবেস:**  
  
* **Postgres (via Supabase)**  
  
**AI/ML:**  
  
* শুরুতে full ML না  
* **rules-based adaptive engine + LLM for parent summary**  
* later: lightweight recommendation layer  
  
**অডিও:**  
  
* pre-recorded human audio for Bengali/Arabic pronunciation  
* simple playback via app assets / Supabase storage  
  
**হোস্টিং:**  
  
* **Vercel** for frontend  
* Supabase for backend  
  
**বিল্ড টুল:**  
  
* **Lovable.dev**: fast UI scaffolding  
* **v0.dev**: screens/components  
* **Cursor**: logic, DB integration, refactor  
* **Figma optional**, but not mandatory  
  
**কেন এই stack:**  
  
* solo-builder friendly  
* low infra complexity  
* secure enough for MVP  
* fast iteration  
* AI tools দিয়ে prompt-based build সম্ভব  
  
⸻  
  
🗄️ ডেটা মডেল  
  
**টেবিল ১: parents**  
  
* id  
* email / auth_id  
* name  
* country  
* created_at  
  
**টেবিল ২: children**  
  
* id  
* parent_id  
* display_name  
* age_group (3-5 / 5-7 / 7-9)  
* avatar  
* interests (animals, cars, fruits etc.)  
* daily_screen_limit_minutes  
  
**টেবিল ৩: modules**  
  
* id  
* name (Bangla, Math, English, Arabic)  
* status  
* min_age_group  
* max_age_group  
  
**টেবিল ৪: lessons**  
  
* id  
* module_id  
* age_group  
* title  
* type (match, tap, trace, listen)  
* difficulty  
* content_json  
* reward_stars  
  
**টেবিল ৫: attempts**  
  
* id  
* child_id  
* lesson_id  
* score  
* mistakes_count  
* completed  
* duration_seconds  
* completed_at  
  
**টেবিল ৬: child_skills**  
  
* id  
* child_id  
* skill_key  
* module_id  
* mastery_level  
* last_practiced_at  
  
**টেবিল ৭: rewards**  
  
* id  
* child_id  
* stars_balance  
* badges_json  
* unlocked_items_json  
  
**টেবিল ৮: weekly_reports**  
  
* id  
* child_id  
* week_start  
* summary_text  
* strengths_json  
* needs_help_json  
  
**টেবিল ৯: settings_parental**  
  
* id  
* parent_id  
* allowed_modules_json  
* screen_time_limit  
* audio_on  
* child_mode_locked  
  
**সম্পর্ক:**  
  
* one parent → many children  
* one module → many lessons  
* one child → many attempts  
* attempts → skill mastery update  
* child → one evolving reward state  
* child → weekly report generated  
  
**নিরাপত্তা নোট:**  
child table-এ full legal name, location, school info, photo—এখনই রাখবেন না। data minimization বজায় রাখুন।  
  
⸻  
  
🎨 UI/UX দিকনির্দেশনা  
  
**রঙ:**  
  
* primary: soft sky blue  
* secondary: warm yellow  
* accent: leaf green  
* success: soft coral / orange  
* background: off-white / cream  
* avoid: overstimulating neon palette  
  
**ফন্ট:**  
  
* Bangla: **Noto Sans Bengali** বা **Hind Siliguri**  
* English: **Inter** / **Nunito**  
* Arabic: readable Quranic-friendly font for letters only, body text minimal  
  
**অ্যানিমেশন:**  
  
* micro-animations only  
* tap করলে bounce  
* reward পেলে star burst  
* screen transition 200–300ms  
* no fast flashing, no hyper-stimulus loops  
  
**শিশু-বান্ধব নীতি:**  
  
* বড় tap target  
* এক screen = এক primary action  
* text কম, visuals বেশি  
* 3-5 গ্রুপে audio-first  
* 7-9 গ্রুপে more challenge + progress bar  
* error messaging: “চলো আরেকবার”  
* কোনো red punishment state না  
  
**বয়সভিত্তিক UX পার্থক্য:**  
  
* **৩-৫:** single-step tasks, voice guidance, huge buttons  
* **৫-৭:** simple choices, beginner progression, visible rewards  
* **৭-৯:** goals, badge path, light autonomy, mini mastery map  
  
⸻  
  
📅 রোডম্যাপ  
  
**ফেজ ১ (সপ্তাহ ১-২): Foundation**  
  
* product scope freeze  
* age bands define  
* module map: Bangla + Math only  
* database schema  
* low-fidelity wireframes  
    → **ফলাফল:** build-ready spec + first screen flows  
  
**ফেজ ২ (সপ্তাহ ৩-৪): MVP Build Sprint**  
  
* onboarding  
* child profile  
* lesson player  
* 20 Bangla lessons  
* 20 Math lessons  
* star rewards  
* parent dashboard v1  
    → **ফলাফল:** clickable MVP working in browser/mobile  
  
**ফেজ ৩ (মাস ২): Adaptive + Safety Polish**  
  
* rules-based adaptive engine  
* weekly AI summary  
* screen-time control  
* parent gate  
* analytics events  
    → **ফলাফল:** testable private beta  
  
**ফেজ ৪ (মাস ৩): Pilot Launch**  
  
* 10–20 parent-child testing  
* fix friction points  
* improve audio, pacing, retention loop  
* add first daily challenge  
    → **ফলাফল:** public MVP launch candidate  
  
**ফেজ ৫ (মাস ৩+): Expansion**  
  
* English phonics  
* Quranic Arabic letters  
* life skills story cards  
* premium content  
    → **ফলাফল:** monetizable v1.5  
  
⸻  
  
💰 মনিটাইজেশন  
  
**মডেল:**  
**Freemium + monthly subscription**  
  
**ফ্রি টিয়ার:**  
  
* ১ child profile  
* limited Bangla + Math lessons  
* basic stars  
* basic parent dashboard  
  
**প্রিমিয়াম:**  
  
* full module library  
* English + Arabic  
* advanced adaptive path  
* weekly AI reports  
* premium rewards/story packs  
* multiple child profiles  
  
**মূল্য:**  
  
* Bangladesh market: **৳199–৳399 / month** MVP stage  
* annual discount রাখা ভালো  
* diaspora pricing আলাদা রাখা যাবে later  
  
**অতিরিক্ত revenue later:**  
  
* school bundle  
* preschool licensing  
* printable worksheet pack  
* Ramadan / Eid / Bengali story thematic packs  
  
**যা করবেন না:**  
  
* ads  
* manipulative loot-box rewards  
* child-targeted upsell popups  
  
⸻  
  
🚀 এখনই শুরু করো (প্রথম ১ ঘণ্টা)  
  
**মিনিট ০-১৫:**  
  
* Notion-এ ১টা page খুলুন:  
    * App Name  
    * Age Groups  
    * MVP Modules  
    * Parent Needs  
    * Safety Rules  
* final নাম lock করুন: **শেখার তারা**  
  
**মিনিট ১৫-৩০:**  
  
* ৪টা core screen লিখুন:  
    1. Parent onboarding  
    2. Child home  
    3. Lesson screen  
    4. Parent dashboard  
* প্রতিটা screen-এর নিচে শুধু লিখুন: “user কী করবে?”  
  
**মিনিট ৩০-৪৫:**  
  
* Lovable.dev বা v0.dev-এ prompt দিন:  
    “Build a mobile-first child learning app with 4 screens: parent onboarding, child home, lesson player, parent dashboard. Soft colors, large buttons, Bangla-first UI, safe and ad-free.”  
  
**মিনিট ৪৫-৬০:**  
  
* Cursor-এ project খুলে এই ৩টা task দিন:  
    1. Supabase schema generate  
    2. lesson JSON structure তৈরি  
    3. stars reward logic add  
* আজকের শেষে goal: **clickable prototype**, full app না  
  
⸻  
  
**প্রথম ড্রাফটের সিদ্ধান্ত: কী আগে, কী পরে**  
  
**আগে:** Bangla + Math + parent dashboard + adaptive basics  
**পরে:** English, Arabic, creativity sandbox, advanced AI  
  
এটাই সঠিক কাট। কারণ MVP-এর কাজ হলো “শিশু engage করে কি না” আর “parent trust পায় কি না” — সব subject একসাথে launch করা না।  
  
⸻  
  
**build prompts (copy-paste ready)**  
  
**Lovable / v0 prompt:**  
Create a mobile-first educational app for children aged 3-9 called “শেখার তারা”.  
Core screens:  
  
1. Parent onboarding with child age-group selection  
2. Child home with today’s lesson, stars, and avatar  
3. Lesson player for Bangla letters and Math counting  
4. Parent dashboard with progress summary and screen-time controls  
  
Design rules:  
  
* Bangla-first  
* soft calming colors  
* large touch targets  
* ad-free  
* no chat  
* no external links  
* child-safe  
* age-friendly  
* reward with stars and stickers  
* no punishment language  
  
Use React/Next.js style components and clean card-based UI.  
  
**Cursor prompt:**  
Set up a Next.js + Supabase MVP for a child learning app.  
Implement:  
  
* parent auth  
* child profiles  
* lessons table  
* attempts table  
* simple adaptive logic: if score < 60, repeat easier variant; if score > 85, unlock next lesson  
* parent dashboard summary  
* secure row-level access by parent_id  
  
⸻  
  
**কঠিন সত্য, সহজ সিদ্ধান্ত**  
  
এই product-এর আসল magic “AI” না।  
আসল magic হলো:  
  
* age-appropriate UX  
* short lesson loop  
* consistent reward  
* parent trust  
* safe environment  
  
AI এখানে enhancer, engine না। MVP-তে এটুকু মাথায় রাখলে build অনেক দ্রুত হবে।  
  
⸻  
  
<div dir="rtl">وَقُلْ رَبِّ زِدْنِي عِلْمًا</div>  
“বলুন, হে আমার রব, আমার জ্ঞান বৃদ্ধি করুন।” — সূরা طه ২০:১১৪  
  
চাইলে আমি এখন এইটার **V2** হিসেবে সরাসরি  
**Notion-ready PRD + database schema + Lovable prompt pack** একসাথে লিখে দেব।  
  
  
21-মার্চ-2569  
