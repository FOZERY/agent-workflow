# When to Mock

Follow the project's existing test-double and fixture conventions at the agreed test level. Isolate external APIs, time, randomness, files or database access when needed for deterministic tests.

An existing test database may be appropriate for an approved integration contract; it is not a default requirement. Reuse available fixtures and doubles. New containers, services, dependencies or network access require the project's permission.

Mocking an internal collaborator can be valid for an agreed unit-test boundary. Prefer assertions about business outcomes over implementation call order, except where the interaction itself is the required behavior.

## Designing for Mockability

When an agreed design change needs a testable boundary, these are options, not reasons to redesign production code merely for tests:

**1. Use dependency injection**

Where the project uses dependency injection, pass external dependencies rather than creating them internally:

```typescript
// Easy to mock
function processPayment(order, paymentClient) {
  return paymentClient.charge(order.total);
}

// Hard to mock
function processPayment(order) {
  const client = new StripeClient(process.env.STRIPE_KEY);
  return client.charge(order.total);
}
```

**2. Consider operation-specific interfaces**

Where appropriate to the project design, specific functions can make external operations easier to stub than one generic function with conditional test logic:

```typescript
// GOOD: Each function is independently mockable
const api = {
  getUser: (id) => fetch(`/users/${id}`),
  getOrders: (userId) => fetch(`/users/${userId}/orders`),
  createOrder: (data) => fetch('/orders', { method: 'POST', body: data }),
};

// BAD: Mocking requires conditional logic inside the mock
const api = {
  fetch: (endpoint, options) => fetch(endpoint, options),
};
```

The SDK approach means:
- Each mock returns one specific shape
- No conditional logic in test setup
- Easier to see which endpoints a test exercises
- Type safety per endpoint
