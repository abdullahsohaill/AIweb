# Consent-O-Matic Extension

This directory should contain the **unpacked** Consent-O-Matic Chrome extension.

## Setup Instructions

1. Clone the extension:
   ```bash
   git clone https://github.com/cavi-au/Consent-O-Matic.git
   ```

2. Build the extension:
   ```bash
   cd Consent-O-Matic
   npm install
   npm run build
   ```

3. Copy the `Extension` folder into this directory:
   ```bash
   cp -r Extension/ ../crawler/extensions/Consent-O-Matic/
   ```

4. The final structure should look like:
   ```
   crawler/extensions/
   └── Consent-O-Matic/
       ├── manifest.chromium.json   ← Chromium manifest (MV3)
       ├── GDPRConfig.js            ← Configure consent values here
       ├── service.js               ← Compiled service worker
       ├── content.js               ← Compiled content script
       └── ...
   ```

## Configuring Consent Values

Edit `GDPRConfig.js` and set `GDPRConfig.defaultValues` to all `true`:

```javascript
GDPRConfig.defaultValues = {
    "A": true,   // Preferences
    "B": true,   // Performance/Analytics
    "D": true,   // Information/Necessary
    "E": true,   // Content/Social Media
    "F": true,   // Ads/Marketing
    "X": true    // Other/Unclassified
};
```

For the crawler, we accept ALL cookies to ensure maximum website
functionality and AI widget loading.

## Reference

- Repository: https://github.com/cavi-au/Consent-O-Matic
- Developed by: CAVI — Aarhus University
