---
name: simplify-codebase
description: "Simplify code changed in the current task and roll back overengineering. Use when the user asks to simplify, tidy or trim recent changes, or when another skill calls it."
---

Read applicable project instructions before starting. Use their sources, artifact locations and workflow settings where specified; otherwise use this skill’s defaults. If a required step conflicts with applicable constraints, report the blocked step.

If the project's root `AGENTS.md` has no `agent-workflow:core` block, tell the user that the project is not set up and suggest `/setup-workflow` (`$setup-workflow` in Codex). Continue only if the user says so.

Make the code that this task changed easier to read and cheaper to own. Choose clarity over brevity. Use two kinds of change:

- **Restructure.** Keep the behavior. Make the shape simpler: flatter flow, clearer names, less duplication.
- **Roll back.** Remove code that solves a problem nobody has. This includes protective code for an edge case of an edge case, when the code costs far more complexity than the problem is worth. It also includes migrations and backward compatibility for a product with no users yet. Keep every check on input that the system does not control.

A restructure keeps the behavior identical: same outputs, same errors, same public interfaces. A rollback changes only the behavior of the code that it removes.

## Principles

1. **Preserve behavior.** Before each change, ask three questions. Does the code give the same output for every input? Does it give the same errors? Does it keep the same side effects in the same order? If an answer is unclear, do not make the change.
2. **Follow the project.** Make the code more consistent with the codebase. Do not impose outside preferences. A change that breaks the project style is churn.
3. **Prefer clarity.** Write explicit code when the compact form makes the reader stop and think.
4. **Stay balanced.** Do not inline a helper that gives a concept its name. Do not merge unrelated logic. Do not remove an abstraction that exists for testing or extension. Fewer lines is not the goal.
5. **Stay in scope.** Change only the code in the diff of this task, or in the whole files that the caller names as the scope. Changes outside that scope add noise and risk.

## Process

### 1. Pin the scope

Use the paths and the starting commit from the caller. Otherwise use the files that you changed in this session. Read each file in full. Read the diff of its changed lines. If the caller names whole files as the scope, for example `refactor-codebase`, all code in those files is in scope. Otherwise touch code outside the diff only when the user asks for a wider scope.

If the scope is empty, report that and stop.

### 2. Read the standards

Read the documented coding standards of the project: `AGENTS.md`, `CODING_STANDARDS.md`, `CONTRIBUTING.md`, and the linter and formatter configs. A documented standard wins over every preference in this skill. If the project documents none, match the style of the surrounding code.

Read what the project says about its consumers: published interfaces, released versions, stored data, and which input is untrusted.

### 3. Check the fence

Do this before you change or remove anything. Answer these questions for the code:

- What is its job?
- What calls it, and what does it call?
- Which test or requirement defines its behavior?
- What do `git log` and `git blame` say about why it exists? The reason can be performance, a platform limit or history.

If you cannot answer, leave the code alone.

Stop in these cases. Report "No changes required" for the first case. Report the reason for the others.

- The code is already clear and nothing in it is unjustified.
- You do not understand what the code does.
- The code is performance-critical, and the simpler form is measurably slower.
- The module will be rewritten soon.

### 4. Restructure

Look for these signals in the scoped code.

| Signal | Fix |
| --- | --- |
| Nesting of 3 or more levels | Use guard clauses and early returns, or extract a named function. |
| Long function with several jobs | Split it into functions with descriptive names. |
| Nested ternary operator or dense one-liner | Use an `if`/`else` chain, a `switch` or a lookup table. |
| Boolean flag parameters, such as `run(true, false)` | Use an options object or separate functions. |
| The same condition in several places | Extract a named predicate. |
| Generic names: `data`, `temp`, `item` | Name the value by its content. |
| Abbreviations: `usr`, `cfg` | Use full words. Keep universal ones: `id`, `url`. |
| A name that misleads, such as a `get` function that changes state | Rename it to match the behavior. |
| A comment that says what the code does | Delete it. Keep comments that say why. |
| The same logic of 5 or more lines in several places | Extract one shared function. |
| Dead branches, unused variables, commented-out code | Delete them after you confirm that they are dead. |
| A redundant type assertion | Delete it. |

#### Examples

The examples show the shape of a good change. The syntax can differ in your language. Apply a change only if it keeps the behavior.

**Clarity over cleverness.**

```typescript
// UNCLEAR: dense ternary chain
const label = isNew ? 'New' : isUpdated ? 'Updated' : isArchived ? 'Archived' : 'Active';

// CLEAR: readable mapping
function getStatusLabel(item: Item): string {
  if (item.isNew) return 'New';
  if (item.isUpdated) return 'Updated';
  if (item.isArchived) return 'Archived';
  return 'Active';
}
```

```typescript
// UNCLEAR: chained reduce with inline logic
const result = items.reduce((acc, item) => ({
  ...acc,
  [item.id]: { ...acc[item.id], count: (acc[item.id]?.count ?? 0) + 1 }
}), {});

// CLEAR: named intermediate step
const countById = new Map<string, number>();
for (const item of items) {
  countById.set(item.id, (countById.get(item.id) ?? 0) + 1);
}
```

**TypeScript and JavaScript.**

```typescript
// Unnecessary async wrapper
// Before
async function getUser(id: string): Promise<User> {
  return await userService.findById(id);
}
// After. Check first that findById never throws before it returns a promise.
function getUser(id: string): Promise<User> {
  return userService.findById(id);
}

// Verbose conditional assignment
// Before
let displayName: string;
if (user.nickname) {
  displayName = user.nickname;
} else {
  displayName = user.fullName;
}
// After
const displayName = user.nickname || user.fullName;

// Manual array building
// Before
const activeUsers: User[] = [];
for (const user of users) {
  if (user.isActive) {
    activeUsers.push(user);
  }
}
// After
const activeUsers = users.filter((user) => user.isActive);

// Redundant boolean return
// Before
function isValid(input: string): boolean {
  if (input.length > 0 && input.length < 100) {
    return true;
  }
  return false;
}
// After
function isValid(input: string): boolean {
  return input.length > 0 && input.length < 100;
}
```

**Python.**

```python
# Verbose dictionary building
# Before
result = {}
for item in items:
    result[item.id] = item.name
# After
result = {item.id: item.name for item in items}

# Nested conditionals -> guard clauses
# Before
def process(data):
    if data is not None:
        if data.is_valid():
            if data.has_permission():
                return do_work(data)
            else:
                raise PermissionError("No permission")
        else:
            raise ValueError("Invalid data")
    else:
        raise TypeError("Data is None")
# After
def process(data):
    if data is None:
        raise TypeError("Data is None")
    if not data.is_valid():
        raise ValueError("Invalid data")
    if not data.has_permission():
        raise PermissionError("No permission")
    return do_work(data)
```

**React and JSX.**

```tsx
// Verbose conditional rendering
// Before
function UserBadge({ user }: Props) {
  if (user.isAdmin) {
    return <Badge variant="admin">Admin</Badge>;
  } else {
    return <Badge variant="default">User</Badge>;
  }
}
// After
function UserBadge({ user }: Props) {
  const variant = user.isAdmin ? 'admin' : 'default';
  const label = user.isAdmin ? 'Admin' : 'User';
  return <Badge variant={variant}>{label}</Badge>;
}

// Prop drilling through intermediate components
// Context or composition can solve this better. This is a judgment call.
// Flag it in the report. Do not refactor it by yourself.
```

### 5. Roll back

Look at each guard, fallback, validation, wrapper, option, extension point, compatibility path and migration that the diff adds or touches. Ask which requirement, verified contract or consumer needs it. If you cannot name one from the task, the callers and the history, the code is a candidate.

Compare each candidate with the patterns below. If the case looks more like the "Keep" example, keep the code. The examples show the shape. The syntax can differ.

| Pattern | Roll back | Keep |
| --- | --- | --- |
| Validation inside trusted code | `if (id <= 0) throw` in an internal `getUser(id: number)`, called only by code that already checks `id` | The email check in the body of a public `/register` endpoint |
| Handler for a failure that cannot happen | `try { JSON.stringify(internalConfig) } catch { return "{}" }` for an object that the code builds itself | `try` around `JSON.parse(userInput)`, a file read or a network call |
| Fallback that hides a bug | `order.price ?? 0` when an order always has a price. A missing price becomes a free order. | A documented default for an optional setting |
| Guard repeated per symptom | The same null check at four call sites, when one place produces the bad value. Fix that place. Propose this rollback. | A shared guard that restores a real contract |
| Interface with one implementation | `UserRepository` plus one `PostgresUserRepository`. A factory and a strategy class for two `if` branches. | `Storage` with real `S3Storage` and `LocalStorage` implementations chosen by environment |
| Helper for similar lines used once or twice | `formatTimestamp(date)` from three lines in two places | `validateOrderTotal(order)` with non-trivial logic, called from six modules |
| Wrapper that only forwards | `isEmpty(list) { return list.length === 0 }`, or a function that calls a standard-library, platform or installed-dependency function with the same arguments | A thin adapter around a volatile external SDK that five modules use |
| Extension point without a second use | A plugin registry with one plugin. An `options` parameter that no caller passes. A strategy for providers that exist only in the roadmap. | Stripe and Razorpay support when the task requires both |
| Configuration for a constant | A `MAX_RETRY_COUNT` environment variable that no environment changes | `DATABASE_URL`, which differs between environments |
| Compatibility shim with no consumers | `processOrder` kept as a deprecated alias of `executeOrder`, when no caller exists outside the diff and nothing was published. Check released versions and public exports first. | The alias of a public method that external callers use |
| Migration or rollout for a change that needs none | A data migration when no stored shape changes. A 10%, 50%, 100% flag rollout for a refactor with no visible effect. | A migration for data that already exists in production |
| Structure larger than the code | `types.ts`, `utils.ts`, `constants.ts` and `index.ts` for 80 lines. `class NotFoundError extends Error {}` that adds nothing. | A split of a 1500-line `service.ts` by responsibility |

Keep these always:

- Validation and encoding of input that the system does not control: HTTP requests, user files, third-party responses, environment, data written by other systems.
- Authentication, authorization and other security checks.
- Protection against data loss.
- Accessibility basics.
- Logging and error reporting that the project requires.
- Comments that explain why.
- Code that a requirement, a contract test or a named consumer needs.

Sort each candidate by size:

- **Small.** It sits inside the diff, nothing else depends on it, and no test names it. Remove it now.
- **Larger.** It spans several files, or a test covers it. It can also be a public interface, a config value, a migration or a compatibility path. Do not edit it. List it as a proposal with the evidence and the smallest safe deletion. The user confirms it.

If you run in a subagent, you cannot confirm with the user. Apply the small rollbacks. Return the larger ones as proposals.

A test that covers only code that you rolled back goes with that code, after the user confirms the rollback. A test that is weak for another reason is a review finding. See the anti-patterns in `tdd`.

### 6. Verify

Apply one change at a time. After each change, run the typecheck of the project and the tests that cover the file. If a check fails, revert that change. Keep the original code.

If the checks cannot run, report which ones and why. Do not claim that the behavior is unchanged without them.

After all changes, compare the result with the original:

- Is the result easier to understand?
- Does it add a pattern that the codebase does not use?
- Is the diff clean and reviewable?

If the result is harder to read than the original, revert it. Not every attempt succeeds.

### 7. Report

Report one line per file: what you changed. List the proposals separately. Mention what you left alone only when the choice affects the reader. Leave the changes uncommitted unless the caller or the project rules say otherwise.

## Red flags

Stop and revert if one of these happens:

- A test needs an edit to pass. The change altered behavior.
- The result is longer and harder to follow than the original.
- A rename follows your preference, not the project convention.
- Error handling was removed or weakened without a rollback with evidence.
- You changed code that you do not fully understand.
- You changed code outside the diff without a request.
- You made many changes at once and cannot tell which one broke a check.

## Done when

- The typecheck and the covering tests pass. No test was edited.
- Every change is a separate step that you can review.
- The diff has no unrelated edits and no unused imports or dead code that your change left.
- The result follows the project conventions.
- Every rollback has a named reason. Every larger candidate is a proposal.
- No error handling was removed from input that the system does not control.
