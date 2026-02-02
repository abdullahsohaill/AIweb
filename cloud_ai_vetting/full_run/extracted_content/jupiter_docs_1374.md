# Jupiter Docs
**URL:** https://station.jup.ag/docs
**Page Title:** Jupiter Developers
--------------------

🚨 Action Required: lite-api.jup.ag will be deprecated on 31st January 2026. View migration guide →
[LINK: View migration guide →](https://dev.jup.ag/portal/migrate-from-lite-api)
[LINK: API Reference](/api-reference)
- Dev Portal
- API Status
- Stay Updated
- Overview
[LINK: Overview](/docs/ultra)
- Get Started
[LINK: Get Started](/docs/ultra/get-started)
- Gasless Support
[LINK: Gasless Support](/docs/ultra/gasless)
- Fees
[LINK: Fees](/docs/ultra/fees)
- Manual Mode
[LINK: Manual Mode](/docs/ultra/manual-mode)
- Get Order
[LINK: Get Order](/docs/ultra/get-order)
- Execute Order
[LINK: Execute Order](/docs/ultra/execute-order)
- Response
[LINK: Response](/docs/ultra/response)
- Rate Limit
[LINK: Rate Limit](/docs/ultra/rate-limit)
- Add Integrator Fees
[LINK: Add Integrator Fees](/docs/ultra/add-fees-to-ultra)
- Add Integrator Payer
[LINK: Add Integrator Payer](/docs/ultra/add-payer)
- Integrate Jupiter Plugin
[LINK: Integrate Jupiter Plugin](/docs/ultra/plugin-integration)
- Quick Launch
- Features
- What About Metis Swap API?
[LINK: What About Metis Swap API?](#what-about-metis-swap-api)

## ​ Quick Launch

[LINK: Ultra Swap API RPC-less architecture and Jupiter handles all trading optimizations for you.](/docs/ultra/get-started)

## Ultra Swap API

## Plugin

## ​ Features

Juno Liquidity Engine
[LINK: Juno Liquidity Engine](/docs/routing)
Best Executed Price
- Predictive Execution : Ultra simulates and compares executed prices (not just quoted prices) before actually sending a transaction, dynamically selecting the route with the least slippage for real user outcomes.
- Ultra Signaling : Ultra provides signaling to Proprietary AMMs to help them distinguish Ultra user flow, incentivizing them to quote tighter spreads and better prices.
- Slippage-Aware Routing : Automatically prioritizes and selects routes that minimize realized slippage, protecting users from misleading “best quotes” that deliver poor executed results.
Sub-second Transaction Landing & MEV Protection
- Leverage our own validator stake and dedicated R&D efforts.
- Complete transaction privacy until on-chain execution.
- Eliminate the risk of artificial delays and front-running, ensuring faster and more secure execution for our users.
- Landing Latency: Improved by 50-66% compared to our previous approach that relied on multiple providers Lands in 0–1 block (~50–400ms) Compared to the 1–3 blocks (~400ms–1.2s) previously.
- Lands in 0–1 block (~50–400ms)
- Compared to the 1–3 blocks (~400ms–1.2s) previously.
- MEV Protection: Routing transactions through our own infrastructure provides: Complete transaction privacy until on-chain execution. Reduce frontrunning exposure - transactions are invisible to public mempool scanners. Reduce risk of sandwich attack vectors - see our blog post on Ultra’s swap volume to value extracted ratio .
- Complete transaction privacy until on-chain execution.
- Reduce frontrunning exposure - transactions are invisible to public mempool scanners.
- Reduce risk of sandwich attack vectors - see our blog post on Ultra’s swap volume to value extracted ratio .
Real Time Slippage Estimator
- Heuristics: Token categories, historical and real-time slippage data, and more. Uses token categories to intelligently estimate slippage for different token types. Automatic prioritization of slippage-protected routes over purely price-optimized routes. Increased volatility sensitivity for tokens with high historical volatility patterns.
- Uses token categories to intelligently estimate slippage for different token types.
- Automatic prioritization of slippage-protected routes over purely price-optimized routes.
- Increased volatility sensitivity for tokens with high historical volatility patterns.
- Algorithms: Exponential Moving Average (EMA) on slippage data, and more.
- Monitoring: Real-time monitoring of failure rates to ensure reactiveness to increase slippage when necessary.
Gasless
- Gasless via Jupiter Z (RFQ): All swaps routed via Jupiter Z are gasless, as the market maker is the fee payer for the transaction.
- Gasless via Gasless Support: Depending on the tokens and trade sizes of your swap, Ultra Swap will automatically determine if it can provide gasless support to your swap by helping you pay for the transaction fee of your swap - you can identify this via the secondary signer in the transaction.
API Latency
[LINK: Add Fees To Ultra Swap](/docs/ultra/add-fees-to-ultra)

## ​ What About Metis Swap API?

- Adding custom instructions.
- Incorporating Cross Program Invocation (CPI) calls.
- Selecting specific broadcasting strategies for signed transactions (e.g., priority fee, Jito, etc.).
- Choosing which DEXes or AMMs to route through.
- Modifying the number of accounts used in a transaction.
- RPC management : Retrieving wallet balances, broadcasting, and tracking transactions.
- Transaction fee selection : Managing priority fees, Jito fees, and more.
- Slippage optimization : Determining the best slippage settings for trade success and price protection.
- Transaction broadcasting : Ultra Swap leverages a proprietary transaction engine for superior speed and reliability.
- Swap result parsing : Handling transaction polling, parsing, and error management.
Was this page helpful?
[LINK: Get Started](/docs/ultra/get-started)

--------------------