# Good and Bad Tests

## Good Tests

**Behavior-focused**: Test the project-approved observable contract at the chosen level. Unit tests of business logic are valid; these examples do not require integration infrastructure.

```typescript
// GOOD: Tests observable behavior
test("user can checkout with valid cart", async () => {
  const cart = createCart();
  cart.add(product);
  const result = await checkout(cart, paymentMethod);
  expect(result.status).toBe("confirmed");
});
```

Characteristics:

- Tests behavior users/callers care about
- Uses the agreed interface, which may be a business function, module boundary or system API
- Survives internal refactors
- Describes WHAT, not HOW
- Assertions together establish one behavior, without an arbitrary assertion-count limit

## Bad Tests

**Implementation-detail tests**: Coupled to incidental structure rather than a required contract. The example is weak when payment dispatch itself is not part of the agreed behavior.

```typescript
// BAD: Tests implementation details
test("checkout calls paymentService.process", async () => {
  const mockPayment = jest.mock(paymentService);
  await checkout(cart, payment);
  expect(mockPayment.process).toHaveBeenCalledWith(cart.total);
});
```

Red flags:

- Mocking collaborators merely to assert implementation wiring
- Testing private details without a required invariant
- Asserting call counts/order where they are not part of the contract
- Test breaks when refactoring without behavior change
- Test name describes HOW not WHAT
- Using a side channel unrelated to the agreed behavior

The database example below assumes the contract is user retrieval. A persistence or migration contract may legitimately require inspecting database state when the project authorizes that test level.

```typescript
// BAD: Bypasses interface to verify
test("createUser saves to database", async () => {
  await createUser({ name: "Alice" });
  const row = await db.query("SELECT * FROM users WHERE name = ?", ["Alice"]);
  expect(row).toBeDefined();
});

// GOOD: Verifies through interface
test("createUser makes user retrievable", async () => {
  const user = await createUser({ name: "Alice" });
  const retrieved = await getUser(user.id);
  expect(retrieved.name).toBe("Alice");
});
```

**Tautological tests**: Expected value restates the implementation, so the test passes by construction.

```typescript
// BAD: Expected value is recomputed the way the code computes it
test("calculateTotal sums line items", () => {
  const items = [{ price: 10 }, { price: 5 }];
  const expected = items.reduce((sum, i) => sum + i.price, 0);
  expect(calculateTotal(items)).toBe(expected);
});

// GOOD: Expected value is an independent, known literal
test("calculateTotal sums line items", () => {
  expect(calculateTotal([{ price: 10 }, { price: 5 }])).toBe(15);
});
```
