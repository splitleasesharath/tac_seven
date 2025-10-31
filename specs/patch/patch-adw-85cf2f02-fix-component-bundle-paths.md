# Patch: Fix Component Bundle and CSS 404 Errors

## Metadata
adw_id: `85cf2f02`
review_change_request: `Issue #1: Component bundle and CSS files fail to load with 404 errors. The HTML page uses relative paths (../../components/dist/split-lease-components.umd.cjs) which are not resolved correctly when served via Python's http.server from the app/split-lease/pages directory. Browser console shows 'Header island failed to mount: missing dependencies', 'PropertyHeader island failed to mount: missing dependencies', and 'Footer island failed to mount: missing dependencies'. This prevents any React components from rendering. Resolution: Fix the resource paths in index.html or adjust the server configuration to correctly serve the component bundle and CSS files. Options: 1) Use absolute paths from the server root, 2) Configure the Python HTTP server to serve from the correct directory with proper path mapping, 3) Use a proper static file server with correct directory structure, or 4) Build and deploy with proper asset path resolution. Severity: blocker`

## Issue Summary
**Original Spec:** N/A
**Issue:** HTML pages use relative paths like `../../components/dist/split-lease-components.umd.cjs` which fail to resolve when served via Python's http.server from `app/split-lease/pages` directory, causing 404 errors and preventing React components from rendering.
**Solution:** Change the Python HTTP server to serve from `app/split-lease` (parent directory) instead of `app/split-lease/pages`, and update all relative paths in HTML files to use paths relative to this new server root. This ensures component bundles at `components/dist/*` are accessible via `/components/dist/*`.

## Files to Modify
Use these files to implement the patch:

1. `app/split-lease/pages/index.html` - Update component bundle and CSS paths
2. `app/split-lease/pages/search/index.html` - Update component bundle and CSS paths
3. `app/split-lease/pages/view-split-lease/index.html` - Update component bundle and CSS paths
4. `README.md` - Update server instructions to run from `app/split-lease` directory

## Implementation Steps
IMPORTANT: Execute every step in order, top to bottom.

### Step 1: Update index.html paths
- Change CSS path from `../components/dist/style.css` to `/components/dist/style.css`
- Change bundle path from `../components/dist/split-lease-components.umd.cjs` to `/components/dist/split-lease-components.umd.cjs`
- Update shared script paths from `shared/js/*` to `/pages/shared/js/*`

### Step 2: Update search/index.html paths
- Change CSS path from `../../components/dist/style.css` to `/components/dist/style.css`
- Change bundle path from `../../components/dist/split-lease-components.umd.cjs` to `/components/dist/split-lease-components.umd.cjs`
- Update shared script paths from `../shared/js/*` to `/pages/shared/js/*`

### Step 3: Update view-split-lease/index.html paths
- Change CSS path from `../../components/dist/style.css` to `/components/dist/style.css`
- Change bundle path from `../../components/dist/split-lease-components.umd.cjs` to `/components/dist/split-lease-components.umd.cjs`
- Update logoSrc paths in inline scripts from `../shared/images/*` to `/pages/shared/images/*`

### Step 4: Update README.md server instructions
- Update section "3. View Pages" to instruct running server from `app/split-lease` directory
- Add command: `cd app/split-lease && python -m http.server 8000`
- Update page URLs to: `http://localhost:8000/pages/index.html`, `http://localhost:8000/pages/search/index.html`, `http://localhost:8000/pages/view-split-lease/index.html`

## Validation
Execute every command to validate the patch is complete with zero regressions.

1. `cd app/split-lease/components && npm run build` - Ensure component bundles are built
2. `cd app/split-lease && python -m http.server 8000` - Start server from correct directory (run in background)
3. Manually verify `http://localhost:8000/pages/index.html` loads without 404 errors in browser console
4. Manually verify `http://localhost:8000/pages/search/index.html` loads without 404 errors in browser console
5. Manually verify `http://localhost:8000/pages/view-split-lease/index.html` loads without 404 errors and components render
6. `cd app/test-harness && npx playwright test` - Run all component tests to ensure no regressions

## Patch Scope
**Lines of code to change:** ~15 lines across 4 files
**Risk level:** low
**Testing required:** Manual browser testing to verify resource loading, automated Playwright tests to verify component functionality
