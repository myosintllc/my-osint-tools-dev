# Tampermonkey OSINT Bookmarklets Guide

## Overview

Bookmarklets are powerful tools for automating tedious OSINT tasks. While individual bookmarklets work well and allow analysts to be flexible in how they are used, managing 30+ bookmarklets quickly clutters your browser bookmark toolbar. This guide shows how to use **Tampermonkey** to install and auto-update all bookmarklets in one step.

> [!NOTE]
> Using the Tampermonkey extension/add-on is a more advanced method of using the bookmarklets and is 100% OPTIONAL. It takes a little setup and some trust but does make it easy to use and update the bookmarklets. Choose your own adventure here....use or do not. You decide.

## What is Tampermonkey?

[Tampermonkey](https://www.tampermonkey.net/) is a cross-browser extension that lets you create custom browser modifications using JavaScript. Think of it as building browser extensions without the complexity. Tampermonkey handles the technical setup while you focus on the functionality.

> [!WARNING]
> **Browser extensions can be awesome, but they can also be malicious.** Some extensions can read (and alter) all requests your browser makes, take screenshots, and transmit that data to someone else without you knowing about it. As an example, recently, an extension that provided a "Free VPN" service was discovered to secretly screenshot all pages users visited and send those images to the creator. That's seriously bad.
>
> We do our best to ensure that bookmarklets hosted on My OSINT Training do nothing malicious. We review all code and have several AIs also review code submitted by third parties to ensure that you can trust our tools. But please do not just take our word for it, do your own analyses of our bookmarklets to make sure you are comfortable with them.


## Installation of Tampermonkey

### 1. Install Tampermonkey Extension

- Download from your browser's extension store
- **For Chromium browsers:** You must do an additional step of enabling Developer Mode in the browser (the extension will tell you how)
- **For Brave:** You must do an additional step: Go to Extensions → Tampermonkey Details → Enable "Allow User Scripts"

### 2. Add the Userscript

Choose one of these methods:

**Method 1: Manual Installation**

> [!WARNING]
> By using this method, you will periodically need to check for updates in the bookmarklets manually and then update the content in your browser. No auto-updating happens with this method.

1. Open Tampermonkey and click the '+' symbol
2. Delete the boilerplate code
3. Copy/paste content from [userscript.js](/tampermonkey/userscript.js)
4. Save the script

**Method 2: Auto-Update Installation**

> [!WARNING]
> This method automatically will update your tools as we update our tools; keeping your browser in sync. It also could be a security risk if you do not trust our tools and review process.

1. Click "Raw" button on [userscript.js](/tampermonkey/userscript.js) in GitHub
2. Copy the URL
3. In Tampermonkey → Utilities → paste URL in "Import from URL"
4. Click "Install"

## Usage

Once installed, access bookmarklets by:
- **Right-clicking** on any webpage to see context menu options like in the image below.
![Context Menu method of using Tampermonkey](assets/tiktok2.png)

- **Clicking** the Tampermonkey extension icon for "less-quick" access like in the image below.
![Tampermonkey icon click method of using Tampermonkey](assets/tiktok.png)

The scripts will automatically show relevant bookmarklets based on the current website domain.

## Conclusion

This Tampermonkey integration streamlines OSINT workflows by centralizing bookmarklet management. However, always balance convenience with security—understand the risks and choose the installation method that matches your security requirements.

---
## Thank You

Micah and Griffin would like to extend our sincerest thanks to the OSINT community member that created the Tampermonkey integration and integrated it into our tools. This person is very well known to Micah and Griffin and wishes to remain anonymous. We appreciate their ideas and contribution to this project.
