# Redux-Saga
**URL:** https://redux-saga.js.org
**Page Title:** Redux-Saga - An intuitive Redux side effect manager. | Redux-Saga
--------------------


### Asynchronous

ES6 generators make asynchronous flows easy to read, write, and test.
      Create complex side effects without getting bogged down by the details.

### Composition-focused

Sagas enable numerous approaches to tackling parallel execution, task concurrency,
      task racing, task cancellation, and more. Keep total control over the flow of your code.

### Easy To Test

Assert results at each step of a generator or for a saga as a whole.
      Either way, side effect testing is quick, concise, and painless, as testing should be.

## Example Usage

- 1. Dispatch an action
- 2. Initiate a side effect
- 3. Connect to the store
- 4. Connect to the store (new version)
Suppose we have a UI to fetch some user data from a remote server when a button is clicked. (For brevity, we'll just show the action triggering code.)
The component dispatches a plain object action to the store. We'll create a Saga that watches for all USER_FETCH_REQUESTED actions and triggers an API call to fetch the user data.
To run our Saga, we have to connect it to the Redux store using the redux-saga middleware.
This is the new version of running saga by using configureStore from reduxjs/toolkit instead of createStore from Redux .

## Backers

Support us with a monthly donation and help us continue our activities. Become a backer

## Sponsors

Become a sponsor and have your logo shown below and on Github with a link to your site. Become a sponsor

--------------------