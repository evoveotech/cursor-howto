---
description: 'Generate API documentation from code automatically'
---

Generate documentation for the selected code (function, class, component, or module).

Detect the type and generate appropriate docs:

**API Endpoint:**
```
## POST /api/v1/resource

### Auth
[Required scopes/roles]

### Request
```json
{schema}
```

### Response
```json
{example response}
```

### Errors
| Code | When |
|------|------|
| 400 | ... |
```

**React Component:**
```
## ComponentName

### Props
| Prop | Type | Required | Default | Description |

### Usage
```tsx
<Example />
```

### Notes
[Performance, accessibility, edge cases]
```

**Utility Function:**
```
## functionName()

### Signature
```ts
function functionName(params): ReturnType
```

### Parameters
| Name | Type | Description |

### Returns
| Type | Description |

### Example
```ts
// Before (the problem)
// After (using this function)
```
```

Match the project's existing documentation style. Extract types from the actual code.
