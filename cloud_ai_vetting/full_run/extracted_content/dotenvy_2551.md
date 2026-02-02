# dotenvy
**URL:** https://crates.io/crates/dotenvy
**Page Title:** dotenvy - crates.io: Rust Package Registry
--------------------


## dotenvy v0.15.7

- # env
- # config
- # environment
- # dotenv
- # settings

## dotenvy

A well-maintained fork of the dotenv crate.
[LINK: dotenv](https://github.com/dotenv-rs/dotenv)
This crate is the suggested alternative for dotenv in security advisory RUSTSEC-2021-0141 .
This library loads environment variables from a .env file. This is convenient for dev environments.

## Components

- dotenvy crate - A well-maintained fork of the dotenv crate.
- dotenvy_macro crate - A macro for compile time dotenv inspection. This is a fork of dotenv_codegen .
- dotenvy CLI tool for running a command using the environment from a .env file (currently Unix only)

## Usage

### Loading at runtime

### Loading at compile time

The dotenv! macro provided by dotenvy_macro crate can be used.
Warning: there is an outstanding issue with rust-analyzer ( rust-analyzer #9606 ) related to the dotenv! macro
[LINK: rust-analyzer #9606](https://github.com/rust-analyzer/rust-analyzer/issues/9606)

## Minimum supported Rust version

Currently: 1.56.1
We aim to support the latest 8 rustc versions - approximately 1 year. Increasing
MSRV is not considered a semver-breaking change.

## Why does this fork exist?

The original dotenv crate has not been updated since June 26, 2020. Attempts to reach the authors and present maintainer were not successful ( dotenv-rs/dotenv #74 ).
[LINK: dotenv-rs/dotenv #74](https://github.com/dotenv-rs/dotenv/issues/74)
This fork intends to serve as the development home for the dotenv implementation in Rust.

## What are the differences from the original?

This repo fixes:
- more helpful errors for dotenv! ( dotenv-rs/dotenv #57 )
[LINK: dotenv-rs/dotenv #57](https://github.com/dotenv-rs/dotenv/pull/57)
It also adds:
- multiline support for environment variable values
- io::Read support via from_read and from_read_iter
[LINK: from_read](https://docs.rs/dotenvy/latest/dotenvy/fn.from_read.html)
[LINK: from_read_iter](https://docs.rs/dotenvy/latest/dotenvy/fn.from_read_iter.html)
- override support via [ dotenv_override ], [ from_filename_override ], [ from_path_override ] and [ from_read_override ]
- improved docs
For a full list of changes, refer to the changelog .
[LINK: changelog](https://github.com/allan2/dotenvy/blob/HEAD/dotenv/./CHANGELOG.md)

## The legend

Legend has it that the Lost Maintainer will return, merging changes from dotenvy into dotenv with such thrust that all Cargo.toml s will lose one keystroke. Only then shall the Rust dotenv crateverse be united in true harmony.
Until then, this repo dutifully carries on the dotenv torch. It is actively maintained. Contributions and PRs are very welcome!

## Metadata

## Install

Running the above command will globally install the dotenvy binary.

### Install as library

Run the following Cargo command in your project directory:
Or add the following line to your Cargo.toml:

## Documentation

[LINK: docs.rs/dotenvy/0.15.7](https://docs.rs/dotenvy/0.15.7)

## Browse source

[LINK: docs.rs/crate/dotenvy/0.15.7/source](https://docs.rs/crate/dotenvy/0.15.7/source/)

## Repository

[LINK: github.com/allan2/dotenvy](https://github.com/allan2/dotenvy)

## Owners

- Allan Zhang

### Stats Overview


--------------------