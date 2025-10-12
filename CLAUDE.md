# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a single-page restaurant menu website (`index.html`) designed to be deployed via GitHub Pages. The menu displays food and drink items in a 5-column responsive layout with a purple gradient background.

## Architecture

The entire application is a single self-contained HTML file with:
- Embedded CSS styles in the `<head>` section
- Static menu content in semantic HTML structure
- Auto-refresh JavaScript that reloads the page every 60 seconds

### Layout Structure

The menu uses CSS Grid with 5 columns:
1. **Column 1**: STARTERS section + KIDS section
2. **Columns 2-3**: MAIN DISHES section (spans 2 columns, split into left/right sub-columns)
3. **Columns 4-5**: DRINKS section (spans 2 columns, split into left/right sub-columns)

Each multi-column section (MAIN DISHES and DRINKS) uses a nested grid layout with a centered header spanning both columns.

### Spacing Configuration

Vertical spacing is intentionally different across sections:
- **STARTERS items**: 35px margin-bottom
- **MAIN DISHES items**: 40px margin-bottom
- **DRINKS items**: 6px margin-bottom (intentionally compact)
- **KIDS items**: 30px margin-bottom

### Typography

- **Item names/prices**: 28px, bold, uppercase
- **Item descriptions**: 19px (1.6x original 12px), line-height 1.1, non-italic
- **Section headers** (e.g., "Green onion & cilantro..."): 19px (matches descriptions)
- **Main headers** (STARTERS, MAIN DISHES, DRINKS): 32px

### CSS Selectors Note

`.menu-container > .column:first-child` is used to target only the STARTERS column, avoiding conflicts with `.drinks-section .column:first-child`.

## Deployment

This repository is configured for GitHub Pages deployment:
- The `index.html` file is served directly
- Auto-refresh ensures visitors see updates within 60 seconds of deployment
- Push to `main` branch to deploy changes

## Making Changes

When editing menu content:
1. Maintain the 5-column grid structure
2. Keep spacing rules consistent per section
3. Verify all menu items match any source images (use verification agents if needed)
4. Test responsive behavior (collapses to single column at max-width: 1200px)

When editing styles:
- All styles are in the `<style>` tag - no external CSS files
- Changes to spacing should respect the intentional differences between sections
- The purple gradient is: `linear-gradient(135deg, #c045d9 0%, #a820c0 50%, #8e18a0 100%)`
