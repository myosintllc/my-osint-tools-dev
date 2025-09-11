# Tampermonkey OSINT Bookmarklets Guide

## Overview

Bookmarklets are powerful tools for automating tedious OSINT tasks. [Myosint.training](https://tools.myosint.training/) maintains a collection of JavaScript bookmarklets that can extract IDs from social media sites and perform other time-saving operations with a simple click.

While individual bookmarklets work great, managing 30+ bookmarks quickly clutters your browser toolbar. This guide shows how to use **Tampermonkey** to install and auto-update all bookmarklets in one step.

## What is Tampermonkey?

[Tampermonkey](https://www.tampermonkey.net/) is a cross-browser extension that lets you create custom browser modifications using JavaScript. Think of it as building browser extensions without the complexity—Tampermonkey handles the technical setup while you focus on the functionality.

## Installation

### 1. Install Tampermonkey Extension

- Download from your browser's extension store
- **For Chromium browsers:** Enable Developer Mode due to Manifest v3 restrictions
- **For Brave:** Go to Extensions → Tampermonkey Details → Enable "Allow User Scripts"

### 2. Add the Userscript

Choose one of these methods:

**Method 1: Manual Installation (Recommended for Security)**
1. Open Tampermonkey and click the '+' symbol
2. Delete the boilerplate code
3. Copy/paste content from [userscript.js](/tampermonkey/userscript.js)
4. Save the script

**Method 2: Auto-Update Installation**
1. Click "Raw" button on [userscript.js](/tampermonkey/userscript.js) in GitHub
2. Copy the URL
3. In Tampermonkey → Utilities → paste URL in "Import from URL"
4. Click "Install"

## Usage

Once installed, access bookmarklets by:
- **Right-clicking** on any webpage to see context menu options
- **Clicking** the Tampermonkey extension icon for quick access

The scripts will automatically show relevant bookmarklets based on the current website domain.

## How It Works

The userscript contains all bookmarklets from the main tools page. Each bookmarklet requires specific attributes:

- **`data-name`** (required): Function name for the bookmarklet
- **`data-domain`** (required): Target domain (use "*" for all domains)  
- **`data-replace-open`** (optional): Replaces `window.open` with `GM_openInTab` to bypass popup blockers

All bookmarklets use **IIFE** (Immediately Invoked Function Expression) format to prevent conflicts.

## Security Warning ⚠️

**Browser extensions can be awesome, but they can also be malicious.** Extensions might be able to read (and alter) all requests your browser makes, take screenshots, and transmit that data to someone else without you knowing about it.

Recently, an extension that provided a "Free VPN" service was discovered to secretly screenshot all pages users visited and send those images to the creator. That's seriously bad.

### The Auto-Update Problem

Extensions and userscripts typically auto-update by default. An extension you install today after thoroughly vetting it might not have the same owner or content tomorrow. All it takes is one malicious update and you're compromised.

The same principle applies to userscripts. In this guide, we showcase two different methods to add the userscript to Tampermonkey:

1. **Manual Installation:** Does not automatically update the userscript. When a bookmarklet is updated on [the tools page](https://tools.myosint.training/) and in the GitHub repository, you'll need to grab it (and ideally vet it) manually before allowing it to run in your browser.

2. **Auto-Update Installation:** Imports directly from the GitHub URL and gets auto-updates whenever the repository updates. This requires you to trust the authors of the userscript completely.

### The Safer Third Option

Consider forking the repository on GitHub (creating your own copy that you and you alone control) and adding that URL to Tampermonkey instead. If the userscript changes on the original GitHub page, you'll be alerted by GitHub. You can then review the changes and pull them into your own fork if you agree they're just harmless snippets of JavaScript that will be helpful to your day-to-day OSINT tasks.

## Conclusion

This Tampermonkey integration streamlines OSINT workflows by centralizing bookmarklet management. However, always balance convenience with security—understand the risks and choose the installation method that matches your security requirements.
