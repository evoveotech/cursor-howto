#!/bin/bash
# Pre-review hook: Run linting and type checking before AI review
# Place in ~/.cursor/hooks/ or project .cursor/hooks/
# Configure in ~/.cursor/settings.json:
# {
#   "hooks": {
#     "PreToolUse": [{
#       "matcher": "Write",
#       "hooks": ["~/.cursor/hooks/pre-review.sh"]
#     }]
#   }
# }

echo "[pre-review] Running quick checks..."

# Run linting if available
if command -v npx &> /dev/null && [ -f "package.json" ]; then
    if npx eslint --quiet . 2>/dev/null; then
        echo "[pre-review] ESLint: PASS"
    else
        echo "[pre-review] ESLint: FAIL — fix linting errors before requesting review"
        exit 1
    fi
fi

# Run type checking if available
if command -v npx &> /dev/null && [ -f "tsconfig.json" ]; then
    if npx tsc --noEmit 2>/dev/null; then
        echo "[pre-review] TypeScript: PASS"
    else
        echo "[pre-review] TypeScript: FAIL — fix type errors before requesting review"
        exit 1
    fi
fi

echo "[pre-review] All checks passed. Ready for AI review."
