# Dynamic
**URL:** https://dynamic.xyz
**Page Title:** Dynamic | Wallet Infrastructure for Fintech, Crypto, and Stablecoins
--------------------

Trusted by leading fintech and crypto teams.
Backed by the security and scale of

## Scale that's battle-tested

50M+
Users onboarded
600+
External wallets supported
< 1
Second signing speed

## Crypto features your customers demand

Dynamic gives your customers the ability to trade, earn, pay, and move money on global crypto rails.

### Trade

Expand what customers can trade from prediction markets to tokenized assets.

### Earn

Offer yield on balances to keep customers engaged with your app.

### Pay

Let customers pay with and deposit crypto from any wallet or exchange. No on/off-ramping required.

### Move

Let customers send money globally, fast, cheap, and 24/7.

## Designed for developers. Built for enterprise.

Build your way — from low-level APIs to full SDKs. Use primitives for full control or prebuilt flows to ship fast. Get sub-second signing and enterprise-grade security. Scale from concept to millions without rebuilding your stack.
Create and control wallets through APIs for programmable money movement at scale.
Learn more
Spin up non-custodial wallets in your app and let users start their onchain journey instantly.
Learn more
Let users connect the wallets they already have across chains & platforms.
Learn more

## One complete wallet stack

Dynamic is the only platform with embedded wallets, external wallets, and multi-chain connectivity in one unified SDK.

## Built for security, engineered for speed

Security is the foundation of everything we do. From key management to infrastructure, every layer of Dynamic is designed for safety, reliability, and compliance.

### Enterprise self-custody

Every wallet benefits from secure distributed signing, flexible thresholds, and built-in recovery paths.

### Fireblocks security

Dynamic inherits Fireblocks’ security expertise, practices, and operational rigor. Together, we deliver institutional-grade protection from custody to consumer wallets.

### Defense in depth

Our infrastructure is regularly audited by top firms and protected by a public bug bounty program.

### Sub-second signing

Transactions complete in under a second. Users get speed and enterprise-grade security in every wallet interaction.

## Recent audits

July 2025
April 2025
February 2025
September 2024
Ongoing Bounty Program
Reviews

## World-class teams build with Dynamic

Trade
We wanted something that just works. That means no seed phrases, no chain switching, and no waiting. You tap a token, you buy it. That’s what we built, and Dynamic helped make it all possible
View case study
Earn
We explored and started implementing various other embedded wallet solutions. Dynamic not only had the most secure solution it had by far the best developer experience. We had a working prototype in a fraction of the time.
View case study
Pay with Crypto
Through Dynamic, Stripe has made crypto pay-ins seamless for millions of merchants.
View case study
Trade
For our users, the experience from their first wallet connection to first trade is smooth. Dynamic is easy to integrate, supports lots of wallets out of the box, and the team is extremely responsive.
View case study

## Install our SDK in minutes!

### Get an environment ID

Set up an account to get your environment ID.

### Install the Dynamic NPM package

This takes a few seconds.

### Set up your snippet and customize

Once you set up your snippet, you can further customize things within your developer dashboard. You can also check out a working demo environment here:
npm i viem @dynamic-labs/sdk-react-core @dynamic-labs/ethereum
import { DynamicContextProvider, DynamicWidget, } from "@dynamic-labs/sdk-react-core"; import { EthereumWalletConnectors } from "@dynamic-labs/ethereum"; export default function App() { return ( <DynamicContextProvider settings={{ // Find your environment id at https://app.dynamic.xyz/dashboard/developer environmentId: "REPLACE-WITH-YOUR-ENVIRONMENT-ID", walletConnectors: [EthereumWalletConnectors], }} > <DynamicWidget /> </DynamicContextProvider> ); }
npm i @dynamic-labs/viem-extension@alpha @dynamic-labs/client@alpha @dynamic-labs/react-native-extension@alpha @dynamic-labs/react-hooks@alpha react-native-webview expo-web-browser expo-linking expo-secure-store
import { createClient } from "@dynamic-labs/client"; import { ReactNativeExtension } from "@dynamic-labs/react-native-extension"; import { ViemExtension } from "@dynamic-labs/viem-extension"; export const dynamicClient = createClient({ // Find your environment id at https://app.dynamic.xyz/dashboard/developer environmentId: "REPLACE-WITH-YOUR-ENVIRONMENT-ID",  // Optional: appLogoUrl: "https://demo.dynamic.xyz/favicon-32x32.png", appName: "Dynamic Demo", }) .extend(ReactNativeExtension()) .extend(ViemExtension()); export function App() { return ( <> <dynamicClient.reactNative.WebView />      <SafeAreaView> <Text>Hello, world!</Text> </SafeAreaView> </> ); }
flutter pub add dynamic_sdk dynamic_sdk_web3dart
import 'package:dynamic_sdk/dynamic_sdk.dart'; void main() { WidgetsFlutterBinding.ensureInitialized(); DynamicSDK.init( props: ClientProps( // Find your environment id at https://app.dynamic.xyz/dashboard/developer environmentId: 'REPLACE-WITH-YOUR-ENVIRONMENT-ID',      // Optional: appLogoUrl: 'https://demo.dynamic.xyz/favicon-32x32.png', appName: 'Dynamic Demo', ), ); runApp(const MyApp()); } class MyApp extends StatelessWidget { const MyApp({super.key}); @override Widget build(BuildContext context) { return MaterialApp( title: 'Flutter Demo', theme: ThemeData( colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple), useMaterial3: true, ), home: Stack( children: [ // Make sure the SDK is ready before using it StreamBuilder<bool?>( stream: DynamicSDK.instance.sdk.readyChanges, builder: (context, snapshot) { final sdkReady = snapshot.data ?? false; return sdkReady ? const MyHomePage(title: 'Flutter Demo Home Page') : const SizedBox.shrink(); }, ), // DynamicSDK widget must be available all the time DynamicSDK.instance.dynamicWidget, ], ), ); } }
import DynamicSwiftSDK let config = DynamicClientConfig( environmentId: "<your env id>" ) let dynamicClient = createDynamicClient(config: config) // Authenticate a user let otpVerification: OTPVerification = try await sendEmailOtp( client: dynamicClient, email: userEmail ) let authenticatedUser: SdkUser = try await verifyOtp( otpVerification: otpVerification, verificationToken: otpCode ) // Create user's wallet let accountAddress = try await createWalletAccount(client: dynamicClient)
npm i @dynamic-labs-sdk/client @dynamic-labs-sdk/evm viem
import { createDynamicClient } from "@dynamic-labs-sdk/client"; import { addEvmExtension } from "@dynamic-labs-sdk/evm"; const client = createDynamicClient({ environmentId: "[YOUR_ENVIRONMENT_ID]", metadata: { name: "[YOUR_APP_NAME]", url: "[YOUR_APP_URL]", }, }); // Add extensions based on your chain configuration addEvmExtension(client);

## Set up Dynamic in minutes

Free to start up to 1,000 MAUs

--------------------