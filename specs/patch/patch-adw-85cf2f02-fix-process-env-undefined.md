# Patch: Fix process.env.NODE_ENV undefined in UMD bundle

## Metadata
adw_id: `85cf2f02`
review_change_request: `Issue #1: UMD bundle contains process.env.NODE_ENV references (lines 17 and 30) that are undefined in browser environments, causing JavaScript error 'process is not defined'. This prevents all React component islands from mounting. Console shows: 'Header island failed to mount: missing dependencies', 'PropertyHeader island failed to mount: missing dependencies', 'Footer island failed to mount: missing dependencies'. Resolution: Update vite.config.ts to define process.env.NODE_ENV for browser builds. Add to the config: define: { 'process.env.NODE_ENV': JSON.stringify('production') } at the root level. Then rebuild the component bundle with npm run build. Severity: blocker`

## Issue Summary
**Original Spec:** N/A (patch for build configuration issue)
**Issue:** UMD bundle contains `process.env.NODE_ENV` references on lines 17 and 30 that cause "process is not defined" error in browsers, preventing all React component islands (Header, PropertyHeader, Footer) from mounting
**Solution:** Add `define` configuration to vite.config.ts to replace `process.env.NODE_ENV` with the string `'production'` during build, then rebuild the component bundle

## Files to Modify
Use these files to implement the patch:

- `app/split-lease/components/vite.config.ts` - Add define configuration to replace process.env.NODE_ENV

## Implementation Steps
IMPORTANT: Execute every step in order, top to bottom.

### Step 1: Update vite.config.ts with define configuration
- Open `app/split-lease/components/vite.config.ts`
- Add `define: { 'process.env.NODE_ENV': JSON.stringify('production') }` at the root level of the config object (same level as `plugins` and `build`)
- This replaces all `process.env.NODE_ENV` references in the bundled code with the literal string `"production"`

### Step 2: Rebuild component bundle
- Execute `cd app/split-lease/components && npm run build` to regenerate the UMD bundle
- Verify the new bundle at `app/split-lease/components/dist/split-lease-components.umd.cjs` no longer contains `process.env.NODE_ENV` references

## Validation
Execute every command to validate the patch is complete with zero regressions.

1. **TypeScript Type Check**
   - Command: `cd app/split-lease/components && npm run typecheck`
   - Expected: Pass with no type errors

2. **Component Build**
   - Command: `cd app/split-lease/components && npm run build`
   - Expected: Build succeeds and generates UMD bundle

3. **UMD Bundle Validation**
   - Command: `cd app/test-harness && npm run test:validate`
   - Expected: Bundle validation passes, no process.env references detected

4. **Component Contract Tests**
   - Command: `cd app/test-harness && npx playwright test --grep "contract"`
   - Expected: All component contract tests pass, islands mount successfully

5. **Component Diagnostic Tests**
   - Command: `cd app/test-harness && npx playwright test --grep "diagnostics"`
   - Expected: No console errors about 'process is not defined'

## Patch Scope
**Lines of code to change:** ~3 lines (single config addition)
**Risk level:** low
**Testing required:** Full test suite validation to confirm islands mount correctly and no console errors occur
