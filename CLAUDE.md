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

The menu includes an animated fairy character that appears repeatedly, starting 2 seconds after page load and repeating every 25 seconds.

### Animation Sequence
1. **2 seconds** after page load, fairy pops up in the **lower left corner**
2. Fairy waves (plays through all sprite frames over 4 seconds)
3. Fairy drops back down
4. **2 second pause**
5. Fairy pops up in the **lower right corner**
6. Fairy waves again (4 seconds)
7. Fairy drops back down
8. **Entire sequence repeats every 25 seconds**

### Technical Implementation

**Sprite Sheet**:
- File: `fairy-sprite.png` (12.93 MB)
- Horizontal layout: 101 frames in a single row
- Individual frame size: 512×256 pixels (original video resolution, cropped to top half, resized)
- Total sprite dimensions: 51712×256 pixels
- Frames have transparent backgrounds (white/light-gray removed, threshold RGB > 200)
- Created from video using Python scripts in the repository
- Format: PNG (WebP cannot handle extremely wide images)

**CSS Animation**:
- Two fixed-position div elements (`#fairy-left` and `#fairy-right`)
- Display size: 512×256 pixels (full frame size, doubled from original plan)
- Position: `bottom: -300px` (hides transparent space at bottom of sprite below viewport)
- Combined animations:
  - `fairy-appear-left` / `fairy-appear-right`: Controls vertical slide (translateY from 20px to -300px) and opacity
  - `fairy-wave`: Steps through sprite frames using horizontal `background-position` (0% to 100%) with `steps(100)`
- Background-size: 10100% × 100% (101 frames horizontally)
- Animation duration: 4 seconds per appearance
- Uses `pointer-events: none` to avoid interfering with menu interaction

**JavaScript Trigger**:
- Initial delay: 2 seconds (`setTimeout(runFairyAnimation, 2000)`)
- Repeats every 25 seconds (`setInterval(runFairyAnimation, 25000)`)
- First animation (left): triggered immediately when function runs
- Second animation (right): triggered 6 seconds after left starts (4s animation + 2s delay)
- Animation classes are removed and re-added on each cycle to allow restart

### Source Files
- `fairy-sprite.png` - The sprite sheet used for animation (horizontal strip, 101 frames)
- `reduced_frames/` - Individual WebP frames (101 files)
- `frames/` - Full-resolution PNG frames (301 files, unprocessed)
- Python scripts for video processing:
  - `process_video_pil.py` - Extracts frames from video, crops to top half, resizes to 512px
  - `reduce_frames.py` - Selects every 3rd frame (301 → 101 frames)
  - `remove_white_background.py` - Makes white/light-gray backgrounds transparent
  - `convert_to_webp.py` - Converts PNG to WebP format
  - `create_sprite_sheet.py` - Combines frames into horizontal sprite sheet (PNG format)

### Modifying the Animation

To adjust timing:
- **Initial delay**: Change the `setTimeout` value in JavaScript (currently 2000ms = 2 seconds)
- **Repeat interval**: Change the `setInterval` value (currently 25000ms = 25 seconds)
- **Animation duration**: Update animation duration in `.fairy.animate-left` and `.fairy.animate-right` (currently 4s)
- **Pause between left/right**: Change the inner `setTimeout` value (currently 6000ms = 4s animation + 2s pause)

To adjust appearance:
- **Size**: Modify `.fairy` width/height (currently 512×256px) and update `background-size` percentage accordingly
- **Horizontal position**: Change `.fairy.left` and `.fairy.right` left/right values (currently 20px)
- **Vertical alignment**: Adjust `.fairy` bottom position (currently -300px to hide transparent space)
- **Slide distance**: Adjust `translateY` values in keyframes (currently starts at 20px, slides to -300px)

To regenerate sprite sheet:
- Modify frames in `reduced_frames/`
- Run `python create_sprite_sheet.py` (creates horizontal PNG strip)
- Update `background-size` in CSS if frame count changes (should be `[frame_count * 100]%` for width)
- Note: Script creates PNG format because WebP has width limitations
