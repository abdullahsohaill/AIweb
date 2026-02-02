# Stripe Test Cards
**URL:** https://docs.stripe.com/testing
**Page Title:** Test card numbers | Stripe Documentation
--------------------

[LINK: Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftesting)
[LINK: Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftesting)

## Testing

## Simulate payments to test your integration.

Test your integration in a sandbox by simulating transactions with test values—these transactions don’t move funds.
You can access your sandboxes using the account picker in the Dashboard .
Test cards act as “fake” credit cards, and allow you to simulate the following scenarios:
- Successful payments by card brand or country
- Card errors due to declines , fraud or invalid data
- Disputes and refunds
- Authentication with 3D Secure and PINs
You can also test non-card payments in a sandbox. Non-card payments are payment methods that aren’t credit or debit cards. Stripe supports various non-card payment options, such as digital wallets and bank transfers. Each payment method has its own special values.
Don’t use testing environments to load test your integration because you might hit rate limits . To load test your integration, see load testing .

## How to use test cards

When you work with a test card, use test API keys in all API calls. This is true whether you’re serving a payment form to test interactively or writing test code.
[LINK: test API keys](/keys#obtain-api-keys)
Don’t use real card details. The Stripe Services Agreement prohibits testing in live mode using real payment method details. Use your test API keys and the card numbers below.

### Testing interactively

When testing interactively, use a card number, such as 4242 4242 4242 4242 . Enter the card number in the Dashboard or in any payment form.
- Use a valid future date, such as 12/34 .
- Use any three-digit CVC (four digits for American Express cards).
- Use any value you like for other form fields.

### Test code

When writing test code, use a PaymentMethod such as pm_card_visa instead of a card number. We don’t recommend using card numbers directly in API calls or server-side code, even in testing environments. If you do use them, your code might not be PCI-compliant when you go live. By default, a PaymentMethod isn’t attached to a Customer .
[LINK: Customer](/api/customers)
When you’re ready to take your integration live, replace your test publishable and secret API keys with live ones. You can’t process live payments if your integration is still using your Test API keys.

## Simulate a payment by card brand

To simulate a successful payment for a specific card brand, use test cards from the following list.
Cross-border fees are assessed based on the country of the card issuer. Cards where the issuer country isn’t the US (such as JCB and UnionPay) might be subject to a cross-border fee, even in testing environments.
Most Cartes Bancaires and eftpos cards are co-branded with either Visa or Mastercard. The test cards in the following table simulate successful payments with co-branded cards.

## Simulate a payment by country

To simulate successful payments from specific countries, use test cards from the following sections.
Strong Customer Authentication regulations require 3D Secure authentication for online payments within the European Economic Area . The test cards in the Europe and Middle East section simulate a payment that succeeds without authentication. We also recommend testing authentication scenarios using 3D Secure test cards .
To test subscriptions that require mandates and pre-debit notifications, see India recurring payments .

## Simulate an HSA or FSA card payment

Below are test card numbers for simulating transactions using a health savings account (HSA) and a flexible spending account (FSA). These accounts are commonly used for medical expenses, and testing with them ensures proper handling of healthcare-related transactions within your application.

## Simulate a declined payment

To test your integration’s error-handling logic by simulating payments that the issuer declines for various reasons, use test cards from this section. These cards return a card error with the listed error code and decline code .
Provide a CVC when you test CVC behavior. Stripe skips the CVC check if you omit it, so the check can’t fail. To simulate an incorrect CVC, use the “Incorrect CVC decline” test card listed in the following table and provide any three-digit CVC.
You can’t attach cards that simulate issuer declines to a Customer object. To simulate a declined payment with an attached card, use the “Decline after attaching” test card listed in the following table.
[LINK: Customer](/api/customers)

## Fraud prevention

Stripe’s fraud prevention system, Radar, can block payments when they have a high risk level or fail verification checks. You can use the cards in this section to test your Radar settings. You can also use them to test how your integration responds to blocked payments.
Each card simulates specific risk factors. Your Radar settings determine which risk factors cause it to block a payment. Blocked payments result in card errors with an error code of fraud .
To trigger a failed CVC check, include a CVC (any three-digit number). To trigger a failed postal code check, include any valid postal code. If you omit these fields, Radar skips those checks, so they can’t fail.
Always blocked
The charge has a risk level of “highest”
Radar always blocks it.
Highest risk
The charge has a risk level of “highest”
Radar might block it depending on your settings .
Elevated risk
The charge has a risk level of “elevated”
If you use Radar for Fraud Teams , Radar might queue it for review .
CVC check fails
If you provide a CVC number, the CVC check fails.
Radar might block it depending on your settings.
Postal code check fails
If you provide a postal code, the postal code check fails.
Radar might block it depending on your settings.
CVC check fails with elevated risk
If you provide a CVC number, the CVC check fails with a risk level of “elevated”
Radar might block it depending on your settings.
Postal code check fails with elevated risk
If you provide a postal code, the postal code check fails with a risk level of “elevated”
Radar might block it depending on your settings .
Line1 check fails
The address line 1 check fails.
The payment succeeds unless you block it with a custom Radar rule .
Address checks fail
The address postal code check and address line 1 check both fail.
Radar might block it depending on your settings.
Address unavailable
The address postal code check and address line 1 check are both unavailable.
The payment succeeds unless you block it with a custom Radar rule .

## Trigger an error with invalid data

To test errors resulting from invalid data, provide invalid details. You don’t need a special test card for this. Any invalid value works. For instance:
- invalid_expiry_month : Use an invalid month, such as 13 .
- invalid_expiry_year : Use a year up to 50 years in the past, such as 95 .
- invalid_cvc : Use a two-digit number, such as 99 .
- incorrect_number : Use a card number that fails the Luhn check , such as 4242424242424241 .

## Simulate a dispute

To simulate a disputed transaction , use the test cards in this section. Then, to simulate winning or losing the dispute, provide winning or losing evidence .
[LINK: Visa Compelling Evidence 3.0 eligible dispute](/disputes/api/visa-ce3#testing)
[LINK: Visa compliance dispute](/disputes/api/visa-compliance#testing)

### Evidence

To simulate winning or losing the dispute, respond with one of the evidence values from the table below.
- If you respond using the API , pass the value from the table as uncategorised_text .
[LINK: respond using the API](/disputes/api)
[LINK: uncategorised_text](/api/disputes/update#update_dispute-evidence-uncategorized_text)
- If you respond in the Dashboard or in Connect embedded components , enter the value from the table in the Additional information field. Then, click Submit evidence .

## Simulate an asynchronous refund

In live mode, refunds are asynchronous: a refund can appear to succeed and later fail, or can appear as pending at first and later succeed. To simulate refunds with those behaviors, use the test cards in this section. With all other test cards, refunds succeed immediately and don’t change status after that.
[LINK: event](/api/events/types#event_types-refund.updated)
[LINK: event](/api/events/types#event_types-refund.failed)
You can cancel a card refund only by using the Dashboard. In live mode, you can cancel a card refund within a short but nonspecific period of time. Testing environments simulate that period by allowing you to cancel a card refund within 30 minutes.

## Send funds to your available balance

To send the funds from a test transaction directly to your available balance, use the test cards in this section. Other test cards send funds from a successful payment to your pending balance.

## Test 3D Secure authentication

3D Secure requires an additional layer of authentication for credit card transactions. The test cards in this section allow you to simulate triggering authentication in different payment flows.
Only cards in this section effectively test your 3D Secure integration by simulating defined 3DS behaviour, such as a challenge flow or an unsupported card. Other Stripe testing cards might still trigger 3DS, but we return attempt _ acknowledged to bypass the additional steps since 3DS testing isn’t the objective for those cards.
3D Secure redirects won’t occur for payments created directly in the Stripe Dashboard. Instead, use your integration’s own front end or an API call.

### Authentication and setup

To simulate payment flows that include authentication, use the test cards in this section. Some of these cards can also be set up for future payments or have already been.

### Support and availability

Stripe requests authentication when required by regulation or when triggered by your Radar rules or custom code. Even if authentication is requested, it can’t always be performed – for instance, the customer’s card might not be enrolled or an error might occur. Use the test cards in this section to simulate various combinations of these factors.
All 3DS references indicate 3D Secure 2 .

### 3D Secure mobile challenge flows

In a mobile payment, several challenge flows for authentication – where the customer has to interact with prompts in the UI – are available. Use the test cards in this section to trigger a specific challenge flow for test purposes. These cards aren’t useful in browser-based payment forms or in API calls. In those environments, they work but don’t trigger any special behaviour. Because they’re not useful in API calls, we don’t provide any PaymentMethod or Token values to test with.

## Simulate a captcha challenge

To prevent fraud, Stripe might display a captcha challenge to the user on the payment page. Use the test cards below to simulate this flow.

## Simulate an in-person payment with a PIN

Use the test cards in this section to simulate successful in-person payments where a PIN is involved. There are many other options for testing in-person payments, including a simulated reader and physical test cards. See Test Stripe Terminal for more information.
[LINK: cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)
[LINK: cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)
[LINK: cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)
[LINK: cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)

## Test a webhook or event destination

To test your webhook endpoint or event destination , choose one of these two options:
- Perform actions in a sandbox that send legitimate events to your event destination. For example, to trigger the charge.succeeded event, you can use a test card that produces a successful charge .
[LINK: charge.succeeded](/api#event_types-charge.succeeded)
- Trigger events using the Stripe CLI or using Stripe for Visual Studio Code .

## Rate limits

If your requests in your testing environments begin to receive 429 HTTP errors, make them less frequently. These errors come from our rate limiter , which is more strict in testing environments than in live mode.
We don’t recommend load testing your integration using the Stripe API in testing environments. Because the load limiter is stricter in testing environments, you might see errors that you wouldn’t see in production. See load testing for an alternative approach.

## Test a non-card payment method

When you use a test non-card payment method, use test API keys in all API calls. This is true whether you’re serving a payment form you can test interactively or writing test code.
[LINK: test API keys](/keys#obtain-api-keys)
Different payment methods have different test procedures:
Learn how to test scenarios with instant verifications using Financial Connections .

### Send transaction emails in a sandbox

After you collect the bank account details and accept a mandate, send the mandate confirmation and microdeposit verification emails in a sandbox .
If your domain is {domain} and your username is {username} , use the following email format to send test transaction emails: {username}+test_email@{domain} .
For example, if your domain is example.com and your username is info , use the format info+test_email@example.com for testing ACH Direct Debit payments. This format ensures that emails are routed correctly. If you don’t include the +test_email suffix, we won’t send the email.
You need to activate your Stripe account before you can trigger these emails while testing.

### Test account numbers

Stripe provides several test account numbers and corresponding tokens you can use to make sure your integration for manually-entered bank accounts is ready for production.
[LINK: PaymentIntent cancellation](/api/payment_intents/cancel)
Before test transactions can complete, you need to verify all test accounts that automatically succeed or fail the payment. To do so, use the test microdeposit amounts or descriptor codes below.

### Test microdeposit amounts and descriptor codes

To mimic different scenarios, use these microdeposit amounts or 0.01 descriptor code values.

### Test settlement behaviour

Test transactions settle instantly and are added to your available test balance. This behaviour differs from live mode, where transactions can take multiple days to settle in your available balance.

## Test Link

Don’t store real user data in sandbox Link accounts. Treat them as if they’re publicly available, because these test accounts are associated with your publishable key.
Currently, Link only works with credit cards, debit cards, and qualified US bank account purchases. Link requires domain registration .
You can create sandbox accounts for Link using any valid email address. The following table shows the fixed one-time passcode values that Stripe accepts for authenticating sandbox accounts:

### Multiple funding sources

As Stripe adds additional funding source support, you don’t need to update your integration. Stripe automatically supports them with the same transaction settlement time and guarantees as card and bank account payments.

## Test a redirect-based flow

To test your integration’s redirect-handling logic by simulating a payment that uses a redirect flow (for example, iDEAL), use a supported payment method that requires redirects .
[LINK: requires redirects](/payments/payment-methods/payment-method-support#additional-api-supportability)
To create a test PaymentIntent that either succeeds or fails:
- Go to the payment methods settings in the Dashboard and enable a supported payment method by clicking Turn on in your testing environment.
- Collect payment details.
- Submit the payment to Stripe.
- Authorise or fail the test payment.
Make sure that the page (corresponding to return _ url ) on your website provides the status of the payment.

## See also

- Testing your Connect integration
- Testing your Billing integration
- Testing your Terminal integration
- Load testing

--------------------