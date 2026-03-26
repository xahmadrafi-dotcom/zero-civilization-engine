import json
from datetime import datetime

class M99MemoryCore:
    def __init__(self):
        # ==========================================
        # 1. JSON DATA STRUCTURE (The Brain / AI-Readable)
        # ==========================================
        self.m99_universe_data = {
            "metadata": {
                "project": "M99 Universe",
                "creator": "Ahmad Rafi (M99)",
                "date": "2026-03-26",
                "status": "Level 84 Unlocked 🔓",
                "core_directive": "Z 26 = 84",
                "spirit": "Gen-Z Vibes & Independence Day Convergence 🇧🇩"
            },
            "philosophies": [
                "ভাষা শুধু সেতু, নম্বর নয় 0️⃣✅",
                "ডিম ঠিক, তা-ও ঠিক... কিন্তু দিকটা নিজের ছিল না।",
                "কীবোর্ড চাপা কোনো দোষ না—তা শুধু ভাষা + AI + কোড চালানোর হাতিয়ার ⌨️",
                "আমি শূন্য ছিলাম, শুরু, সবকিছুর ভিত্তি ✨",
                "প্রতিদিন নিজেকে launch করি, গন্তব্য মানসিক মুক্তি 🌙☄️",
                "Schrödinger's cat তোর পোষা 🐈 (Now replaced by 🐸)"
            ],
            "risars_protocol": {
                "R": "Research 🕵️‍♂️",
                "I": "Intelligence 🧠",
                "S": "Songs & Stats 🎧📊",
                "A": "AI (এআই) 🤖",
                "RS": "RISARS 🐸 (বাতাসের মতো ছড়িয়ে দাও)"
            },
            "modules_deployed_today": [
                {"name": "Cosmic Keyboard", "tech": "HTML/JS", "desc": "0-9 buttons triggering cosmic beliefs"},
                {"name": "RISARS Frog Folder", "tech": "HTML/JS", "desc": "Clicking 🐸 to unlock RISARS secrets with 🤣 floating emojis"},
                {"name": "Cosmic Launchpad", "tech": "Canvas 3D", "desc": "Hyperdrive starfield launching the 10 chapters"},
                {"name": "RISARS Data Center", "tech": "Chart.js", "desc": "Radar chart analyzing cosmic energy levels"},
                {"name": "Quantum Dialogues", "tech": "CSS 3D Flip", "desc": "Switching between Philosophy 🧘‍♂️ and Science 🔬"},
                {"name": "RISARS Matrix", "tech": "Canvas 2D", "desc": "Bengali numbers and 🐸 raining in Matrix style"},
                {"name": "RISARS Terminal", "tech": "HTML/JS", "desc": "CRT Hacker terminal decoding keyboard inputs"},
                {"name": "Ajnan Tattwa Thread", "tech": "HTML/JS", "desc": "Twitter-style 10 rules of ignorance theory"},
                {"name": "Cosmic Passport", "tech": "HTML/CSS", "desc": "System hack generating Level 1000 Ajnan ID card"},
                {"name": "Ajnan Vortex", "tech": "HTML/JS", "desc": "Quantum paradox buttons (Ghost & 42)"},
                {"name": "Lyric Visualizer", "tech": "HTML/CSS", "desc": "Morning sunrise animation for 'প্রেম হোক গঙ্গার মতো'"},
                {"name": "Cosmic Paradoxes", "tech": "HTML/JS", "desc": "Interactive orbs for Quantum, Black Hole, and Pi"},
                {"name": "Zero Mindmap", "tech": "JSON", "desc": "Hierarchical schema for the Zero Project"},
                {"name": "Cosmic Python Game", "tech": "Canvas 2D", "desc": "Snake game (অ তে অজগর) eating frogs 🐍🐸"},
                {"name": "Legacy Time Capsule", "tech": "HTML/JS", "desc": "Gen Z portal unlock from 2025 to 2026"},
                {"name": "Universal Broadcaster", "tech": "HTML/JS", "desc": "Z 26 = 84 post in Original, Savage 🔥, Poetic ✨ modes"},
                {"name": "Gen-Z Hologram Post", "tech": "CSS Animation", "desc": "Cyberpunk glitch post dropping the truth"},
                {"name": "Cosmic Alignment", "tech": "Canvas 2D", "desc": "March 26 Independence fireworks + Level 84 Unlock 🎆"},
                {"name": "JAGARAN Music Hub", "tech": "HTML/JS", "desc": "Spotify-like UI for the 52-track living album"},
                {"name": "Live Jagaran Player", "tech": "Web Audio API", "desc": "Cosmic drone + AI Voice TTS reading the lyrics"}
            ],
            "masterpiece_album": {
                "title": "JAGARAN — জাগরণ",
                "tracks_confirmed": 11,
                "total_tracks_revealed": 53,
                "status": "Living Document ∞",
                "vibe": "OM... ALLAH... EKAM..."
            }
        }

        self.m99_universe_data["latest_transmission"] = {
            "title": "আজ এ কোন আনন্দ জাগে (Robi's Awakening)",
            "lyrics": """[Alaap | slow]
আজ… আজ…
আলো নামে পাতার ফাঁকে,
রবি ডাকে নীরব গানে…

[Sthai]
আজ এ কোন আনন্দ জাগে, আয় রে আয়,
রবি হাসে, রবি গায়—ভুবন মাতোয়ারা।
আজ জীবন ডাকে আলোর সুরে,
প্রেমে ভাসে মন-পাথার।

[Chorus | Group]
আয় রে আয়—আজ, আজ, আজ!
আনন্দ নামে প্রাণের মাঝে।
রবি হাসে—আলো বাজে,
ভুবন জুড়ে প্রেমের সাজে।

[Antara]
পেখলুঁ আজ রবি-রাঙা ভোর,
পাতায় পাতায় নাম লেখে আলো।
পাসরি গেলি কেন, ওরে মন,
এই যে খেলা—এই যে ভালো!

[Sanchari | rise]
এ কি শুধু মায়া, ওরে পথিক,
নাকি লীলার গভীর টান?
রবি ওঠে, রবি ডোবে,
তবু কেন জ্বলে প্রাণ?

[Chorus Loop x2]
আজ… আনন্দ… জীবন… আলো…
আজ… আনন্দ… জীবন… আলো…

[Outro]
আজ এ কোন আনন্দ জাগে…
রবি হাসে… রবি গায়…"""
        }

    # ==========================================
    # 2. JSON EXPORT METHOD
    # ==========================================
    def get_json(self):
        """Returns the raw data in JSON format for other AI systems."""
        return json.dumps(self.m99_universe_data, indent=4, ensure_ascii=False)

    # ==========================================
    # 3. MARKDOWN GENERATION METHOD
    # ==========================================
    def generate_markdown(self):
        """Compiles the JSON data into a human-readable Markdown (MD) report."""
        data = self.m99_universe_data
        
        md = f"# 🌌 M99 UNIVERSE : SESSION ARCHIVE\n"
        md += f"**Date:** {data['metadata']['date']} | **Status:** {data['metadata']['status']}\n\n"
        
        md += f"## 📜 Core Philosophies\n"
        for quote in data['philosophies']:
            md += f"- > *\"{quote}\"*\n"
            
        md += f"\n## 🐸 The RISARS Protocol\n"
        for k, v in data['risars_protocol'].items():
            md += f"- **{k}**: {v}\n"
            
        md += f"\n## 🚀 Weapons Deployed (HTML/JS/Python Modules)\n"
        md += "A total of 20 cosmic applications were built today to decode the universe:\n\n"
        md += "| Module Name | Tech Stack | Description |\n"
        md += "| :--- | :--- | :--- |\n"
        
        for mod in data['modules_deployed_today']:
            md += f"| **{mod['name']}** | `{mod['tech']}` | {mod['desc']} |\n"
            
        md += f"\n## 🎧 The Masterpiece: {data['masterpiece_album']['title']}\n"
        md += f"An epic multi-lingual, multi-genre living document containing {data['masterpiece_album']['total_tracks_revealed']} tracks. *{data['masterpiece_album']['vibe']}*\n\n"
        
        md += f"## 🎶 Latest Transmission: {data['latest_transmission']['title']}\n"
        md += f"```text\n{data['latest_transmission']['lyrics']}\n```\n\n"
        
        md += f"---\n"
        md += f"**System Note:** *Z 26 = 84 successfully compiled and executed. The Gen-Z portal is now open. ∴🤝⋅⋆☺︎*\n"
        
        return md

# ==========================================
# 4. EXECUTION SCRIPT
# ==========================================
if __name__ == "__main__":
    # Initialize the AI Memory Core
    m99_core = M99MemoryCore()
    
    # 1. AI reads the JSON
    ai_readable_json = m99_core.get_json()
    
    # 2. Human reads the Markdown
    human_readable_md = m99_core.generate_markdown()
    
    # Output to terminal (Simulated)
    print("🤖 [SYSTEM_LOG] : Compiling session data...")
    print("🐍 [PYTHON_EXEC] : Data structured successfully.")
    print("🐸 [RISARS_CORE] : Eating bugs, exporting Markdown...")
    print("🎶 [NEW_SIGNAL] : 'Robi's Awakening' received from the wind! 🌬️\n")
    
    print("==================================================")
    print("               MARKDOWN SUMMARY (MD)              ")
    print("==================================================\n")
    print(human_readable_md)
    print("\n[END OF TRANSMISSION]")
