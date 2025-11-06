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
- **IMPORTANT**: When updating the menu, you MUST increment the version number in `version.txt` to trigger auto-refresh on client devices
- The page checks `version.txt` every 30 seconds and reloads only if the version has changed
- Push to `main` branch to deploy changes

## Making Changes

When editing menu content:
1. Maintain the 5-column grid structure
2. Keep spacing rules consistent per section
3. Verify all menu items match any source images (use verification agents if needed)
4. Test responsive behavior (collapses to single column at max-width: 1200px)
5. **CRITICAL**: After making changes to `index.html`, increment the number in `version.txt` to trigger client auto-refresh

When editing styles:
- All styles are in the `<style>` tag - no external CSS files
- Changes to spacing should respect the intentional differences between sections
- The purple gradient overlay is: `linear-gradient(135deg, #c045d9 0%, #a820c0 50%, #8e18a0 100%)` at 50% opacity over the cherry blossom background

## Version Control System

The menu uses a version-based auto-refresh system:
- `version.txt` contains a simple version number (increment by 1 each update)
- Client browsers check this file every 30 seconds
- If the version changes, the page automatically reloads to show the latest menu
- **Always increment `version.txt` when updating `index.html`** - this is how clients know to refresh

## Fairy Animation Feature

The menu includes an animated fairy character that appears repeatedly, starting 2 seconds after page load and repeating every 25 seconds. There are two variants: **Original Waving Fairy** and **Winter Fairy (Snowball Throw)**.

### Animation Sequence
1. **2 seconds** after page load, fairy pops up in the **lower left corner**
2. Fairy performs animation (plays through all sprite frames)
3. Fairy drops back down
4. **4 second pause**
5. Fairy pops up in the **lower right corner**
6. Fairy performs animation again
7. Fairy drops back down
8. **Entire sequence repeats every 25 seconds**

### Current Active Variant: Winter Fairy (Snowball Throw)

**Sprite Sheet**:
- File: `fairy-sprite.png` (24.30 MB) - **Currently the winter variant**
- Horizontal layout: 145 frames in a single row
- Individual frame size: 512×512 pixels (square aspect ratio)
- Total sprite dimensions: 74240×512 pixels
- Frames have transparent backgrounds (white/light-gray removed, threshold RGB > 245)
- Snowball overlay applied to frames 51-144
- Created from video using Python scripts in the repository
- Format: PNG (WebP cannot handle extremely wide images)

**CSS Animation (Winter Fairy)**:
- Two fixed-position div elements (`#fairy-left` and `#fairy-right`)
- Display size: 512×512 pixels (square frames)
- Position: `bottom: -300px` (hides transparent space below viewport)
- Combined animations:
  - `fairy-appear-left` / `fairy-appear-right`: Controls vertical slide (translateY from 20px to -300px) and opacity
  - `fairy-wave`: Steps through sprite frames using horizontal `background-position` (0% to 100%) with `steps(144)`
- Background-size: 14500% × 100% (145 frames horizontally)
- Animation duration: 8 seconds per appearance
- Uses `pointer-events: none` to avoid interfering with menu interaction
- Cache-busting query parameter in URL: `fairy-sprite.png?v=XX` (update when sprite changes)

**JavaScript Trigger**:
- Initial delay: 2 seconds (`setTimeout(runFairyAnimation, 2000)`)
- Repeats every 25 seconds (`setInterval(runFairyAnimation, 25000)`)
- First animation (left): triggered immediately when function runs
- Second animation (right): triggered 12 seconds after left starts (8s animation + 4s delay)
- Animation classes are removed and re-added on each cycle to allow restart

### Fairy Variants

#### Winter Fairy (Current - Snowball Throw)
- **Sprite File**: `fairy-sprite.png` (current)
- **Backup**: `fairy-sprite-original.png` contains the original waving fairy
- **Frames**: 145 frames (512×512 each)
- **Animation**: 8 seconds
- **Special**: Snowball overlay on frames 51-144
- **Source Files**:
  - `winter_frames/` - Processed frames with transparent backgrounds and snowball overlay
  - `winter_frames_raw/` - Raw frames without background removal
  - `snowball-overlay.png` - Snowball image overlaid at position (10, 204), sized 524×514
- **Processing Scripts**:
  - `extract_winter_raw.py` - Extracts all frames from winter video, resizes to 512px width
  - `remove_winter_background.py` - Removes backgrounds (RGB > 245 threshold to preserve snowball)
  - `overlay_snowball.py` - Overlays snowball image on frames 51+
  - `create_winter_sprite.py` - Combines frames into horizontal sprite sheet

#### Original Fairy (Waving - Backed Up)
- **Sprite File**: `fairy-sprite-original.png` (backup)
- **Frames**: 101 frames (512×256 each)
- **Animation**: 4 seconds
- **Special**: Cropped to top half, reduced frame count (every 3rd frame)
- **Source Files**:
  - `reduced_frames/` - Individual WebP frames (101 files)
  - `frames/` - Full-resolution PNG frames (301 files, unprocessed)
- **Processing Scripts**:
  - `process_video_pil.py` - Extracts frames, crops to top half, resizes to 512px
  - `reduce_frames.py` - Selects every 3rd frame (301 → 101 frames)
  - `remove_white_background.py` - Makes backgrounds transparent (RGB > 200 threshold)
  - `convert_to_webp.py` - Converts PNG to WebP format
  - `create_sprite_sheet.py` - Combines frames into horizontal sprite sheet

### Switching Between Fairy Variants

#### To Restore Original Waving Fairy:
1. Restore sprite: `cp fairy-sprite-original.png fairy-sprite.png`
2. Edit `index.html` CSS (`.fairy` class):
   - Change `height: 512px` to `height: 256px`
   - Change `background-size: 14500%` to `background-size: 10100%`
   - Update cache-busting: `url('fairy-sprite.png?v=XX')` (increment XX)
3. Edit `index.html` CSS (`.fairy.animate-left` and `.fairy.animate-right`):
   - Change `fairy-appear-left 8s` to `fairy-appear-left 4s`
   - Change `fairy-appear-right 8s` to `fairy-appear-right 4s`
   - Change `fairy-wave 8s steps(144)` to `fairy-wave 4s steps(100)`
4. Edit `index.html` JavaScript (inside `runFairyAnimation` function):
   - Change `setTimeout(..., 12000)` to `setTimeout(..., 6000)`
5. Increment `version.txt`

#### To Switch to Winter Fairy (Snowball):
1. Ensure `fairy-sprite.png` is the winter version (24.30 MB, 145 frames)
2. Edit `index.html` CSS (`.fairy` class):
   - Change `height: 256px` to `height: 512px`
   - Change `background-size: 10100%` to `background-size: 14500%`
   - Update cache-busting: `url('fairy-sprite.png?v=XX')` (increment XX)
3. Edit `index.html` CSS (`.fairy.animate-left` and `.fairy.animate-right`):
   - Change `fairy-appear-left 4s` to `fairy-appear-left 8s`
   - Change `fairy-appear-right 4s` to `fairy-appear-right 8s`
   - Change `fairy-wave 4s steps(100)` to `fairy-wave 8s steps(144)`
4. Edit `index.html` JavaScript (inside `runFairyAnimation` function):
   - Change `setTimeout(..., 6000)` to `setTimeout(..., 12000)`
5. Increment `version.txt`

### Regenerating Winter Fairy Sprite Sheet

If you need to regenerate with updated snowball or video:
1. Extract frames: `python extract_winter_raw.py` (creates `winter_frames_raw/`)
2. Remove backgrounds: `python remove_winter_background.py` (creates `winter_frames/`)
3. Overlay snowball: `python overlay_snowball.py` (overlays on frames 51-144)
4. Create sprite: `python create_winter_sprite.py` (creates `fairy-sprite.png`)
5. Update cache-busting version in CSS: `url('fairy-sprite.png?v=XX')`
6. Increment `version.txt`

### Animation Timing Reference

**Winter Fairy (Current)**:
- Animation duration: 8s
- Pause between left/right: 12s (8s animation + 4s delay)
- Steps: 144 (145 frames - 1)
- Background-size: 14500% (145 × 100%)
- Frame dimensions: 512×512

**Original Fairy (Waving)**:
- Animation duration: 4s
- Pause between left/right: 6s (4s animation + 2s delay)
- Steps: 100 (101 frames - 1)
- Background-size: 10100% (101 × 100%)
- Frame dimensions: 512×256
