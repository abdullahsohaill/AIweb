# Git LFS
**URL:** https://git-lfs.com
**Page Title:** Git Large File Storage | Git Large File Storage (LFS) replaces large files such as audio samples, videos, datasets, and graphics with text pointers inside Git, while storing the file contents on a remote server like GitHub.com or GitHub Enterprise.
--------------------


## An open source Git extension for versioning large files

Git Large File Storage (LFS) replaces large files such as audio samples, videos, datasets, and graphics with text pointers inside Git, while storing the file contents on a remote server like GitHub.com or GitHub Enterprise.
Download v3.7.1 (Windows)
[LINK: Download v3.7.1 (Windows)](https://github.com/git-lfs/git-lfs/releases/download/v3.7.1/git-lfs-windows-v3.7.1.exe)
Download v3.7.1 (Mac - Intel Silicon)
[LINK: Download v3.7.1 (Mac - Intel Silicon)](https://github.com/git-lfs/git-lfs/releases/download/v3.7.1/git-lfs-darwin-amd64-v3.7.1.zip)
Download v3.7.1 (Mac - Apple Silicon)
[LINK: Download v3.7.1 (Mac - Apple Silicon)](https://github.com/git-lfs/git-lfs/releases/download/v3.7.1/git-lfs-darwin-arm64-v3.7.1.zip)
Homebrew : brew install git-lfs MacPorts : port install git-lfs
Install v3.7.1 via PackageCloud (Linux)
[LINK: Install v3.7.1 via PackageCloud (Linux)](https://packagecloud.io/github/git-lfs/install)
Download v3.7.1 (Linux - x86-64)
[LINK: Download v3.7.1 (Linux - x86-64)](https://github.com/git-lfs/git-lfs/releases/download/v3.7.1/git-lfs-linux-amd64-v3.7.1.tar.gz)

## How it works:

[LINK: Git LFS security update: All users should update to 3.7.1 .](https://github.com/git-lfs/git-lfs/security/advisories/GHSA-6pvw-g552-53c5)

## Getting Started

- Download and install the Git command line extension. Once downloaded and installed, set up Git LFS for your user account by running: git lfs install You only need to run this once per user account.
Download and install the Git command line extension. Once downloaded and installed, set up Git LFS for your user account by running:
You only need to run this once per user account.
- In each Git repository where you want to use Git LFS, select the file types you'd like Git LFS to manage (or directly edit your .gitattributes). You can configure additional file extensions at anytime. git lfs track "*.psd" Now make sure .gitattributes is tracked: git add .gitattributes Note that defining the file types Git LFS should track will not, by itself, convert any pre-existing files to Git LFS, such as files on other branches or in your prior commit history. To do that, use the git lfs migrate(1) command, which has a range of options designed to suit various potential use cases.
In each Git repository where you want to use Git LFS, select the file types you'd like Git LFS to manage (or directly edit your .gitattributes). You can configure additional file extensions at anytime.
Now make sure .gitattributes is tracked:
Note that defining the file types Git LFS should track will not, by itself, convert any pre-existing files to Git LFS, such as files on other branches or in your prior commit history. To do that, use the git lfs migrate(1) command, which has a range of options designed to suit various potential use cases.
[LINK: git lfs migrate(1)](https://github.com/git-lfs/git-lfs/blob/main/docs/man/git-lfs-migrate.adoc?utm_source=gitlfs_site&utm_medium=doc_man_migrate_link&utm_campaign=gitlfs)
- There is no step three. Just commit and push as you normally would; for instance, if your current branch is named main : git add file.psd
git commit -m "Add design file"
git push origin main Check out our wiki , discussion forum , and documentation for help with any questions you might have!
There is no step three. Just commit and push as you normally would; for instance, if your current branch is named main :
Check out our wiki , discussion forum , and documentation for help with any questions you might have!
[LINK: wiki](https://github.com/git-lfs/git-lfs/wiki?utm_source=gitlfs_site&utm_medium=wiki_link&utm_campaign=gitlfs)
[LINK: discussion forum](https://github.com/git-lfs/git-lfs/discussions?utm_source=gitlfs_site&utm_medium=discussions_link&utm_campaign=gitlfs)
[LINK: documentation](https://github.com/git-lfs/git-lfs/tree/main/docs?utm_source=gitlfs_site&utm_medium=docs_link&utm_campaign=gitlfs)

## Git LFS is an open source project

To start a discussion, file an issue, or contribute to the project, head over to the repository or read our guide to contributing .
[LINK: to the repository](https://github.com/git-lfs/git-lfs?utm_source=gitlfs_site&utm_medium=repo_link&utm_campaign=gitlfs)
[LINK: guide to contributing](https://github.com/git-lfs/git-lfs/blob/main/CONTRIBUTING.md?utm_source=gitlfs_site&utm_medium=contributing_link&utm_campaign=gitlfs)
If you're interested in integrating Git LFS into another tool or product, you might want to read the API specification or check out our reference server implementation .
[LINK: API specification](https://github.com/git-lfs/git-lfs/blob/main/docs/api/README.md?utm_source=gitlfs_site&utm_medium=api_spec_link&utm_campaign=gitlfs)
[LINK: reference server implementation](https://github.com/git-lfs/lfs-test-server?utm_source=gitlfs_site&utm_medium=reference_servedr&utm_campaign=gitlfs)

## Features

- Large file versioning Version large files—even those as large as a couple GB in size—with Git.

### Large file versioning

Version large files—even those as large as a couple GB in size—with Git.
- More repository space Host more in your Git repositories. External file storage makes it easy to keep your repository at a manageable size.

### More repository space

Host more in your Git repositories. External file storage makes it easy to keep your repository at a manageable size.
- Faster cloning and fetching Download less data. This means faster cloning and fetching from repositories that deal with large files.

### Faster cloning and fetching

Download less data. This means faster cloning and fetching from repositories that deal with large files.
- Same Git workflow Work like you always do on Git—no need for additional commands, secondary storage systems, or toolsets.

### Same Git workflow

Work like you always do on Git—no need for additional commands, secondary storage systems, or toolsets.
- Same access controls and permissions Keep the same access controls and permissions for large files as the rest of your Git repository when working with a remote host like GitHub.

### Same access controls and permissions

Keep the same access controls and permissions for large files as the rest of your Git repository when working with a remote host like GitHub.

--------------------