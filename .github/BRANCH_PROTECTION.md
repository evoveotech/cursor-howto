# Branch Protection Setup Guide

Protecting `main` prevents accidental pushes, enforces code review, and ensures CI passes before anything lands. This takes under 5 minutes.

---

## Method 1: GitHub UI (Recommended)

### Step 1: Go to Settings
1. Open your repo on GitHub: `https://github.com/evoveotech/cursor-howto`
2. Click **Settings** tab (rightmost tab, next to Insights)
3. In left sidebar, click **Branches** under "Code and automation"

### Step 2: Add Rule
1. Click **Add branch ruleset** or **Add classic protection rule**
2. Branch name pattern: `main`
3. Enable these settings:

```
☑ Require a pull request before merging
   ☑ Require approvals (set to 1)
   ☑ Dismiss stale PR approvals when new commits are pushed
   ☑ Require review from code owners (if you have CODEOWNERS)

☑ Require status checks to pass before merging
   ☑ Require branches to be up to date before merging
   [Search for and select these checks:]
   - Documentation Checks / Summary
   - Automated Testing / Test Summary

☑ Require conversation resolution before merging

☑ Do not allow bypassing the above settings

☑ Restrict pushes that create files larger than 100MB
```

### Step 3: Save
Click **Create** or **Save changes**.

Done. From now on, all changes to `main` must go through a reviewed PR with passing CI.

---

## Method 2: GitHub API / CLI (Power Users)

If you have admin access and the GitHub CLI installed:

```bash
# Install gh CLI if you haven't
# https://cli.github.com

# Authenticate
git auth login

# Create branch protection rule via API
curl -X PUT \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/evoveotech/cursor-howto/branches/main/protection \
  -d '{
    "required_status_checks": {
      "strict": true,
      "contexts": [
        "Summary",
        "Test Summary"
      ]
    },
    "enforce_admins": true,
    "required_pull_request_reviews": {
      "required_approving_review_count": 1,
      "dismiss_stale_reviews": true,
      "require_code_owner_reviews": false
    },
    "restrictions": null,
    "allow_force_pushes": false,
    "allow_deletions": false
  }'
```

Replace `YOUR_GITHUB_TOKEN` with a [fine-grained personal access token](https://github.com/settings/tokens?type=beta) that has **Repository administration** read/write permissions for `evoveotech/cursor-howto`.

---

## What This Prevents

| Scenario | Without Protection | With Protection |
|----------|-------------------|-----------------|
| `git push origin main` | Works instantly | ❌ Blocked. Must open PR. |
| Pushing broken CI | Lands on main | ❌ Blocked. CI must pass. |
| Merging without review | One-click merge | ❌ Blocked. Need 1 approval. |
| Force push to main | `git push --force` works | ❌ Blocked. No force pushes. |
| Accidental deletion | `git push origin :main` works | ❌ Blocked. Can't delete. |

---

## Workflow-Level Enforcement (Backup)

If you can't access repo settings (e.g., org repos), the CI workflow in `.github/workflows/branch-protection.yml` adds a second layer: it fails any direct push to `main` that bypasses a PR. See the workflow file for details.

---

## Tips

- **Solo maintainer?** Set required approvals to 0, but keep status checks. You still get CI gating without needing a second person.
- **Team repo?** Require 1-2 approvals depending on team size. Enable "dismiss stale reviews" to ensure fresh eyes on updated PRs.
- **Don't lock yourself out:** Make sure your admin account is exempt from restrictions if needed, or keep a second admin.

---

## Verify It's Working

After setup, try this locally:

```bash
git checkout main
git commit --allow-empty -m "test: verify branch protection"
git push origin main
```

You should see:
```
! [remote rejected] main -> main (protected branch hook declined)
error: failed to push some refs to 'github.com:evoveotech/cursor-howto.git'
```

That's the protection working. Undo the test commit: `git reset --hard HEAD~1`
