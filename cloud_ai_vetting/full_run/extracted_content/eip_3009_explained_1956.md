# EIP-3009 Explained
**URL:** https://ethereum.org/en/developers/docs/standards/tokens/erc-20
**Page Title:** ERC-20 Token Standard | ethereum.org
--------------------


## ERC-20 Token Standard

Page last update: October 27, 2025
[LINK: w opens in a new tab](https://github.com/wackerow)
[LINK: p opens in a new tab](https://github.com/pete-vielhaber)
[LINK: v opens in a new tab](https://github.com/vittominacori)

## Introduction

What is a Token?
Tokens can represent virtually anything in Ethereum:
- reputation points in an online platform
- skills of a character in a game
- financial assets like a share in a company
- a fiat currency like USD
- an ounce of gold
- and more...
Such a powerful feature of Ethereum must be handled by a robust standard, right? That's exactly
where the ERC-20 plays its role! This standard allows developers to build token applications that are interoperable with other products and services. The ERC-20 standard is also used to provide additional functionality to .
What is ERC-20?
The ERC-20 introduces a standard for Fungible Tokens, in other words, they have a property that makes each Token be exactly
the same (in type and value) as another Token. For example, an ERC-20 Token acts just like the ETH, meaning that 1 Token
is and will always be equal to all the other Tokens.

## Prerequisites

- Accounts
[LINK: Accounts](/developers/docs/accounts/)
- Smart Contracts
[LINK: Smart Contracts](/developers/docs/smart-contracts/)
- Token standards
[LINK: Token standards](/developers/docs/standards/tokens/)

## Body

The ERC-20 (Ethereum Request for Comments 20), proposed by Fabian Vogelsteller in November 2015, is a Token Standard that
implements an API for tokens within Smart Contracts.
Example functionalities ERC-20 provides:
- transfer tokens from one account to another
- get the current token balance of an account
- get the total supply of the token available on the network
- approve whether an amount of token from an account can be spent by a third-party account
If a Smart Contract implements the following methods and events it can be called an ERC-20 Token Contract and, once deployed, it
will be responsible to keep track of the created tokens on Ethereum.
From EIP-20 opens in a new tab :

### Methods

### Events

### Examples

Let's see how a Standard is so important to make things simple for us to inspect any ERC-20 Token Contract on Ethereum.
We just need the Contract Application Binary Interface (ABI) to create an interface to any ERC-20 Token. As you can
see below we will use a simplified ABI, to make it a low friction example.
First, make sure you have installed Web3.py opens in a new tab Python library:
[LINK: Web3.py opens in a new tab](https://web3py.readthedocs.io/en/stable/quickstart.html#installation)

## Known issues

### ERC-20 token reception issue

As of 06/20/2024 at least $83,656,418 worth of ERC-20 tokens were lost due to this issue. Note that a pure ERC-20 implementation is prone to this problem unless you implement a set of additional restrictions on top of the standard as listed below.
When ERC-20 tokens are sent to a smart contract that is not designed to handle ERC-20 tokens, those tokens can be permanently lost. This happens because the receiving contract does not have the functionality to recognize or respond to the incoming tokens, and there’s no mechanism in the ERC-20 standard to notify the receiving contract about the incoming tokens. The main ways this issue takes form is through:
- Token transfer mechanism
- ERC-20 tokens are transferred using the transfer or transferFrom functions When a user sends tokens to a contract address using these functions, the tokens are transferred regardless of whether the receiving contract is designed to handle them
- When a user sends tokens to a contract address using these functions, the tokens are transferred regardless of whether the receiving contract is designed to handle them
- Lack of notification The receiving contract does not receive a notification or callback that tokens have been sent to it If the receiving contract lacks a mechanism to handle tokens (e.g., a fallback function or a dedicated function to manage token reception), the tokens are effectively stuck in the contract’s address
- The receiving contract does not receive a notification or callback that tokens have been sent to it
- If the receiving contract lacks a mechanism to handle tokens (e.g., a fallback function or a dedicated function to manage token reception), the tokens are effectively stuck in the contract’s address
- No built-in handling The ERC-20 standard does not include a mandatory function for receiving contracts to implement, leading to a situation where many contracts are unable to manage incoming tokens properly
- The ERC-20 standard does not include a mandatory function for receiving contracts to implement, leading to a situation where many contracts are unable to manage incoming tokens properly
Possible Solutions
While it is not possible to prevent this issue with ERC-20 completely there are methods that would allow to significantly reduce the possibility of a tokens loss for the end user:
- The most common problem is when a user sends tokens to the token contract address itself (e.g., USDT deposited to the address of USDT token contract). It is recommended to restrict transfer(..) function to revert such transfer attempts. Consider adding require(_to != address(this)); check within the implementation of the transfer(..) function.
- The transfer(..) function in general is not designed for depositing tokens to contracts. approve(..) & transferFrom(..) pattern is used to deposit ERC-20 tokens to contracts instead. It is possible to restrict the transfer function to disallow depositing tokens to any contracts with it, however it may break compatibility with contracts that assume tokens can be deposited to contracts with the trasnfer(..) function (e.g., Uniswap liquidity pools).
- Always assume that ERC-20 tokens can end up in your contract even if your contract is not supposed to ever receive any. There is no way to prevent or reject accidental deposits on the recipients end. It is recommended to implement a function that would allow to extract accidentally deposited ERC-20 tokens.
- Consider using alternative token standards.
Some alternative standards have come out of this issue such as ERC-223 or ERC-1363 .
[LINK: ERC-223](/developers/docs/standards/tokens/erc-223/)
[LINK: ERC-1363](/developers/docs/standards/tokens/erc-1363/)

## Further reading

- EIP-20: ERC-20 Token Standard opens in a new tab
- OpenZeppelin - Tokens opens in a new tab
[LINK: OpenZeppelin - Tokens opens in a new tab](https://docs.openzeppelin.com/contracts/3.x/tokens#ERC20)
- OpenZeppelin - ERC-20 Implementation opens in a new tab
[LINK: OpenZeppelin - ERC-20 Implementation opens in a new tab](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol)
- Alchemy - Guide to Solidity ERC20 Tokens opens in a new tab

## Other fungible token standards

- ERC-223
[LINK: ERC-223](/developers/docs/standards/tokens/erc-223/)
- ERC-1363
[LINK: ERC-1363](/developers/docs/standards/tokens/erc-1363/)
- ERC-777
[LINK: ERC-777](/developers/docs/standards/tokens/erc-777/)
- ERC-4626 - Tokenized vaults
[LINK: ERC-4626 - Tokenized vaults](/developers/docs/standards/tokens/erc-4626/)

## Was this article helpful?


--------------------