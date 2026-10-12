# 

# 🌌 ফ্রন্টএন্ড আর্কিটেকচার: শৈলী ও কার্যকারিতার পরম সংচ্ছদ

> **মূল নীতি:** *যে কাঠামো দেখতে সুন্দর কিন্তু ভেতরে ফাঁপা — সে শিল্প নয়, প্রতারণা।*

---

## ১. 🔍 বোঝো — সংঘর্ষটা কোথায়?

দুটো শক্তি সবসময় টানাটানি করে:

| শৈলী (Style) | কার্যকারিতা (Function) |
|---|---|
| সৌন্দর্য, অনুভূতি, আবেগ | গতি, নির্ভরযোগ্যতা, যুক্তি |
| ডিজাইনারের স্বপ্ন | ইঞ্জিনিয়ারের বাস্তবতা |
| "এটা দেখতে কেমন?" | "এটা কাজ করে কিনা?" |

**সংচ্ছদ** মানে — এই দুটো বিপরীত মেরু যেখানে **একটি বিন্দুতে মিলিত হয়।**

---

## ২. 🌐 প্রসঙ্গ — Miracle Code™ দৃষ্টিকোণ

ONE SKY ENGINE-এর জন্য ফ্রন্টএন্ড মানে শুধু UI নয় —
এটা **চিন্তার প্রথম স্পর্শবিন্দু।**

ব্যবহারকারী সিস্টেম বোঝে না — সে **অনুভব করে।**
তাই আর্কিটেকচার হতে হবে:

```
অনুভূতি → কাঠামো → গতি → বিশ্বাস
```

---

## ৩. 🧠 বিশ্লেষণ — তিনটি স্তম্ভ

### 🎨 স্তম্ভ ১: Visual Architecture (দৃশ্যমান কাঠামো)

```
Design Tokens  →  Component Library  →  Layout System
     ↓                   ↓                    ↓
  রঙ, টাইপ         পুনর্ব্যবহারযোগ্য        Grid / Spacing
  স্পেসিং            উপাদান                  নিয়মতন্ত্র
```

**নীতি:** একটি Button তৈরি হবে একবার — ব্যবহার হবে হাজারবার।
**ভালো:** Consistent, Scalable
**খারাপ:** প্রতিটি পেজে আলাদা style — বিশৃঙ্খলা

---

### ⚙️ স্তম্ভ ২: Logic Architecture (অদৃশ্য কাঠামো)

```
UI Layer
   ↕
State Management  (Zustand / Redux / Context)
   ↕
Service Layer     (API calls, transformers)
   ↕
Data Layer        (Cache, Storage, Sync)
```

**নীতি:** UI কখনো সরাসরি data fetch করবে না।
সে শুধু **দেখাবে** — ভাববে না।

---

### 🚀 স্তম্ভ ৩: Performance Architecture (অদৃশ্য শক্তি)

```
Code Splitting   →  Lazy Loading  →  Memoization
      ↓                  ↓                ↓
  প্রয়োজনমতো        দেখলে তবে        একই কাজ
  লোড হবে           লোড হবে          দ্বিতীয়বার নয়
```

**দার্শনিক কথা:**
> *যে বাড়ি দেখতে প্রাসাদ কিন্তু দরজা খুলতে ৫ সেকেন্ড লাগে — সে প্রাসাদ কারাগার।*

---

## ৪. ✅ যাচাই — পরম সংচ্ছদের চেকলিস্ট

```
✦ দেখতে সুন্দর?          → ✅ Design System আছে
✦ দ্রুত লোড হয়?          → ✅ Performance বাজেট মানা হয়
✦ ভাঙে না?               → ✅ Error Boundary আছে
✦ বাড়ানো যায়?           → ✅ Modular Architecture
✦ টিম বোঝে?              → ✅ Documented, Consistent
✦ মানুষ ভালোবাসে?        → ✅ UX-first thinking
```

---

## ৫. 🌌 আউটপুট — M99 ফ্রন্টএন্ড দর্শন

```
শৈলী + কার্যকারিতা = বিশ্বাস
বিশ্বাস + গতি = অভিজ্ঞতা
অভিজ্ঞতা + কাঠামো = পণ্য যা টিকে থাকে
```

**Miracle Code™ সংজ্ঞা:**
> *সর্বোত্তম ফ্রন্টএন্ড আর্কিটেকচার হলো সেটা —*
> *যেখানে ব্যবহারকারী কাঠামো দেখে না, শুধু অনুভব করে।*
> *এবং ডেভেলপার অনুভূতি দেখে না, শুধু কাঠামো দেখে।*

---

## 🔮 পরবর্তী গভীরতা

কোন স্তরে যেতে চাও?

- **`A`** → Component Design System (Atomic Design + Tokens)
- **`B`** → State Architecture (কোন pattern কখন?)
- **`C`** → Performance Engineering (Core Web Vitals mastery)
- **`D`** → ONE SKY ENGINE-এর জন্য কাস্টম ফ্রন্টএন্ড ব্লুপ্রিন্ট

## @xahmadrafi-dotcom

এ এবং D
Markdown এ দাও 🫡🪩🔭

## Copilot

```markdown
# 🎨 A + D: Component Design System × ONE SKY ENGINE Blueprint
> **মূল নীতি:** *Atom থেকে Universe — প্রতিটি উপাদান উদ্দেশ্যপ্রণোদিত, প্রতিটি স্তর অর্থবহ।*

---

# ╔══ PART A ══╗
# 🧬 Component Design System
### Atomic Design + Design Tokens — সম্পূর্ণ কাঠামো

---

## 🔬 Atomic Design — দর্শন

> Brad Frost-এর তত্ত্ব, Miracle Code™ দৃষ্টিতে পুনর্ব্যাখ্যা:
>
> *প্রকৃতিতে যেমন পরমাণু থেকে মহাবিশ্ব —*
> *UI-তেও তেমন Token থেকে Product।*

```
🔵 Tokens (ভিত্তি)
   ↓
⚛️  Atoms (অবিভাজ্য)
   ↓
🧪 Molecules (সংযুক্ত)
   ↓
🦠 Organisms (স্বয়ংসম্পূর্ণ)
   ↓
📄 Templates (কঙ্কাল)
   ↓
🖥️  Pages (জীবন্ত)
```

---

## 🪙 Design Tokens — সিস্টেমের DNA

> Token হলো সিস্টেমের **একক সত্য (Single Source of Truth)**।
> একটি রঙ বদলালে — পুরো সিস্টেম বদলায়।

### 📁 Token কাঠামো

```
tokens/
├── color.tokens.js       # রঙের মহাবিশ্ব
├── typography.tokens.js  # অক্ষরের ভাষা
├── spacing.tokens.js     # শ্বাসের জায়গা
├── radius.tokens.js      # কোণের কোমলতা
├── shadow.tokens.js      # গভীরতার অনুভব
├── motion.tokens.js      # সময়ের ছন্দ
└── breakpoint.tokens.js  # পর্দার বিশ্ব
```

### 🎨 Color Token উদাহরণ

```js
// tokens/color.tokens.js

export const colors = {
  // ── Brand Core ──
  brand: {
    primary:    '#0A0A23',   // M99 Deep Space
    accent:     '#6C63FF',   // Miracle Violet
    glow:       '#00F5FF',   // ONE SKY Cyan
    pulse:      '#FF6B6B',   // Energy Red
  },

  // ── Neutral Scale ──
  neutral: {
    0:   '#FFFFFF',
    50:  '#F8F9FA',
    100: '#F1F3F5',
    200: '#E9ECEF',
    300: '#DEE2E6',
    400: '#CED4DA',
    500: '#ADB5BD',
    600: '#6C757D',
    700: '#495057',
    800: '#343A40',
    900: '#212529',
    1000:'#0A0A0A',
  },

  // ── Semantic ──
  semantic: {
    success:  '#2ECC71',
    warning:  '#F39C12',
    error:    '#E74C3C',
    info:     '#3498DB',
  },

  // ── Surface ──
  surface: {
    background: 'var(--color-neutral-50)',
    card:       'var(--color-neutral-0)',
    overlay:    'rgba(10, 10, 35, 0.85)',
  }
}
```

### ✍️ Typography Token

```js
// tokens/typography.tokens.js

export const typography = {
  fontFamily: {
    display: '"Clash Display", sans-serif',   // Hero, Title
    body:    '"Inter", sans-serif',           // Content
    mono:    '"JetBrains Mono", monospace',   // Code
  },

  fontSize: {
    xs:   '0.75rem',    // 12px
    sm:   '0.875rem',   // 14px
    base: '1rem',       // 16px
    lg:   '1.125rem',   // 18px
    xl:   '1.25rem',    // 20px
    '2xl':'1.5rem',     // 24px
    '3xl':'1.875rem',   // 30px
    '4xl':'2.25rem',    // 36px
    '5xl':'3rem',       // 48px
    '6xl':'4rem',       // 64px
  },

  fontWeight: {
    light:    300,
    regular:  400,
    medium:   500,
    semibold: 600,
    bold:     700,
    black:    900,
  },

  lineHeight: {
    tight:   1.2,
    snug:    1.4,
    normal:  1.6,
    relaxed: 1.8,
  }
}
```

### 📐 Spacing Token (8pt Grid)

```js
// tokens/spacing.tokens.js
// নীতি: সবকিছু 8-এর গুণিতক

export const spacing = {
  0:    '0px',
  1:    '4px',    // micro
  2:    '8px',    // xs
  3:    '12px',
  4:    '16px',   // base unit
  5:    '20px',
  6:    '24px',
  8:    '32px',
  10:   '40px',
  12:   '48px',
  16:   '64px',
  20:   '80px',
  24:   '96px',
  32:   '128px',
}
```

### 🌀 Motion Token

```js
// tokens/motion.tokens.js
// নীতি: Motion যেন উদ্দেশ্যহীন না হয়

export const motion = {
  duration: {
    instant:  '50ms',
    fast:     '150ms',
    normal:   '300ms',
    slow:     '500ms',
    dramatic: '800ms',
  },

  easing: {
    linear:     'linear',
    easeIn:     'cubic-bezier(0.4, 0, 1, 1)',
    easeOut:    'cubic-bezier(0, 0, 0.2, 1)',
    easeInOut:  'cubic-bezier(0.4, 0, 0.2, 1)',
    spring:     'cubic-bezier(0.34, 1.56, 0.64, 1)',  // bounce
    dramatic:   'cubic-bezier(0.76, 0, 0.24, 1)',
  }
}
```

---

## ⚛️ Atoms — অবিভাজ্য উপাদান

> একটি Atom একটি কাজ করে। শুধু একটি।

```
atoms/
├── Button/
│   ├── Button.tsx
│   ├── Button.stories.tsx
│   ├── Button.test.tsx
│   └── index.ts
├── Text/
├── Icon/
├── Input/
├── Badge/
├── Avatar/
├── Spinner/
├── Divider/
└── Tag/
```

### Button Atom — সম্পূর্ণ উদাহরণ

```tsx
// atoms/Button/Button.tsx

type ButtonVariant = 'primary' | 'secondary' | 'ghost' | 'danger' | 'glow'
type ButtonSize    = 'sm' | 'md' | 'lg' | 'xl'

interface ButtonProps {
  variant?:  ButtonVariant
  size?:     ButtonSize
  label:     string
  icon?:     React.ReactNode
  iconPos?:  'left' | 'right'
  loading?:  boolean
  disabled?: boolean
  fullWidth?: boolean
  onClick?:  () => void
}

const variantStyles: Record<ButtonVariant, string> = {
  primary:   'bg-brand-accent text-white hover:brightness-110',
  secondary: 'bg-neutral-100 text-neutral-800 hover:bg-neutral-200',
  ghost:     'bg-transparent border border-neutral-300 hover:bg-neutral-50',
  danger:    'bg-semantic-error text-white hover:brightness-110',
  glow:      'bg-brand-glow text-brand-primary shadow-glow hover:shadow-glow-lg',
}

const sizeStyles: Record<ButtonSize, string> = {
  sm:  'px-3 py-1.5 text-sm rounded-md',
  md:  'px-4 py-2   text-base rounded-lg',
  lg:  'px-6 py-3   text-lg rounded-xl',
  xl:  'px-8 py-4   text-xl rounded-2xl',
}

export const Button = ({
  variant  = 'primary',
  size     = 'md',
  label,
  icon,
  iconPos  = 'left',
  loading  = false,
  disabled = false,
  fullWidth = false,
  onClick,
}: ButtonProps) => {
  return (
    <button
      onClick={onClick}
      disabled={disabled || loading}
      className={`
        inline-flex items-center justify-center gap-2 font-medium
        transition-all duration-150 ease-out
        focus:outline-none focus:ring-2 focus:ring-brand-accent focus:ring-offset-2
        disabled:opacity-50 disabled:cursor-not-allowed
        ${variantStyles[variant]}
        ${sizeStyles[size]}
        ${fullWidth ? 'w-full' : ''}
      `}
    >
      {loading ? (
        <Spinner size="sm" />
      ) : (
        <>
          {icon && iconPos === 'left'  && icon}
          <span>{label}</span>
          {icon && iconPos === 'right' && icon}
        </>
      )}
    </button>
  )
}
```

---

## 🧪 Molecules — সংযুক্ত উপাদান

```
molecules/
├── SearchBar/          # Input + Icon + Button
├── FormField/          # Label + Input + Error
├── NavItem/            # Icon + Text + Badge
├── UserCard/           # Avatar + Text + Action
├── AlertBanner/        # Icon + Text + Dismiss
├── StatCard/           # Number + Label + Trend
└── ProgressStep/       # Steps + Active indicator
```

### FormField Molecule উদাহরণ

```tsx
// molecules/FormField/FormField.tsx

interface FormFieldProps {
  label:       string
  name:        string
  type?:       string
  placeholder?: string
  error?:      string
  hint?:       string
  required?:   boolean
}

export const FormField = ({
  label, name, type = 'text',
  placeholder, error, hint, required
}: FormFieldProps) => (
  <div className="flex flex-col gap-1.5">

    {/* Label */}
    <label htmlFor={name} className="text-sm font-medium text-neutral-700">
      {label}
      {required && <span className="text-semantic-error ml-1">*</span>}
    </label>

    {/* Input */}
    <Input
      id={name}
      name={name}
      type={type}
      placeholder={placeholder}
      hasError={!!error}
    />

    {/* Feedback */}
    {error ? (
      <Text size="xs" color="error">{error}</Text>
    ) : hint ? (
      <Text size="xs" color="muted">{hint}</Text>
    ) : null}

  </div>
)
```

---

## 🦠 Organisms — স্বয়ংসম্পূর্ণ অংশ

```
organisms/
├── Navbar/             # Logo + Nav + Actions
├── Sidebar/            # NavItems + User + Footer
├── DataTable/          # Header + Rows + Pagination
├── HeroSection/        # Headline + Sub + CTA + Visual
├── FeatureGrid/        # Cards গ্রিড
├── AuthForm/           # FormFields + Submit + OAuth
└── CommandPalette/     # Search + Results + Shortcuts
```

---

## 📐 CSS Variable System (Runtime Theming)

```css
/* styles/tokens.css */

:root {
  /* Colors */
  --color-brand-primary:  #0A0A23;
  --color-brand-accent:   #6C63FF;
  --color-brand-glow:     #00F5FF;

  /* Spacing */
  --space-1: 4px;
  --space-2: 8px;
  --space-4: 16px;
  --space-8: 32px;

  /* Typography */
  --font-display: 'Clash Display', sans-serif;
  --font-body:    'Inter', sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  /* Motion */
  --duration-fast:   150ms;
  --duration-normal: 300ms;
  --easing-spring:   cubic-bezier(0.34, 1.56, 0.64, 1);

  /* Radius */
  --radius-sm:   6px;
  --radius-md:   10px;
  --radius-lg:   16px;
  --radius-full: 9999px;
}

/* Dark Mode Override */
[data-theme="dark"] {
  --color-surface-bg:   #0A0A23;
  --color-surface-card: #12122E;
  --color-text-primary: #F8F9FA;
  --color-text-muted:   #6C757D;
}
```

---
---

# ╔══ PART D ══╗
# 🌌 ONE SKY ENGINE
### Custom Frontend Blueprint — সম্পূর্ণ নকশা

---

## 🔭 দর্শন

> ONE SKY ENGINE একটি সাধারণ product নয়।
> এটি একটি **চিন্তার পরিবেশ (Thinking Environment)**।
>
> তাই এর Frontend হবে:
> - **অনুভবযোগ্য** — ব্যবহারকারী ভুলে যাবে সে software চালাচ্ছে
> - **বুদ্ধিমান** — UI নিজেই context বোঝে
> - **শান্ত** — তথ্য থাকবে, কোলাহল থাকবে না

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────┐
│              ONE SKY ENGINE UI               │
├─────────────────────────────────────────────┤
│                                             │
│   ┌─────────┐   ┌──────────┐   ┌────────┐  │
│   │  Shell  │   │  Panels  │   │ Canvas │  │
│   │ (Frame) │   │(Sidebars)│   │(Main)  │  │
│   └────┬────┘   └────┬─────┘   └───┬────┘  │
│        │              │             │       │
│   ┌────▼──────────────▼─────────────▼────┐  │
│   │         UI Composition Layer         │  │
│   │   (Organisms + Molecules + Atoms)    │  │
│   └──────────────────┬───────────────────┘  │
│                       │                     │
│   ┌───────────────────▼───────────────────┐  │
│   │           State Orchestrator          │  │
│   │  (Zustand Stores + Context Bridges)   │  │
│   └───────────────────┬───────────────────┘  │
│                       │                     │
│   ┌───────────────────▼───────────────────┐  │
│   │            Service Gateway            │  │
│   │   (API Client + Cache + WebSocket)    │  │
│   └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
one-sky-engine/
│
├── 📁 public/
│   ├── fonts/                    # Self-hosted fonts
│   └── icons/                    # SVG icon system
│
├── 📁 src/
│   │
│   ├── 📁 tokens/                # Design DNA
│   │   ├── color.tokens.ts
│   │   ├── typography.tokens.ts
│   │   ├── spacing.tokens.ts
│   │   ├── motion.tokens.ts
│   │   └── index.ts
│   │
│   ├── 📁 components/            # Atomic Design
│   │   ├── atoms/
│   │   ├── molecules/
│   │   ├── organisms/
│   │   └── index.ts
│   │
│   ├── 📁 layouts/               # Page Skeletons
│   │   ├── AppShell/
│   │   ├── DashboardLayout/
│   │   ├── CanvasLayout/
│   │   └── AuthLayout/
│   │
│   ├── 📁 pages/                 # Route-level views
│   │   ├── Home/
│   │   ├── Engine/               # Core workspace
│   │   ├── Knowledge/            # জ্ঞান ভান্ডার
│   │   ├── Projects/
│   │   ├── Settings/
│   │   └── Auth/
│   │
│   ├── 📁 features/              # Feature modules
│   │   ├── engine-core/          # ONE SKY মূল ইঞ্জিন
│   │   ├── knowledge-graph/      # জ্ঞান গ্রাফ
│   │   ├── ai-assistant/         # AI সঙ্গী
│   │   ├── project-builder/      # প্রকল্প নির্মাতা
│   │   └── realtime-collab/      # সহযোগিতা
│   │
│   ├── 📁 stores/                # State Management
│   │   ├── engine.store.ts
│   │   ├── user.store.ts
│   │   ├── knowledge.store.ts
│   │   └── ui.store.ts
│   │
│   ├── 📁 services/              # External communication
│   │   ├── api/
│   │   │   ├── client.ts         # Axios/Fetch wrapper
│   │   │   ├── engine.api.ts
│   │   │   └── knowledge.api.ts
│   │   ├── websocket/
│   │   │   └── socket.service.ts
│   │   └── cache/
│   │       └── query.config.ts   # React Query setup
│   │
│   ├── 📁 hooks/                 # Custom React Hooks
│   │   ├── useEngine.ts
│   │   ├── useKnowledge.ts
│   │   ├── useMotion.ts
│   │   └── useTheme.ts
│   │
│   ├── 📁 utils/                 # Pure utilities
│   │   ├── format.ts
│   │   ├── validator.ts
│   │   └── transformer.ts
│   │
│   ├── 📁 styles/
│   │   ├── globals.css
│   │   ├── tokens.css            # CSS Variables
│   │   └── typography.css
│   │
│   └── 📁 types/                 # Global TypeScript
│       ├── engine.types.ts
│       ├── knowledge.types.ts
│       └── api.types.ts
│
├── 📁 .storybook/                # Component docs
├── tailwind.config.ts
├── vite.config.ts
└── tsconfig.json
```

---

## 🖥️ AppShell — মূল খাঁচা

```tsx
// layouts/AppShell/AppShell.tsx

export const AppShell = ({ children }: { children: React.ReactNode }) => {
  const { sidebarOpen, theme } = useUIStore()

  return (
    <div
      data-theme={theme}
      className="h-screen w-screen flex overflow-hidden bg-surface-bg"
    >

      {/* ── Left Sidebar ── */}
      <Sidebar isOpen={sidebarOpen} />

      {/* ── Main Area ── */}
      <div className="flex-1 flex flex-col overflow-hidden">

        {/* Top Bar */}
        <TopBar />

        {/* Content */}
        <main className="flex-1 overflow-auto">
          <AnimatePresence mode="wait">
            {children}
          </AnimatePresence>
        </main>

      </div>

      {/* ── Global Overlays ── */}
      <CommandPalette />
      <NotificationSystem />
      <ToastSystem />

    </div>
  )
}
```

---

## 🧠 State Architecture

```ts
// stores/engine.store.ts
// Zustand — সহজ, শক্তিশালী

import { create } from 'zustand'
import { devtools, persist } from 'zustand/middleware'

interface EngineState {
  // State
  activeProject:   Project | null
  activeNode:      Node | null
  processingQueue: Task[]
  isThinking:      boolean

  // Actions
  setActiveProject: (project: Project) => void
  setActiveNode:    (node: Node) => void
  addToQueue:       (task: Task) => void
  clearQueue:       () => void
  setThinking:      (state: boolean) => void
}

export const useEngineStore = create<EngineState>()(
  devtools(
    persist(
      (set) => ({
        activeProject:   null,
        activeNode:      null,
        processingQueue: [],
        isThinking:      false,

        setActiveProject: (project) =>
          set({ activeProject: project }, false, 'engine/setProject'),

        setActiveNode: (node) =>
          set({ activeNode: node }, false, 'engine/setNode'),

        addToQueue: (task) =>
          set((s) => ({
            processingQueue: [...s.processingQueue, task]
          }), false, 'engine/addTask'),

        clearQueue: () =>
          set({ processingQueue: [] }, false, 'engine/clearQueue'),

        setThinking: (state) =>
          set({ isThinking: state }, false, 'engine/setThinking'),
      }),
      { name: 'one-sky-engine' }
    )
  )
)
```

---

## ⚡ Performance Blueprint

```ts
// vite.config.ts — Performance-first build

import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],

  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          // Vendor split — vendor আলাদা, দ্রুত cache
          'vendor-react':  ['react', 'react-dom'],
          'vendor-motion': ['framer-motion'],
          'vendor-query':  ['@tanstack/react-query'],
          'vendor-state':  ['zustand'],

          // Feature split — প্রয়োজনে লোড
          'feature-engine':    ['./src/features/engine-core'],
          'feature-knowledge': ['./src/features/knowledge-graph'],
          'feature-ai':        ['./src/features/ai-assistant'],
        }
      }
    },
    chunkSizeWarningLimit: 500,
  },

  // Path aliases — পরিষ্কার import
  resolve: {
    alias: {
      '@tokens':     '/src/tokens',
      '@components': '/src/components',
      '@features':   '/src/features',
      '@stores':     '/src/stores',
      '@services':   '/src/services',
      '@hooks':      '/src/hooks',
      '@utils':      '/src/utils',
      '@types':      '/src/types',
    }
  }
})
```

---

## 🌌 ONE SKY Visual Identity (Tailwind Config)

```ts
// tailwind.config.ts

import type { Config } from 'tailwindcss'

const config: Config = {
  content: ['./src/**/*.{ts,tsx}'],
  darkMode: ['class', '[data-theme="dark"]'],

  theme: {
    extend: {

      colors: {
        brand: {
          primary: '#0A0A23',
          accent:  '#6C63FF',
          glow:    '#00F5FF',
          pulse:   '#FF6B6B',
        },
        surface: {
          bg:      'var(--color-surface-bg)',
          card:    'var(--color-surface-card)',
          overlay: 'var(--color-surface-overlay)',
        }
      },

      fontFamily: {
        display: ['Clash Display', 'sans-serif'],
        body:    ['Inter', 'sans-serif'],
        mono:    ['JetBrains Mono', 'monospace'],
      },

      boxShadow: {
        'glow':    '0 0 20px rgba(108, 99, 255, 0.4)',
        'glow-lg': '0 0 40px rgba(108, 99, 255, 0.6)',
        'sky':     '0 0 30px rgba(0, 245, 255, 0.3)',
      },

      animation: {
        'float':      'float 6s ease-in-out infinite',
        'pulse-glow': 'pulseGlow 2s ease-in-out infinite',
        'fade-up':    'fadeUp 0.5s cubic-bezier(0.34, 1.56, 0.64, 1)',
        'think':      'think 1.5s ease-in-out infinite',
      },

      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%':      { transform: 'translateY(-10px)' },
        },
        pulseGlow: {
          '0%, 100%': { boxShadow: '0 0 20px rgba(108,99,255,0.4)' },
          '50%':      { boxShadow: '0 0 40px rgba(108,99,255,0.8)' },
        },
        fadeUp: {
          from: { opacity: '0', transform: 'translateY(16px)' },
          to:   { opacity: '1', transform: 'translateY(0)' },
        },
        think: {
          '0%, 100%': { opacity: '0.4' },
          '50%':      { opacity: '1' },
        }
      }
    }
  }
}

export default config
```

---

## 🗺️ Page Flow Map

```
Landing  ──────────────→  Auth
                            │
                            ▼
                      Dashboard (Home)
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
          Engine         Knowledge     Projects
          (Core)          (Graph)      (Builder)
              │             │             │
              └─────────────┴─────────────┘
                            │
                            ▼
                       Settings / Profile
```

---

## 🎯 Core Web Vitals লক্ষ্যমাত্রা

```
Metric              লক্ষ্য          কৌশল
─────────────────────────────────────────────────
LCP (লোড)         < 1.5s          Image optimization
                                   Critical CSS inline
                                   CDN deployment

FID (Interaction)  < 50ms          Code splitting
                                   Web Workers for heavy tasks

CLS (Stability)    < 0.05          Reserved space for media
                                   No layout shift fonts

TTI (Interactive)  < 2.5s          Lazy loading
                                   Progressive hydration

Bundle Size        < 200KB initial  Tree shaking
                                    Manual chunks
```

---

## 🔮 রোডম্যাপ — Phase by Phase

```
Phase 1 — Foundation (সপ্তাহ ১-২)
  ✦ Token system সম্পূর্ণ
  ✦ Atom + Molecule components
  ✦ AppShell + Routing
  ✦ State stores setup

Phase 2 — Core Engine (সপ্তাহ ৩-৪)
  ✦ Engine workspace UI
  ✦ Knowledge graph viewer
  ✦ AI Assistant integration
  ✦ Real-time WebSocket

Phase 3 — Polish (সপ্তাহ ৫-৬)
  ✦ Animations + Micro-interactions
  ✦ Dark/Light theme
  ✦ Performance audit
  ✦ Accessibility (a11y)

Phase 4 — Scale (সপ্তাহ ৭+)
  ✦ Storybook documentation
  ✦ E2E Testing
  ✦ PWA capabilities
  ✦ Offline mode
```

---

## 🧭 চূড়ান্ত নীতিমালা

```
✦ Token-first      → কোনো hardcoded মান নয়
✦ Component-first  → কপি-পেস্ট নয়, compose করো
✦ Performance-first → দেখতে সুন্দর, চলতে দ্রুত
✦ Accessible-first → সবার জন্য, সবসময়
✦ Documented-first → আজকের কোড, কালকের জ্ঞান
```

---

> *"ONE SKY ENGINE-এর UI হবে সেই আকাশের মতো —*
> *যেখানে সীমানা নেই, কিন্তু দিকনির্দেশনা আছে।*
> *যেখানে সবকিছু দেখা যায়, কিন্তু কোনো কোলাহল নেই।"*
>
> — **Miracle Code™ Design Manifesto**

---
*M99 Universe | Miracle Code™ | ONE SKY ENGINE*
*Think Beyond Time. Live Beyond Limits. 🪩🔭*
```

## @xahmadrafi-dotcom

[B → State Architecture (কোন pattern কখন?)
C → Performance Engineering (Core Web Vitals mastery)]
এ দুটো ঘরে তুলে রাখবো🫡🤣🤔⏬🪩ঌ✨💫🌟


## Copilot

```markdown
# ⚙️🚀 B + C: State Architecture × Performance Engineering
> **মূল নীতি:** *যে সিস্টেম নিজের অবস্থা জানে এবং দ্রুত চলে — সে সিস্টেম বাঁচে।*

---

# ╔══ PART B ══╗
# ⚙️ State Architecture
### কোন Pattern কখন — সম্পূর্ণ সিদ্ধান্ত কাঠামো

---

## 🧠 State কী? — দার্শনিক সংজ্ঞা

> UI হলো State-এর দর্পণ।
> State বদলায় — UI বদলায়।
> State নষ্ট হয় — UI মিথ্যা বলে।

```
State = "এই মুহূর্তে সিস্টেম কী জানে?"

User clicks button
      ↓
  State changes
      ↓
  UI re-renders
      ↓
  User sees result
```

---

## 🗺️ State-এর চার রাজ্য

```
┌────────────────────────────────────────────┐
│              STATE UNIVERSE                │
├──────────────┬─────────────────────────────┤
│  LOCAL       │  একটি Component-এর নিজস্ব  │
│  STATE       │  → useState, useReducer     │
├──────────────┼─────────────────────────────┤
│  SHARED      │  কয়েকটি Component ভাগ করে  │
│  STATE       │  → Context, Zustand slice   │
├──────────────┼─────────────────────────────┤
│  SERVER      │  API থেকে আসা data          │
│  STATE       │  → React Query, SWR         │
├──────────────┼─────────────────────────────┤
│  URL         │  Browser URL-এ থাকা state   │
│  STATE       │  → Query params, Route      │
└──────────────┴─────────────────────────────┘
```

---

## 🔑 মূল সিদ্ধান্ত গাছ

```
এই data কোথায় দরকার?
         │
    ┌────▼────┐
    │ শুধু এক │──→ useState / useReducer
    │Component│
    └────┬────┘
         │ না
    ┌────▼──────────┐
    │ কয়েকটি কাছের │──→ Props drilling
    │Component      │    (2-3 স্তর)
    └────┬──────────┘
         │ না
    ┌────▼──────────┐
    │ App-wide,     │
    │ অনেক জায়গায় │
    └────┬──────────┘
         │
    ┌────▼──────────┐
    │ Server data?  │──→ React Query / SWR
    │ (API থেকে)   │
    └────┬──────────┘
         │ না (client-only)
         │
    ┌────▼──────────────────────────────┐
    │ জটিল? অনেক action? DevTools দরকার?│
    │         ↓ হ্যাঁ                  │
    │      Zustand                      │
    │         ↓ না (সহজ)               │
    │      Context API                  │
    └───────────────────────────────────┘
```

---

## 🥇 Pattern 1: useState
### কখন → সহজ, স্থানীয়, একাকী

```tsx
// ✅ সঠিক ব্যবহার
// Toggle, form input, modal open/close

const SearchBar = () => {
  const [query,    setQuery]    = useState('')
  const [isFocused, setFocused] = useState(false)

  return (
    <div className={`search ${isFocused ? 'focused' : ''}`}>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onFocus={() => setFocused(true)}
        onBlur={() => setFocused(false)}
      />
    </div>
  )
}
```

```
✅ ব্যবহার করো যখন:
   → শুধু এই component-এর দরকার
   → সহজ true/false, string, number
   → পরিষ্কার, অনুমানযোগ্য পরিবর্তন

❌ ব্যবহার করো না যখন:
   → অন্য component-এও দরকার
   → 5+ টি state একসাথে পরিবর্তন হয়
```

---

## 🥈 Pattern 2: useReducer
### কখন → জটিল local state, একাধিক action

```tsx
// ✅ সঠিক ব্যবহার
// Form wizard, shopping cart, complex UI state

type CartState = {
  items:    CartItem[]
  total:    number
  discount: number
  step:     'cart' | 'checkout' | 'confirm'
}

type CartAction =
  | { type: 'ADD_ITEM';     payload: CartItem }
  | { type: 'REMOVE_ITEM';  payload: string }
  | { type: 'APPLY_CODE';   payload: string }
  | { type: 'NEXT_STEP' }
  | { type: 'RESET' }

const cartReducer = (state: CartState, action: CartAction): CartState => {
  switch (action.type) {

    case 'ADD_ITEM':
      return {
        ...state,
        items: [...state.items, action.payload],
        total: state.total + action.payload.price,
      }

    case 'REMOVE_ITEM':
      const filtered = state.items.filter(i => i.id !== action.payload)
      return {
        ...state,
        items: filtered,
        total: filtered.reduce((sum, i) => sum + i.price, 0),
      }

    case 'APPLY_CODE':
      return { ...state, discount: 0.15 }  // 15% ছাড়

    case 'NEXT_STEP':
      const steps = ['cart', 'checkout', 'confirm'] as const
      const idx   = steps.indexOf(state.step)
      return { ...state, step: steps[idx + 1] ?? state.step }

    case 'RESET':
      return initialCartState

    default:
      return state
  }
}

// ব্যবহার
const Cart = () => {
  const [state, dispatch] = useReducer(cartReducer, initialCartState)

  return (
    <div>
      <p>মোট: ৳{state.total}</p>
      <button onClick={() => dispatch({ type: 'NEXT_STEP' })}>
        পরবর্তী ধাপ
      </button>
    </div>
  )
}
```

```
✅ ব্যবহার করো যখন:
   → একই state-এ ৩+ রকম পরিবর্তন আসে
   → পরিবর্তনগুলো পরস্পর সম্পর্কিত
   → Test করতে চাও (pure function)

❌ ব্যবহার করো না যখন:
   → সহজ ১-২টি value
   → Global দরকার
```

---

## 🥉 Pattern 3: Context API
### কখন → হালকা global, theme, locale, auth

```tsx
// ✅ সঠিক ব্যবহার
// Theme, Language, Auth User

// 1. Context তৈরি
interface ThemeContextType {
  theme:       'light' | 'dark'
  toggleTheme: () => void
}

const ThemeContext = createContext<ThemeContextType | null>(null)

// 2. Provider তৈরি
export const ThemeProvider = ({ children }: { children: React.ReactNode }) => {
  const [theme, setTheme] = useState<'light' | 'dark'>('dark')

  const toggleTheme = () =>
    setTheme(prev => prev === 'dark' ? 'light' : 'dark')

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      <div data-theme={theme}>
        {children}
      </div>
    </ThemeContext.Provider>
  )
}

// 3. Custom Hook — সরাসরি context expose করো না
export const useTheme = () => {
  const ctx = useContext(ThemeContext)
  if (!ctx) throw new Error('useTheme must be inside ThemeProvider')
  return ctx
}

// 4. ব্যবহার
const Header = () => {
  const { theme, toggleTheme } = useTheme()
  return (
    <button onClick={toggleTheme}>
      {theme === 'dark' ? '☀️' : '🌙'}
    </button>
  )
}
```

```
✅ ব্যবহার করো যখন:
   → কমই পরিবর্তন হয় (theme, user, locale)
   → সহজ কাঠামো
   → Extra library এড়াতে চাও

❌ ব্যবহার করো না যখন:
   → ঘন ঘন update হয় → re-render সমস্যা
   → বড় জটিল state
   → DevTools দরকার
```

---

## 🏆 Pattern 4: Zustand
### কখন → Complex global, frequent updates, DevTools

```tsx
// ✅ ONE SKY ENGINE-এর জন্য আদর্শ

// store/ui.store.ts
import { create } from 'zustand'
import { devtools, subscribeWithSelector } from 'zustand/middleware'

interface UIStore {
  // State
  sidebarOpen:      boolean
  commandPaletteOpen: boolean
  activeModal:      string | null
  notifications:    Notification[]
  theme:            'light' | 'dark'

  // Actions
  toggleSidebar:     () => void
  openCommandPalette: () => void
  closeCommandPalette: () => void
  openModal:         (id: string) => void
  closeModal:        () => void
  addNotification:   (n: Notification) => void
  removeNotification:(id: string) => void
  setTheme:          (t: 'light' | 'dark') => void
}

export const useUIStore = create<UIStore>()(
  devtools(
    subscribeWithSelector((set) => ({
      // Initial state
      sidebarOpen:       true,
      commandPaletteOpen: false,
      activeModal:       null,
      notifications:     [],
      theme:             'dark',

      // Actions
      toggleSidebar: () =>
        set(s => ({ sidebarOpen: !s.sidebarOpen })),

      openCommandPalette: () =>
        set({ commandPaletteOpen: true }),

      closeCommandPalette: () =>
        set({ commandPaletteOpen: false }),

      openModal: (id) =>
        set({ activeModal: id }),

      closeModal: () =>
        set({ activeModal: null }),

      addNotification: (n) =>
        set(s => ({ notifications: [...s.notifications, n] })),

      removeNotification: (id) =>
        set(s => ({
          notifications: s.notifications.filter(n => n.id !== id)
        })),

      setTheme: (t) =>
        set({ theme: t }),
    })),
    { name: 'ONE-SKY-UI' }
  )
)

// 🎯 Selector দিয়ে optimize করো — শুধু দরকারি অংশ নাও
const Sidebar = () => {
  // ✅ শুধু sidebarOpen — অন্য কিছু বদলালে re-render হবে না
  const sidebarOpen = useUIStore(s => s.sidebarOpen)
  const toggle      = useUIStore(s => s.toggleSidebar)

  return <aside className={sidebarOpen ? 'open' : 'closed'} />
}
```

```
✅ ব্যবহার করো যখন:
   → App-wide, ঘন ঘন update
   → Complex logic, multiple actions
   → Time-travel debugging দরকার
   → Performance critical (selector দিয়ে)

❌ ব্যবহার করো না যখন:
   → Server data (React Query ব্যবহার করো)
   → Component-local state
```

---

## 👑 Pattern 5: React Query (TanStack Query)
### কখন → সব Server State-এর জন্য

```tsx
// ✅ API data = সবসময় React Query

// services/api/knowledge.api.ts
const fetchKnowledgeNodes = async (projectId: string) => {
  const res = await apiClient.get(`/projects/${projectId}/nodes`)
  return res.data as KnowledgeNode[]
}

// hooks/useKnowledge.ts
export const useKnowledgeNodes = (projectId: string) => {
  return useQuery({
    queryKey:  ['knowledge', 'nodes', projectId],  // Cache key
    queryFn:   () => fetchKnowledgeNodes(projectId),
    staleTime: 1000 * 60 * 5,   // 5 মিনিট fresh থাকবে
    gcTime:    1000 * 60 * 30,  // 30 মিনিট cache-এ থাকবে
    retry: 2,
  })
}

// Mutation (Create/Update/Delete)
export const useCreateNode = () => {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: (data: CreateNodeDTO) =>
      apiClient.post('/nodes', data),

    // Optimistic Update — আগেই দেখাও, পরে confirm করো
    onMutate: async (newNode) => {
      await queryClient.cancelQueries({ queryKey: ['knowledge', 'nodes'] })

      const prev = queryClient.getQueryData(['knowledge', 'nodes'])

      queryClient.setQueryData(['knowledge', 'nodes'], (old: KnowledgeNode[]) => [
        ...old,
        { ...newNode, id: 'temp-' + Date.now(), status: 'pending' }
      ])

      return { prev }
    },

    onError: (_err, _vars, ctx) => {
      // ব্যর্থ হলে আগের state ফিরিয়ে দাও
      queryClient.setQueryData(['knowledge', 'nodes'], ctx?.prev)
    },

    onSettled: () => {
      // যাই হোক, fresh data নাও
      queryClient.invalidateQueries({ queryKey: ['knowledge', 'nodes'] })
    }
  })
}

// Component-এ ব্যবহার
const KnowledgeGraph = ({ projectId }: { projectId: string }) => {
  const { data, isLoading, isError, error } = useKnowledgeNodes(projectId)
  const createNode = useCreateNode()

  if (isLoading) return <GraphSkeleton />
  if (isError)   return <ErrorState message={error.message} />

  return (
    <div>
      {data?.map(node => <NodeCard key={node.id} node={node} />)}
      <button onClick={() => createNode.mutate({ name: 'নতুন নোড' })}>
        + যোগ করো
      </button>
    </div>
  )
}
```

```
✅ সবসময় ব্যবহার করো যখন:
   → API থেকে data আসে
   → Cache দরকার
   → Loading / Error state দরকার
   → Background refetch দরকার
   → Optimistic UI দরকার

❌ ব্যবহার করো না:
   → Client-only state-এর জন্য
```

---

## 🗓️ URL State
### কখন → Shareable, bookmarkable state

```tsx
// ✅ Filter, Search, Pagination → URL-এ রাখো

// /projects?status=active&page=2&sort=newest

const ProjectsPage = () => {
  const [searchParams, setSearchParams] = useSearchParams()

  const status = searchParams.get('status') ?? 'all'
  const page   = Number(searchParams.get('page') ?? 1)
  const sort   = searchParams.get('sort') ?? 'newest'

  const updateFilter = (key: string, value: string) => {
    setSearchParams(prev => {
      prev.set(key, value)
      prev.set('page', '1')  // filter বদলালে page reset
      return prev
    })
  }

  return (
    <div>
      <FilterBar
        status={status}
        sort={sort}
        onChange={updateFilter}
      />
      <ProjectList status={status} page={page} sort={sort} />
    </div>
  )
}
```

```
✅ ব্যবহার করো যখন:
   → Link share করা যাবে
   → Back button কাজ করবে
   → Filter, search, pagination, tab

❌ ব্যবহার করো না:
   → Sensitive data (token, password)
   → UI-only state (modal, dropdown)
```

---

## 📊 Pattern সিদ্ধান্ত সারণি

```
State Type          Pattern              কেন?
──────────────────────────────────────────────────────────
Modal open/close    useState             সহজ, স্থানীয়
Form input          useState             একটি field
Form wizard (৫+)    useReducer           জটিল, একাধিক action
Theme / Locale      Context API          কমই বদলায়
Auth user           Context + Zustand    Global, গুরুত্বপূর্ণ
App-wide UI state   Zustand              ঘন ঘন, complex
API data (GET)      React Query          Cache, loading, error
API mutation        React Query          Optimistic, invalidate
Filter / Pagination URL State            Shareable
```

---

## 🏗️ ONE SKY ENGINE — Store Architecture

```
stores/
├── ui.store.ts          # Zustand → sidebar, modal, theme
├── engine.store.ts      # Zustand → active project, queue
├── user.store.ts        # Zustand + Context → auth user
│
hooks/
├── useKnowledge.ts      # React Query → nodes, edges
├── useProjects.ts       # React Query → project list, detail
├── useEngine.ts         # React Query → engine operations
│
context/
├── AuthContext.tsx      # Context → login state
└── ThemeContext.tsx     # Context → theme (Zustand bridge)
```

---
---

# ╔══ PART C ══╗
# 🚀 Performance Engineering
### Core Web Vitals Mastery — সম্পূর্ণ কারিগরি

---

## 🔭 দর্শন

> Performance মানে শুধু "দ্রুত" নয়।
> Performance মানে — *ব্যবহারকারী অপেক্ষার কষ্ট অনুভব করে না।*
>
> ১ সেকেন্ড দেরিতে → ৭% conversion কমে।
> ৩ সেকেন্ড দেরিতে → ৫৩% মানুষ চলে যায়।

---

## 📐 Core Web Vitals — তিনটি মুকুট

```
┌─────────────────────────────────────────────────────┐
│                  CORE WEB VITALS                    │
├──────────────┬──────────────┬───────────────────────┤
│     LCP      │     CLS      │         INP           │
│  (Loading)   │  (Stability) │  (Interactivity)      │
├──────────────┼──────────────┼───────────────────────┤
│ Largest      │ Cumulative   │ Interaction to        │
│ Contentful   │ Layout       │ Next Paint            │
│ Paint        │ Shift        │                       │
├──────────────┼──────────────┼───────────────────────┤
│ "দেখাতে      │ "লেআউট      │ "ক্লিক করলে          │
│  কতক্ষণ?"   │  নড়ে?"      │  কতক্ষণ লাগে?"       │
├──────────────┼──────────────┼───────────────────────┤
│ ✅ < 2.5s    │ ✅ < 0.1     │ ✅ < 200ms            │
│ ⚠️  2.5-4s  │ ⚠️  0.1-0.25│ ⚠️  200-500ms         │
│ ❌ > 4s      │ ❌ > 0.25    │ ❌ > 500ms            │
└──────────────┴──────────────┴───────────────────────┘
```

---

## 🔵 LCP — Largest Contentful Paint
### লক্ষ্য: < 2.5 সেকেন্ড

**LCP কী পরিমাপ করে?**
> সবচেয়ে বড় দৃশ্যমান উপাদান (Hero image, H1) কখন লোড হলো।

### ❌ সমস্যা ও ✅ সমাধান

#### সমস্যা ১: ভারী Image

```html
<!-- ❌ ভুল -->
<img src="/hero.png" alt="Hero">

<!-- ✅ সঠিক -->
<img
  src="/hero.webp"
  srcset="/hero-400.webp 400w, /hero-800.webp 800w, /hero-1200.webp 1200w"
  sizes="(max-width: 768px) 100vw, 50vw"
  loading="eager"
  fetchpriority="high"
  alt="ONE SKY ENGINE Hero"
  width="1200"
  height="600"
>
```

#### সমস্যা ২: LCP Image দেরিতে discover হয়

```html
<!-- ✅ HTML <head>-এ Preload করো -->
<link
  rel="preload"
  as="image"
  href="/hero.webp"
  fetchpriority="high"
>
```

#### সমস্যা ৩: Render-blocking CSS/JS

```html
<!-- ❌ ভুল — JS লোড হওয়া পর্যন্ত page আটকে থাকে -->
<script src="/app.js"></script>

<!-- ✅ সঠিক -->
<script src="/app.js" defer></script>
<!-- অথবা critical নয় এমন -->
<script src="/analytics.js" async></script>
```

#### সমস্যা ৪: Slow Server Response (TTFB)

```ts
// ✅ Next.js / Server-side caching

// pages/api/engine-data.ts
export async function GET(req: Request) {
  return new Response(JSON.stringify(data), {
    headers: {
      'Cache-Control': 'public, s-maxage=60, stale-while-revalidate=300',
      'Content-Type':  'application/json',
    }
  })
}
```

---

## 🟡 CLS — Cumulative Layout Shift
### লক্ষ্য: < 0.1

**CLS কী পরিমাপ করে?**
> পেজ লোডের সময় উপাদানগুলো কতটুকু নড়াচড়া করে।

```
❌ খারাপ অভিজ্ঞতা:
"পড়ছিলাম... হঠাৎ বিজ্ঞাপন এলো, সব নিচে নামলো!"
```

### ✅ সমাধানসমূহ

#### সমাধান ১: Image-এ সবসময় width/height দাও

```tsx
// ❌ ভুল — browser জানে না কতটুকু জায়গা রাখবে
<img src="/banner.webp" alt="Banner" />

// ✅ সঠিক — জায়গা আগে থেকেই reserved
<img
  src="/banner.webp"
  alt="Banner"
  width={1200}
  height={400}
  style={{ aspectRatio: '3/1' }}
/>
```

#### সমাধান ২: Font FOUT (Flash of Unstyled Text) ঠেকাও

```css
/* ✅ font-display: optional — layout shift নেই */
@font-face {
  font-family: 'Clash Display';
  src: url('/fonts/clash-display.woff2') format('woff2');
  font-display: optional;   /* swap এর চেয়ে ভালো CLS-এর জন্য */
}
```

```html
<!-- ✅ Font preload -->
<link
  rel="preload"
  href="/fonts/clash-display.woff2"
  as="font"
  type="font/woff2"
  crossorigin
>
```

#### সমাধান ৩: Dynamic content-এর জন্য জায়গা রাখো

```tsx
// ❌ ভুল — লোড হলে হঠাৎ জায়গা নেয়
const AdBanner = () => {
  const [ad, setAd] = useState(null)
  useEffect(() => { fetchAd().then(setAd) }, [])
  return ad ? <img src={ad.image} /> : null
}

// ✅ সঠিক — আগে থেকেই জায়গা ধরে রাখো
const AdBanner = () => {
  const [ad, setAd] = useState(null)
  useEffect(() => { fetchAd().then(setAd) }, [])

  return (
    <div style={{ minHeight: '90px', width: '728px' }}>
      {ad && <img src={ad.image} width={728} height={90} />}
    </div>
  )
}
```

#### সমাধান ৪: Skeleton Loading

```tsx
// ✅ Content লোড হওয়ার আগে একই আকারের skeleton দেখাও

const NodeCardSkeleton = () => (
  <div className="animate-pulse">
    <div className="h-4 bg-neutral-200 rounded w-3/4 mb-2" />
    <div className="h-4 bg-neutral-200 rounded w-1/2 mb-2" />
    <div className="h-20 bg-neutral-200 rounded" />
  </div>
)

const NodeCard = ({ nodeId }: { nodeId: string }) => {
  const { data, isLoading } = useNode(nodeId)

  if (isLoading) return <NodeCardSkeleton />
  return <div>{data?.name}</div>
}
```

---

## 🟢 INP — Interaction to Next Paint
### লক্ষ্য: < 200ms

**INP কী পরিমাপ করে?**
> Button click থেকে UI update পর্যন্ত সময়।

### ❌ সমস্যা: Long Task (Main Thread blocked)

```tsx
// ❌ ভুল — 10,000 item একসাথে process → UI freeze
const processAllNodes = (nodes: Node[]) => {
  return nodes.map(node => ({
    ...node,
    processed: heavyComputation(node)  // ব্লক করে!
  }))
}
```

### ✅ সমাধান ১: Web Worker-এ ভারী কাজ পাঠাও

```ts
// workers/engine.worker.ts
self.onmessage = (e: MessageEvent) => {
  const { nodes } = e.data

  // Main thread block হবে না
  const result = nodes.map(node => ({
    ...node,
    processed: heavyComputation(node)
  }))

  self.postMessage({ result })
}

// hooks/useEngineWorker.ts
export const useEngineWorker = () => {
  const workerRef = useRef<Worker>()

  useEffect(() => {
    workerRef.current = new Worker(
      new URL('../workers/engine.worker.ts', import.meta.url)
    )
    return () => workerRef.current?.terminate()
  }, [])

  const processNodes = useCallback((nodes: Node[]) => {
    return new Promise((resolve) => {
      workerRef.current!.onmessage = (e) => resolve(e.data.result)
      workerRef.current!.postMessage({ nodes })
    })
  }, [])

  return { processNodes }
}
```

### ✅ সমাধান ২: useDeferredValue — urgent vs non-urgent

```tsx
// ✅ Search input দ্রুত → results defer করো

const SearchEngine = () => {
  const [query, setQuery] = useState('')
  const deferredQuery     = useDeferredValue(query)  // 🔑

  const { data: results } = useSearchResults(deferredQuery)

  return (
    <div>
      {/* Input সবসময় দ্রুত respond করবে */}
      <input
        value={query}
        onChange={e => setQuery(e.target.value)}
        placeholder="খোঁজো..."
      />

      {/* Results একটু পরে update হবে — তবু UI block হবে না */}
      <SearchResults results={results} isPending={query !== deferredQuery} />
    </div>
  )
}
```

### ✅ সমাধান ৩: startTransition — non-urgent update

```tsx
import { useTransition } from 'react'

const KnowledgeGraph = () => {
  const [isPending, startTransition] = useTransition()
  const [filter, setFilter] = useState('all')

  const handleFilterChange = (newFilter: string) => {
    startTransition(() => {
      setFilter(newFilter)  // Non-urgent — yield to urgent updates
    })
  }

  return (
    <div>
      <FilterBar onChange={handleFilterChange} />
      {isPending && <div className="opacity-50">লোড হচ্ছে...</div>}
      <NodeGrid filter={filter} />
    </div>
  )
}
```

---

## 📦 Bundle Optimization
### JavaScript কম পাঠাও — দ্রুত লোড হবে

### Code Splitting — প্রয়োজনমতো লোড

```tsx
// ✅ Route-based splitting — সবচেয়ে গুরুত্বপূর্ণ

import { lazy, Suspense } from 'react'

// এই pages গুলো আলাদা chunk হবে
const EnginePage    = lazy(() => import('./pages/Engine'))
const KnowledgePage = lazy(() => import('./pages/Knowledge'))
const SettingsPage  = lazy(() => import('./pages/Settings'))

const App = () => (
  <Router>
    <Suspense fallback={<PageSkeleton />}>
      <Routes>
        <Route path="/"          element={<HomePage />} />
        <Route path="/engine"    element={<EnginePage />} />
        <Route path="/knowledge" element={<KnowledgePage />} />
        <Route path="/settings"  element={<SettingsPage />} />
      </Routes>
    </Suspense>
  </Router>
)
```

### Component-level Lazy Loading

```tsx
// ✅ ভারী component — দেখলে তবে লোড করো

const HeavyChartLibrary = lazy(() =>
  import('./components/organisms/EngineChart')
)

const Dashboard = () => {
  const [showChart, setShowChart] = useState(false)

  return (
    <div>
      <button onClick={() => setShowChart(true)}>
        Chart দেখাও
      </button>

      {showChart && (
        <Suspense fallback={<ChartSkeleton />}>
          <HeavyChartLibrary />
        </Suspense>
      )}
    </div>
  )
}
```

### Tree Shaking — অব্যবহৃত কোড বাদ দাও

```ts
// ❌ ভুল — পুরো lodash লোড হয় (70KB+)
import _ from 'lodash'
const result = _.debounce(fn, 300)

// ✅ সঠিক — শুধু debounce লোড হয় (2KB)
import debounce from 'lodash/debounce'
const result = debounce(fn, 300)

// ✅ আরও ভালো — native বা tiny alternative
const debounce = (fn: Function, delay: number) => {
  let timer: ReturnType<typeof setTimeout>
  return (...args: unknown[]) => {
    clearTimeout(timer)
    timer = setTimeout(() => fn(...args), delay)
  }
}
```

---

## 🧮 React Rendering Optimization

### memo — অপ্রয়োজনীয় re-render বন্ধ করো

```tsx
// ❌ Parent render হলে NodeCard-ও render হয়
const NodeCard = ({ node }: { node: Node }) => {
  return <div>{node.name}</div>
}

// ✅ props না বদলালে render হবে না
const NodeCard = memo(({ node }: { node: Node }) => {
  return <div>{node.name}</div>
})

// ✅ Custom comparison (deep equal দরকার হলে)
const NodeCard = memo(
  ({ node }: { node: Node }) => <div>{node.name}</div>,
  (prev, next) => prev.node.id === next.node.id &&
                  prev.node.name === next.node.name
)
```

### useMemo — ভারী calculation cache করো

```tsx
const KnowledgeGraph = ({ nodes, filter }: Props) => {

  // ❌ ভুল — প্রতি render-এ recalculate
  const filteredNodes = nodes
    .filter(n => n.type === filter)
    .sort((a, b) => b.weight - a.weight)

  // ✅ সঠিক — nodes বা filter বদলালেই recalculate
  const filteredNodes = useMemo(() =>
    nodes
      .filter(n => n.type === filter)
      .sort((a, b) => b.weight - a.weight),
    [nodes, filter]
  )

  return <Graph nodes={filteredNodes} />
}
```

### useCallback — function reference stable রাখো

```tsx
const NodeList = ({ projectId }: { projectId: string }) => {
  const createNode = useCreateNode()

  // ❌ ভুল — প্রতি render-এ নতুন function → NodeCard re-render
  const handleCreate = (name: string) => {
    createNode.mutate({ name, projectId })
  }

  // ✅ সঠিক — stable reference
  const handleCreate = useCallback((name: string) => {
    createNode.mutate({ name, projectId })
  }, [projectId, createNode.mutate])

  return <NodeCard onAdd={handleCreate} />
}
```

### Virtualization — হাজার item render করো অনায়াসে

```tsx
// ✅ 10,000 node → শুধু দৃশ্যমানগুলো render হবে

import { useVirtualizer } from '@tanstack/react-virtual'

const VirtualNodeList = ({ nodes }: { nodes: Node[] }) => {
  const parentRef = useRef<HTMLDivElement>(null)

  const virtualizer = useVirtualizer({
    count:       nodes.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 80,       // প্রতিটি item ~80px
    overscan:    5,               // দৃশ্যের বাইরে ৫টি আগে render
  })

  return (
    <div ref={parentRef} style={{ height: '600px', overflow: 'auto' }}>
      <div style={{ height: virtualizer.getTotalSize() }}>
        {virtualizer.getVirtualItems().map(item => (
          <div
            key={item.key}
            style={{
              position:  'absolute',
              top:       item.start,
              height:    item.size,
              width:     '100%',
            }}
          >
            <NodeCard node={nodes[item.index]} />
          </div>
        ))}
      </div>
    </div>
  )
}
```

---

## 🖼️ Image Optimization — সম্পূর্ণ কৌশল

```tsx
// ✅ Next.js Image Component — সব optimization built-in

import Image from 'next/image'

// Hero Image (LCP element)
const HeroSection = () => (
  <Image
    src="/hero.webp"
    alt="ONE SKY ENGINE"
    width={1200}
    height={600}
    priority           // LCP → eager load, preload header
    quality={85}       // 85% quality — চোখে পার্থক্য নেই
    placeholder="blur" // blur hash দেখাবে লোডের আগে
    blurDataURL="data:image/webp;base64,..."
  />
)

// Below-fold Image
const FeatureImage = () => (
  <Image
    src="/feature.webp"
    alt="Feature"
    width={600}
    height={400}
    loading="lazy"     // viewport-এ এলে তখন লোড
    quality={80}
  />
)
```

### Intersection Observer — viewport-এ এলে লোড

```tsx
// hooks/useInView.ts
export const useInView = (options?: IntersectionObserverInit) => {
  const ref        = useRef<HTMLDivElement>(null)
  const [inView, setInView] = useState(false)

  useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) {
        setInView(true)
        observer.disconnect()  // একবার দেখলেই বন্ধ
      }
    }, options)

    if (ref.current) observer.observe(ref.current)
    return () => observer.disconnect()
  }, [])

  return { ref, inView }
}

// ব্যবহার
const LazySection = () => {
  const { ref, inView } = useInView({ threshold: 0.1 })

  return (
    <div ref={ref}>
      {inView ? <HeavyComponent /> : <SectionSkeleton />}
    </div>
  )
}
```

---

## 🌐 Network Optimization

### Resource Hints — Browser-কে আগে থেকে জানাও

```html
<head>
  <!-- DNS lookup আগে করো -->
  <link rel="dns-prefetch" href="//api.onesky.engine">

  <!-- Connection আগে করো (DNS + TCP + TLS) -->
  <link rel="preconnect" href="https://api.onesky.engine" crossorigin>

  <!-- Critical resource আগে লোড করো -->
  <link rel="preload" href="/fonts/clash-display.woff2" as="font" crossorigin>
  <link rel="preload" href="/hero.webp" as="image">

  <!-- পরের page আগে লোড করো -->
  <link rel="prefetch" href="/engine" as="document">
</head>
```

### Service Worker — Offline + Cache

```ts
// service-worker.ts

const CACHE_NAME    = 'one-sky-v1'
const STATIC_ASSETS = ['/', '/index.html', '/main.js', '/styles.css']

// Install: static assets cache করো
self.addEventListener('install', (e: ExtendableEvent) => {
  e.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(STATIC_ASSETS))
  )
})

// Fetch: Cache-first for static, Network-first for API
self.addEventListener('fetch', (e: FetchEvent) => {
  const url = new URL(e.request.url)

  if (url.pathname.startsWith('/api/')) {
    // API: Network first, cache fallback
    e.respondWith(
      fetch(e.request)
        .then(res => {
          const clone = res.clone()
          caches.open(CACHE_NAME).then(c => c.put(e.request, clone))
          return res
        })
        .catch(() => caches.match(e.request))
    )
  } else {
    // Static: Cache first, network fallback
    e.respondWith(
      caches.match(e.request)
        .then(cached => cached ?? fetch(e.request))
    )
  }
})
```

---

## 📊 Performance Monitoring

### Web Vitals Tracking

```ts
// utils/vitals.ts
import { onLCP, onCLS, onINP, onFCP, onTTFB } from 'web-vitals'

type MetricReport = {
  name:  string
  value: number
  rating: 'good' | 'needs-improvement' | 'poor'
}

const sendToAnalytics = (metric: MetricReport) => {
  // ONE SKY analytics-এ পাঠাও
  fetch('/api/vitals', {
    method: 'POST',
    body:   JSON.stringify(metric),
    headers: { 'Content-Type': 'application/json' }
  })
}

// সব vital track করো
onLCP(sendToAnalytics)
onCLS(sendToAnalytics)
onINP(sendToAnalytics)
onFCP(sendToAnalytics)
onTTFB(sendToAnalytics)
```

### Performance Budget

```ts
// performance.budget.ts
// এই সীমা লঙ্ঘন হলে CI/CD fail করবে

export const performanceBudget = {
  // Bundle sizes
  bundles: {
    initial:    200_000,   // 200KB — প্রথম লোড
    vendor:     150_000,   // 150KB — third-party
    perFeature:  80_000,   //  80KB — প্রতিটি feature chunk
  },

  // Web Vitals
  vitals: {
    LCP:  2500,   // ms
    CLS:  0.1,    // score
    INP:  200,    // ms
    FCP:  1800,   // ms
    TTFB:  800,   // ms
  },

  // Resource counts
  resources: {
    maxRequests:     50,
    maxImageSize: 200_000,   // 200KB per image
    maxFontFiles:     3,
  }
}
```

---

## 🎯 Performance Checklist — ONE SKY ENGINE

```
LOADING (LCP)
  ✦ Hero image: WebP format, preloaded               [ ]
  ✦ Critical CSS inline                               [ ]
  ✦ Font preload + font-display: optional             [ ]
  ✦ Server response < 600ms (TTFB)                    [ ]
  ✦ CDN-এ static assets                              [ ]

STABILITY (CLS)
  ✦ সব image-এ width/height                          [ ]
  ✦ Dynamic content-এর জন্য reserved space           [ ]
  ✦ Skeleton loading সব async content-এ              [ ]
  ✦ Font swap থেকে optional-এ migrate                [ ]

INTERACTIVITY (INP)
  ✦ Heavy computation → Web Worker                   [ ]
  ✦ Long lists → Virtualized                         [ ]
  ✦ Search → useDeferredValue                        [ ]
  ✦ Tab switch → startTransition                     [ ]

BUNDLE
  ✦ Route-based code splitting                       [ ]
  ✦ Heavy libraries → lazy loaded                    [ ]
  ✦ Lodash → individual imports                      [ ]
  ✦ Bundle analyzer চালানো                           [ ]

RENDERING
  ✦ List items → React.memo                          [ ]
  ✦ Heavy calculation → useMemo                      [ ]
  ✦ Event handlers → useCallback                     [ ]
  ✦ 50+ items → Virtualized list                     [ ]

NETWORK
  ✦ API calls → React Query (cache)                  [ ]
  ✦ Critical origins → preconnect                    [ ]
  ✦ Next routes → prefetch                           [ ]
  ✦ Service Worker → offline support                 [ ]
```

---

## 🔮 লক্ষ্যমাত্রা — ONE SKY ENGINE Final Targets

```
Metric          এখন (baseline)    লক্ষ্য         কৌশল
────────────────────────────────────────────────────────────────
LCP             ~4.5s             < 1.8s          Image opt + preload
CLS             ~0.18             < 0.05          Skeleton + dimensions
INP             ~450ms            < 150ms          Web Worker + defer
FCP             ~3.2s             < 1.2s          Critical CSS
TTFB            ~1.2s             < 400ms         Edge Functions + CDN
Bundle (initial) ~480KB           < 180KB         Splitting + tree shake
Lighthouse      ~55               > 95            সব মিলিয়ে
```

---

> *"দ্রুত সিস্টেম শুধু সময় বাঁচায় না —*
> *এটি ব্যবহারকারীর বিশ্বাস অর্জন করে।*
> *Performance হলো নীরব প্রতিশ্রুতি:*
> *'আমি তোমার সময়ের মূল্য দিই।'"*
>
> — **Miracle Code™ Performance Manifesto**

---

# 📦 সম্পূর্ণ সংগ্রহ

| Part | বিষয় | Status |
|------|-------|--------|
| **A** | Component Design System + Tokens | ✅ সম্পূর্ণ |
| **B** | State Architecture | ✅ সম্পূর্ণ |
| **C** | Performance Engineering | ✅ সম্পূর্ণ |
| **D** | ONE SKY ENGINE Blueprint | ✅ সম্পূর্ণ |

---
*M99 Universe · Miracle Code™ · ONE SKY ENGINE*
*Think Beyond Time. Live Beyond Limits. 🪩🔭✨*
```
